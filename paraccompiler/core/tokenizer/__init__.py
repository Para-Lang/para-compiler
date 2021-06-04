# coding=utf-8
""" Tokenizer and Basic Analyser for the Para-C code """

__all__ = [
    'Tokenizer'
]

import abc
from enum import Enum
from os import PathLike
from typing import Union, List


class Tokenizer:
    """
    Tokenizer class which is used as the interface for tokenising a file
    """
    LINE_SEPERATOR = ";"

    @staticmethod
    def read_file_content(
            path: Union[str, PathLike],
            encoding:  str,
            line_ending: str = "\n",
            line_seperator: str = ";"
    ) -> List[List[str]]:
        """
        Reads a files content and returns it as simple strings split
        between spaces and semicolomns (One List for every statement e.g. ;)
        """
        lines: List[List[str]] = []
        with open(path, "r+", encoding=encoding) as file:
            content: str = file.read()

            def _strip_spaces(c: str) -> str:
                c = c.strip()
                new_c = ""
                prev_c = ""
                for char in c:
                    char: str
                    if not (char.isspace() and prev_c.isspace()):
                        new_c += char
                    prev_c = char

                return c

            content = _strip_spaces(content)
            assert content
        return lines

    @classmethod
    def tokenize_file(
            cls,
            file_path: Union[str, PathLike],
            encoding: str = "utf-8",
            line_ending: str = "\n"
    ) -> List[str]:
        """
        Tokenizes a file and checks for basic issues like valid characters
        sand basic syntax like known valid characters, valid usage of
        strings, ints etc.

        :param file_path: The path to the file (Can be relative or absolute)
        :param encoding: The encoding the file should be opened
        :param line_ending: The line endings of the file
        """
        file_content = cls.read_file_content(
            file_path, encoding, line_ending, cls.LINE_SEPERATOR
        )

        tokens: List[str] = []
        return tokens

