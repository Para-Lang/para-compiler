# coding=utf-8
"""
File containing the classes which will be used to track and run a pre-processor
compilation. The context classes will track directives and correctly run the
commands as given in the file.
"""
from __future__ import annotations

from os import PathLike
from typing import Dict, Union, List, TYPE_CHECKING, Tuple

from .abc import PreProcessorLogicToken

__all__ = [
    'FilePreProcessorContext',
    'ProgramPreProcessorContext'
]

if TYPE_CHECKING:
    from paraccompiler import ProgramCompilationProcess


class FilePreProcessorContext:
    """
    Class used inside the listener for managing the context of a single file,
    where directives and code are stored and managed.
    """

    def __init__(
            self,
            relative_file_name: Union[str, PathLike]
    ):
        self._program_ctx: Union[ProgramPreProcessorContext, None] = None
        self._content: Dict[str, PreProcessorLogicToken] = {}
        self._relative_file_name = relative_file_name

    @property
    def relative_file_name(self) -> Union[str, PathLike]:
        """
        Returns the relative file name, which goes out from the entry file
        and has a relative path to every file imported and used.
        """
        return self._relative_file_name

    @property
    def program_ctx(self) -> Union[ProgramPreProcessorContext, None]:
        """
        Returns the program_ctx if it was already set using set_program_ctx()
        """
        return self._program_ctx

    @property
    def content(self) -> Dict[str, PreProcessorLogicToken]:
        """ Returns the content of the file represented as a dict """
        return self._content

    def set_program_ctx(self, ctx: ProgramPreProcessorContext) -> None:
        """
        Sets the program context, containing the information for the entire
        compilation and relative structure
        """
        self._program_ctx = ctx


class ProgramPreProcessorContext:
    """
    Program Compilation Context, which serves as the base for an entire
    pre-processor compilation
    """

    def __init__(self, process: ProgramCompilationProcess):
        self._entry_ctx: Union[FilePreProcessorContext, None] = None
        self._context_dict: Dict[
            Union[str, PathLike], FilePreProcessorContext
        ] = {}
        self.process = process

    @property
    def work_dir(self) -> Union[str, PathLike]:
        """
        Returns the working directory / base-path for the program. If the entry
        file path was relative, then the working directory where the compiler
        is run is used as the working directory.
        """
        return self.process.work_dir

    @property
    def encoding(self) -> str:
        """ Returns the encoding of the project """
        return self.process.encoding

    @property
    def entry_file_path(self) -> str:
        """ Returns the entry_file_path of the context """
        return self.process.entry_file_path

    @property
    def entry_ctx(self) -> FilePreProcessorContext:
        """ Returns the entry context """
        return self._entry_ctx

    @property
    def context_dict(self) -> Dict[
        Union[str, PathLike], FilePreProcessorContext
    ]:
        """ Returns a list for all context instances """
        return self._context_dict

    def set_entry_ctx(
            self,
            ctx: FilePreProcessorContext,
            relative_file_name: Union[str, PathLike]
    ) -> None:
        """ Sets the entry-file FilePreProcessorContext """
        ctx.set_program_ctx(self)
        self._entry_ctx = ctx
        self._context_dict[relative_file_name] = ctx

    def add_file_ctx(
            self,
            ctx: FilePreProcessorContext,
            relative_file_name: Union[str, PathLike]
    ) -> None:
        """
        Adds a FilePreProcessorContext to the list of file ctx instances.
        The context instance should only be created using this class
        """
        ctx.set_program_ctx(self)
        self._context_dict[relative_file_name] = ctx

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
