# coding=utf-8
""" Main compiler management file """
from __future__ import annotations

import json
import logging
import os
import sys
import time
from os import PathLike
from typing import Union, Generator, Tuple, Dict, TYPE_CHECKING
import antlr4

from .parser.python import ParaCLexer
from .parser.python import ParaCParser
from .parser.listener import Listener
from .compilation_ctx import ProgramCompilationContext
from ..logger import (ParacFormatter, ParacFileHandler, ParacStreamHandler,
                      get_rich_console as console, print_log_banner,
                      ParacErrorListener)
from ..utils import decode_if_bytes, cleanup_path, SEPARATOR
from ..para_exceptions import (FilePermissionError,
                               FileNotFoundError, FileAccessError,
                               CCompilerError, LexerError, LinkerError,
                               ParacCompilerError, CCompilerNotFoundError)

if TYPE_CHECKING:
    from .parser.listener import CompilationUnitContext
    from .compilation_ctx import FileCompilationContext

__all__ = [
    'INIT_OVERWRITE',
    'COMPILER_DIR',
    'is_c_compiler_ready',
    'ProgramCompilationContext',
    'initialise_c_compiler',
    'VALID_FILE_ENDINGS',
    'DEFAULT_LOG_PATH',
    'DEFAULT_BUILD_PATH',
    'DEFAULT_DIST_PATH',
    'ParacCompiler',
    'BasicProcess',
    'ProgramCompilationProcess',
    'FinishedProcess'
]

logger = logging.getLogger(__name__)

VALID_FILE_ENDINGS = [".para", ".parah", ".c", ".h", ".ph"]

DEFAULT_LOG_PATH: str = "./para.log"
DEFAULT_BUILD_PATH: str = "./build"
DEFAULT_DIST_PATH: str = "./dist"

# If the init overwrite is true =>
# Existence check for the c-compiler will always return True
INIT_OVERWRITE: bool = False

COMPILER_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
CONFIG_PATH = ""
DEFAULT_CONFIG = {
    "c-compiler-path": ""
}


def _valid_file_ending(path: Union[str, PathLike]) -> bool:
    return all(map(path.endswith, VALID_FILE_ENDINGS))


def validate_path_like(path_like: Union[PathLike, str]) -> None:
    """
    Checking whether path exists and the user has permission to access it.
    Raises Exception on failure else returns

    :raises EntryFileNotFoundError: If the file can't be found
    :raises EntryFilePermissionError: If the file can't be read from
    """
    if not os.access(path_like, os.R_OK):  # Can be read
        if not os.access(path_like, os.F_OK):  # Exists
            raise FileNotFoundError(
                f"Failed to read entry-point '{path_like}'."
                f" File does not exist!"
            )
        else:
            raise FilePermissionError(
                f"Missing file reading permissions for ''{path_like}'"
            )


def is_c_compiler_ready() -> bool:
    """
    Returns whether the Para-C Compiler is correctly
    initialised and the c-compiler can be found
    """
    if INIT_OVERWRITE:
        return True

    global COMPILER_DIR
    COMPILER_DIR = cleanup_path(COMPILER_DIR)
    global CONFIG_PATH
    CONFIG_PATH = f"{COMPILER_DIR}{SEPARATOR}compile-config.json"

    if os.access(CONFIG_PATH, os.R_OK):
        with open(CONFIG_PATH, "r") as file:
            config: dict = json.loads(file.read())
            if config.get('c-compiler-path'):
                # if executable
                return os.access(config['c-compiler-path'], os.X_OK)
    return False


def initialise_c_compiler() -> None:
    """
    Initialises the Para-C compiler and creates the config file.
    Will prompt the user to enter the compiler path
    """
    _input = console().input(
        "[bold bright_cyan]"
        " > Please enter the path for the C-compiler: "
        "[/bold bright_cyan]"
    )
    console().print('\n', end="")
    path = cleanup_path(decode_if_bytes(_input))

    # it exists
    if not os.access(_input, os.F_OK):
        raise CCompilerNotFoundError(
            f"The passed path '{path}' for the executable does not exist"
        )

    # is executable
    if not os.access(_input, os.X_OK):
        raise FilePermissionError(
            f"The passed path '{path}' for the executable can't be executed."
            " Possibly missing Permissions?"
        )

    config = DEFAULT_CONFIG
    config['c-compiler-path'] = path
    with open(CONFIG_PATH, "w+") as file:
        file.write(json.dumps(config, indent=4))

    logger.info(
        "Validated path and successfully created compile-config.json"
    )


