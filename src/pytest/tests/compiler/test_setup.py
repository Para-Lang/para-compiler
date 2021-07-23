# coding=utf-8
""" Test for the cli setup """
import pytest

import os

from parac import (FileNotFoundError as ParaFileNotFoundError,
                   SEPARATOR as SEP, UserInputError)
from parac.logging import set_avoid_print_banner_overwrite
from parac.compiler import ParacCompiler
from parac_cli import cli_run_output_dir_validation, cli_create_process

from .. import (add_folder, overwrite_builtin_input, reset_input,
                create_test_file)

LOG_PATH = 'para.log'
ENCODING = 'utf-8'
main_file_path = f"{os.getcwd()}{SEP}test_files{SEP}entry.para"
set_avoid_print_banner_overwrite(True)


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

        overwrite_builtin_input('True')
        cli_run_output_dir_validation(False, True)
        assert not os.path.exists("./build_2/example.txt")
        assert os.path.exists("./build/example.txt")

        create_test_file("build", "example.txt")

        overwrite_builtin_input('False')
        cli_run_output_dir_validation(True, True)
        assert not os.path.exists("./build/example.txt")
        add_folder("build")

    def test_dist_exists_setup(self):
        add_folder("dist")
        create_test_file("dist", "example.txt")

        overwrite_builtin_input('True')  # Overwrite data -> True
        cli_run_output_dir_validation(True, False)
        assert not os.path.exists("./dist_2/example.txt")
        assert os.path.exists("./dist/example.txt")

        create_test_file("dist", "example.txt")
        overwrite_builtin_input('False')  # Overwrite data -> False
        cli_run_output_dir_validation(True, True)
        assert not os.path.exists("./dist/example.txt")
        add_folder("dist")

    def test_simple_setup_compilation_process(self):
        b_path = add_folder("build")
        d_path = add_folder("dist")

        p = cli_create_process(
            main_file_path, ENCODING, LOG_PATH, b_path, d_path
        )

        assert p.build_path == b_path
        assert p.dist_path == d_path

    @pytest.mark.parametrize(
        "path", [
            "not_existing.para", "not_existing"
        ]
    )
    def test_wrong_path_compilation_process_1(self, path: str):
        b_path = add_folder("build")
        d_path = add_folder("dist")
        try:
            p = cli_create_process(
                file=path,
                encoding=ENCODING,
                log_path=LOG_PATH,
                build_path=b_path,
                dist_path=d_path
            )
            assert False
        except ParaFileNotFoundError as e:
            ...

    @pytest.mark.parametrize(
        "path", [
            "", "", "ddf $  &/`='|.*"
        ]
    )
    def test_wrong_path_compilation_process_2(self, path: str):
        b_path = add_folder("build")
        d_path = add_folder("dist")
        try:
            p = cli_create_process(
                file=path,
                encoding=ENCODING,
                log_path=LOG_PATH,
                build_path=b_path,
                dist_path=d_path
            )
            assert False
        except UserInputError:
            ...

    @pytest.mark.parametrize(
        "expected,input_str,line_ending", [
            ("x y z", "x y z", "\n"),
            ("x y z", "x y z", "\r\n"),
            ("x \ny z", "x // some \ny z", "\n"),
            ("x \r\ny z", "x // some \ny z", "\r\n"),
            ("\nx \ny \nz", "/* xx  */x // some \ny // x x x \r\nz", "\n"),
            ("\rx \ry \rz", "/* xx  */x // some \ny // x x x \r\nz", "\r"),
            ("x \n\n\ny z", "x // x \r// x \n// x \r\ny z", "\n"),
            ("x \r\r\ry z", "x // x \r// x \n// x \r\ny z", "\r"),
            ("x \n\n\n\ny \nz", "x // x \r\n\n// x \n// x \r\ny \nz", "\n"),
            ("x \r\r\r\ry \rz", "x // x \r\n\n// x \n// x \r\ny \nz", "\r"),
        ]
    )
    def test_remove_comments_from_str(
            self, expected: str, input_str: str, line_ending: str
    ):
        assert expected == ParacCompiler.remove_comments_from_str(
            input_str, line_ending
        )
