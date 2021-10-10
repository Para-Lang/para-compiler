# coding=utf-8
""" Tokens in the Para-C compiler """
from __future__ import annotations

from abc import ABC, abstractmethod
from os import PathLike
from typing import Optional, Any, List, Union, TYPE_CHECKING
from antlr4 import ParserRuleContext
from cached_property import cached_property

from .python.ParaCPreProcessorParser import ParaCPreProcessorParser as _p
from ..abc import NULL_CHILDREN
from .abc import PreProcessorLogicToken

if TYPE_CHECKING:
    from .ctx import FilePreProcessorContext

__all__ = [
    'NonPreProcessorItem',
    'PreProcessorDirective',
    'DefineDirective',
    'IncludeDirective',
    'ComputedIncludeDirective',
    'FileIncludeDirective',
    'SelectionDirective',
    'StartSelectionDirective',
    'AlternativeSelectionDirective',
    'ElseSelectionDirective',
    'EndIfDirective',
    'ErrorDirective',
    'LineDirective',
    'PragmaDirective',
]


class NonPreProcessorItem(PreProcessorLogicToken):
    """
    Non Pre-Processor Token, which can be either a Para-C statement or a
    comment
    """
    name = "NonPreProcessorItem"

    def __init__(
            self,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.NonPreProcessorItemSequenceContext,
            parent: Optional[Any] = None,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            self.name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> Any:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return super()._antlr4_ctx

    @cached_property
    def parent_file(self) -> FilePreProcessorContext:
        """ Returns the parent file context class """
        return self._parent_file

    @cached_property
    def relative_parent_file_name(self) -> str:
        """ Returns the relative name of the parent file """
        return self._relative_parent_file_name

    @cached_property
    def get_name(self) -> str:
        """ Gets the name of the token """
        return self._name

    @cached_property
    def get_line(self) -> int:
        """ Gets the line of code of the token in the file """
        return self.antlr4_ctx.start.getLine()

    @cached_property
    def get_column(self) -> int:
        """ Gets the column of the token in the file """
        return self.antlr4_ctx.start.getCharPositionInLine()

    @cached_property
    def is_directive(self) -> bool:
        """
        Returns whether the token is a directive. Always false for this class
        """
        return False

    @cached_property
    def has_children(self) -> bool:
        """
        Returns whether the token has children that are other tokens.
        Always false for this class
        """
        return False

    @cached_property
    def has_code_block_scope(self) -> bool:
        """
        Returns whether it is possible to pass a code-block after the
        item. Always false for this class
        """
        return False

    @cached_property
    def has_code_block_child(self) -> bool:
        """
        Returns whether the token has code-block children that are associated
        with the tokens scope. Always false for this class
        """
        return False


class PreProcessorDirective(PreProcessorLogicToken, ABC):
    """
    Pre-Processor Directive representing a Para-C PreProcessor Directive
    used to interact with the Compiler
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: Any,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    @abstractmethod
    def antlr4_ctx(self) -> ParserRuleContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return super()._antlr4_ctx

    @cached_property
    def parent_file(self) -> FilePreProcessorContext:
        """ Returns the parent file context class """
        return super().parent_file

    @property
    def relative_parent_file_name(self) -> str:
        """ Returns the relative name of the parent file """
        return self._relative_parent_file_name

    @property
    def children_code_block(self) -> Union[str, NULL_CHILDREN]:
        """
        Returns the children code block that could be associated with a
        directive

        Example:

            #if defined(x)

            // associated code-block

            #else

            // associated code-block
        """
        return self._children_code_block

    @cached_property
    def get_name(self) -> str:
        """ Gets the name of the token """
        return self._name

    @cached_property
    def get_line(self) -> int:
        """ Gets the line of code of the token in the file """
        return self.antlr4_ctx.start.getLine()

    @cached_property
    def get_column(self) -> int:
        """ Gets the column of the token in the file """
        return self.antlr4_ctx.start.getCharPositionInLine()

    @cached_property
    def is_directive(self) -> bool:
        """ Returns whether the token is a directive """
        return True

    def has_children(self) -> bool:
        """ Returns whether the token has children that are other tokens """
        ...  # TODO!

    def has_code_block_scope(self) -> bool:
        """
        Returns whether it is possible to pass a code-block after the
        item. If this is False, then has_code_block_child can only be
        False as well and children_code_block will return NULL_CHILDREN
        """
        return self._has_code_block_scope

    def has_code_block_child(self) -> bool:
        """
        Returns whether the token has code-block children that are associated
        with the tokens scope
        """
        if self.has_code_block_scope():
            return getattr(
                self, 'children_code_block', NULL_CHILDREN
            ) not in (NULL_CHILDREN, None)
        return False

    @abstractmethod
    def process_directive_based_on_ctx(self) -> str:
        """
        Processes the contents of this directive.
        If the directive does not alter anything -> empty string
        """
        ...


class IncludeDirective(PreProcessorDirective):
    """
    Include Directive for including code from other files. This serves as the
    parent class for FileIncludeDirective and ComputedIncludeDirective

    If a context other than 'IncludeDirectiveContext' is passed
    to antlr4_ctx, it will be assumed this class is taken as a parent to a
    sub-class.
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: Union[
                _p.IncludeDirectiveContext,
                _p.ComputedIncludeDirectiveContext,
                _p.FileIncludeDirectiveContext
            ],
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.IncludeDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class FileIncludeDirective(IncludeDirective):
    """
    Include Directive which includes a file based on a string literal. This
    can be either a library include or a regular file include.
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.FileIncludeDirectiveContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.FileIncludeDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class ComputedIncludeDirective(IncludeDirective):
    """
    Computed Include Directive, which includes based on a macro a header.
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.ComputedIncludeDirectiveContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.ComputedIncludeDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class DefineDirective(PreProcessorDirective):
    """
    Define Directive for defining a macro (identifier). The macro can either
    be empty, an expression or a statement
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.ComplexDefineDirectiveContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.ComplexDefineDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class SelectionDirective(PreProcessorDirective):
    """
    Parent class Selection Directive, which is used for a Selection Directive
    Block, which consist of two or more directives, which specify
    based on evaluated expressions, which child code-block should be used.

    If a context other than 'SelectionPreProcessorDirectiveContext' is passed
    to antlr4_ctx, it will be assumed this class is taken as a parent to a
    sub-class.
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: Union[
                _p.SelectionPreProcessorDirectiveContext,
                _p.StartOfSelectionBlockContext,
                _p.SelectionDirectiveAlternativesContext,
                _p.SelectionElseDirectiveContext,
                _p.EndIfDirectiveContext
            ],
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.SelectionPreProcessorDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class StartSelectionDirective(SelectionDirective):
    """
    Start of a Selection Directive Block. Possible Directives for a Start Block
    are IfDirective, IfDefinedDirective or IfNotDefinedDirective. A
    AlternativeSelectionDirective or a EndIfDirective MUST be placed after this
    directive.
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.StartOfSelectionBlockContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.StartOfSelectionBlockContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class AlternativeSelectionDirective(SelectionDirective):
    """
    Alternative Directive Block that can be placed following a
    StartSelectionDirective or another AlternativeSelectionDirective (A
    StartSelectionDirective is required).

    The entire statement must be closed with an EndIfDirective
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.SelectionDirectiveAlternativesContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.SelectionDirectiveAlternativesContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class ElseSelectionDirective(SelectionDirective):
    """
    Else Selection Directive, which can follow a AlternativeSelectionDirective
    or StartSelectionDirective. This directive must be followed by an +
    EndIfDirective.
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.SelectionElseDirectiveContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.SelectionElseDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class EndIfDirective(SelectionDirective):
    """
    Endif Directive, which closes a SelectionDirective. This directive can be
    used in an nested pre-processor directive, without any effects on the
    higher level directive (spaces between the # and the identifier are only
    stylistic and not required):

    #ifdef x
    # ifdef y
    # endif // nested endif
    #endif
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.EndIfDirectiveContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.EndIfDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class ErrorDirective(PreProcessorDirective):
    """
    Error Directive, which if encountered writes a string to stderr and
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.ErrorDirectiveContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.ErrorDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class LineDirective(PreProcessorDirective):
    """
    Line Directive, which sets the __LINE__ and __FILE__ (optional) macros.
    If set the numeric value will be the __LINE__ macro in the next line.
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.LineDirectiveContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.LineDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...


class PragmaDirective(PreProcessorDirective):
    """
    Pragma Directive for using compiler specific commands, which affect the
    code, compilation or execution.
    """

    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: _p.PragmaDirectiveContext,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, parent_file,
            relative_parent_file_name, antlr4_ctx, parent, children
        )

    @cached_property
    def antlr4_ctx(self) -> _p.PragmaDirectiveContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    def process_directive_based_on_ctx(self) -> str:
        """ Processes the contents of this directive """
        ...
