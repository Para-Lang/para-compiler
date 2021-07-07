# coding=utf-8
""" Tokens in the Para-C compiler """
from os import PathLike
from typing import Optional, Any, List, Union

from paraccompiler.core.abc.base_tokens import NULL_CHILDREN
from .abc import PreProcessorLogicToken

__all__ = [
    'PreProcessorDirective'
]


class PreProcessorDirective(PreProcessorLogicToken):
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
            relative_parent_file_name: Union[str, PathLike],
            antlr4_item,
            has_code_block_scope: bool,
            parent: Optional[Any] = None,
            children_code_block: Optional[str] = NULL_CHILDREN,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._children_code_block = children_code_block
        self._has_code_block_scope = has_code_block_scope
        super().__init__(
            name, as_str, line, column, relative_parent_file_name,
            antlr4_item, parent, children
        )

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

    def get_as_str(self) -> str:
        """ Gets the value of the token as a string """
        ...

    def get_name(self) -> str:
        """ Gets the name of the token """
        ...

    def get_line(self) -> int:
        """ Gets the line of code of the token in the file """
        ...

    def get_column(self) -> int:
        """ Gets the column of the token in the file """
        ...

    def is_directive(self) -> bool:
        """ Returns whether the token is a directive """
        return True

    def has_children(self) -> bool:
        """ Returns whether the token has children that are other tokens """
        ...

    def has_code_block_scope(self) -> bool:
        """
        Returns whether it is possible to pass a code-block after the
        directive. If this is False, then has_code_block_child can only be
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
