# coding=utf-8
""" Configuration file for pytest """
import logging
import os
import sys
from pathlib import Path

import pytest

here = Path(str(os.path.abspath(__file__))).resolve().parent.parent
sys.path.insert(0, str(here))

import para

para.RUNTIME_COMPILER.init_logging_session(
    level=logging.DEBUG, print_banner=False
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
