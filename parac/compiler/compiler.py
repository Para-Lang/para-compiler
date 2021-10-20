# coding=utf-8
""" Main compiler management file """
from __future__ import annotations

import logging
import pathlib
from os import PathLike
from pathlib import Path
from typing import Union, TYPE_CHECKING, Tuple, Literal
import antlr4

from .process import BasicProcess
from .error_handler import ParacErrorListener
from .logic_stream import ParacLogicStream, CLogicStream
from .parser.python import ParaCLexer
from .parser.python import ParaCParser
from ..logging import (ParacFormatter, ParacFileHandler, ParacStreamHandler,
                       print_log_banner)
from ..util import get_file_stream, get_input_stream, ensure_pathlib_path
from ..exceptions import (FilePermissionError, LexerError, LinkerError,
                          ParacCompilerError, FailedToProcessError,
                          ParaCSyntaxErrorCollection)

if TYPE_CHECKING:
    from .parser.listener import CompilationUnitContext

__all__ = [
    'ParacCompiler',
]

logger = logging.getLogger(__name__)

ONE_LINE_COMMENT_START: str = '//'
ONE_LINE_COMMENT_END: Tuple[str, str, str] = ('\n', '\r\n', '\r')
MULTI_LINE_COMMENT_START: str = '/*'
MULTI_LINE_COMMENT_END: str = '*/'


class ParacCompiler:
    """ Main Class for the entire Compiler containing processing functions """
    logger: logging.Logger = None
    stream_handler: ParacStreamHandler = None
    file_handler: ParacFileHandler = None

    @property
    def log_initialised(self) -> bool:
        """ Returns whether the logger is initialised and ready to be used """
        return getattr(self, 'logger') is not None

    @classmethod
    def init_logging_session(
            cls,
            log_path: Union[str, PathLike, pathlib.Path] = None,
            level: int = logging.INFO,
            print_banner: bool = True,
            banner_name: str = "Compiler",
            additional_newline: bool = True
    ):
        """
        Initialising the logging module for the Compiler
        and adds the formatting defaults

        :param log_path: Path where the log file should be placed. If None
         logging to files will be ignored
        :param level: Level the logger should be initialised with.
         Defaults to INFO
        :param print_banner: If set to True the logging banner will be printed
        :param banner_name: The name used for the logging banner
        :param additional_newline: If set to True an additional newline will be
         added before the logging banner
        """
        if print_banner:
            print_log_banner(banner_name, additional_newline)

        cls.logger: logging.Logger = logging.getLogger("parac")
        cls.logger.setLevel(level)

        # if the stream handler exists it will always get removed by default
        if cls.stream_handler:
            cls.logger.removeHandler(cls.stream_handler)

        # if the file handler exists and a new log_path was passed ->
        # remove and generate new file_handler
        if cls.file_handler and log_path:
            cls.logger.removeHandler(cls.file_handler)

        cls.stream_handler = ParacStreamHandler()
        cls.stream_handler.setFormatter(ParacFormatter(datefmt="%H:%M:%S"))
        cls.logger.addHandler(cls.stream_handler)

        if type(log_path) in (str, pathlib.Path) \
                and log_path.lower() != 'none':
            try:
                path: Path = ensure_pathlib_path(log_path)
                cls.file_handler = ParacFileHandler(filename=path)
            except PermissionError:
                raise FilePermissionError(
                    "Failed to access the specified log file-path"
                )
            cls.file_handler.setFormatter(ParacFormatter(file_mng=True))
            cls.logger.addHandler(cls.file_handler)

        if type(log_path) is str:
            if '.' not in log_path:
                logger.warning(
                    "The log-path does not contain the '.log' file-ending"
                )

    @staticmethod
    async def parse(
            input_stream: antlr4.InputStream,
            log_errors_and_warnings: bool = True
    ) -> CompilationUnitContext:
        """
        Parses the passed input_stream using antlr4 and returns the
        compilation unit context which can be used with the listener to compile
        and process the file

        :param input_stream: The token stream of the file
        :param log_errors_and_warnings: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        :returns: The compilationUnit (file) context
        :raises ParaCSyntaxError: If the parsing failed due to a syntax issue
         aka. input error from the user.
        """
        # Error handler which uses the default error strategy to handle the
        # incoming antlr4 errors
        error_listener = ParacErrorListener()

        # Initialising the lexer, which will tokenize the input_stream and
        # raise basic errors if needed
        lexer = ParaCLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        logger.debug("Lexing the file and generating the tokens")

        # Parsing the lexer and generating a token stream
        stream = antlr4.CommonTokenStream(lexer)

        # Parser which generates based on the top entry rule the logic tree
        parser = ParaCParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        # Parsing from the entry - compilationUnit
        cu = parser.compilationUnit()

        # Raise one or multiple errors if they were caught during the parsing
        if len(error_listener.errors) > 0:
            raise ParaCSyntaxErrorCollection(
                error_listener.errors,
                log_errors_and_warnings
            )  # Raising the syntax error/s

        return cu

    @classmethod
    async def validate_syntax(
            cls,
            process: BasicProcess,
            log_errors_and_warnings: bool = True
    ) -> None:
        """
        Validates the syntax of a file and logs or raises errors while running.

        :param process: The BasicProcess containing the path to the entry-file
        :param log_errors_and_warnings: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance,
         instead of directly returned. They will be 'raised from' with the
         FailedToProcessError exception.
        :raises FailedToProcessError: If log_errors_and_warnings is True and
         an exception is encountered. The logs of the exception will be printed
         onto the console.
        :raises ParacCompilerError: If any exception is encountered and
         log_errors_and_warnings is False
        """
        file_stream: antlr4.FileStream = get_file_stream(
            process.entry_file_path, process.encoding
        )
        stream: antlr4.InputStream = get_input_stream(
            cls.remove_comments_from_str(file_stream.strdata),  # rm comments
            name=file_stream.name
        )
        try:
            cls.logger.info(f"Parsing file ({file_stream.fileName})")
            await cls.parse(stream, log_errors_and_warnings)

        except (LexerError, ParaCSyntaxErrorCollection, LinkerError,
                ParacCompilerError) as e:
            if log_errors_and_warnings:
                raise FailedToProcessError(exc=e) from e
            else:
                raise e

        cls.logger.info(
            "Successfully finished syntax-check for file "
            f"{file_stream.fileName}"
        )

    @staticmethod
    def remove_comments_from_str(
        string: str, line_ending: str = '\n'
    ) -> str:
        """
        Removes comments from the passed string and returns the modified
        string. Only comments in the (// ... ) and (/* ... */) format will
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
    async def compile_logic_stream(
            cls,
            logic_stream: ParacLogicStream
    ) -> CLogicStream:
        """ Compiles the passed ParacLogicStream into the C counterpart """
        ...
