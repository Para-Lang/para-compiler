# coding=utf-8
""" Tokens in the Pqra-C compiler """
import abc
from abc import abstractmethod, ABC

__all__ = [
    "Token",
    "CToken",
    "ParacToken"
]


class Token(abc.ABC):
    """ Base Token Class """

    @abstractmethod
    def __init__(
            self,
            name: str,
            value: str,
            line: int,
            colomn: int,
            file_association: str
    ):
        self._name = name
        self._value = value
        self._line = line
        self._colomn = colomn
        self._file_association = file_association

    @abstractmethod
    def __str__(self) -> str:
        return self.get_value()

    @abstractmethod
    def __repr__(self) -> str:
        return f"<{self.get_name()}: '{self.get_value()}'>"

    @property
    @abstractmethod
    def associated_file(self) -> str:
        """ Returns the file associated with the token """
        ...

    @abstractmethod
    def get_value(self) -> str:
        """ Gets the value of the token e.g. name: Type-Def -> value: int """
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
    def get_colomn(self) -> int:
        """ Gets the colomn of the token in the file """
        ...


class SpecialToken(Token, ABC):
    """ Special Token that is not a keyword or built-in """
    ...


class CToken(Token, ABC):
    """ Native C tokens """
    ...


class ParacToken(Token, ABC):
    """ Tokens of the Para-C language that are not native to C """
    ...

