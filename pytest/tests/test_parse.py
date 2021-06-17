# coding=utf-8
""" Tests for the Tokenizer """
import logging
import os
from typing import List

import paraccompiler
from . import reset_input


logger = logging.getLogger('paraccompiler')

paraccompiler.set_avoid_print_banner_overwrite(True)
compiler = paraccompiler.ParacCompiler()

sep = paraccompiler.SEPARATOR
main_file_path = f"{os.getcwd()}{sep}test_files{sep}entry.para"
test_c_files = f"{os.getcwd()}{sep}test_files{sep}c_files{sep}"
test_para_files = f"{os.getcwd()}{sep}test_files{sep}"


class TestParser:
    def teardown_method(self, method):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
         """
        reset_input()

    def test_entry_file(self):
        logger.debug(f"\nParsing {main_file_path}")

        stream = compiler.get_file_stream(main_file_path, "ascii")
        compiler.parse(stream)

    def test_para_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_para_files):
            entry: os.DirEntry
            if entry.path.endswith(".para") or entry.path.endswith(".parah"):
                files.append(entry)

        for file in files:
            logger.debug(f"Parsing {file.path}")
            stream = compiler.get_file_stream(file.path, "ascii")
            compiler.parse(stream)

    def test_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files):
            entry: os.DirEntry
            if entry.path.endswith(".c") or entry.path.endswith(".h"):
                files.append(entry)

        for file in files:
            logger.debug(f"Parsing {file.path}")
            stream = compiler.get_file_stream(file.path, "ascii")
            compiler.parse(stream)
