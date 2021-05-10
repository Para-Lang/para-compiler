""" Test for the core setup """
import paraccompiler
import os
import pkg_resources


compiler = paraccompiler.ParacCompiler()
path = pkg_resources.resource_filename(__name__, 'main.para')


class TestSetup:
    def teardown_method(self, method):
        """ This method is being called after each test case, and it will revert input back to the original function """
        paraccompiler.__main__.input = input

    def test_setup(self,):
        compiler.validate_setup(path, "para.log", True, True)
        assert os.path.exists("./para.log")

    @staticmethod
    def _overwrite_input(overwrite: str):
        paraccompiler.__main__.input = lambda *args, **kwargs: overwrite

    def test_build_exists_setup(self):
        if os.path.exists("./build"):
            paraccompiler.shutil.rmtree("./build")
        os.mkdir("./build")

        with open('./build/example.txt', 'w+') as file:
            file.write("x")
        assert os.path.exists("./build/example.txt")

        self._overwrite_input('True')
        compiler.validate_setup(path, "para.log", False, True)
        assert not os.path.exists("./build/example.txt")

        with open('./build/example.txt', 'w+') as file:
            file.write("x")
        assert os.path.exists("./build/example.txt")

        self._overwrite_input('False')
        compiler.validate_setup(path, "para.log", True, True)
        assert not os.path.exists("./build/example.txt")

    def test_dist_exists_setup(self):
        if os.path.exists("./dist"):
            paraccompiler.shutil.rmtree("./dist")
        os.mkdir("./dist")

        with open('./dist/example.txt', 'w+') as file:
            file.write("x")
        assert os.path.exists("./dist/example.txt")

        self._overwrite_input('True')
        compiler.validate_setup(path, "para.log", True, False)
        assert not os.path.exists("./dist/example.txt")

        with open('./dist/example.txt', 'w+') as file:
            file.write("x")
        assert os.path.exists("./dist/example.txt")

        self._overwrite_input('False')
        compiler.validate_setup(path, "para.log", True, True)
        assert not os.path.exists("./dist/example.txt")
