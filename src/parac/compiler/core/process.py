# coding=utf-8
"""
Compiler Process Implementations which represent a compilation process aka.
one execution of the compiler as a whole
"""
from __future__ import annotations

import logging
import os
from os import PathLike
from typing import Union, Tuple, List, Optional, AsyncGenerator

from ...preprocessor import PreProcessorProcessResult
from ...preprocessor.ctx import ProgramPreProcessorContext

from .ctx import ProgramCompilationContext
from ..utils import (decode_if_bytes, cleanup_path, validate_file_ending,
                     validate_path_like)
from ..para_exceptions import FileAccessError

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
            entry_file_path: Union[str, bytes, PathLike],
            encoding: str
    ):
        """
        Initialises the instance and validates the passed entry file for
        further usage.

        :param entry_file_path: The entry-file of the program. The compiler
                                will use the working directory as base dir if
                                the path is relative
        """
        entry_file_path = cleanup_path(decode_if_bytes(entry_file_path))

        # Getting the last element aka. the lowest level of the path
        _last_path_elem = entry_file_path.replace("/", "\\").split("\\")[-1]
        # for the sake of checking; all paths used are converted into
        # the windows path-style
        if "." not in _last_path_elem or _last_path_elem.endswith("\\"):
            logger.warning(
                "The given file does not seem to be in the correct format!"
            )
        elif validate_file_ending(_last_path_elem):
            logger.warning(
                "The given file ending does not follow "
                "the Para-C conventions (.para, .ph, .c, .h, .parah)!"
            )

        try:
            validate_path_like(entry_file_path)
        except FileAccessError as e:
            # If the validation failed the path might be a relative path
            # that does not have a . signalising its going python from the
            # current path meaning the work-directory path needs to be
            # appended. If that also fails it is an invalid path or permissions
            # are missing
            absolute_path = cleanup_path(f"{os.getcwd()}\\{entry_file_path}")
            failed = False
            try:
                validate_path_like(absolute_path)
            except FileAccessError:
                failed = True
            if failed:
                raise e
            entry_file_path = absolute_path
        self._entry_file_path = entry_file_path
        self._encoding = encoding
        self._work_dir = self._get_work_dir()

    @property
    def work_dir(self) -> Union[str, PathLike]:
        """
        Returns the working directory / base-path for the program. If the entry
        file path was relative, then the working directory where the compiler
        is run is used as the working directory.
        """
        return self._work_dir

    @property
    def entry_file_path(self) -> Union[str, PathLike]:
        """ Returns the entry-file of the process """
        return self._entry_file_path

    @property
    def encoding(self) -> str:
        """ Returns the encoding of the process """
        return self._encoding

    def _get_work_dir(self) -> str:
        """ Gets the working directory for the program """
        from .. import SEPARATOR
        return SEPARATOR.join(self.entry_file_path.split(SEPARATOR)[:-1])

    async def validate_syntax(self, enable_out: bool) -> bool:
        """
        Validates the syntax of the file of this entry-file and logs or raises
        errors while running

        :param enable_out: If set to True errors, warnings and info will be
                           logged onto the console using the local logger
                           instance. If an exception is raised or error is
                           encountered, it will be reraised with the
                           FailedToProcessError.
        :returns: True if the syntax check was successful else False
        """
        from .compiler import ParacCompiler
        return await ParacCompiler.validate_syntax(self, enable_out)


class FinishedProcess(BasicProcess):
    """ Class used to represent a done compilation process """

    def __init__(self, process: ProgramCompilationProcess):
        self.done_process = process
        super().__init__(process.entry_file_path, process.encoding)


