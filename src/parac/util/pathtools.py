# coding=utf-8
""" Path-tools for managing path usage and implementation in the Compiler """
import os
from typing import Union, Type, Optional

_in_FileNotFoundError = FileNotFoundError
from ..exceptions import FilePermissionError, FileNotFoundError
from ..const import (SEPARATOR, INVALID_UNIX_FILE_NAME_CHARS,
                     INVALID_WIN_FILE_NAME_CHARS, WIN, VALID_FILE_ENDINGS)

__all__ = [
    "validate_file_ending",
    "validate_path_like",
    "decode_if_bytes",
    "cleanup_path_str",
    "check_valid_path_name",
    "get_relative_file_name"
]


def validate_file_ending(path: Union[str, os.PathLike]) -> bool:
    """
    Validates the file ending of the passed path and returns as bool whether
    it follows the correct requirements
    """
    return all(map(path.endswith, VALID_FILE_ENDINGS))


def validate_path_like(path_like: Union[os.PathLike, str]) -> None:
    """
    Checking whether path exists and the user has permission to access it.
    Raises Exception on failure else returns

    :raises EntryFileNotFoundError: If the file can't be found
    :raises EntryFilePermissionError: If the file can't be read from
    """
    # Due to an empty string '' being recognised as existing it will be
    # excluded from the check
    valid_in = str(path_like).strip() != ''

    if not valid_in or not os.access(path_like, os.F_OK):  # Exists
        raise FileNotFoundError(
            f"Failed to read entry-point '{path_like}'."
            f" File does not exist!"
        )
    elif not os.access(path_like, os.R_OK):  # Can be read:
        raise FilePermissionError(
            f"Missing file reading permissions for ''{path_like}'"
        )


def decode_if_bytes(
        byte_like: Union[str, bytes, os.PathLike, Type],
        encoding: str = "utf-8"
) -> Union[str, os.PathLike]:
    """ Decodes the passed PathLike if it is in bytes """
    if type(byte_like) is str:
        return byte_like
    elif type(byte_like) is bytes or isinstance(byte_like, bytes):
        return byte_like.decode(encoding)
    else:
        return byte_like


def cleanup_path_str(_p: str) -> str:
    """ Cleans the path for the specific current os """
    if WIN:
        _p = _p.replace("/", SEPARATOR).replace("\\\\", SEPARATOR)
    else:
        # UNIX path
        _p = _p.replace("\\", SEPARATOR).replace("\\\\", SEPARATOR)

    if _p.startswith(f".{SEPARATOR}"):
        _p = os.getcwd() + _p[1:]  # Replacing . with current directory
    return _p


def check_valid_path_name(
        path: Union[str, os.PathLike],
        win_path: Optional[bool] = None
) -> bool:
    """
    Checks whether the name is a valid path-name. This means the file name
    cannot contain < , > , : , " , / , \\ (Escaped) , | , ? , *

    :param path: A path-like or file-name which should be checked
    :param win_path: If explicitly set to True, the path will be checked if it
    was a windows path, even if it's a os of a different kind
    """
    path = cleanup_path_str(path)
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
        file_path: Union[str, os.PathLike],
        base_path: Union[str, os.PathLike],
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
    file_path = cleanup_path_str(file_path)
    base_path = cleanup_path_str(base_path)

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
