# coding=utf-8
""" Script for building the compiler as an executable """
import PyInstaller.__main__
from distutils.dir_util import copy_tree
import pkg_resources
import shutil
import os

from paraccompiler import SEPARATOR

if not os.path.exists(f".{SEPARATOR}dist"):
    os.mkdir(f".{SEPARATOR}dist")
if not os.path.exists(f".{SEPARATOR}build"):
    os.mkdir(f".{SEPARATOR}build")

required = [
    'parac.ico',
    'parac.png',
    'LICENSE',
    'USAGE-README.md'
]

CURRENT_PATH: str = os.getcwd()
PBL_PATH: str = f"{CURRENT_PATH}{SEPARATOR}parac-base-library"
CONFIG_EXAMPLE_PATH: str = f"{CURRENT_PATH}{SEPARATOR}config-examples"
EXAMPLE_PATH: str = f"{CURRENT_PATH}{SEPARATOR}examples"

path: str = pkg_resources.resource_filename(__name__, 'compiler-cli.py')
icon_path: str = f"{CURRENT_PATH}{SEPARATOR}parac.ico"

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
    out = f"{CURRENT_PATH}{SEPARATOR}{output_type}{SEPARATOR}parac"
    bin_path: str = f"{out}{SEPARATOR}bin"
    lib_path: str = f"{out}{SEPARATOR}lib"
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
            copy_tree(entry.path, f"{lib_path}{SEPARATOR}{entry.name}{SEPARATOR}")
        else:
            shutil.copy(entry.path, lib_path)

    for entry in required:
        shutil.copy(f"{CURRENT_PATH}{SEPARATOR}{entry}", out)

    shutil.copy(f"{CURRENT_PATH}{SEPARATOR}README.md", f"{out}{SEPARATOR}GITHUB-README.md")
    copy_tree(CONFIG_EXAMPLE_PATH, f"{out}{SEPARATOR}config-examples{SEPARATOR}")
    copy_tree(EXAMPLE_PATH, f"{out}{SEPARATOR}examples{SEPARATOR}")


create_parac_modules("dist")
create_parac_modules("build")
