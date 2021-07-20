# coding=utf-8
""" Main compiler management file """
from __future__ import annotations

import logging
from os import PathLike
from typing import Union, TYPE_CHECKING, Tuple, Literal
import antlr4

from .process import BasicProcess
from .error_handler import ParacErrorListener
from .logic_stream import ParacLogicStream, CLogicStream
from .parser.python import ParaCLexer
from .parser.python import ParaCParser
from .parser.listener import Listener
from ..logging import (ParacFormatter, ParacFileHandler, ParacStreamHandler,
                       print_log_banner)
from ..utils import get_relative_file_name, get_input_stream, get_file_stream
from ..para_exceptions import (FilePermissionError, LexerError, LinkerError,
                               ParacCompilerError)

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
            log_path: Union[str, PathLike] = None,
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
        :param additional_newline: If set to True an additional newline
                                   will be added before the logging banner
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

        if type(log_path) is str and log_path.lower() != 'none':
            try:
                cls.file_handler = ParacFileHandler(filename=f'./{log_path}')
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
            enable_out: bool = True
    ) -> CompilationUnitContext:
        """
        Parses the passed input_stream using antlr4 and returns the
        compilation unit context which can be used with the listener to compile
        and process the file

        :param input_stream: The token stream of the file
        :param enable_out: If set to True errors, warnings and info will be
                           logged onto the console using the local logger
                           instance. If an exception is raised or error is
                           encountered, it will be reraised with the
                           FailedToProcessError.
        :returns: The compilationUnit (file) context
        """
        # Error handler which uses the default error strategy to handle the 
        # incoming antlr4 errors
        error_listener = ParacErrorListener(enable_out)

        # Initialising the lexer, which will tokenize the input_stream and
        # raise basic errors if needed
        lexer = ParaCLexer.ParaCLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        logger.debug("Lexing the file and generating the tokens")

        # Parsing the lexer and generating a token stream
        stream = antlr4.CommonTokenStream(lexer)

        # Parser which generates based on the top entry rule the logic tree
        parser = ParaCParser.ParaCParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        return parser.compilationUnit()

    @classmethod
    async def validate_syntax(
            cls,
            process: BasicProcess,
            enable_out: bool = True
    ) -> bool:
        """
        Validates the syntax of a file and logs or raises errors while running

        :param process: The BasicProcess containing the path to the entry-file
        :param enable_out: If set to True errors, warnings and info will be
                           logged onto the console using the local logger
                           instance. If an exception is raised or error is
                           encountered, it will be reraised with the
                           FailedToProcessError.
        :returns: True if the syntax check was successful else False
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
            antlr4_file_ctx = await cls.parse(stream, enable_out)

            relative_file_name = get_relative_file_name(
                file_stream.name,
                file_stream.fileName,
                process.work_dir
            )

            # Walking through the tree but without compiling! -> Only default
            # structure and syntax will be validated and checked
            listener = Listener(antlr4_file_ctx, stream, relative_file_name)
            await listener.walk(enable_out)

        except (LexerError, LinkerError, ParacCompilerError):
            # TODO! Add proper error handling and logging
            return False

        from ..__main__ import para_compiler

        if para_compiler.stream_handler.errors > 0:
            return False
        return True

    @staticmethod
    def remove_comments_from_str(
        string: str, line_ending: str = '\n'
    ) -> str:
        """
        Removes comments from the passed string and returns the modified
        string. Only comments in the (// ... \\n) and (/* ... */) format will
        be removed, but else the string will be ignored.

        For proper handling line-endings are all set to \\n, if this is
        not wanted the wanted line ending should be passed. Note: This will
        not make the function ignore every other line-ending but simply in the
        end replace every occurrence of \n with the wanted line-ending.
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
                    prev_c = '\n'
            prev_c = c
        return result.replace('\n', line_ending)

    @classmethod
    async def compile_logic_stream(
            cls,
            logic_stream: ParacLogicStream
    ) -> CLogicStream:
        """ Compiles the passed ParacLogicStream into the Parac counterpart """
        ...
