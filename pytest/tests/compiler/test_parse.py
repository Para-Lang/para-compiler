# coding=utf-8
""" Tests for the Lexer and Parser """
import logging
import os
from typing import List

import paraccompiler
from paraccompiler import BasicProcess
from . import reset_input


logger = logging.getLogger('paraccompiler')

paraccompiler.para_compiler.init_logging_session(
    level=logging.DEBUG, print_banner=False
)
paraccompiler.set_avoid_print_banner_overwrite(True)
compiler = paraccompiler.ParacCompiler()

sep = paraccompiler.SEPARATOR
main_file_path = f"{os.getcwd()}{sep}test_files{sep}entry.para"
test_c_files = f"{os.getcwd()}{sep}test_files{sep}c_files{sep}"
test_para_files = f"{os.getcwd()}{sep}test_files{sep}"


class TestParser:
    @staticmethod
    def teardown_method(_):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
         """
        reset_input()

    def test_entry_file_path(self):
        logger.debug(f"\nParsing {main_file_path}")

        p = BasicProcess(main_file_path, 'utf-8')
        p.validate_syntax(True)

    def test_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            logger.debug(f"Parsing {file.path}")
            BasicProcess(file.path, 'utf-8').validate_syntax(True)

    def test_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            logger.debug(f"Parsing {file.path}")
            BasicProcess(file.path, 'utf-8').validate_syntax(True)
