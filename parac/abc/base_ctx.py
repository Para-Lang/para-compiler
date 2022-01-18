# coding=utf-8
"""
Base Program ABC classes for the Pre-Processor and Compiler Context Classes
"""
import logging
from abc import ABC, abstractmethod
from os import PathLike
from pathlib import Path
from typing import Union, Dict, Any, List

import antlr4

__all__ = [
    'FileRunContext',
    'ProgramRunContext'
]

logger = logging.getLogger(__name__)


class FileRunContext(ABC):
    """
    Base ABC Class for a File Run Context. Used in both
    FilePreProcessorContext and FileCompilationContext
    """

    @abstractmethod
    def __init__(
            self,
            program_ctx,
            logic_stream,
            processed_stream,
            relative_file_name: Union[str, PathLike]
    ):
        self._program_ctx = program_ctx
        self._logic_stream = logic_stream
        self._processed_stream = processed_stream
        self._relative_file_name = relative_file_name

    @property
    def relative_file_name(self) -> Union[str, PathLike]:
        """
        Returns the relative file name, which goes out from the entry file
        and has a relative path to every file imported and used.
        """
        return self._relative_file_name

    @property
    @abstractmethod
    def program_ctx(self) -> Any:
        """
        Returns the program_ctx if it was already set using set_program_ctx()
        """
        return self._program_ctx

    @property
    @abstractmethod
    def logic_stream(self) -> Any:
        """
        Returns the content of the file represented as a stream containing
        logic tokens
        """
        return self._logic_stream

    @abstractmethod
    def set_program_ctx(self, ctx: Any) -> None:
        """
        Sets the program context, containing the information for the entire
        compilation and relative structure
        """
        self._program_ctx = ctx


class ProgramRunContext(ABC):
    """
    Base ABC Class for a Program Context. Used in both
    ProgramPreProcessorContext and ProgramCompilationContext
    """

    @abstractmethod
    def __init__(self, process):
        self._context_dict: Dict[
            Union[str, PathLike], FileRunContext
        ] = {}
        self._process = process

    @property
    @abstractmethod
    def process(self) -> Any:
        """ Compilation Process of this instance """
        return self._process

    @property
    @abstractmethod
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
        return self._process.work_dir

    @property
    @abstractmethod
    def encoding(self) -> str:
        """ Returns the encoding of the project """
        return self._process.encoding

    @property
    def context_dict(self) -> Dict[
        Union[str, PathLike], FileRunContext
    ]:
        """
        Returns a list for all context instances. The key is a relative path
        name to the FileContext
        """
        return self._context_dict

    def add_file_ctx(
            self,
            ctx: FileRunContext,
            relative_file_name: Union[str, PathLike]
    ) -> None:
        """
        Adds a FilePreProcessorContext to the list of file ctx instances.
        The context instance should only be created using this class
        """
        ctx.set_program_ctx(self)
        self._context_dict[relative_file_name] = ctx

    @abstractmethod
    async def parse_file(
            self,
            file_path: Union[str, PathLike],
            prefer_logging: bool
    ) -> FileRunContext:
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
        ...

    @abstractmethod
    async def _parse_stream(
            self,
            stream: antlr4.InputStream,
            relative_file_name: str,
            prefer_logging: bool,
    ) -> FileRunContext:
        """
        Parses a single file and generates a file context for it

        :param stream: The Antlr4 InputStream which represents a string stream
        :param relative_file_name: Relative name of the file (fetch-able
         using get_relative_file_name)
        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        :returns: The generated FilePreProcessorContext instance
        """
        ...

    @abstractmethod
    async def parse_all_files(
            self, prefer_logging: bool
    ) -> List[FileRunContext]:
        """
        Parses all files, and generates the logic streams for them

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """
        ...
