# coding=utf-8
"""
File containing the classes which will be used to track and run a pre-processor
compilation. The context classes will track directives and correctly run the
commands as given in the file.
"""
from __future__ import annotations

__all__ = [
    'FilePreProcessorContext',
    'ProgramPreProcessorContext'
]

from typing import Dict, Union, List, TYPE_CHECKING

if TYPE_CHECKING:
    from paraccompiler import ProgramCompilationProcess


class FilePreProcessorContext:
    """
    Class used inside the listener for managing the context of a single file,
    where specific directives are used and stated.
    """
    ...


# TODO! Add proper logic
class ProgramPreProcessorContext:
    """
    Program Compilation Context, which serves as the base for an entire
    pre-processor compilation
    """

    def __init__(self, process: ProgramCompilationProcess):
        self._entry_ctx: Union[FilePreProcessorContext, None] = None
        self._ctx_list: List[FilePreProcessorContext] = []
        self.process = process

    @property
    def entry_file(self) -> str:
        """ Returns the entry_file of the context """
        return self.process.entry_file

    @property
    def entry_ctx(self) -> FilePreProcessorContext:
        """ Returns the entry context """
        return self._entry_ctx

    @property
    def ctx_list(self) -> List[FilePreProcessorContext]:
        """ Returns a list for all context instances """
        return self._ctx_list

    def set_entry_ctx(self, ctx: FilePreProcessorContext) -> None:
        """ Sets the entry-file FileCompilationContext """
        self._entry_ctx = ctx
        self._ctx_list.append(ctx)

    def add_file_ctx(self, ctx: FilePreProcessorContext) -> None:
        """
        Adds a FilePreProcessorContext to the list of file ctx instances
        """
        self._ctx_list.append(ctx)

        # TODO! Logical integration

    def generate_source(self) -> Dict[str, Dict[str, FilePreProcessorContext]]:
        """
        Generates the source C-code from the tokens stored inside the class.

        :returns: Dict[
                  str - Name of the file (Relative name),
                  Dict[
                    str - The code-string,
                    FileCompilationContext - The context of the file
                  ]
                 ]
        """
        ...
