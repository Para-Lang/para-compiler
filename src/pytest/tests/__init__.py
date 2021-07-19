# coding=utf-8
""" Init file for the core tests """
import os
import shutil
import sys

sys.path.append(os.getcwd())

import parac
from parac.compiler import SEPARATOR

github_run = '--github=true' in sys.argv

parac.compiler.init_rich_console()
prev_input = parac.compiler.get_rich_console().input
parac.compiler.set_avoid_print_banner_overwrite(True)


def overwrite_builtin_input(overwrite: str):
    """ Overwrites the input with a lambda that returns the specified value """
    getattr(parac.compiler.logging, 'output_console').input =\
        lambda *args, **kwargs: overwrite


def reset_input():
    """ Resets the output method of the console object """
    getattr(parac.compiler.logging, 'output_console').input = prev_input


def add_folder(folder_name: str) -> str:
    """
    Removes any pre-existing data if it exists and adds the folder

    :returns: The path of the folder
    """
    cwd = os.getcwd()
    remove_folder(folder_name)

    p = f"{cwd}{SEPARATOR}{folder_name}"
    os.mkdir(p)
    return p


def remove_folder(folder_name: str):
    """ Removes the build and dist folder if they exist """
    cwd = os.getcwd()
    path = f"{cwd}{SEPARATOR}{folder_name}"
    if os.path.exists(path):
        shutil.rmtree(path)

    counter = 2
    while os.path.exists(path := f"{cwd}{SEPARATOR}{folder_name}_{counter}"):
        shutil.rmtree(path)
        counter += 1


def create_test_file(folder_name: str, file_name: str):
    """ Creates a test file in the specified path with the specified name """
    cwd = os.getcwd()
    with open(f'{cwd}/{folder_name}/{file_name}', 'w+') as file:
        file.write("x")
    assert os.path.exists(f"{cwd}/{folder_name}/{file_name}")
