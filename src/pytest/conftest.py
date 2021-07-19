# coding=utf-8
""" Configuration file for pytest """
import shutil
import sys
import pytest
import logging
import os

# Installing new version of the package
os.system("pip install --upgrade -e ..")
logging.basicConfig(level=logging.DEBUG)
shutil.rmtree("../parac.egg-info")

import parac
assert parac


def pytest_addoption(parser):
    """ Adds the --github command line option"""
    parser.addoption(
        "--github", action="store", default="", help="Signalises it's run by github actions"
    )


@pytest.fixture(autouse=True)
def capture_wrap():
    """
    Workaround for pytest, where after finishing the testing
    (ValueError: I/O operation on closed file.) is raised since
    the integrated logging module interferes with it

    REF:
    https://github.com/pytest-dev/pytest/issues/5502#issuecomment-678368525
    """
    sys.stderr.close = lambda *args: None
    sys.stdout.close = lambda *args: None
    yield


@pytest.fixture(autouse=True)
def cleanup(request):
    """ Cleanup for the tests """
    from tests import remove_folder
    remove_folder("build")
    remove_folder("dist")
