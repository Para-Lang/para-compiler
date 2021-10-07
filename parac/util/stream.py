# coding=utf-8
""" Stream File for implementing functions for the antlr4 streams """
import pathlib
from os import PathLike
from typing import Union
import antlr4

from .pathtools import ensure_pathlib_path

__all__ = [
    "get_file_stream",
    "get_input_stream"
]


def get_file_stream(
        path: Union[str, PathLike, pathlib.Path], encoding: str
) -> antlr4.FileStream:
    """
    Fetches the FileStream from a file

    :raises ValueError: If the passed value is not a valid path to a file
    """
    path: pathlib.Path = ensure_pathlib_path(path)
    if not path.is_file():
        raise ValueError("The passed value is not a valid file")

    stream = antlr4.FileStream(str(path), encoding)
    stream.name = path.name
    return stream


def get_input_stream(
        string: str, name: str
) -> antlr4.InputStream:
    """ Creates a new InputStream based on the passed string """
    stream = antlr4.InputStream(string)
    stream.name = name
    return stream
