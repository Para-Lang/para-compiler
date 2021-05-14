""" Init file for the core tests """
import paraccompiler
import sys
import os
import shutil

github_run = '--github' in sys.argv
prev_input = paraccompiler.output_console.input


def overwrite_input(overwrite: str):
    """ Overwrites the input with a lambda that returns the specified value """
    paraccompiler.__main__.console.input = lambda *args, **kwargs: overwrite


def add_folder(folder_name: str):
    """ Removes any pre-existing data if it exists and adds the folder """
    cwd = os.getcwd()
    remove_folder(folder_name)
    os.mkdir(f"{cwd}/{folder_name}")


def remove_folder(folder_name: str):
    """ Removes the build and dist folder if they exist """
    cwd = os.getcwd()
    path = f"{cwd}/{folder_name}"
    if os.path.exists(path):
        shutil.rmtree(path)

    counter = 2
    while os.path.exists(path := f"{cwd}/{folder_name}_{counter}"):
        shutil.rmtree(path)
        counter += 1


def create_test_file(folder_name: str, file_name: str):
    """ Creates a test file in the specified path with the specified name """
    cwd = os.getcwd()
    with open(f'{cwd}/{folder_name}/{file_name}', 'w+') as file:
        file.write("x")
    assert os.path.exists(f"{cwd}/{folder_name}/{file_name}")