class BasicProcess:
    """ Basic Process serving as parent class for the process instances """

    def __init__(
            self,
            entry_file: Union[str, bytes, PathLike],
            encoding: str
    ):
        """
        Initialises the instance and validates the passed entry file for
        further usage.

        :param entry_file: The entry-file of the program. The compiler will use
                           the working directory as base dir if the path is
                           relative
        """
        entry_file = cleanup_path(decode_if_bytes(entry_file))

        _last_path_elem = entry_file.replace("/", "\\").split("\\")[-1]
        # for the sake of checking; all paths used are converted into
        # the windows path-style
        if "." not in _last_path_elem or _last_path_elem.endswith("\\"):
            ParacCompiler.logger.warning(
                "The given file does not seem to be in the correct format!"
            )
        elif _valid_file_ending(_last_path_elem):
            ParacCompiler.logger.warning(
                "The given file ending does not follow "
                "the Para-C conventions (.para, .ph, .c, .h, .parah)!"
            )

        try:
            validate_path_like(entry_file)
        except FileAccessError as e:
            # If the validation failed the path might be a relative path
            # that does not have a . signalising its going python from the
            # current path meaning the work-directory path needs to be
            # appended. If that also fails it is an invalid path or permissions
            # are missing
            absolute_path = cleanup_path(f"{os.getcwd()}\\{entry_file}")
            failed = False
            try:
                validate_path_like(absolute_path)
            except FileAccessError:
                failed = True
            if failed:
                raise e
            entry_file = absolute_path
        self._entry_file = entry_file
        self._encoding = encoding

    @property
    def entry_file(self) -> Union[str, PathLike]:
        """ Returns the entry-file of the process """
        return self._entry_file

    @property
    def encoding(self) -> str:
        """ Returns the encoding of the process """
        return self._encoding

    def validate_syntax(self, enable_out: bool) -> bool:
        """
        Validates the syntax of the file of this entry-file and logs or raises
        errors while running

        :param enable_out: If set to True errors, warnings and info will be
                           logged onto the console using the local logger
                           instance. (Errors will then NOT be raised but only
                           logged)
        :returns: True if the syntax check was successful else False
        """
        return ParacCompiler.validate_syntax(self, enable_out)


class FinishedProcess(BasicProcess):
    """ Class used to represent a done compilation process """

    def __init__(self, process: ProgramCompilationProcess):
        self.done_process = process
        super().__init__(process.entry_file, process.encoding)


class ProgramCompilationProcess(BasicProcess):
    """ Process instance used for a program compilation process """

    def __init__(
            self,
            entry_file: Union[str, bytes, PathLike],
            encoding: str,
            build_path: Union[str, bytes, PathLike],
            dist_path: Union[str, bytes, PathLike]
    ):
        """
        Initialises and validates the provided parameter for the compilation
        process. In case of an error an exception will be raised and the
        process cancelled.

        :param entry_file: The entry-file of the program. The compiler will use
                           the working directory as base dir if the path is
                            relative
        :param build_path: The path to the output folder
        :param dist_path: The path to the dist folder
        :returns: The file name, the output build path, the output dist path
                  and the arguments passed for the compilation
        """
        super().__init__(entry_file, encoding)

        build_path: Union[str, PathLike] = decode_if_bytes(build_path)
        dist_path: Union[str, PathLike] = decode_if_bytes(dist_path)

        self._build_path = build_path
        self._dist_path = dist_path
        self._context = ProgramCompilationContext(self)

    @property
    def context(self) -> ProgramCompilationContext:
        """ Context for the compilation """
        return self._context

    @property
    def entry_file(self) -> Union[str, PathLike]:
        """ Entry file of the program """
        return self._entry_file

    @property
    def build_path(self) -> Union[str, PathLike]:
        """ Path to the build folder """
        return self._build_path

    @property
    def dist_path(self) -> Union[str, PathLike]:
        """ Path to the dist folder """
        return self._dist_path

    def compile_with_progress_iterator(
            self
    ) -> Generator[Tuple[int, str, int, FinishedProcess], None, None]:
        """
        Runs the compilation but yields the progress in form of tuples:
        int - Progress count from 0 to 1000 (0 = 0%, 1000 = 100%)
        str - Name of the next step in form of a string. Is None when the
              process finished
        int - Log level for the returned string message
        FinishedProcess - None until the process finally finished

        For info on compiling go to compile()
        """

        # Currently only a replacement for testing purposes
        yield 50, "Fetching files", logging.INFO, None
        time.sleep(5)
        yield 1000, None, logging.INFO, FinishedProcess(self)

    def compile(self) -> FinishedProcess:
        """
        Default function which compiles the passed input data and returns
        a new finished process instance
        """
        # Currently empty since the compilation is not done yet
        ...


