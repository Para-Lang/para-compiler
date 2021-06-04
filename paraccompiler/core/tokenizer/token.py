# coding=utf-8
""" Tokens in the Pqra-C compiler """
import abc
from abc import abstractmethod

__all__ = [
    "Token",
    "CToken",
    "ParacToken",
    "UnregisteredToken"
]


class Token(abc.ABC):
    """ Base Token Class """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        ...

    @abstractmethod
    def __str__(self) -> str:
        return self.get_value()

    @abstractmethod
    def __repr__(self) -> str:
        return f"<{self.get_name()}: '{self.get_value()}'>"

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


class CToken(Token):
    """ Native C tokens """
    ...

class ParacToken(Token):
    """ Tokens of the Para-C language that are not native to C """
    ...


class UnregisteredToken():
    """ Unregistered token that was not assigned to an item yet """
    ...
