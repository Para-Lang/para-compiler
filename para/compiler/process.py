# coding=utf-8
"""
Compilation Process Classes, which are the management classes, which then
implement the Compilation Context classes. It's the main storage class, which
also contains the functions for various usage cases and is intended as the
main point where the compilation will happen.
"""
from __future__ import annotations

import logging
import os
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
    'BasicProcess',
    'ProgramCompilationProcess',
    'FinishedProcess'
]

logger = logging.getLogger(__name__)


class BasicProcess:
    """ Basic Process serving as parent class for the process instances """

    def __init__(
            self,
            files: List[Union[str, bytes, PathLike]],
            project_root: Union[str, bytes, PathLike],
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


class FinishedProcess:
    """ Class used to represent a done compilation process """

    def __init__(self, files, process: ProgramCompilationProcess):
        self.done_process = process
        self.files = files


class ProgramCompilationProcess(BasicProcess):
    """
    Process instance used for a program compilation process. Interface for
    running a compilation and storing basic values.

    This does not contain direct program vital data like
    ProgramCompilationContext.
    """

    def __init__(
            self,
            files: List[Union[str, bytes, PathLike]],
            project_root: Union[str, bytes, PathLike],
            encoding: str,
            build_path: Union[str, bytes, PathLike],
            dist_path: Union[str, bytes, PathLike]
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
        :param build_path: The path to the output folder
        :param dist_path: The path to the dist folder
        :returns: The file name, the output build path, the output dist path
         and the arguments passed for the compilation
        """
        super().__init__(files, project_root, encoding)

        self._build_path = ensure_pathlib_path(build_path)
        self._dist_path = ensure_pathlib_path(dist_path)
        self._temp_files: List[str] = []
        self._preprocessor_ctx = ProgramPreProcessorContext(self)
        self._compilation_ctx = ProgramCompilationContext(self)

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

    @property
    def temp_build_folder(self) -> Union[str, PathLike]:
        """ Returns the temp folder in the build folder """
        return (self.build_path / Path("temp")).resolve()

    @property
    def temp_dist_folder(self) -> Union[str, PathLike]:
        """ Returns the temp folder in the dist folder """
        return (self.dist_path / Path("temp")).resolve()

    @property
    def temp_files(self) -> List[str]:
        """
        Returns the temporary files that were created by the Pre-Processor
        """
        return self._temp_files

    @property
    def build_path(self) -> Path:
        """ Path to the build folder """
        return self._build_path

    @property
    def dist_path(self) -> Path:
        """ Path to the dist folder """
        return self._dist_path

    def _make_temp_folder(self):
        """
        Creates the folder for the temporary files that will be used by the
        preprocessor
        """
        os.makedirs(self.temp_build_folder, exist_ok=True)
        os.makedirs(self.temp_dist_folder, exist_ok=True)
        logger.debug("Created temp folders for the Pre-Processor")

    async def compile_with_progress_iterator(self) -> AsyncGenerator[
        Tuple[
            int,
            Optional[str],
            int,
            Optional[FinishedProcess]
        ], None, None
    ]:
        """
        Runs the compilation but yields the progress in form of tuples:

        int - Progress count from 0 to 1000 (0 = 0%, 1000 = 100%)
        Optional[str] - Name of the next step in form of a string. Is None
        when the  process finished
        int - Log level for the returned string message
        Optional[FinishedProcess] - None until the process finally finished

        For info about compilation see compile()
        """
        return self.ci_compile(True)

    async def compile(self) -> FinishedProcess:
        """
        Default function which compiles the passed input data and returns
        a new finished process instance. This function should be used as the
        default entry point for a compilation (when using the module version,
        which will raise errors when using), without having to specify too
        much for the input.
        """
        async for result in self.ci_compile(False):
            if type(result[3]) is FinishedProcess:
                return result[3]  # Optional[FinishedProcess]

    async def preprocess_files(
            self, prefer_logging: bool
    ) -> PreProcessorProcessResult:
        """ Runs the Pre-Processor and generates the temporary files """
        logger.info(
            "Processing project files in the Pre-Processor"
        )
        self._make_temp_folder()
        return await self.preprocessor_ctx.process_program(
            prefer_logging
        )

    async def gen_preprocessor_temp_files(
            self, preprocessor_result: PreProcessorProcessResult
    ) -> None:
        """
        Generates the temp files based on the output of the preprocessor
        """
        raise NotImplementedError("This function is not implemented yet")

        # TODO! This needs to be finished later

        logger.debug("Generating the modified temporary files")

        # Generating the temp files which are then used for the further
        # compilation
        self._temp_files = await self.preprocessor_ctx.make_temp_files(
            preprocessor_result
        )
        logger.debug("Wrote processed files to temp storage")

    async def ci_compile(self, track_progress: bool) -> AsyncGenerator[
        Tuple[
            int,
            Optional[str],
            int,
            Optional[FinishedProcess]
        ], None, None
    ]:
        """
        Actual compile that serves as c-implementation for compile() and
        compile_with_progress_iterator()
        """
        if track_progress:
            yield 5, "Running Pre-Processor", logging.INFO, None

        preprocessor_result = await self.preprocess_files(True)

        if track_progress:
            yield 15, "Generating modified temp files", logging.INFO, None

        await self.gen_preprocessor_temp_files(preprocessor_result)

        if track_progress:
            yield 20, "Parsing files and generating logic streams", \
                  logging.INFO, None

        await self.compilation_ctx.process_program(True)

        ...  # TODO! Add remaining stuff

        yield 100, None, logging.INFO, FinishedProcess(self)
