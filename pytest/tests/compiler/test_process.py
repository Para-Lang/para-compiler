# coding=utf-8
""" Test for the compiler process setup """
from pathlib import Path

from parac import initialise_default_paths
from parac.compiler import ProgramCompilationProcess
from parac.logging import set_avoid_print_banner_overwrite
from .. import add_folder, reset_input, BASE_TEST_PATH

main_file_path: Path = Path(BASE_TEST_PATH) / "test_files" / "entry.para"

# Avoiding printing the banner (CLI)
set_avoid_print_banner_overwrite(True)

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestProcess:
    @staticmethod
    def teardown_method(_):
        """
        This method is being called after each test case, and it will revert
        input back to the original function
         """
        reset_input()

    def test_init(self):
        b_path: Path = add_folder("build")
        d_path: Path = add_folder("dist")
        p = ProgramCompilationProcess(
            main_file_path, 'utf-8', b_path, d_path
        )

        assert p.build_path == b_path
        assert p.dist_path == d_path

    def test_bytes_init(self):
        path = str(main_file_path).encode()

        b_path: bytes = str(add_folder("build")).encode()
        d_path: bytes = str(add_folder("dist")).encode()
        p: ProgramCompilationProcess = ProgramCompilationProcess(
            path, 'utf-8', b_path, d_path
        )

        assert p.build_path == Path(b_path.decode())
        assert p.dist_path == Path(d_path.decode())
