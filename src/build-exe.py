# coding=utf-8
""" Script for building the compiler as an executable """
from pathlib import Path
from typing import List

import PyInstaller.__main__
from distutils.dir_util import copy_tree
import pkg_resources
import shutil
import os


BASE_PATH: Path = Path(__file__).parent.parent.resolve()
DIST_PATH: Path = BASE_PATH / "dist"
BUILD_PATH: Path = BASE_PATH / "build"
PBL_PATH: Path = BASE_PATH / "lib"
EXAMPLE_PATH: Path = BASE_PATH / "examples"

# get entry path for the compiler
entry_path: Path = pkg_resources.resource_filename(__name__, "cli.py")
icon_path: Path = BASE_PATH / "img" / "parac.ico"

required: List[Path] = [
    BASE_PATH / "img" / "parac.ico",
    BASE_PATH / "img" / "parac-banner.png",
    BASE_PATH / "img" / "parac.png",
    BASE_PATH / "CHANGELOG.md",
    BASE_PATH / "LICENSE",
    BASE_PATH / "USAGE-README.md"
]

with open(
        BASE_PATH / "src" / "INSTALL_AVOID_MODULES.txt", "r", encoding='utf-8'
) as file:
    AVOID_MODULES: List[str] = list(
        i.removesuffix('\n') for i in file.readlines()
    )
    _ = []
    for i in AVOID_MODULES:
        _.append("--exclude-module")
        _.append(i)
    AVOID_MODULES = _

for i in (DIST_PATH, BUILD_PATH):
    if not os.path.exists(str(i.resolve())):
        os.makedirs(str(i.resolve()), exist_ok=True)

run_config = [
    entry_path,
    "--log-level",
    "DEBUG",
    "--name",
    "parac",
    "--icon",
    str(icon_path.resolve()),
    *AVOID_MODULES,
]
PyInstaller.__main__.run(run_config)


def create_parac_modules(output_type: str):
    """ Creates the required parac modules for the compiler """
    origin = BASE_PATH / "src" / output_type / "parac"
    destination = BASE_PATH / output_type / "parac"
    bin_path: Path = destination / "bin"
    lib_path: Path = destination / "lib"
    avoid = ["bin", "lib"]

    os.makedirs(str(bin_path.resolve()), exist_ok=True)
    os.makedirs(str(lib_path.resolve()), exist_ok=True)

    for entry in os.scandir(origin):
        entry: os.DirEntry
        # Avoid directories that are in avoid
        if not (entry.name in avoid and entry.is_dir()):
            shutil.move(entry.path, bin_path)

    for entry in os.scandir(PBL_PATH):
        entry: os.DirEntry
        if entry.is_dir():
            copy_tree(entry.path, str((lib_path / entry.name).resolve()))
        else:
            shutil.copy(entry.path, lib_path)

    for entry in required:
        entry: Path
        shutil.copy(str(entry.resolve()), destination)

    shutil.copy(
        BASE_PATH / "README.md", destination / "PROJECT-DESCRIPTION.md"
    )
    copy_tree(
        str(EXAMPLE_PATH.resolve()),
        str((destination / "examples").resolve())
    )

    shutil.rmtree(str((BASE_PATH / "src" / output_type).resolve()))


create_parac_modules("dist")
create_parac_modules("build")
