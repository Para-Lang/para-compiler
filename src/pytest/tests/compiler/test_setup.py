# coding=utf-8
""" Test for the cli setup """
import pytest

import os

from parac.compiler import (ParacCompiler, create_process,
                            FileNotFoundError as ParaFileNotFoundError,
                            set_avoid_print_banner_overwrite, SEPARATOR as SEP,
                            run_output_dir_validation)

from . import (add_folder, overwrite_builtin_input, reset_input,
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
        run_output_dir_validation(False, True)
        assert not os.path.exists("./build_2/example.txt")
        assert os.path.exists("./build/example.txt")

        create_test_file("build", "example.txt")

        overwrite_builtin_input('False')
        run_output_dir_validation(True, True)
        assert not os.path.exists("./build/example.txt")
        add_folder("build")

    def test_dist_exists_setup(self):
        add_folder("dist")
        create_test_file("dist", "example.txt")

        overwrite_builtin_input('True')  # Overwrite data -> True
        run_output_dir_validation(True, False)
        assert not os.path.exists("./dist_2/example.txt")
        assert os.path.exists("./dist/example.txt")

        create_test_file("dist", "example.txt")
        overwrite_builtin_input('False')  # Overwrite data -> False
        run_output_dir_validation(True, True)
        assert not os.path.exists("./dist/example.txt")
        add_folder("dist")

    def test_simple_setup_compilation_process(self):
        b_path = add_folder("build")
        d_path = add_folder("dist")

        p = create_process(
            main_file_path, ENCODING, LOG_PATH, b_path, d_path
        )

        assert p.build_path == b_path
        assert p.dist_path == d_path

    @pytest.mark.parametrize(
        "path", [
            "not_existing.para", "not_existing", " ", ""
        ]
    )
    def test_wrong_path_compilation_process(self, path: str):
        b_path = add_folder("build")
        d_path = add_folder("dist")
        try:
            create_process(
                path, ENCODING, LOG_PATH, b_path, d_path
            )
        except ParaFileNotFoundError as e:
            ...
        else:
            assert False

    @pytest.mark.parametrize(
        "expected,input_str,line_ending", [
            ("x y z", "x y z", "\n"),
            ("x y z", "x y z", "\r\n"),
            ("x y z", "x // something \ny z", "\n"),
            ("x y z", "x // something \ny z", "\r\n"),
            ("x y z", "/* xx  */x // something \ny // x x x \r\nz", "\n"),
            ("x y z", "/* xx  */x // something \ny // x x x \r\nz", "\r"),
            ("x y z", "x // x \r// x \n// x \r\ny z", "\n"),
            ("x y z", "x // x \r// x \n// x \r\ny z", "\r"),
            ("x \ny \nz", "x // x \r\n\n// x \n// x \r\ny \nz", "\n"),
            ("x \r\ny \r\nz", "x // x \r\n\n// x \n// x \r\ny \nz", "\r\n"),
        ]
    )
    def test_remove_comments_from_str(
            self, expected: str, input_str: str, line_ending: str
    ):
        assert expected == ParacCompiler.remove_comments_from_str(
            input_str, line_ending
        )
