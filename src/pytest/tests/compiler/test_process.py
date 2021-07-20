# coding=utf-8
""" Test for the compiler process setup """
import os

from parac.compiler import (ProgramCompilationProcess, SEPARATOR as SEP,
                            set_avoid_print_banner_overwrite)
from . import reset_input
from .. import add_folder

main_file_path = f"{os.getcwd()}{SEP}test_files{SEP}entry.para"
set_avoid_print_banner_overwrite(True)


class TestProcess:
    @staticmethod
    def teardown_method(_):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
         """
        reset_input()

    def test_init(self):
        b_path = add_folder("build")
        d_path = add_folder("dist")
        p = ProgramCompilationProcess(
            main_file_path, 'utf-8', b_path, d_path
        )

        assert p.build_path == b_path
        assert p.dist_path == d_path

    def test_bytes_init(self):
        path = main_file_path.encode()

        b_path = add_folder("build").encode()
        d_path = add_folder("dist").encode()
        p = ProgramCompilationProcess(
            path, 'utf-8', b_path, d_path
        )

        assert p.build_path == b_path.decode()
        assert p.dist_path == d_path.decode()
