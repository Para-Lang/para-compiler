# coding=utf-8
""" Tests for the Lexer and Parser """
import logging
import os
from pathlib import Path
from typing import List
import asyncio

from parac import RUNTIME_COMPILER, initialise_default_paths
from parac.logging import set_avoid_print_banner_overwrite
from parac.compiler import ParacCompiler, BasicProcess

from .. import reset_input, BASE_TEST_PATH

logger = logging.getLogger('compiler')

compiler = ParacCompiler()

# Initialises the logging session for the compiler
RUNTIME_COMPILER.init_logging_session(
    level=logging.DEBUG, print_banner=False
)

main_file_path: Path = BASE_TEST_PATH / "test_files" / "entry.para"
test_c_files_dir: Path = BASE_TEST_PATH / "test_files" / "c_ref_files"
test_para_files_dir: Path = BASE_TEST_PATH / "test_files"

# Avoiding printing the banner (CLI)
set_avoid_print_banner_overwrite(True)

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestParser:
    @staticmethod
    def teardown_method(_):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
        """
        reset_input()

    def test_entry_file_path(self):
        p = BasicProcess(main_file_path, 'utf-8')
        asyncio.run(p.validate_syntax(True))

    def test_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            p = BasicProcess(file.path, 'utf-8')
            asyncio.run(p.validate_syntax(True))

    def test_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            p = BasicProcess(file.path, 'utf-8')
            asyncio.run(p.validate_syntax(True))
