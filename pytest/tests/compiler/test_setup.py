# coding=utf-8
""" Test for the cli setup """
import paraccompiler
import os

from paraccompiler.para_exceptions import InterruptError, InternalError

from . import (add_folder, overwrite_input, reset_input,
               create_test_file)

sep = paraccompiler.SEPARATOR
main_file_path = f"{os.getcwd()}{sep}test_files{sep}entry.para"
paraccompiler.set_avoid_print_banner_overwrite(True)


class TestCLISetup:
    @staticmethod
    def teardown_method(_):
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
        b_path = add_folder("build")
        d_path = add_folder("dist")
        p = paraccompiler.create_process(
            main_file_path, 'utf-8', 'para.log', b_path, d_path
        )

        assert p.build_path == b_path
        assert p.dist_path == d_path

    def test_wrong_path(self):
        b_path = add_folder("build")
        d_path = add_folder("dist")
        try:
            paraccompiler.create_process(
                "not_existing.para", 'utf-8', 'para.log', b_path, d_path
            )
        except InternalError:
            pass
        else:
            assert False
