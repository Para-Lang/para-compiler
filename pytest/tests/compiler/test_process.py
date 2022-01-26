# coding=utf-8
""" Test for the compiler process setup """
from pathlib import Path

from paralang_base import initialise_default_paths
from paralang_base.compiler import CompileProcess

from .. import BASE_TEST_PATH


main_file_path: Path = Path(BASE_TEST_PATH) / "test_files" / "main.para"

# Initialises the default paths for the compiler using the work directory
initialise_default_paths(BASE_TEST_PATH)


class TestProcess:
    def test_init(self):
        p = CompileProcess(
            [main_file_path], main_file_path.parent, 'utf-8'
        )
        assert p.project_root == main_file_path.parent
        assert len(p.files) == 1
        assert p.encoding == 'utf-8'

    def test_bytes_init(self):
        p: CompileProcess = CompileProcess(
            [str(main_file_path).encode()], main_file_path.parent, 'utf-8'
        )

        assert p.project_root == main_file_path.parent
        assert len(p.files) == 1
        assert p.encoding == 'utf-8'
