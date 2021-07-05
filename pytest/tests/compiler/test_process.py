# coding=utf-8
""" Test for the compiler process setup """
import os
import paraccompiler

from . import reset_input
from .. import add_folder

sep = paraccompiler.SEPARATOR
main_file_path = f"{os.getcwd()}{sep}test_files{sep}entry.para"
paraccompiler.set_avoid_print_banner_overwrite(True)


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
        p = paraccompiler.ProgramCompilationProcess(
            main_file_path, 'utf-8', b_path, d_path
        )

        assert p.build_path == b_path
        assert p.dist_path == d_path

    def test_bytes_init(self):
        path = main_file_path.encode()

        b_path = add_folder("build").encode()
        d_path = add_folder("dist").encode()
        p = paraccompiler.ProgramCompilationProcess(
            path, 'utf-8', b_path, d_path
        )

        assert p.build_path == b_path.decode()
        assert p.dist_path == d_path.decode()
