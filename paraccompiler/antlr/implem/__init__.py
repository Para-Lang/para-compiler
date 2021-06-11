# coding=utf-8
""" Tokenizer and Basic Analyser for the Para-C code """
from os import PathLike
from typing import Union, List

__all__ = [
    'Parser'
]

from .token import Token
from .out import parse_file


class Parser:
    """
    Tokenizer class which is used as the interface for tokenising and parsing
    a file
    """

    @staticmethod
    def antlr_parse(
            path: Union[str, PathLike],
            encoding: str = 'ascii'
    ) -> List[Token]:
        """ Parses the file using antlr and returns the parse treess """
        return parse_file(path, encoding)
