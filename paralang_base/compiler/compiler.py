# coding=utf-8
""" Main compiler management file """
from __future__ import annotations

import logging
import pathlib
from os import PathLike
from pathlib import Path
from typing import Union, TYPE_CHECKING, Tuple, Literal, List, Optional
import antlr4
from antlr4 import BailErrorStrategy

from .error_handler import ParaErrorListener
from .parse_stream import ParaQualifiedParseStream, CParseStream
from .parser.python import ParaLexer
from .parser.python import ParaParser
from .process import CompileResult
from ..exceptions import (FilePermissionError, LexerError, LinkerError,
                          ParaCompilerError, FailedToProcessError,
                          ParaSyntaxErrorCollection)
from ..util import get_file_stream, get_input_stream, ensure_pathlib_path

try:
    import paralang_cli

    PARAC_EXT_CLI_AVAILABLE: bool = True
except ImportError:
    PARAC_EXT_CLI_AVAILABLE: bool = False

if TYPE_CHECKING:
    from .parser.listener import CompilationUnitContext

    paralang_cli = None
    if PARAC_EXT_CLI_AVAILABLE:
        from paralang_cli import (ParaCLIStreamHandler, ParaCLIFileHandler,
                                  ParaCLIFormatter)
    else:
        from typing import NewType

        ParaCLIStreamHandler = NewType('ParaCLIStreamHandler', None)
        ParaCLIFileHandler = NewType('ParaCLIFileHandler', None)

__all__ = [
    'ParaCompiler',
]

logger = logging.getLogger(__name__)

ONE_LINE_COMMENT_START: str = '//'
ONE_LINE_COMMENT_END: Tuple[str, str, str] = ('\n', '\r\n', '\r')
MULTI_LINE_COMMENT_START: str = '/*'
MULTI_LINE_COMMENT_END: str = '*/'


