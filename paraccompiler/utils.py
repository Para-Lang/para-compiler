# coding=utf-8
""" Utility in the Para-C Compiler"""
import logging
import re
import os
from click.utils import WIN
from os import PathLike
from typing import Union, Type


__all__ = [
    'SEPARATOR',
    'decode_if_bytes',
    'cleanup_path',
    'escape_ansi',
    'SpecialBoolDefault'
]

logger = logging.getLogger(__name__)

SEPARATOR = "\\" if WIN else "/"


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
