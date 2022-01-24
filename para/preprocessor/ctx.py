# coding=utf-8
"""
File containing the classes which will be used to track and run a pre-processor
compilation. The context classes will track directives and correctly run the
commands as given in the file.
"""
from __future__ import annotations

import logging
from os import PathLike
from pathlib import Path
from typing import Dict, Union, List, TYPE_CHECKING, Tuple

import antlr4

from .__main__ import PreProcessor, PreProcessorProcessResult
from .logic_stream import PreProcessorStream
from ..abc import ProgramRunContext, FileRunContext
from ..exceptions import (FailedToProcessError, ParserError, LexerError,
                          ParaSyntaxErrorCollection, ParaCompilerError)

if TYPE_CHECKING:
    from ..compiler import ProgramCompilationProcess

__all__ = [
    'FilePreProcessorContext',
    'ProgramPreProcessorContext'
]

logger = logging.getLogger(__name__)


class FilePreProcessorContext(FileRunContext):
    """
    Class used inside the listener for managing the context of a single file,
    where directives and code are stored and managed.
    """

    def __init__(
            self,
            relative_file_name: Union[str, PathLike],
            program_ctx: ProgramPreProcessorContext
    ):
        super().__init__(
            program_ctx=program_ctx,
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

    async def process_directives(self) -> str:
        """
        Process the directives for this single file and returns a string
        containing the altered file
        """
        ...

        # TODO! Implement this


class ProgramPreProcessorContext(ProgramRunContext):
    """
    Program Compilation Context, which serves as the base for an entire
    pre-processor compilation.

    This class will be initialised using a ProgramCompilationProcess and
    use the context info for fetching the files, parsing them and altering
    them appropriately depending on their content. The result will be an
    `PreProcessorProcessResult`, which is returned from the function
    `async process_program()`
    """

    def __init__(self, process: ProgramCompilationProcess):
        self._context_dict: Dict[
            Union[str, PathLike], FilePreProcessorContext
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
    def context_dict(self) -> Dict[
        Union[str, PathLike], FilePreProcessorContext
    ]:
        """
        Returns a list for all context instances. The key is a relative path
        name to the FileContext
        """
        return self._context_dict

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

    @staticmethod
    async def make_temp_files(
            process: PreProcessorProcessResult
    ) -> List[Path]:
        """
        Creates the temporary files based on the passed output of
        process_program().

        :returns: A tuple containing at 0 the path to the entry-file and at 1
         a list of all paths of all other files.
        """
        for name, context in process.generated_files():
            name: str
            context: Dict[str, FilePreProcessorContext]

            # TODO! Add logic to properly generate these files

        raise NotImplementedError()

    async def process_program(
            self, prefer_logging: bool
    ) -> PreProcessorProcessResult:
        """
        Processes this instance and generates the logic streams required
        for generating the finished code.

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        :returns: A PreProcessorProcessResult instance
        """
        # TODO! Run listener for every single file of those

        # TODO! Finish by processing the directives and altering the files

        # Processing the directives
        return await PreProcessor.process_directives(self)

    async def parse_file(
            self,
            file_path: Union[str, PathLike],
            prefer_logging: bool
    ) -> FilePreProcessorContext:
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
        from ..compiler import Paraompiler
        from ..util import (
            get_file_stream, get_relative_file_name, get_input_stream
        )

        file_stream = get_file_stream(file_path, self.encoding)
        relative_file_name = get_relative_file_name(
            file_name=file_stream.name,
            file_path=file_stream.fileName,
            base_path=self.work_dir
        )
        stream = get_input_stream(
            # rm comments
            ParaCompiler.remove_comments_from_str(file_stream.strdata),
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
    ) -> FilePreProcessorContext:
        """
        Parses a single file and generates the FilePreProcessorContext

        :param stream: The Antlr4 InputStream which represents a string stream
        :param relative_file_name: Relative name of the file (fetch-able
         using get_relative_file_name)
        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        :returns: The generated FilePreProcessorContext instance
        :raises FailedToProcessError: If prefer_logging is True and
         an exception is encountered. The logs of the exception will be printed
         onto the console.
        """
        from .listener import Listener

        try:
            antlr4_file_ctx = await PreProcessor.parse(
                stream, prefer_logging
            )
            listener = Listener(
                antlr4_file_ctx, stream, relative_file_name, program_ctx=self
            )
            await listener.walk_and_process_directives(prefer_logging)
            logger.info(
                f"Finished parsing for file '{relative_file_name}' "
                "(relative name)"
            )

            # NOTE! At the current version the result of the listener is a
            # logic-stream that only contains include directives and
            # non-preprocessor items

            return listener.file_ctx
        except (LexerError, ParserError, ParaSyntaxErrorCollection,
                ParaCompilerError) as e:
            if prefer_logging:
                raise FailedToProcessError(exc=e) from e
            else:
                raise e

    async def parse_all_files(
            self, prefer_logging: bool
    ) -> List[FilePreProcessorContext]:
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