class ParacCompiler:
    """ Main Class for the Para-C compiler containing the main functions """
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
            print_log_banner(banner_name)

        cls.logger: logging.Logger = logging.getLogger("paraccompiler")
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
    def parse(
            input_stream: antlr4.FileStream,
            enable_out: bool = True
    ) -> CompilationUnitContext:
        """
        Parses the passed input_stream using antlr4 and returns the
        compilation unit context which can be used with the listener to compile
        and process the file

        :param input_stream: The token stream of the file
        :param enable_out: If set to True errors, warnings and info will be
                   logged onto the console using the local logger
                   instance. (Errors will then NOT be raised but only
                   logged)
        :returns: The compilationUnit (file) context
        """
        # Listener which will implement the ParaC exceptions
        error_listener = ParacErrorListener(enable_out)

        # Initialising the lexer, which will analyse the input_stream and
        # raise basic errors if needed
        lexer = ParaCLexer.ParaCLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        logger.debug("Lexing the file and generating the tokens")

        # Parsing the lexer and generating a token stream
        stream = antlr4.CommonTokenStream(lexer)

        logger.debug("Parsing the tokens and generating the logic tree")

        # Parser which should generate the logic trees
        parser = ParaCParser.ParaCParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        return parser.compilationUnit()

    @classmethod
    def validate_syntax(
            cls,
            process: BasicProcess,
            enable_out: bool = True
    ) -> bool:
        """
        Validates the syntax of a file and logs or raises errors while running

        :param process: The BasicProcess containing the path to the entry-file
        :param enable_out: If set to True errors, warnings and info will be
                           logged onto the console using the local logger
                           instance. (Errors will then NOT be raised but only
                           logged)
        :returns: True if the syntax check was successful else False
        """
        stream = cls.get_file_stream(process.entry_file, process.encoding)

        try:
            unit_ctx = cls.parse(stream, enable_out)

            # Walking through the tree but without compiling! -> Only default
            # structure and syntax will be validated and checked
            listener = Listener(unit_ctx, stream)
            listener.walk(enable_out)

        except (LexerError, LinkerError, ParacCompilerError):
            # TODO! Add proper error handling and logging
            ...
            return False

        from ..__main__ import para_compiler

        if para_compiler.stream_handler.errors > 0:
            return False
        return True

    @staticmethod
    def get_file_stream(
            path: Union[str, PathLike], encoding: str
    ) -> antlr4.FileStream:
        """ Fetches the FileStream from a file"""
        stream = antlr4.FileStream(path, encoding)
        stream.name = path.split(SEPARATOR)[-1]
        return stream

    @classmethod
    def antlr_parse_and_compile(
            cls,
            ctx: ProgramCompilationContext,
            enable_out: bool = True
    ) -> Dict[str, Dict[str, FileCompilationContext]]:
        """
        Parses the file using Antlr and runs the compilation over the listener.
        The listener here will serve as the base where the logical processes
        will run over and where the resulting C-code will be constructed.

        :returns: Generated Output Dict
                  -> see CompilationContext.generate_source()
        """
        stream = cls.get_file_stream(
            ctx.process.entry_file, ctx.process.encoding
        )
        unit_ctx = cls.parse(stream, enable_out)

        # Walking through the file and triggering the functions inside the
        # listener -> Basic compilation
        listener = Listener(unit_ctx, stream)
        listener.walk_and_compile(enable_out)

        ctx.set_entry_ctx(listener.file_ctx)

        # TODO! Generate the tokens based on the return of the listener and
        # manage all dependencies -> generating the tokens for these files as
        # well. Merging in the end all files in the CompilationContext, where
        # the final compiling and logical checking will occur. In the end
        # the optimiser should optimise the imports and remove unneeded parts.

        return ctx.generate_source()
