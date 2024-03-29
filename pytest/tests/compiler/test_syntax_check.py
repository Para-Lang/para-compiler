# coding=utf-8
""" Tests for the Lexer and Parser """
import asyncio
import os
from pathlib import Path
from typing import List

from paralang_base import initialise_default_paths
from paralang_base.compiler import ParaCompiler
from .. import BASE_TEST_PATH


compiler = ParaCompiler()

main_file_path: Path = BASE_TEST_PATH / "test_files" / "main.para"
test_c_files_dir: Path = BASE_TEST_PATH / "test_files" / "c_ref_files"
test_para_files_dir: Path = BASE_TEST_PATH / "test_files"

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestValidateSyntax:
    def test_single_file_without_prefer_logging(self):
        asyncio.run(
            compiler.validate_syntax(main_file_path, 'utf-8', False)
        )

    def test_single_file_with_prefer_logging(self):
        asyncio.run(
            compiler.validate_syntax(main_file_path, 'utf-8')
        )

    def test_multiple_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            asyncio.run(
                compiler.validate_syntax(str(file.path), 'utf-8', False)
            )

    def test_multiple_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            asyncio.run(
                compiler.validate_syntax(str(file.path), 'utf-8', False)
            )
