# coding=utf-8
""" Tests for the Lexer and Parser """
import logging
import os
from typing import List

import asyncio

import paraccompiler
from . import reset_input

logger = logging.getLogger('paraccompiler')

sep = paraccompiler.SEPARATOR
compiler = paraccompiler.ParacCompiler()
paraccompiler.para_compiler.init_logging_session(
    level=logging.DEBUG, print_banner=False
)
paraccompiler.set_avoid_print_banner_overwrite(True)
main_file_path = f"{os.getcwd()}{sep}test_files{sep}entry.para"
test_c_files_dir = f"{os.getcwd()}{sep}test_files{sep}c_files{sep}"
test_para_files_dir = f"{os.getcwd()}{sep}test_files{sep}"


class TestParser:
    @staticmethod
    def teardown_method(_):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
        """
        reset_input()

    def test_entry_file_path(self):
        p = paraccompiler.BasicProcess(main_file_path, 'utf-8')
        asyncio.run(p.validate_syntax(True))

    def test_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            p = paraccompiler.BasicProcess(file.path, 'utf-8')
            asyncio.run(p.validate_syntax(True))

    def test_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files_dir):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            p = paraccompiler.BasicProcess(file.path, 'utf-8')
            asyncio.run(p.validate_syntax(True))