class ParaCompiler:
    """ Main Class for the entire Compiler containing processing functions """

    def __init__(self):
        self._stream_handler: ParaCLIStreamHandler = None
        self._file_handler: ParaCLIFileHandler = None
        self._logger: Optional[logging.Logger] = None

    @property
    def is_cli_logger_ready(self) -> bool:
        """
        Returns whether the CLI logger is initialised ('init_cli_logging' was
        called)
        """
        return getattr(self, 'logger') is not None

    @property
    def stream_handler(self) -> ParaCLIStreamHandler:
        """ Stream handler, which handles the logging output """
        return self._stream_handler

    @property
    def file_handler(self) -> ParaCLIFileHandler:
        """
        File handler, which handles the logging output that will be written
        onto a file
        """
        return self._file_handler

    @property
    def logger(self) -> logging.Logger:
        """
        The logger for this class - If the CLI logger should be used it
        will have to be specifically initialised using 'init_cli_logging'
        """
        if self._logger:
            return self._logger
        else:
            self._logger = logger
            return logger

    def init_cli_logging(
            self,
            log_path: Union[str, PathLike, pathlib.Path] = None,
            level: int = logging.INFO,
            print_banner: bool = True,
            banner_name: str = "Compiler",
            additional_newline: bool = True
    ):
        """
        Initialising the logging module for the Compiler
        and defines the formatting defaults for the CLI

        :param log_path: Path where the log file should be placed. If None
         logging to files will be ignored
        :param level: Level the logger should be initialised with.
         Defaults to INFO
        :param print_banner: If set to True the logging banner will be printed.
         Requires 'para_ext_cli' to function properly!
        :param banner_name: The name used for the logging banner
        :param additional_newline: If set to True an additional newline will be
         added before the logging banner
        """
        if not PARAC_EXT_CLI_AVAILABLE or paralang_cli is None:
            raise RuntimeError(
                "To utilise this function, 'paralang_cli' is required!"
            )
        else:
            from paralang_cli import (ParaCLIStreamHandler, ParaCLIFileHandler,
                                      ParaCLIFormatter, cli_print_log_banner)

        if print_banner:
            cli_print_log_banner(banner_name, additional_newline)

        self._logger: logging.Logger = logging.getLogger("parac")
        self.logger.setLevel(level)

        # if the stream handler exists it will always get removed by default
        if self.stream_handler:
            self.logger.removeHandler(self.stream_handler)

        # if the file handler exists and a new log_path was passed ->
        # remove and generate new file_handler
        if self.file_handler and log_path:
            self.logger.removeHandler(self.file_handler)

        self._stream_handler = ParaCLIStreamHandler()
        self._stream_handler.setFormatter(
            ParaCLIFormatter(datefmt="%H:%M:%S")
        )
        self.logger.addHandler(self.stream_handler)

        if type(log_path) in (str, pathlib.Path) \
                and log_path.lower() != 'none':
            try:
                path: Path = ensure_pathlib_path(log_path)
                self._file_handler = ParaCLIFileHandler(
                    filename=path
                )
            except PermissionError:
                raise FilePermissionError(
                    "Failed to access the specified log file-path"
                )
            self.file_handler.setFormatter(
                ParaCLIFormatter(file_mng=True)
            )
            self.logger.addHandler(self.file_handler)

        if type(log_path) is str:
            if '.' not in log_path:
                logger.warning(
                    "The log-path does not contain the '.log' file-ending"
                )

    @staticmethod
    async def parse(
            input_stream: antlr4.InputStream,
            prefer_logging: bool = True
    ) -> CompilationUnitContext:
        """
        Parses the passed input_stream using antlr4 and returns the
        compilation unit context which can be used with the listener to compile
        and process the file

        :param input_stream: The token stream of the file
        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        :returns: The compilationUnit (file) context
        :raises ParaSyntaxError: If the parsing failed due to a syntax issue
         aka. input error from the user.
        """
        # Error handler which uses the default error strategy to handle the
        # incoming antlr4 errors
        error_listener = ParaErrorListener()

        # Initialising the lexer, which will tokenize the input_stream and
        # raise basic errors if needed
        lexer = ParaLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        logger.debug("Lexing the file and generating the tokens")

        # Parsing the lexer and generating a token stream
        stream = antlr4.CommonTokenStream(lexer)

        # Parser which generates based on the top entry rule the parse tree
        parser = ParaParser(stream)
        parser._errHandler = BailErrorStrategy()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        # Parsing from the entry - compilationUnit
        cu = parser.compilationUnit()

        # Raise one or multiple errors if they were caught during the parsing
        if len(error_listener.errors) > 0:
            raise ParaSyntaxErrorCollection(
                error_listener.errors,
                prefer_logging
            )  # Raising the syntax error/s

        return cu

    async def validate_syntax(
            self,
            file: Union[str, PathLike, pathlib.Path],
            encoding: str,
            prefer_logging: bool = True
    ) -> None:
        """
        Validates the syntax of a file and logs or raises errors if any
        problems are encountered while running. This is at the moment
        specifically designed to not return anything, but only raise exceptions
        if anything is found.

        TODO! Implement the return of a list of warnings to allow the usage of
         warnings without having to use a logger.

        :param file: The file to run the syntax checks on
        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance,
         instead of directly returned. They will be 'raised from' with the
         FailedToProcessError exception.
        :param encoding: The encoding of the file
        :raises FailedToProcessError: If prefer_logging is True and
         an exception is encountered. The logs of the exception will be printed
         onto the console.
        :raises ParaCompilerError: If any exception is encountered and
         prefer_logging is False
        """
        file_stream: antlr4.FileStream = get_file_stream(file, encoding)
        stream: antlr4.InputStream = get_input_stream(
            self.remove_comments_from_str(file_stream.strdata),  # rm comments
            name=file_stream.name
        )
        try:
            logger.info(f"Parsing file ({file_stream.fileName})")
            await self.parse(stream, prefer_logging)

            # TODO! Implement the usage of a FileCompilationContext to also
            #  generate a parse stream and get Para specific errors

        except (LexerError, ParaSyntaxErrorCollection, LinkerError,
                ParaCompilerError) as e:
            if prefer_logging:
                raise FailedToProcessError(exc=e) from e
            else:
                raise e

        logger.info(
            "Successfully finished syntax-check for file "
            f"{file_stream.fileName}"
        )

    @staticmethod
    def remove_comments_from_str(
            string: str, line_ending: str = '\n'
    ) -> str:
        """
        Removes comments from the passed string and returns the modified
        string. Only comments in the (// ... ) and (/*...*/) format will
        be removed, but else the string will be ignored.

        For proper handling line-endings are all set to win-style, if this is
        not wanted the wanted line ending should be passed. Note: This will
        not make the function ignore every other line-ending but simply in the
        end replace every occurrence of win-style with the wanted line-ending.
        """
        prev_c: str = ""
        result: str = ""
        in_type: Literal['std', 'one_c', 'mult_c'] = "std"

        # For ease replacing \r and \r\n with \n
        string = string.replace('\r\n', '\n').replace('\r', '\n')

        for c in string:
            c: str
            _: str = f'{prev_c}{c}'
            if in_type == "std":
                if _ == ONE_LINE_COMMENT_START:
                    result = result[0:-1]  # Removing the previous char
                    in_type = "one_c"
                elif _ == MULTI_LINE_COMMENT_START:
                    result = result[0:-1]  # Removing the previous char
                    in_type = "mult_c"
                else:
                    result += c
            else:
                if any((
                        in_type == "one_c" and c in ONE_LINE_COMMENT_END,
                        in_type == "mult_c" and _ == MULTI_LINE_COMMENT_END
                )):
                    in_type = 'std'
                    result += '\n'
            prev_c = c
        return result.replace('\n', line_ending)

    @classmethod
    async def compile_files(
            cls,
            file: List[Union[str, PathLike, pathlib.Path]],
            encoding: str
    ) -> CompileResult:
        """
        Compiles the passed files and directly creates a CompileResult.

        This function takes away most of the configuration and customisation
        by using the usable defaults to create the CompileProcess and run
        the code-generation.

        This should be specifically used if no specific behaviour is wanted.

        TODO! Implement this function by using a CompileProcess
        """
        raise NotImplementedError()

    @classmethod
    async def compile_parse_stream(
            cls,
            parse_stream: ParaQualifiedParseStream
    ) -> CParseStream:
        """
        Compiles the passed ParaQualifiedParseStream into the C counterpart
        """
        raise NotImplementedError()
