# coding=utf-8
"""
File containing the class which will be used to track and run a compilation.
The compile unit will track variables, stack, logic and general compiling
information which is only related to the specified file.
"""
from __future__ import annotations

__all__ = [
    'FileCompilationContext',
    'CompilationContext'
]

from typing import Dict, Union, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .compiler import CompilationProcess


class FileCompilationContext:
    """
    Class used inside the listener which 'listens' to events / registers
    tokens, which will keep track of variables, the stack, logic and
    general compiling information which is only related to the specified file.

    Dependencies will be managed using the CompilationContext, which will keep
    track of all files and in the end process the resulting dependencies and
    whether they work
    """
    ...


# TODO! Add proper logic and dependency management
class CompilationContext:
    """ Compilation Context """

    def __init__(self, process: CompilationProcess):
        self._entry_ctx: Union[FileCompilationContext, None] = None
        self._ctx_list: List[FileCompilationContext] = []
        self.process = process

    @property
    def entry_file(self) -> str:
        """ Returns the entry_file of the context """
        return self.process.entry_file

    @property
    def entry_ctx(self) -> FileCompilationContext:
        """ Returns the entry context """
        return self._entry_ctx

    @property
    def ctx_list(self) -> List[FileCompilationContext]:
        """ Returns a list for all context instances """
        return self._ctx_list

    def set_entry_ctx(self, ctx: FileCompilationContext) -> None:
        """ Sets the entry-file FileCompilationContext """
        self._entry_ctx = ctx
        self._ctx_list.append(ctx)

    def add_file_ctx(self, ctx: FileCompilationContext) -> None:
        """ Adds a FileCompilationContext to the list of file ctx instances """
        self._ctx_list.append(ctx)

        # TODO! Logical integration

    def generate_source(self) -> Dict[str, Dict[str, FileCompilationContext]]:
        """
        Generates the source C-code from the tokens stored inside the class

        :returns: Dict[
                  str - Name of the file (Relative name),
                  Dict[
                    str - The code-string,
                    FileCompilationContext - The context of the file
                  ]
                 ]
        """
        ...
