""" Main compiler management file """
import logging
import os
from os import PathLike
from typing import Union, Type

from . import ParacFormatter, ParacFileHandler, ParacStreamHandler, WIN
from .logger import output_console
from .exceptions import EntryFilePermissionError, EntryFileNotFoundError, EntryFileAccessError

__all__ = [
    'DEFAULT_LOG_PATH',
    'DEFAULT_BUILD_PATH',
    'DEFAULT_DIST_PATH',
    'ParacCompiler',
    'CompilationProcess',
    'FinishedProcess'
]

DEFAULT_LOG_PATH: str = "./para.log"
DEFAULT_BUILD_PATH: str = "./build"
DEFAULT_DIST_PATH: str = "./dist"
SEPARATOR = "\\" if WIN else "/"


def _decode_if_bytes(byte_like: Union[str, bytes, PathLike, Type]):
    if type(byte_like) is str:
        return byte_like
    elif type(byte_like) is bytes or isinstance(bytes, byte_like):
        return byte_like.decode()
    else:
        return byte_like


def _cleanup_path(_p: str) -> str:
    if WIN:
        _p = _p.replace("/", SEPARATOR).replace("\\\\", SEPARATOR)
    else:
        # UNIX path
        _p = _p.replace("\\", SEPARATOR).replace("\\\\", SEPARATOR)

    if _p.startswith(f".{SEPARATOR}"):
        # Replacing . with current directory
        _p = os.getcwd() + _p[1:]
    return _p


def _validate_path_like(path_like: Union[PathLike, str]) -> None:
    """ Checking whether path exists and the user has permission to access it. Raises Exception on failure else returns

    :raises EntryFileNotFoundError: If the file can't be found
    :raises EntryFilePermissionError: If the file can't be read from
    """
    if not os.access(path_like, os.R_OK):  # Can be read
        if not os.access(path_like, os.F_OK):  # Exists
            raise EntryFileNotFoundError(f"Failed to read entry-point '{path_like}'. File does not exist!")
        else:
            raise EntryFilePermissionError(f"Missing file reading permissions for ''{path_like}'")


class ParacCompiler:
    """ Main Class for the Para-C compiler containing the main functions """
    logger: logging.Logger = None

    @property
    def log_initialised(self) -> bool:
        """ Returns whether the logger is initialised and ready to be used """
        return getattr(self, 'logger') is not None

    @classmethod
    def init_logging_session(cls, log_path: Union[str, PathLike], level: int):
        """ Initialising the logging module for the Compiler and adds the formatting defaults """
        cls.logger: logging.Logger = logging.getLogger("paraccompiler")
        cls.logger.setLevel(level)

        stream_handler = ParacStreamHandler(console=output_console)
        stream_handler.setFormatter(ParacFormatter(datefmt="%H:%M:%S"))
        cls.logger.addHandler(stream_handler)

        if log_path.lower() != 'none':
            try:
                handler = ParacFileHandler(filename=f'./{log_path}')
            except PermissionError:
                raise EntryFilePermissionError("Failed to access the specified log file-path")
            handler.setFormatter(ParacFormatter(file_mng=True))
            cls.logger.addHandler(handler)


class CompilationProcess:
    """ Process instance used for a single compilation process """

    def __init__(
            self,
            entry_file: Union[str, bytes, PathLike],
            build_path: Union[str, bytes, PathLike],
            dist_path: Union[str, bytes, PathLike]
    ):
        self._entry_file = entry_file
        self._build_path = build_path
        self._dist_path = dist_path

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

    @classmethod
    def create_from_args(
            cls,
            entry_file: Union[str, bytes, PathLike],
            build_path: Union[str, bytes, PathLike],
            dist_path: Union[str, bytes, PathLike]
    ):
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
        entry_file: Union[str, PathLike] = _decode_if_bytes(entry_file)
        build_path: Union[str, PathLike] = _decode_if_bytes(build_path)
        dist_path: Union[str, PathLike] = _decode_if_bytes(dist_path)

        path = _cleanup_path(entry_file)

        _last_path_elem = path.replace("/", "\\").split("\\")[-1]
        # for the sake of checking all paths used are converted into the windows path-style, but only while checking
        if "." not in _last_path_elem or _last_path_elem.endswith("\\"):
            ParacCompiler.logger.warning("The given file does not seem to be a file!")
        elif not _last_path_elem.endswith('.para') and not _last_path_elem.endswith('.ph'):
            ParacCompiler.logger.warning("The given file ending does not follow the Para-C conventions (.para, .ph)!")

        try:
            _validate_path_like(path)
        except EntryFileAccessError:
            # If the validation failed the path might be a relative path
            # that does not have a . signalising its going out from the
            # current path meaning the work-directory path needs to be appended.
            # If that also fails it is an invalid path or permissions are missing
            absolute_path = _cleanup_path(f"{os.getcwd()}\\{path}")
            try:
                _validate_path_like(absolute_path)
            except EntryFileAccessError:
                raise
            path = absolute_path

        return cls(path, build_path, dist_path)


class FinishedProcess:
    """ Class used to represent a done compilation process """

    def __init__(self, p: CompilationProcess):
        self.p = p
