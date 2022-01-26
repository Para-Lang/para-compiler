# coding=utf-8
"""
Compilation Process Classes, which are the management classes, which then
implement the Compilation Context classes. It's the main storage class, which
also contains the functions for various usage cases and is intended as the
main point where the compilation will happen.
"""
from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from os import PathLike
from pathlib import Path
from typing import Union, Tuple, List, Optional, AsyncGenerator

from .compile_ctx import ProgramCompilationContext
from ..exceptions import FileAccessError
from ..preprocessor import PreProcessorProcessResult
from ..preprocessor.ctx import ProgramPreProcessorContext
from ..util import (has_valid_file_ending, validate_path_like,
                    ensure_pathlib_path)

__all__ = [
    'Process',
    'CompileProcess',
    'CompileResult'
]

logger = logging.getLogger(__name__)


class Process(ABC):
    """ Basic Process serving as parent class for the process instances """

    @abstractmethod
    def __init__(
            self,
            files: List[Union[str, bytes, PathLike, Path]],
            project_root: Union[str, bytes, PathLike, Path],
            encoding: str
    ):
        """
        Initialises the instance and validates the passed entry file for
        further usage.

        :param files: A list of files that should be used in the program. All
         possible sys-links will be resolved and made absolute by
         ensure_pathlib_path()
        :param project_root: The working directory / source directory to use as
         root
        :param encoding: The encoding for the files
        """
        files: List[Path] = list(ensure_pathlib_path(i) for i in files)

        # Validating correct file endings
        for file in files:
            if has_valid_file_ending(file.name) is False:
                logger.warning(
                    "The given file ending does not follow "
                    "the Para conventions (.para, .ph, .c, .h, .parah)!"
                )

            try:
                validate_path_like(file)
            except FileAccessError as e:
                # If the validation failed the path might be an invalid path or
                # permissions for proper accessing/reading are missing
                raise e

        self._files = files
        self._encoding = encoding
        self._project_root = ensure_pathlib_path(project_root)

    @property
    def project_root(self) -> Union[Path]:
        """
        Returns the working directory / base-path for the program.
        """
        return self._project_root

    @property
    def files(self) -> List[Path]:
        """ Returns the source files for the process """
        return self._files

    @property
    def encoding(self) -> str:
        """ Returns the encoding of the process """
        return self._encoding


class CompileResult(Process):
    """
    Class used to represent the result of a compilation. This will be returned
    by the function 'CompileProcess.compile()'
    """

    def __init__(
            self,
            files: List[Union[str, bytes, PathLike, Path]],
            project_root: Union[str, bytes, PathLike, Path],
            encoding: str,
            process: CompileProcess
    ):
        self.done_process = process
        super().__init__(files, project_root, encoding)

    def write_results(
            self,
            build_path: Union[str, bytes, PathLike, Path],
            dist_path: Union[str, bytes, PathLike, Path]
    ):
        """
        This function will write the results of the compilation into
        the specified build and dist path
        """
        raise NotImplementedError()


class CompileProcess(Process):
    """
    Process instance used for a program compilation process. Interface for
    running a compilation and storing basic values.

    This does not contain direct program vital data like
    ProgramCompilationContext.
    """

    def __init__(
            self,
            files: List[Union[str, bytes, PathLike, Path]],
            project_root: Union[str, bytes, PathLike, Path],
            encoding: str
    ):
        """
        Initialises and validates the provided parameter for the compilation
        process. In case of an error an exception will be raised and the
        process cancelled.

        :param files: A list of files that should be used in the program. All
         possible sys-links will be resolved and made absolute by
         ensure_pathlib_path()
        :param project_root: The working directory / source directory to use as
         root
        :param encoding: The encoding for the files
        :returns: The file name, the output build path, the output dist path
         and the arguments passed for the compilation
        """
        super().__init__(files, project_root, encoding)

        self._temp_files: List[str] = []
        self._preprocessor_ctx = \
            ProgramPreProcessorContext(files, project_root, encoding)
        self._compilation_ctx = \
            ProgramCompilationContext(files, project_root, encoding)

    @property
    def files(self) -> List[Path]:
        """ Returns the source files for the process """
        return self._files

    @property
    def preprocessor_ctx(self) -> ProgramPreProcessorContext:
        """ Context for the Pre-Processor """
        return self._preprocessor_ctx

    @property
    def compilation_ctx(self) -> ProgramCompilationContext:
        """ Context for the compilation """
        return self._compilation_ctx

    async def preprocess_files(
            self, prefer_logging: bool
    ) -> PreProcessorProcessResult:
        """ Runs the Pre-Processor and generates the temporary files """
        logger.info(
            "Processing files in the Pre-Processor"
        )
        return await self.preprocessor_ctx.process_files(
            prefer_logging
        )

    async def compile(self) -> CompileResult:
        """
        Default function which compiles the passed input data and returns
        a new finished process instance. This function should be used as the
        default entry point for a compilation (when using the module version,
        which will raise errors when using), without having to specify too
        much for the input.
        """
        async for result in self.compile_gen(False):
            if type(result[3]) is CompileResult:
                return result[3]  # Optional[FinishedProcess]

    async def compile_gen(self, track_progress: bool = True) -> AsyncGenerator[
        Tuple[
            int,
            Optional[str],
            int,
            Optional[CompileResult]
        ], None, None
    ]:
        """
        Runs the compilation as an async generator returning the progress and
        results of the compilation. This function should help to accurately
        visualise progress, and show how fast the compilation is going.

        :param track_progress: If set to True, the function will only return
         the final result and not yield any progress using the generator.
        """
        if track_progress:
            yield 5, "Running Pre-Processor", logging.INFO, None

        res: PreProcessorProcessResult = await self.preprocess_files(True)

        if track_progress:
            yield 20, "Parsing files and generating Parse Streams", \
                  logging.INFO, None

        await self.compilation_ctx.process_program(True)

        ...  # TODO! Add remaining stuff

        yield 100, None, logging.INFO, CompileResult(
            self.files, self.project_root, self.encoding, self
        )
