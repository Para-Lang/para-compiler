# coding=utf-8
""" Path-tools for managing path usage and implementation in the Compiler """
import os
import pathlib
from typing import Union, Type, List

_in_FileNotFoundError = FileNotFoundError
from ..exceptions import FilePermissionError, FileNotFoundError


__all__ = [
    "has_valid_file_ending",
    "validate_path_like",
    "decode_if_bytes",
    "get_relative_file_name",
    "ensure_pathlib_path"
]


def has_valid_file_ending(path: Union[str, os.PathLike]) -> bool:
    """
    Validates the file ending of the passed path and returns as bool whether
    it follows the correct requirements
    """
    from .. import const
    # If any target is met, it's valid
    return any(map(path.endswith, const.VALID_FILE_ENDINGS))


def validate_path_like(path_like: Union[os.PathLike, str]) -> None:
    """
    Checking whether path exists and the user has permission to access it.
    Raises Exception on failure else returns

    :raises EntryFileNotFoundError: If the file can't be found
    :raises EntryFilePermissionError: If the file can't be read from
    """
    # Due to an empty string '' being recognised as existing it will be
    # excluded from the check
    empty_path = str(path_like).strip() == ''

    if empty_path or not os.access(path_like, os.F_OK):  # Exists
        raise FileNotFoundError(
            f"Failed to read entry-point '{path_like}'."
            f" File does not exist!"
        )
    elif not os.access(path_like, os.R_OK):  # Can be read
        raise FilePermissionError(
            f"Missing file reading permissions for ''{path_like}'"
        )


def decode_if_bytes(
        byte_like: Union[str, bytes, os.PathLike, Type],
        encoding: str = "utf-8"
) -> Union[str, os.PathLike]:
    """
    Decodes the passed PathLike if it is in bytes

    :raises UnicodeDecodeError: If the decoding failed
    """
    if type(byte_like) is bytes or isinstance(byte_like, bytes):
        return byte_like.decode(encoding)
    else:
        return byte_like


def get_relative_file_name(
        file_name: str,
        file_path: Union[str, os.PathLike],
        base_path: Union[str, os.PathLike],
) -> str:
    """
    Gets the relative file name from the passed str. If the file_path does not
    match the file_name passed RuntimeError will be raised

    :param file_name: File name
    :param file_path: Full path of the file
    :param base_path: Full base path for the working directory
    """
    file_path: pathlib.Path = ensure_pathlib_path(file_path)
    base_path: pathlib.Path = ensure_pathlib_path(base_path)

    if str(base_path) not in str(file_path):
        raise RuntimeError(
            "base_path and file_path are mismatching. file_path is not in "
            "base_path"
        )
    if ' ' in file_name:
        raise RuntimeError(
            "The Para-C naming conventions do not allow spaces in the filename"
        )

    # removing the base_path, which is the work-directory/source, where the
    # relative name should extend from -> ./../../
    relative_path: str = str(file_path).replace(str(base_path), '')

    # Resolving the relative path of the split path
    relative_path: pathlib.Path = pathlib.Path(
        relative_path[1:] if relative_path[0] in ("/", "\\") else relative_path
    )

    if relative_path.name != file_name:
        raise RuntimeError(
            f"Mismatching file_names (file_path: {relative_path.name} and "
            f"file_name: {file_name} do not match)"
        )

    # a/b/c/FILE.PARAC -> a.b.c.FILE
    relative_file_name = ""
    # get every item except the last one
    items: List[str] = list(relative_path.parts)[:-1]
    for elem in items:
        relative_file_name += "".join((elem, "."))

    # FILE.PARAC -> FILE
    relative_file_name += file_name.split('.')[0]
    return relative_file_name


def ensure_pathlib_path(
        p: Union[str, bytes, os.PathLike, pathlib.Path]
) -> pathlib.Path:
    """
    Ensures the entered path is of type pathlib.Path. If it's in bytes or a
    string, it will be converted to the pathlib.Path type.

    This will also resolve all sys-links. If it is bytes and has to be
    encoded, UTF-8 will be used by default.
    """
    if type(p) is str:
        p: pathlib.Path = pathlib.Path(p)
    elif type(p) is bytes:
        p: pathlib.Path = pathlib.Path(decode_if_bytes(p))
    elif not type(p) is pathlib.Path:
        # if this is a unique type then it will just attempt to use str() on it
        p: pathlib.Path = pathlib.Path(str(p))

    return p.resolve()
