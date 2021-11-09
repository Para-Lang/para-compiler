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
    'ExternalPreProcessorItem',
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


class ExternalPreProcessorItem(PreProcessorLogicToken):
    """
    External PreProcessor item - initialised as a general logic token, which
    stores a child token (NonPreProcessorItem, PreProcessorDirective)
    """

    name = "externalItem"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.ExternalItemContext,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, children
        )

    @cached_property
    def as_str(self) -> str:
        """ Gets the value of the Pre-Processor token as a string """
        return super().as_str

    @cached_property
    def antlr4_ctx(self) -> _p.ExternalItemContext:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return getattr(self, '_antlr4_ctx')

    @cached_property
    def parent_file(self) -> FilePreProcessorContext:
        """ Returns the parent file context class """
        return super().parent_file

    @cached_property
    def relative_parent_file_name(self) -> str:
        """ Returns the relative name of the parent file """
        return super().relative_parent_file_name

    @cached_property
    def get_name(self) -> str:
        """ Gets the name of the token """
        return super().get_name()

    @cached_property
    def get_line(self) -> int:
        """ Gets the line of code of the token in the file """
        return super().get_line()

    @cached_property
    def get_column(self) -> int:
        """ Gets the column of the token in the file """
        return super().get_column()

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
        Always True for this class
        """
        return True

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


class NonPreProcessorItem(PreProcessorLogicToken):
    """
    Non Pre-Processor Token, which can be either a Para-C statement or a
    comment
    """
    name = "nonPreProcessorItemSequence"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.NonPreProcessorItemSequenceContext,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, children
        )

    @cached_property
    def as_str(self) -> str:
        """ Gets the value of the Pre-Processor token as a string """
        return super().as_str

    @cached_property
    def antlr4_ctx(self) -> Any:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return super()._antlr4_ctx

    @cached_property
    def parent_file(self) -> FilePreProcessorContext:
        """ Returns the parent file context class """
        return super().parent_file

    @cached_property
    def relative_parent_file_name(self) -> str:
        """ Returns the relative name of the parent file """
        return super().relative_parent_file_name

    @cached_property
    def get_name(self) -> str:
        """ Gets the name of the token """
        return super().get_name()

    @cached_property
    def get_line(self) -> int:
        """ Gets the line of code of the token in the file """
        return super().get_line()

    @cached_property
    def get_column(self) -> int:
        """ Gets the column of the token in the file """
        return super().get_column()

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

    name = "preProcessorDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.preProcessorDirective,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            parent_file, antlr4_ctx, children
        )

    @cached_property
    @abstractmethod
    def antlr4_ctx(self) -> _p.preProcessorDirective:
        """
        Returns the Antlr4 ctx instance associated with this logic token
        """
        return super().antlr4_ctx

    @cached_property
    def as_str(self) -> str:
        """ Gets the value of the Pre-Processor token as a string """
        return super().as_str

    @cached_property
    def parent_file(self) -> FilePreProcessorContext:
        """ Returns the parent file context class """
        return super().parent_file

    @cached_property
    def relative_parent_file_name(self) -> str:
        """ Returns the relative name of the parent file """
        return super().relative_parent_file_name

    @cached_property
    def get_name(self) -> str:
        """ Gets the name of the token """
        return super().get_name()

    @cached_property
    def get_line(self) -> int:
        """ Gets the line of code of the token in the file """
        return super().get_line()

    @cached_property
    def get_column(self) -> int:
        """ Gets the column of the token in the file """
        return super().get_column()

    @cached_property
    def is_directive(self) -> bool:
        """ Returns whether the token is a directive """
        return True

    @property
    def children_code_block(self) -> Union[str, NonPreProcessorItem]:
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

    name = "includeDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: Union[
                _p.IncludeDirectiveContext,
                _p.ComputedIncludeDirectiveContext,
                _p.FileIncludeDirectiveContext
            ],
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "fileIncludeDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.FileIncludeDirectiveContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "computedIncludeDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.ComputedIncludeDirectiveContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "defineDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.ComplexDefineDirectiveContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "selectionPreProcessorDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: Union[
                _p.SelectionPreProcessorDirectiveContext,
                _p.StartOfSelectionBlockContext,
                _p.SelectionDirectiveAlternativesContext,
                _p.SelectionElseDirectiveContext,
                _p.EndIfDirectiveContext
            ],
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "startOfSelectionBlock"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.StartOfSelectionBlockContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "selectionDirectiveAlternatives"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.SelectionDirectiveAlternativesContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "selectionElseDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.SelectionElseDirectiveContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "endIfDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.EndIfDirectiveContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "errorDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.ErrorDirectiveContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "lineDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.LineDirectiveContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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

    name = "pragmaDirective"

    def __init__(
            self,
            parent_file: FilePreProcessorContext,
            antlr4_ctx: _p.PragmaDirectiveContext,
            has_code_block_scope: bool,
            children_code_block: Optional[NonPreProcessorItem] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        super().__init__(
            parent_file, antlr4_ctx, has_code_block_scope,
            children_code_block, children
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
