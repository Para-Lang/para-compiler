""" Test for the cli setup """
import logging
import subprocess
from string import printable
import paraccompiler
import os
from paraccompiler import __version__, __title__

from . import github_run, prev_input, add_folder, overwrite_input, create_test_file

main_file_path = f"{os.getcwd()}\\test_files\\main.para"


class TestCLISetup:
    def teardown_method(self, method):
        """ This method is being called after each test case, and it will revert input back to the original function """
        paraccompiler.output_console.input = prev_input

    def test_version(self):
        if github_run:
            return

        output = subprocess.run(
            ["python", f"{os.getcwd()}\\..\\compiler.py", "--version"],
            shell=True,
            capture_output=True
        )

        def _decode(stdout):
            stdout = ''.join(
                char for char in str(stdout.decode()) if char in printable
            )

            return stdout.replace('[0m', '').replace('\r', '').replace('\n', '')

        assert _decode(output.stdout) == ' '.join([__title__.title(), __version__])

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
        p = paraccompiler.create_process(main_file_path, 'para.log', b_path, d_path, logging.DEBUG)

        assert p.entry_file == main_file_path
        assert p.build_path == b_path
        assert p.dist_path == d_path
