# coding=utf-8
"""
File containing the classes which will be used to track and run a pre-processor
compilation. The context classes will track directives and correctly run the
commands as given in the file.
"""
from __future__ import annotations

from os import PathLike
from typing import Dict, Union, List, TYPE_CHECKING, Tuple
import antlr4

from ..abc import ProgramRunContext, FileRunContext
from .logic_stream import PreProcessorStream
from .__main__ import PreProcessor, PreProcessorProcessResult

if TYPE_CHECKING:
    from ..compiler import ProgramCompilationProcess

__all__ = [
    'FilePreProcessorContext',
    'ProgramPreProcessorContext'
]


class FilePreProcessorContext(FileRunContext):
    """
    Class used inside the listener for managing the context of a single file,
    where directives and code are stored and managed.
    """

    def __init__(
            self,
            relative_file_name: Union[str, PathLike]
    ):
        super().__init__(
            program_ctx=None,
            logic_stream=PreProcessorStream(),
            processed_stream=None,
            relative_file_name=relative_file_name
        )

    @property
    def program_ctx(self) -> Union[ProgramPreProcessorContext, None]:
        """
        Returns the program_ctx if it was already set using set_program_ctx()
        """
        return self._program_ctx

    @property
    def logic_stream(self) -> PreProcessorStream:
        """
        Returns the content of the file represented as a stream containing
        PreProcessorLogicToken
        """
        return self._logic_stream

    def set_program_ctx(self, ctx: ProgramPreProcessorContext) -> None:
        """
        Sets the program context, containing the information for the entire
        compilation and relative structure
        """
        self._program_ctx = ctx


class ProgramPreProcessorContext(ProgramRunContext):
    """
    Program Compilation Context, which serves as the base for an entire
    pre-processor compilation
    """

    def __init__(self, process: ProgramCompilationProcess):
        self._entry_ctx: Union[FilePreProcessorContext, None] = None
        self._context_dict: Dict[
            Union[str, PathLike], FilePreProcessorContext
        ] = {}
        super().__init__(process=process)

    @property
    def process(self) -> ProgramCompilationProcess:
        """ Compilation Process of this instance """
        return self._process

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
        return super().encoding

    @property
    def entry_file_path(self) -> str:
        """ Returns the entry_file_path of the context """
        return super().entry_file_path

    @property
    def entry_ctx(self) -> FilePreProcessorContext:
        """ Returns the entry context """
        return self._entry_ctx

    @property
    def context_dict(self) -> Dict[
        Union[str, PathLike], FilePreProcessorContext
    ]:
        """
        Returns a list for all context instances. The key is a relative path
        name to the FileContext
        """
        return self._context_dict

    def set_entry_ctx(
            self,
            ctx: FilePreProcessorContext
    ) -> None:
        """ Sets the entry-file FilePreProcessorContext """
        ctx.set_program_ctx(self)
        self._entry_ctx = ctx
        self._context_dict[ctx.relative_file_name] = ctx

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

    async def make_temp_files(
            self, process: PreProcessorProcessResult
    ) -> Tuple[str, List[str]]:
        """
        Creates the temporary files based on the passed output of
        process_program()

        :returns: A tuple containing at 0 the path to the entry-file and at 1
        a list of all paths of all other files.
        """
        ...

    async def process_program(
            self, enable_out: bool
    ) -> PreProcessorProcessResult:
        """
        Processes this instance and generates the logic streams required
        for generating the finished code.

        :param enable_out: If set to True errors, warnings and info will be
        logged onto the console using the local logger instance. If an
        exception is raised or error is encountered, it will be reraised with
        the FailedToProcessError.
        :returns: A PreProcessorProcessResult instance
        """
        await self.parse_entry_file(enable_out)

        ...  # TODO! Run listener for every file

        # Processing the directives
        return await PreProcessor.process_directives(self)

    async def get_stream_and_parse(
            self,
            file_path: Union[str, PathLike],
            enable_out: bool
    ) -> FilePreProcessorContext:
        """
        Gets a FileStream, converts it to a string stream and parses it
        returning the resulting FilePreProcessorContext

        :param file_path: Path to the file
        :param enable_out: If set to True errors, warnings and info will be
        logged onto the console using the local logger instance. If an
        exception is raised or error is encountered, it will be reraised with
        the FailedToProcessError.
        :returns: The FilePreProcessorContext instance for the file
        """
        from ..compiler import ParacCompiler
        from ..util import (get_file_stream, get_relative_file_name,
                            get_input_stream)

        file_stream = get_file_stream(file_path, self.encoding)
        relative_file_name = get_relative_file_name(
            file_name=file_stream.name,
            file_path=file_stream.fileName,
            base_path=self.work_dir
        )
        stream = get_input_stream(
            # rm comments
            ParacCompiler.remove_comments_from_str(file_stream.strdata),
            name=file_stream.name
        )
        return await self.parse_single_file(
            stream, relative_file_name, enable_out
        )

    @staticmethod
    async def parse_single_file(
            stream: antlr4.InputStream,
            relative_file_name: str,
            enable_out: bool,
    ) -> FilePreProcessorContext:
        """
        Parses a single file and generates the FilePreProcessorContext

        :param stream: The Antlr4 InputStream which represents a string stream
        :param relative_file_name: Relative name of the file (fetch-able
        using get_relative_file_name)
        :param enable_out: If set to True errors, warnings and info will be
        logged onto the console using the local logger instance. If an
        exception is raised or error is encountered, it will be reraised with
        the FailedToProcessError.
        :returns: The generated FilePreProcessorContext instance
        """
        from .listener import Listener

        antlr4_file_ctx = await PreProcessor.parse(stream, enable_out)
        listener = Listener(antlr4_file_ctx, stream, relative_file_name)
        await listener.walk_and_process_directives(enable_out)

        return listener.file_ctx
