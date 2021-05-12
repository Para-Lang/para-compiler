""" Main compiler management file """
import logging
import os
from . import ParacFormatter, ParacFileHandler
from .exceptions import FileWritingPermissionError

__all__ = [
    'DEFAULT_LOG_PATH',
    'DEFAULT_BUILD_PATH',
    'DEFAULT_DIST_PATH',
    'ParacCompiler',
    'CompilationProcess'
]

DEFAULT_LOG_PATH: str = "./para.log"
DEFAULT_BUILD_PATH: str = "./build"
DEFAULT_DIST_PATH: str = "./dist"


class ParacCompiler:
    """ Main Class for the Para-C compiler containing the main functions """
    logger: logging.Logger = None

    @property
    def log_initialised(self) -> bool:
        """ Returns whether the logger is initialised and ready to be used """
        return getattr(self, 'logger') is not None

    @classmethod
    def init_logging_session(cls, log_path: str, level: int):
        """ Initialising the logging module for the Compiler and adds the formatting defaults """
        cls.logger: logging.Logger = logging.getLogger("paraccompiler")
        cls.logger.setLevel(level)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(ParacFormatter(datefmt="%H:%M:%S"))
        cls.logger.addHandler(stream_handler)

        if log_path.lower() != 'none':
            try:
                handler = ParacFileHandler(filename=f'./{log_path}')
            except PermissionError:
                raise FileWritingPermissionError("Failed to access the specified log file-path")
            handler.setFormatter(ParacFormatter(file_mng=True))
            cls.logger.addHandler(handler)


class CompilationProcess:
    """ Process instance used for a single compilation process """
    def __init__(self, entry_file: str, build_path: str, dist_path: str):
        self.entry_file = entry_file
        self.build_path = build_path
        self.dist_path = dist_path

    @classmethod
    def create_from_args(cls, entry_file: str, build_path: str, dist_path: str):
        """
        Validates the provided setup parameter for the compilation process. In case of an error an
        exception will be raised and the process cancelled.

        :param entry_file: The entry-file of the program. The compiler will use the working directory as base dir if
                           the path is relative
        :param build_path: The path to the output folder
        :param dist_path: The path to the dist folder
        :returns: The file name, the output build path, the output dist path and the arguments passed for the
                  compilation
        """
        if not entry_file.endswith('.para') and not entry_file.endswith('.ph'):
            ParacCompiler.logger.warning("The given file ending does not follow the Para-C conventions (.para, .ph)")

        if not any([item in entry_file for item in ['\\', '/', '//']]):
            path = f"{os.getcwd()}\\{entry_file}"
        else:
            path = entry_file
        if not os.path.exists(path):
            raise FileNotFoundError(f"Failed to read entry-point path '{path}'. File does not exist!")

        return cls(entry_file, build_path, dist_path)