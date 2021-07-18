# coding=utf-8
""" Utility in the Para-C Compiler"""
import json
import logging
import re
import os
from os import PathLike
from typing import Union, Type, Optional

__all__ = [
    'validate_file_ending',
    'validate_path_like',
    'is_c_compiler_ready',
    'initialise_c_compiler',
    'decode_if_bytes',
    'cleanup_path',
    'escape_ansi',
    'check_valid_path_name',
    'get_relative_file_name',
    'SpecialBoolDefault'
]


from .logging import get_rich_console as console
from .para_exceptions import FilePermissionError, CCompilerNotFoundError

logger = logging.getLogger(__name__)


def validate_file_ending(path: Union[str, PathLike]) -> bool:
    """
    Validates the file ending of the passed path and returns as bool whether
    it follows the correct requirements
    """
    from . import VALID_FILE_ENDINGS
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
    from . import INIT_OVERWRITE, CONFIG_PATH
    if INIT_OVERWRITE:
        return True

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
    from . import CONFIG_PATH
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

    from . import DEFAULT_CONFIG
    config = DEFAULT_CONFIG
    config['c-compiler-path'] = path
    with open(CONFIG_PATH, "w+") as file:
        file.write(json.dumps(config, indent=4))

    logger.info(
        "Validated path and successfully created compile-config.json"
    )


def decode_if_bytes(
        byte_like: Union[str, bytes, PathLike, Type],
        encoding: str = "utf-8"
) -> Union[str, PathLike]:
    """ Decodes the passed PathLike if it is in bytes """
    if type(byte_like) is str:
        return byte_like
    elif type(byte_like) is bytes or isinstance(bytes, byte_like):
        return byte_like.decode(encoding)
    else:
        return byte_like


def cleanup_path(_p: str) -> str:
    """ Cleans the path for the specific current os """
    from . import WIN, SEPARATOR
    if WIN:
        _p = _p.replace("/", SEPARATOR).replace("\\\\", SEPARATOR)
    else:
        # UNIX path
        _p = _p.replace("\\", SEPARATOR).replace("\\\\", SEPARATOR)

    if _p.startswith(f".{SEPARATOR}"):
        _p = os.getcwd() + _p[1:]  # Replacing . with current directory
    return _p


def escape_ansi(string: str) -> str:
    """ Removes ansi colouring in the passed string """
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', string)


def check_valid_path_name(
        path: Union[str, PathLike],
        win_path: Optional[bool] = None
) -> bool:
    """
    Checks whether the name is a valid path-name. This means the file name
    cannot contain < , > , : , " , / , \\ (Escaped) , | , ? , *

    :param path: A path-like or file-name which should be checked
    :param win_path: If explicitly set to True, the path will be checked if it
                     was a windows path, even if it's a os of a different kind
    """
    from . import (SEPARATOR, INVALID_UNIX_FILE_NAME_CHARS,
                   INVALID_WIN_FILE_NAME_CHARS, WIN)
    path = cleanup_path(path)
    path = path.replace(SEPARATOR, '')

    if WIN or win_path:
        if path[1:].startswith(':'):
            path = path[2:]

        if path.endswith(' ') or path.endswith('.'):
            return False
        char_set = INVALID_WIN_FILE_NAME_CHARS
    else:
        char_set = INVALID_UNIX_FILE_NAME_CHARS

    count = 0
    for c in path:
        if 0 <= ord(c) < 28:  # Control chars are forbidden
            return False
        if c in char_set:
            return False
        count += 1
    return True


def get_relative_file_name(
        file_name: str,
        file_path: Union[str, PathLike],
        base_path: Union[str, PathLike],
        win_path: Optional[bool] = None
) -> str:
    """
    Gets the relative file name from the passed str. If the file_path does not
    match the file_name passed RuntimeError will be raised

    :param file_name: Simple file name which cannot contain < , > , : , " , / ,
                      \\ (Escaped) , | , ? , *
    :param file_path: Full path of the file
    :param base_path: Full base path for the working directory
    :param win_path: If explicitly set to True, the path will be checked if it
                     was a windows path, even if it's a os of a different kind
    """
    from . import SEPARATOR
    file_path = cleanup_path(file_path)
    base_path = cleanup_path(base_path)

    if base_path not in file_path:
        raise RuntimeError(
            "base_path and file_path are mismatching. file_path is not in "
            "base_path"
        )

    if ' ' in file_name:
        raise RuntimeError(
            "The Para-C naming conventions do not allow spaces in the filename"
        )

    relative_path = file_path.replace(base_path, '')
    if relative_path.startswith(SEPARATOR):
        relative_path = relative_path[len(SEPARATOR):]

    if not check_valid_path_name(file_path, win_path):
        raise RuntimeError(
            "The file_path contains invalid characters that can not be "
            "processed"
        )

    if not check_valid_path_name(base_path, win_path):
        raise RuntimeError(
            "The base_path contains invalid characters that can not be "
            "processed"
        )

    if relative_path.split(SEPARATOR)[-1] != file_name:
        raise RuntimeError(
            "Mismatching file_names (file_path and file_name do not match)"
        )

    relative_file_name = ""

    relative_elements = relative_path.split(SEPARATOR)[:-1]
    for elem in relative_elements:
        relative_file_name += "".join((elem, "."))

    relative_file_name += file_name.split('.')[0]
    return relative_file_name


class SpecialBoolDefault:
    """
    Special Bool serving to separate wanted flags with default flags
    """

    def __init__(self, value: bool):
        if type(value) is not bool:
            raise ValueError("Expected boolean")
        self.true_default: bool = bool(value)
        self.actual_value: bool = bool(value)

    def set(self, value):
        """ Sets the actual_value in the instance """
        if type(bool) is bool:
            self.actual_value = value
        else:
            raise ValueError("Expected boolean")

    def __eq__(self, other):
        return self.actual_value == other

    def __hash__(self):
        return hash(self.actual_value)

    def __bool__(self):
        return self.actual_value
