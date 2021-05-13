""" Test for the core setup """
import shutil
import subprocess
from string import printable
import paraccompiler
import os
from paraccompiler import __version__, __title__
import pkg_resources

main_file_path = pkg_resources.resource_filename(__name__, 'main.para')
_prev_input = paraccompiler.output_console.input


class TestSetup:
    def teardown_method(self, method):
        """ This method is being called after each test case, and it will revert input back to the original function """
        paraccompiler.output_console.input = _prev_input

    def test_version(self, ):
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

    @staticmethod
    def _overwrite_input(overwrite: str):
        paraccompiler.__main__.console.input = lambda *args, **kwargs: overwrite

    @staticmethod
    def _remove_folders(folder_name: str):
        cwd = os.getcwd()
        path = f"{cwd}/{folder_name}"
        if os.path.exists(path):
            shutil.rmtree(path)

        counter = 2
        while os.path.exists(path := f"{cwd}/{folder_name}_{counter}"):
            shutil.rmtree(path)
            counter += 1

        os.mkdir(f"{cwd}/{folder_name}")

    @staticmethod
    def _create_test_folder(folder_name: str):
        cwd = os.getcwd()
        with open(f'{cwd}/{folder_name}/example.txt', 'w+') as file:
            file.write("x")
        assert os.path.exists(f"{cwd}/{folder_name}/example.txt")

    def test_build_exists_setup(self):
        self._remove_folders("build")
        self._create_test_folder("build")

        self._overwrite_input('True')
        paraccompiler.run_output_dir_validation(False, True)
        assert not os.path.exists("./build_2/example.txt")

        self._create_test_folder("build")

        self._overwrite_input('False')
        paraccompiler.run_output_dir_validation(True, True)
        assert not os.path.exists("./build/example.txt")
        self._remove_folders("build")

    def test_dist_exists_setup(self):
        self._remove_folders("dist")
        self._create_test_folder("dist")

        self._overwrite_input('True')
        paraccompiler.run_output_dir_validation(True, False)
        assert not os.path.exists("./dist_2/example.txt")

        self._create_test_folder("dist")

        self._overwrite_input('False')
        paraccompiler.run_output_dir_validation(True, True)
        assert not os.path.exists("./dist/example.txt")
        self._remove_folders("dist")
