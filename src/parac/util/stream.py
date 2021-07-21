# coding=utf-8
""" Stream File for implementing functions for the antlr4 streams """
from os import PathLike
from typing import Union
import antlr4

__all__ = [
    "get_file_stream",
    "get_input_stream"
]


def get_file_stream(
        path: Union[str, PathLike], encoding: str
) -> antlr4.FileStream:
    """ Fetches the FileStream from a file """
    from ..const import SEPARATOR
    stream = antlr4.FileStream(path, encoding)
    stream.name = path.split(SEPARATOR)[-1]
    return stream


def get_input_stream(
        string: str, name: str
) -> antlr4.InputStream:
    """ Creates a new InputStream based on the passed string """
    stream = antlr4.InputStream(string)
    stream.name = name
    return stream
