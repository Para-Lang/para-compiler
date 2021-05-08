import logging
import sys

import pytest

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(autouse=True)
def capture_wrap():
    """
    Workaround for pytest, where after finishing the testing (ValueError: I/O operation on closed file.) is raised since
    the integrated logging module interferes with it

    REF: https://github.com/pytest-dev/pytest/issues/5502#issuecomment-678368525
    """
    sys.stderr.close = lambda *args: None
    sys.stdout.close = lambda *args: None
    yield


@pytest.fixture(scope="module", autouse=True)
def logging_init():
    logging.basicConfig(level=logging.DEBUG)
