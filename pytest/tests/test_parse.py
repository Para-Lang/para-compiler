# coding=utf-8
""" Tests for the Tokenizer """
import logging
import os
from typing import List

import paraccompiler
from paraccompiler import CompilationContext
from . import reset_input


logger = logging.getLogger('paraccompiler')

sep = paraccompiler.SEPARATOR
main_file_path = f"{os.getcwd()}{sep}test_files{sep}entry.para"
test_c_files = f"{os.getcwd()}{sep}test_files{sep}c_files{sep}"
paraccompiler.set_avoid_print_banner_overwrite(True)
compiler = paraccompiler.ParacCompiler()


class TestParser:
    def teardown_method(self, method):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
         """
        reset_input()

    def test_read_file(self):
        logger.debug(f"\nParsing {main_file_path}")
        ctx = CompilationContext()
        r = compiler.antlr_parse_and_compile(ctx, main_file_path)

    def test_c_files(self):
        files: List[os.DirEntry] = []

        for entry in os.scandir(test_c_files):
            entry: os.DirEntry
            if entry.path.endswith(".c"):
                files.append(entry)

        for file in files:
            logger.debug(f"Parsing {file.path}")
            ctx = CompilationContext()
            compiler.antlr_parse_and_compile(ctx, file.path)
