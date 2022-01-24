# coding=utf-8
""" Main compiler management file """
from __future__ import annotations

import logging
import pathlib
from os import PathLike
from pathlib import Path
from typing import Union, TYPE_CHECKING, Tuple, Literal

import antlr4

from .error_handler import ParaErrorListener
from .logic_stream import ParaQualifiedLogicStream, CLogicStream
from .parser.python import ParaLexer
from .parser.python import ParaParser
from .process import BasicProcess
from ..exceptions import (FilePermissionError, LexerError, LinkerError,
                          ParaCompilerError, FailedToProcessError,
                          ParaSyntaxErrorCollection)
from ..logging import (ParaFormatter, ParaFileHandler, ParaStreamHandler,
                       print_log_banner)
from ..util import get_file_stream, get_input_stream, ensure_pathlib_path

if TYPE_CHECKING:
    from .parser.listener import CompilationUnitContext

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
    logger: logging.Logger = None
    stream_handler: ParaStreamHandler = None
    file_handler: ParaFileHandler = None

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

        cls.logger: logging.Logger = logging.getLogger("para")
        cls.logger.setLevel(level)

        # if the stream handler exists it will always get removed by default
        if cls.stream_handler:
            cls.logger.removeHandler(cls.stream_handler)

        # if the file handler exists and a new log_path was passed ->
        # remove and generate new file_handler
        if cls.file_handler and log_path:
            cls.logger.removeHandler(cls.file_handler)

        cls.stream_handler = ParaStreamHandler()
        cls.stream_handler.setFormatter(ParaFormatter(datefmt="%H:%M:%S"))
        cls.logger.addHandler(cls.stream_handler)

        if type(log_path) in (str, pathlib.Path) \
                and log_path.lower() != 'none':
            try:
                path: Path = ensure_pathlib_path(log_path)
                cls.file_handler = ParaFileHandler(filename=path)
            except PermissionError:
                raise FilePermissionError(
                    "Failed to access the specified log file-path"
                )
            cls.file_handler.setFormatter(ParaFormatter(file_mng=True))
            cls.logger.addHandler(cls.file_handler)

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

        # Parser which generates based on the top entry rule the logic tree
        parser = ParaParser(stream)
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

    @classmethod
    async def validate_syntax(
            cls,
            file: Union[str, PathLike, pathlib.Path],
            encoding: str,
            prefer_logging: bool = True
    ) -> None:
        """
        Validates the syntax of a file and logs or raises errors while running.

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
            cls.remove_comments_from_str(file_stream.strdata),  # rm comments
            name=file_stream.name
        )
        try:
            cls.logger.info(f"Parsing file ({file_stream.fileName})")
            await cls.parse(stream, prefer_logging)

        except (LexerError, ParaSyntaxErrorCollection, LinkerError,
                ParaCompilerError) as e:
            if prefer_logging:
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
    async def compile_logic_stream(
            cls,
            logic_stream: ParaQualifiedLogicStream
    ) -> CLogicStream:
        """
        Compiles the passed ParaQualifiedLogicStream into the C counterpart
        """
        ...
