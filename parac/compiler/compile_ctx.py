# coding=utf-8
"""
File containing the classes which will be used to track and run a compilation.
The context classes will track variables, stack, logic and general compiling
information.
"""
from __future__ import annotations

import logging
from pathlib import Path
from os import PathLike
from typing import Dict, Union, TYPE_CHECKING, List

import antlr4

from .logic_stream import ParacQualifiedLogicStream
from ..abc import FileRunContext, ProgramRunContext
from ..util import get_input_stream

if TYPE_CHECKING:
    from .process import ProgramCompilationProcess

__all__ = [
    'FileCompilationContext',
    'ProgramCompilationContext'
]

logger = logging.getLogger(__name__)


class FileCompilationContext(FileRunContext):
    """
    Class used inside the listener for managing the context of a single file,
    which will keep track of variables, the stack, logic and
    general compiling information which is only related to the specified file.

    Note that unknown identifiers will not count as an error, since they
    might be from another file that is included.

    Dependencies will be managed using the CompilationContext, which will keep
    track of all files and in the end process the resulting dependencies and
    whether they work. (-> Linker and Semantic Analysis)
    """

    def __init__(
            self,
            relative_file_name: Union[str, PathLike],
            program_ctx: ProgramCompilationContext
    ):
        self._program_ctx: ProgramCompilationContext = program_ctx
        self._logic_stream: ParacQualifiedLogicStream = \
            ParacQualifiedLogicStream()
        self._relative_file_name = relative_file_name

    @property
    def relative_file_name(self) -> Union[str, PathLike]:
        """
        Returns the relative file name, which goes out from the entry file
        and has a relative path to every file imported and used.
        """
        return self._relative_file_name

    @property
    def program_ctx(self) -> ProgramCompilationContext:
        """
        Returns the program_ctx if it was already set using set_program_ctx()
        """
        return self._program_ctx

    @property
    def logic_stream(self) -> ParacQualifiedLogicStream:
        """
        Returns the content of the file represented as a stream containing
        LogicTokens
        """
        return self._logic_stream

    def set_program_ctx(self, ctx: ProgramCompilationContext) -> None:
        """
        Sets the program context, containing the information for the entire
        compilation and relative structure
        """
        self._program_ctx = ctx


class ProgramCompilationContext(ProgramRunContext):
    """
    Program Compilation Context, which serves as the base for the compilation
    of an entire program containing possibly more than one file. Holds the
    entire context of the program and is used in the linker and last step of
    semantic analysis to validate the program.
    """

    def __init__(self, process: ProgramCompilationProcess):
        self._context_dict: Dict[
            Union[str, PathLike], FileCompilationContext
        ] = {}
        super().__init__(process=process)

    @property
    def process(self) -> ProgramCompilationProcess:
        """ Compilation Process of this instance """
        return self._process

    @property
    def files(self) -> List[Path]:
        """ Returns the source files for the process """
        return self.process.files

    @property
    def project_root(self) -> Union[str, PathLike]:
        """
        Returns the working directory / base-path for the program.
        """
        return self.process.project_root

    @property
    def encoding(self) -> str:
        """ Returns the encoding of the project """
        return super().encoding

    @property
    def context_dict(self) -> Dict[
        Union[str, PathLike], FileCompilationContext
    ]:
        """
        Returns a list for all context instances. The key is a relative path
        name to the FileContext
        """
        return self._context_dict

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

    async def gen_source(self) -> Dict[str, Dict[str, FileCompilationContext]]:
        """
        Generates the source C-code from the tokens stored inside the class.

        :returns: If the dict is returned, the items will be as followed: Name
         of the file (Relative name), The code-string, The compilation context
         of the file.
        """
        ...

    async def process_program(self, prefer_logging: bool) -> None:
        """
        Processes this instance and generates the logic streams required
        for generating the finished code.

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """
        ...  # TODO! Run listener for every file

    async def parse_file(
            self,
            file_path: Union[str, PathLike, Path],
            prefer_logging: bool
    ) -> FileCompilationContext:
        """
        Gets a FileStream, converts it to a string stream and parses it
        returning the resulting FilePreProcessorContext

        :param file_path: Path to the file
        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        :returns: The FilePreProcessorContext instance for the file
        """
        from .compiler import ParacCompiler
        from ..util import (get_file_stream, get_relative_file_name)

        if type(file_path) is not Path:
            file_path: Path = Path(str(file_path)).resolve()

        file_stream: antlr4.FileStream = get_file_stream(
            file_path, self.encoding
        )
        relative_file_name: str = get_relative_file_name(
            file_name=file_stream.name,
            file_path=file_stream.fileName,
            base_path=self.project_root
        )
        stream: antlr4.InputStream = get_input_stream(
            # rm comments
            ParacCompiler.remove_comments_from_str(file_stream.strdata),
            name=file_stream.name
        )
        return await self._parse_stream(
            stream, relative_file_name, prefer_logging
        )

    async def _parse_stream(
            self,
            stream: antlr4.InputStream,
            relative_file_name: str,
            prefer_logging: bool,
    ) -> FileCompilationContext:
        """
        Parses a single file based on the passed stream and
        generates the FilePreProcessorContext

        :param stream: The Antlr4 InputStream which represents a string stream
        :param relative_file_name: Relative name of the file (fetch-able using
         get_relative_file_name)
        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        :returns: The generated FilePreProcessorContext instance
        """
        from .compiler import ParacCompiler
        from .parser.listener import Listener

        logger.debug(f"Parsing file ({relative_file_name})")
        antlr4_file_ctx = await ParacCompiler.parse(
            stream, prefer_logging
        )

        listener = Listener(
            antlr4_file_ctx, stream, relative_file_name, program_ctx=self
        )
        await listener.walk_and_generate_logic_stream(prefer_logging)
        return listener.file_ctx

    async def parse_all_files(
            self, prefer_logging: bool
    ) -> List[FileCompilationContext]:
        """
        Parses all files, and generates the logic streams for them

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """
        return list(
            await self.parse_file(
                str(file.absolute()), prefer_logging
            ) for file in self.files
        )
