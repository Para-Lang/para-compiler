# coding=utf-8
""" File containing the ABC classes for tokens """

from abc import abstractmethod, ABC

__all__ = [
    'NULL_CHILDREN',
    'Token',
    'SpecialToken',
    'LogicToken',
    'CLogicToken',
    'ParacLogicToken'
]

from os import PathLike

from typing import Optional, Any, List, TypeVar, Union

NULL_CHILDREN = TypeVar('NULL_CHILDREN')


class Token(ABC):
    """ Base Token Class """

    @abstractmethod
    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            relative_parent_file_name: Union[str, PathLike]
    ):
        self._name = name
        self._as_str = as_str
        self._line = line
        self._column = column
        self._relative_parent_file_name = relative_parent_file_name

    def __str__(self) -> str:
        return self.get_as_str()

    def __repr__(self) -> str:
        return f"<{self.get_name()}: '{self.get_as_str()}'>"

    @property
    @abstractmethod
    def relative_parent_file_name(self) -> str:
        """ Returns the relative name of the parent file """
        ...

    @abstractmethod
    def get_as_str(self) -> str:
        """ Gets the value of the token as a string """
        ...

    @abstractmethod
    def get_name(self) -> str:
        """ Gets the name of the token """
        ...

    @abstractmethod
    def get_line(self) -> int:
        """ Gets the line of code of the token in the file """
        ...

    @abstractmethod
    def get_column(self) -> int:
        """ Gets the column of the token in the file """
        ...


class SpecialToken(Token, ABC):
    """ Special Token that is not a keyword or built-in """
    ...


class LogicToken(Token, ABC):
    """
    Logic token class, which represents entire expressions, statements,
    selection statement and more
    """

    @abstractmethod
    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            relative_parent_file_name:  Union[str, PathLike],
            antlr4_item,
            parent: Optional[Any] = None,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        if children is NULL_CHILDREN:
            self.children = NULL_CHILDREN
        else:
            self.children = children
        self.antlr4_item = antlr4_item
        self.parent = parent

        super().__init__(name, as_str, line, column, relative_parent_file_name)


class CLogicToken(LogicToken, ABC):
    """ Native C tokens """
    ...


class ParacLogicToken(LogicToken, ABC):
    """ Tokens of the Para-C language """
    ...
