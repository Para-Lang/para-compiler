# coding=utf-8
""" Test for the cli setup """
import subprocess
from string import printable
import paraccompiler
import os

from paraccompiler import __version__, __title__
from paraccompiler.para_exceptions import AbortError

from . import (github_run, add_folder, overwrite_input, reset_input,
               create_test_file)

sep = paraccompiler.SEPARATOR
main_file_path = f"{os.getcwd()}{sep}test_files{sep}entry.para"
paraccompiler.set_avoid_print_banner_overwrite(True)


class TestCLISetup:
    def teardown_method(self, method):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
        """
        reset_input()

    def test_build_exists_setup(self):
        add_folder("build")
        create_test_file("build", "example.txt")

        overwrite_input('True')
        paraccompiler.run_output_dir_validation(False, True)
        assert not os.path.exists("./build_2/example.txt")

        create_test_file("build", "example.txt")

        overwrite_input('False')
        paraccompiler.run_output_dir_validation(True, True)
        assert not os.path.exists("./build/example.txt")
        add_folder("build")

    def test_dist_exists_setup(self):
        add_folder("dist")
        create_test_file("dist", "example.txt")

        overwrite_input('True')
        paraccompiler.run_output_dir_validation(True, False)
        assert not os.path.exists("./dist_2/example.txt")

        create_test_file("dist", "example.txt")

        overwrite_input('False')
        paraccompiler.run_output_dir_validation(True, True)
        assert not os.path.exists("./dist/example.txt")
        add_folder("dist")

    def test_simple_setup(self):
        b_path = f"{os.getcwd()}\\build\\"
        d_path = f"{os.getcwd()}\\dist\\"
        p = paraccompiler.create_process(
            main_file_path, 'para.log', b_path, d_path
        )

        assert p.build_path == b_path
        assert p.dist_path == d_path

    def test_wrong_path(self):
        b_path = f"{os.getcwd()}\\build\\"
        d_path = f"{os.getcwd()}\\dist\\"
        try:
            paraccompiler.create_process(
                "not_existing.para", 'para.log', b_path, d_path
            )
        except AbortError:
            pass
        else:
            assert False
