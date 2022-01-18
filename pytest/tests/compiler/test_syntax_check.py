# coding=utf-8
""" Tests for the Lexer and Parser """
import asyncio
import logging
import os
from pathlib import Path
from typing import List

from parac import RUNTIME_COMPILER, initialise_default_paths
from parac.compiler import ParacCompiler, BasicProcess
from parac.logging import set_avoid_print_banner_overwrite
from .. import reset_input, BASE_TEST_PATH

logger = logging.getLogger('compiler')

compiler = ParacCompiler()

# Initialises the logging session for the compiler
RUNTIME_COMPILER.init_logging_session(
    level=logging.DEBUG, print_banner=False
)

main_file_path: Path = BASE_TEST_PATH / "test_files" / "basic.para"
test_c_files_dir: Path = BASE_TEST_PATH / "test_files" / "c_ref_files"
test_para_files_dir: Path = BASE_TEST_PATH / "test_files"

# Avoiding printing the banner (CLI)
set_avoid_print_banner_overwrite(True)

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestSyntaxCheck:
    @staticmethod
    def teardown_method(_):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
        """
        reset_input()

    def test_single_file(self):
        asyncio.run(
            RUNTIME_COMPILER.validate_syntax(main_file_path, 'utf-8', False)
        )

    def test_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            asyncio.run(
                RUNTIME_COMPILER.validate_syntax(
                    str(file.path), 'utf-8', False
                )
            )

    def test_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            asyncio.run(
                RUNTIME_COMPILER.validate_syntax(
                    str(file.path), 'utf-8', False
                )
            )
