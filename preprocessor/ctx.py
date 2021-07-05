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

from os import PathLike
from typing import Dict, Union, List, TYPE_CHECKING, Tuple

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
    def encoding(self) -> str:
        """ Returns the encoding of the project """
        return self.process.encoding

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

    def gen_source(self) -> Dict[str, Dict[str, FilePreProcessorContext]]:
        """
        Generates the source C-code from the tokens stored inside the class.

        :returns: Dict[
                  str - Name of the file (Relative name),
                  Dict[
                    str - The code-string,
                    FilePreProcessorContext - The context of the file
                  ]
                 ]
        """
        ...

    def make_temp_files(
            self,
            gen_src_o: Dict[str, Dict[str, FilePreProcessorContext]],
            build_path: Union[str, PathLike],
            dist_path: Union[str, PathLike]
    ) -> Tuple[str, List[str]]:
        """
        Creates the temporary files based on the passed output of
        generated_source()

        :returns: A tuple containing at 0 the path to the entry-file and at 1
                  a list of all paths of all other files.
        """
        ...
