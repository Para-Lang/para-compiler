""" Test for the core setup """
import paraccompiler
import os


compiler = paraccompiler.ParacCompiler()


def test_setup():
    compiler.validate_setup("main.para", "para.log", True, True)
    assert os.path.exists("./para.log")
