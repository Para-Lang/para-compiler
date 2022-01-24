# coding=utf-8
""" Tests for the Lexer and Parser """
import asyncio
import logging
import os
from pathlib import Path
from typing import List

from parac import initialise_default_paths
from parac.compiler import ParacCompiler, BasicProcess
from .. import BASE_TEST_PATH

logger = logging.getLogger('compiler')

compiler = ParacCompiler()

main_file_path: Path = BASE_TEST_PATH / "test_files" / "entry.para"
test_c_files_dir: Path = BASE_TEST_PATH / "test_files" / "c_ref_files"
test_para_files_dir: Path = BASE_TEST_PATH / "test_files"

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestValidateSyntax:
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
