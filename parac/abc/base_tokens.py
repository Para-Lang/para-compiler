# coding=utf-8
""" File containing the ABC classes for tokens """
from abc import abstractmethod, ABC
from os import PathLike
from typing import Optional, Any, List, TypeVar, Union
import antlr4
from antlr4 import ParserRuleContext

from .base_ctx import FileRunContext


__all__ = [
    'NULL_CHILDREN',
    'Token',
    'SpecialToken',
    'LogicToken',
    'CLogicToken',
    'ParacLogicToken',
    'ParaCLogicParentContextToken'
]

NULL_CHILDREN = TypeVar('NULL_CHILDREN')


class Token(ABC):
    """ Base Token Class """

    name = "token"

    @abstractmethod
    def __init__(
            self,
            relative_parent_file_name: Union[str, PathLike],
            parent_file: Any
    ):
        self._relative_parent_file_name = relative_parent_file_name
        self._parent_file = parent_file

    def __str__(self) -> str:
        return self.as_str

    def __repr__(self) -> str:
        return f"<{self.get_name()}: '{self.as_str}'>"

    @property
    @abstractmethod
    def relative_parent_file_name(self) -> str:
        """ Returns the relative name of the parent file """
        return self._relative_parent_file_name

    @property
    @abstractmethod
    def parent_file(self) -> Any:
        """ Returns the parent file context instance """
        return self._parent_file

    @abstractmethod
    def get_name(self) -> str:
        """ Gets the name of the token """
        return self.name

    @property
    @abstractmethod
    def as_str(self) -> str:
        """ Gets the value of the token as a string """
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

    name = "logicToken"

    @abstractmethod
    def __init__(
            self,
            relative_parent_file_name: Union[str, PathLike],
            parent_file: Any,
            parent: Optional[Any] = None,
            children: Union[Optional[List[Any]], NULL_CHILDREN] = NULL_CHILDREN
    ):
        self.children = children
        self.parent = parent
        super().__init__(relative_parent_file_name, parent_file)

    def append_children(self, item: Any) -> None:
        """ Adds a child ctx to the property children of this class """
        if self.children is NULL_CHILDREN:
            self.children = [item]
        else:
            self.children.append(item)


class CLogicToken(LogicToken, ABC):
    """ Native C tokens """

    name = "cLogicToken"

    ...


class ParacLogicToken(LogicToken, ABC):
    """ Tokens of the Para-C language """

    name = "paracLogicToken"

    @abstractmethod
    def __init__(
            self,
            antlr4_ctx: ParserRuleContext,
            parent_file: FileRunContext,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._antlr4_ctx = antlr4_ctx
        super().__init__(
            relative_parent_file_name=parent_file.relative_file_name,
            parent=antlr4_ctx.parentCtx,
            children=children,
            parent_file=parent_file
        )

    @property
    @abstractmethod
    def antlr4_ctx(self) -> ParserRuleContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    @property
    def input_stream(self) -> antlr4.InputStream:
        """ Input Stream for the file of this element """
        from ..util import get_input_stream_from_ctx
        return get_input_stream_from_ctx(self.antlr4_ctx)

    def extract_original_text(self) -> str:
        """ Extracts the original text based on the ctx """
        from ..util import get_original_text
        return get_original_text(self.antlr4_ctx)

    @property
    @abstractmethod
    def as_str(self) -> str:
        """ Gets the value of the token as a string """
        return self.extract_original_text()

    @abstractmethod
    def get_line(self) -> int:
        """ Gets the line of code of the token in the file """
        return self.antlr4_ctx.start.getLine()

    @abstractmethod
    def get_column(self) -> int:
        """ Gets the column of the token in the file """
        return self.antlr4_ctx.start.getCharPositionInLine()


class ParaCLogicParentContextToken(ParacLogicToken, ABC):
    """
    This is a parent context token class, designed to serve as the actual base
    class, where the compilation logic for each specific expression, statement
    and token is written.
    """

    def __init__(self):
        ...