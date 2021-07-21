# coding=utf-8
""" Tests for the Lexer and Parser """
import logging
import os
from typing import List
import asyncio

from parac import SEPARATOR as SEP
from parac.logging import set_avoid_print_banner_overwrite
from parac.compiler import ParacCompiler, para_compiler, BasicProcess

from .. import reset_input

logger = logging.getLogger('compiler')

compiler = ParacCompiler()
para_compiler.init_logging_session(
    level=logging.DEBUG, print_banner=False
)
set_avoid_print_banner_overwrite(True)
main_file_path = f"{os.getcwd()}{SEP}test_files{SEP}entry.para"
test_c_files_dir = f"{os.getcwd()}{SEP}test_files{SEP}c_files{SEP}"
test_para_files_dir = f"{os.getcwd()}{SEP}test_files{SEP}"


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
