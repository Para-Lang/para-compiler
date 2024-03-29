# coding=utf-8
""" Init file for the core tests """
import logging
import os
import shutil
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('paralang_base')
logger.setLevel(logging.DEBUG)


def resolve_test_path() -> Path:
    """
    Resolves the test path and tries to find the directory that contains the
    test files
    """
    p: Path = Path(os.getcwd()).resolve()
    if p.name == "pytest":
        return p
    elif os.path.exists(_ := p.joinpath("pytest")):
        p = _
    elif os.path.exists(_ := p.parent.joinpath("pytest")):
        p = _
    elif "pytest" in str(p):
        # detecting the path by going back each item until reaching the pytest
        # folder
        while p.parts[-1] != "pytest":
            p = (p / "..").resolve()
    else:
        raise RuntimeError("Failed to resolve test path")

    return Path(str(p)).resolve()


BASE_TEST_PATH = resolve_test_path()


def add_folder(folder_name: str) -> Path:
    """
    Removes any pre-existing data if it exists and adds the folder

    :returns: The path of the folder
    """
    remove_folder(folder_name)
    os.mkdir(p := BASE_TEST_PATH / folder_name)
    return Path(str(p)).resolve()


def remove_folder(folder_name: str) -> None:
    """ Removes the build and dist folder if they exist """
    path: Path = BASE_TEST_PATH / folder_name
    if os.path.exists(path):
        shutil.rmtree(str(path.resolve()))

    counter = 2
    while os.path.exists(path := BASE_TEST_PATH / f"{folder_name}_{counter}"):
        shutil.rmtree(str(path.resolve()))
        counter += 1


def create_test_file(folder_name: str, file_name: str) -> None:
    """ Creates a test file in the specified path with the specified name """
    with open(BASE_TEST_PATH / folder_name / file_name, 'w+') as file:
        file.write("x")
    assert os.path.exists(BASE_TEST_PATH / folder_name / file_name)
