# coding=utf-8
""" Tokenizer and Basic Analyser for the Para-C code """

__all__ = ['Tokenizer']

from enum import Enum
from os import PathLike
from typing import Union, List


class CTokens(Enum):
    """ Native C tokens """
    ...


class ParacTokens(Enum):
    """ Tokens of the Para-C language that are not native to C """
    ...


class Tokenizer:
    """
    Tokenizer class which is used as the interface for tokenizing a file
    """
    @staticmethod
    def tokenize_file(
            file: Union[str, PathLike],
            encoding: str = "utf-8",
            line_endings: str = "\n"
    ) -> List[str]:
        """
        Tokenizes a file and checks for basic issues like valid characters
        sand basic syntax like known valid characters, valid usage of
        strings, ints etc.

        """
        tokens: List[str] = []

        return tokens

