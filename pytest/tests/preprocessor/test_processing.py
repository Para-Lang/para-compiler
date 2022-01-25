# coding=utf-8
""" Tests for the Pre-Processor Lexer and Parser """
import asyncio
import logging
import os
from pathlib import Path
from typing import List

from paralang import initialise_default_paths
from paralang.compiler import (ParaCompiler, CompilationProcess)
from .. import add_folder, remove_folder, BASE_TEST_PATH

logger = logging.getLogger('paralang')
logger.setLevel(logging.DEBUG)
compiler = ParaCompiler()

test_c_files_dir: Path = BASE_TEST_PATH / "test_files" / "c_ref_files"
test_para_files_dir: Path = BASE_TEST_PATH / "test_files"
test_processor_files_dir: Path = BASE_TEST_PATH / "test_files" / "preprocessor"

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestProcessing:
    def test_parse_preprocessor_targets(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_processor_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            b_path: Path = add_folder("build")
            d_path: Path = add_folder("dist")

            asyncio.run(CompilationProcess(
                [file.path], Path(str(file.path)).parent, 'utf-8'
            ).preprocess_files(True))

            remove_folder("build")
            remove_folder("dist")

    def test_parse_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            asyncio.run(CompilationProcess(
                [file.path], Path(file.path).parent, 'utf-8'
            ).preprocess_files(True))

    def test_parse_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            asyncio.run(CompilationProcess(
                [file.path], Path(file.path).parent, 'utf-8'
            ).preprocess_files(True))
