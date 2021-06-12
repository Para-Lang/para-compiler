# coding=utf-8
""" Tests for the Tokenizer """
import os

import paraccompiler
from . import reset_input

sep = paraccompiler.SEPARATOR
main_file_path = f"{os.getcwd()}{sep}test_files{sep}main.para"
paraccompiler.set_avoid_print_banner_overwrite(True)


class TestParser:
    def teardown_method(self, method):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
         """
        reset_input()

    def test_read_file(self):
        tokeniser = paraccompiler.antlr.implem.Parser()
        r = tokeniser.antlr_parse(main_file_path, encoding="utf-8")