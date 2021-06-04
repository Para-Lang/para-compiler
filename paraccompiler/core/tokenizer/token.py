# coding=utf-8
""" Tokens in the Pqra-C compiler """
import abc
from abc import abstractmethod, ABC

__all__ = [
    "Token",
    "CToken",
    "ParacToken",
    "UnregisteredToken"
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


class CToken(Token, ABC):
    """ Native C tokens """
    ...


class ParacToken(Token, ABC):
    """ Tokens of the Para-C language that are not native to C """
    ...


class UnregisteredToken(Token):
    """ Unregistered token that was not assigned to an item yet """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    def associated_file(self) -> str:
        """
        Returns the token of the unregistered token. This can be any
        file
        """
        return super().associated_file

    def get_line(self) -> int:
        """ Returns the line of the file where the token is used """
        return super()._line

    def get_name(self) -> str:
        """
        Returns the name of the unassociated token. This can be any name.
        Special characters like ; or " are treated as STATEMENT_END or
        STRING_START / STRING_END, while built-ins like 'int' are treated as
        BUILT-IN-TYPE with value INT
        """
        return super()._name

    def get_value(self) -> str:
        """ Returns the actual value """
        return super()._value

    def get_colomn(self) -> int:
        """ Returns the colomn of the file where the token is used """
        return super()._colomn
