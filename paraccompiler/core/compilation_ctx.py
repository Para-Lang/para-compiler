# coding=utf-8
"""
File containing the classes which will be used to track and run a compilation.
The context classes will track variables, stack, logic and general compiling
information.
"""
from __future__ import annotations

__all__ = [
    'FileCompilationContext',
    'ProgramCompilationContext'
]

from os import PathLike
from typing import Dict, Union, TYPE_CHECKING

from .abc import ParacLogicToken

if TYPE_CHECKING:
    from .compiler import ProgramCompilationProcess


class FileCompilationContext:
    """
    Class used inside the listener for managing the context of a single file,
    which will keep track of variables, the stack, logic and
    general compiling information which is only related to the specified file.
    -> Unknown identifiers will not count as an error, since they might be
    from another file that is included.

    Dependencies will be managed using the CompilationContext, which will keep
    track of all files and in the end process the resulting dependencies and
    whether they work. (-> Linker and Semantic Analysis)
    """
    def __init__(
            self,
            relative_file_name: Union[str, PathLike]
    ):
        self._program_ctx: Union[ProgramCompilationContext, None] = None
        self._content: Dict[str, ParacLogicToken] = {}

    @property
    def program_ctx(self) -> Union[ProgramCompilationContext, None]:
        """
        Returns the program_ctx if it was already set using set_program_ctx()
        """
        return self._program_ctx

    @property
    def content(self) -> Dict[str, ParacLogicToken]:
        """ Returns the content of the file represented as a dict """
        return self._content

    def set_program_ctx(self, ctx: ProgramCompilationContext) -> None:
        """
        Sets the program context, containing the information for the entire
        compilation and relative structure
        """
        self._program_ctx = ctx


class ProgramCompilationContext:
    """
    Program Compilation Context, which serves as the base for the compilation
    of an entire program containing possibly more than one file. Holds the
    entire context of the program and is used in the linker and last step of
    semantic analysis to validate the program.
    """

    def __init__(self, process: ProgramCompilationProcess):
        self._entry_ctx: Union[FileCompilationContext, None] = None
        self._context_dict: Dict[
            Union[str, PathLike], FileCompilationContext
        ] = {}
        self.process = process

    @property
    def encoding(self) -> str:
        """ Returns the encoding of the project """
        return self.process.encoding

    @property
    def entry_file(self) -> str:
        """ Returns the entry_file of the context """
        return self.process.entry_file

    @property
    def entry_ctx(self) -> FileCompilationContext:
        """ Returns the entry context """
        return self._entry_ctx

    @property
    def context_dict(self) -> Dict[
            Union[str, PathLike], FileCompilationContext
        ]:
        """ Returns a list for all context instances """
        return self._context_dict

    def set_entry_ctx(
            self,
            ctx: FileCompilationContext,
            relative_file_name: Union[str, PathLike]
    ) -> None:
        """ Sets the entry-file FileCompilationContext """
        ctx.set_program_ctx(self)
        self._entry_ctx = ctx
        self._context_dict[relative_file_name] = ctx

    def add_file_ctx(
            self,
            ctx: FileCompilationContext,
            relative_file_name: Union[str, PathLike]
    ) -> None:
        """
        Adds a FileCompilationContext to the list of file ctx instances.
        The context instance should only be created using this class
        """
        ctx.set_program_ctx(self)
        self._context_dict[relative_file_name] = ctx

    def gen_source(self) -> Dict[str, Dict[str, FileCompilationContext]]:
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