class ProgramCompilationProcess(BasicProcess):
    """
    Process instance used for a program compilation process. Interface for
    running a compilation and storing basic values.

    This does not contain direct program vital data like
    ProgramCompilationContext.
    """

    def __init__(
            self,
            entry_file_path: Union[str, bytes, PathLike],
            encoding: str,
            build_path: Union[str, bytes, PathLike],
            dist_path: Union[str, bytes, PathLike]
    ):
        """
        Initialises and validates the provided parameter for the compilation
        process. In case of an error an exception will be raised and the
        process cancelled.

        :param entry_file_path: The entry-file of the program. The compiler
                                will use the working directory as base dir
                                if the path is relative
        :param build_path: The path to the output folder
        :param dist_path: The path to the dist folder
        :returns: The file name, the output build path, the output dist path
                  and the arguments passed for the compilation
        """
        super().__init__(entry_file_path, encoding)

        build_path: Union[str, PathLike] = decode_if_bytes(build_path)
        dist_path: Union[str, PathLike] = decode_if_bytes(dist_path)

        self._build_path = cleanup_path(build_path)
        self._dist_path = cleanup_path(dist_path)
        self._temp_files: List[str] = []
        self._temp_entry_file_path: Union[str, None] = None
        self._preprocessor_ctx = ProgramPreProcessorContext(self)
        self._compilation_ctx = ProgramCompilationContext(self)
        self._make_temp_folder()

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
        # SEPARATOR should in this case point to the correct path separator
        # due to the cleanup of paths in the initialisation
        from .. import SEPARATOR
        if self.build_path.endswith(SEPARATOR):
            return cleanup_path(f"{self.build_path}temp")
        else:
            return cleanup_path(f"{self.build_path}{SEPARATOR}temp")

    @property
    def temp_dist_folder(self) -> Union[str, PathLike]:
        """ Returns the temp folder in the dist folder """
        # SEPARATOR should in this case point to the correct path separator
        # due to the cleanup of paths in the initialisation
        from .. import SEPARATOR
        if self.dist_path.endswith(SEPARATOR):
            return cleanup_path(f"{self.dist_path}temp")
        else:
            return cleanup_path(f"{self.dist_path}{SEPARATOR}temp")

    @property
    def temp_files(self) -> List[str]:
        """
        Returns the temporary files that were created by the Pre-Processor
        """
        return self._temp_files

    @property
    def temp_entry_file_path(self) -> str:
        """
        Returns the temporary entry-file that was created by the Pre-Processor
        """
        return self._temp_entry_file_path

    @property
    def entry_file_path(self) -> Union[str, PathLike]:
        """ Entry file of the program """
        return self._entry_file_path

    @property
    def build_path(self) -> Union[str, PathLike]:
        """ Path to the build folder """
        return self._build_path

    @property
    def dist_path(self) -> Union[str, PathLike]:
        """ Path to the dist folder """
        return self._dist_path

    def _make_temp_folder(self):
        """
        Creates the folder for the temporary files that will be created by the
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
        return self._compile(True)

    async def compile(self) -> FinishedProcess:
        """
        Default function which compiles the passed input data and returns
        a new finished process instance
        """
        async for result in self._compile(False):
            if type(result[3]) is FinishedProcess:
                return result[3]  # Optional[FinishedProcess]

    async def _run_preprocessor(
            self, enable_out: bool
    ) -> PreProcessorProcessResult:
        """ Runs the Pre-Processor and generates the temporary files """
        logger.info(
            "Processing files in the Pre-Processor"
        )
        return await self.preprocessor_ctx.process_program(enable_out)

    async def _gen_preprocessor_temp_files(
            self, preprocessor_result: PreProcessorProcessResult
    ) -> None:
        """
        Generates the temp files based on the output of the preprocessor
        """
        logger.debug("Generating the modified temporary files")

        # Generating the temp files which are then used for the further
        # compilation
        tmp = await self.preprocessor_ctx.make_temp_files(
            preprocessor_result
        )
        self._temp_entry_file_path, self._temp_files = tmp
        logger.debug("Wrote processed files to temp storage")

    async def _compile(self, track_progress: bool) -> AsyncGenerator[
        Tuple[
            int,
            Optional[str],
            int,
            Optional[FinishedProcess]
        ], None, None
    ]:
        """
        Actual compile that serves as implementation for compile() and
        compile_with_progress_iterator()
        """
        if track_progress:
            # Currently only a replacement for testing purposes
            yield 5, "Running Pre-Processor", logging.INFO, None

        preprocessor_result = await self._run_preprocessor(True)

        if track_progress:
            # Currently only a replacement for testing purposes
            yield 15, "Generating modified temp files", logging.INFO, None

        await self._gen_preprocessor_temp_files(preprocessor_result)

        if track_progress:
            # Currently only a replacement for testing purposes
            yield 20, "Parsing files and generating logic streams",\
                  logging.INFO, None

        await self.compilation_ctx.process_program(True)

        ...

        yield 100, None, logging.INFO, FinishedProcess(self)
