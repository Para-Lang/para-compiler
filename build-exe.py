# coding=utf-8
""" Script for building the compiler as an executable """
import PyInstaller.__main__
from distutils.dir_util import copy_tree
import pkg_resources
import shutil
import os

if not os.path.exists(".\\dist"):
    os.mkdir(".\\dist")
if not os.path.exists(".\\build"):
    os.mkdir(".\\build")

required = [
    'parac.ico',
    'parac.png',
    'LICENSE',
    'USAGE-README.md'
]

CURRENT_PATH: str = os.getcwd()
PBL_PATH: str = f"{CURRENT_PATH}\\parac-base-library"
CONFIG_EXAMPLE_PATH: str = f"{CURRENT_PATH}\\config-examples"
EXAMPLE_PATH: str = f"{CURRENT_PATH}\\examples"

path: str = pkg_resources.resource_filename(__name__, 'compiler.py')
icon_path: str = f"{CURRENT_PATH}\\parac.ico"

PyInstaller.__main__.run([
    path,
    '--log-level',
    'DEBUG',
    '--name',
    'parac',
    f'--icon={icon_path}'
])


def create_parac_modules(output_type: str):
    """ Creates the required parac modules for the compiler """
    out = f"{CURRENT_PATH}\\{output_type}\\parac"
    bin_path: str = f"{out}\\bin"
    lib_path: str = f"{out}\\lib"
    avoid = ["bin", "lib"]

    os.mkdir(bin_path)
    os.mkdir(lib_path)

    for entry in os.scandir(out):
        entry: os.DirEntry
        if not (entry.name in avoid and entry.is_dir()):
            shutil.move(entry.path, bin_path)

    for entry in os.scandir(PBL_PATH):
        entry: os.DirEntry
        if entry.is_dir():
            copy_tree(entry.path, f"{lib_path}\\{entry.name}\\")
        else:
            shutil.copy(entry.path, lib_path)

    for entry in required:
        shutil.copy(f"{CURRENT_PATH}\\{entry}", out)

    shutil.copy(f"{CURRENT_PATH}\\README.md", f"{out}\\GITHUB-README.md")
    copy_tree(CONFIG_EXAMPLE_PATH, f"{out}\\config-examples\\")
    copy_tree(EXAMPLE_PATH, f"{out}\\examples\\")


create_parac_modules("dist")
create_parac_modules("build")
