# coding=utf-8
""" Script for building the compiler as an executable """
import json
import platform
import re
import sys
import time
from pathlib import Path
from typing import List, Dict, Optional, Union, NoReturn, Tuple
import PyInstaller.__main__
from distutils.dir_util import copy_tree
import shutil
import os
import requests

# File constant
COMPATIBLE_VERSION: str = "v0.1.dev6"

# Input regex
IN_REGEX: str = "(--[A-z0-9]+=[A-z0-9]+)"

# Run Constants
BASE_PATH: Path = Path(os.getcwd())
DIST_PATH: Path = BASE_PATH / "dist"
BUILD_PATH: Path = BASE_PATH / "build"
ENTRY_PATH: Path = BASE_PATH / "dummy-entry.py"
EXAMPLE_PATH: Path = BASE_PATH / "examples"
ICON_PATH: Path = BASE_PATH / "img" / "parac.ico"
C_COMPILER = "gcc"
C_LIB_IDENTIFIER = "libpbl.a"
LIBPBL = f"https://github.com/Para-C/Para-C-Base-Library/releases/download/{COMPATIBLE_VERSION}/{C_LIB_IDENTIFIER}"
C_LIB_TEMP_DESTINATION = BASE_PATH / "tmp" / C_LIB_IDENTIFIER
TARGET: str = platform.system()
IS_64_BIT: bool = sys.maxsize > 2**32

# Configuration Defaults
ACTION: str = "normal"

# Possible Configuration
POSSIBLE_ACTION_CONF: Tuple[str, str, str] = (
    "normal", "pbl", "compiler-standalone"
)

# Etc.
ACTIONS_THAT_REQUIRE_PBL: Tuple[str, str] = (
    "normal", "pbl"
)

# Run Configuration - default values are passed onto the dictionary
CONFIG: Dict[str, Optional[str]] = {
    "ACTION": ACTION,
    "TARGET": TARGET,
    "LIBPBL": LIBPBL
}

# Required additional data files that have to be added
COPY_FILES: List[Path] = [
    BASE_PATH / "img" / "parac.ico",
    BASE_PATH / "img" / "parac-banner.png",
    BASE_PATH / "img" / "parac.png",
    BASE_PATH / "CHANGELOG.md",
    BASE_PATH / "LICENSE",
    BASE_PATH / "README.md"
]

# Avoid modules that PyInstaller is detecting, even though they are unused
AVOID_MODULES: List[str] = [
    "jedi",
    "IPython",
    "numpy",
    "matplotlib"
]

# Hidden imports that PyInstaller is unable to detect, meaning we have to
# specify it directly as an argument
HIDDEN_IMPORT = ["parac_ext_cli", "parac"]


def create_bin_config(dest_dir: Path) -> None:
    """
    Creates the binaries config file - Uses empty-bin-config.json as reference
    """
    conf = {
        "c-compiler": C_COMPILER,
        "target": CONFIG["TARGET"],
        "mode": CONFIG["ACTION"],
        "version": COMPATIBLE_VERSION,
        "build-time": time.time()  # unix timestamp
    }
    with open(dest_dir / "bin-config.json", "w+") as f:
        f.write(json.dumps(conf, indent=4))


def parse_avoid_and_hidden_imports() -> None:
    """ Correctly parsing and modifying the avoid modules and hidden imports"""
    _ = []
    global AVOID_MODULES
    for module in AVOID_MODULES:
        _.append("--exclude-module")
        _.append(module)
    AVOID_MODULES = _

    _ = []
    global HIDDEN_IMPORT
    for module in HIDDEN_IMPORT:
        _.append("--hiddenimport")
        _.append(module)
    HIDDEN_IMPORT = _


def validate_action() -> Union[None, NoReturn]:
    """ Validates whether the action is valid """
    if CONFIG["ACTION"] not in POSSIBLE_ACTION_CONF:
        raise ValueError(
            f"Invalid argument 'ACTION' with value '{CONFIG['ACTION']}'"
        )
    return


def parse_input() -> None:
    """ Parses the input and updates the global constants """
    args = sys.argv[1:]

    if not all(map(lambda n: bool(re.findall(IN_REGEX, n)), args)):
        raise ValueError("Invalid input! Check Syntax: '--ARG=VALUE'")

    for in_arg in args:
        in_arg: str = in_arg[2:]
        name, value = tuple(in_arg.split('='))
        if name not in CONFIG.keys():
            raise ValueError("Invalid argument name!")

        CONFIG[name] = value

    validate_action()


def cleanup_and_create_tmp_folder() -> None:
    """
    Creates the temp folder for this run

    Deletes the previous one if it exists
    """
    if os.path.exists(tmp := BASE_PATH / "tmp"):
        shutil.rmtree(tmp)
    os.mkdir(tmp)


def cleanup_and_remove_tmp_folder() -> None:
    """ Removes the tmp folder if found """
    if os.path.exists(tmp := BASE_PATH / "tmp"):
        shutil.rmtree(tmp)


def fetch_pbl_build() -> None:
    """ Fetches the pbl build """
    # if there is an independent built of libpbl, then use that
    if CONFIG["LIBPBL"] != LIBPBL:
        if not (p := Path(CONFIG["LIBPBL"]).resolve()).exists():
            raise ValueError(
                f"Invalid argument 'LIBPBL' with value '{CONFIG['LIBPBL']}'"
            )
        shutil.copy(p, C_LIB_TEMP_DESTINATION)
        return

    # fetching the file and writing it to the temp destination
    r = requests.get(CONFIG["LIBPBL"], allow_redirects=True)
    if r.status_code != 200:
        raise RuntimeError(
            f"Failed to execute request! Received '{r.status_code}' "
            f"for endpoint {LIBPBL}"
        )

    with open(C_LIB_TEMP_DESTINATION, "wb+") as f:
        f.write(r.content)


def create_parac_modules(output_type: str) -> None:
    """ Creates the required parac modules for the compiler """
    # copying the generated files to the tmp directory
    shutil.move(
        BASE_PATH / output_type / "parac",
        str(origin := BASE_PATH / "tmp" / output_type)
    )

    # destination where the files should be copied to
    destination = (BASE_PATH / output_type / "parac").resolve()

    # removing any previous data
    if os.path.exists(destination):
        shutil.rmtree(str(destination))

    bin_path: Path = (destination / "bin").resolve()
    avoid = ["bin"]

    # creating the binary directory
    os.makedirs(str(bin_path), exist_ok=True)

    # copying the lib item if the mode says we have to
    if CONFIG["ACTION"] in ACTIONS_THAT_REQUIRE_PBL:
        shutil.copy(
            C_LIB_TEMP_DESTINATION,
            bin_path / C_LIB_IDENTIFIER
        )

    # All items are going to be copied to the bin path, since the output of
    # pyinstaller will already contain the binary as needed, so the rest of the
    # items will be from the Para-C module and managed by us
    for entry in os.scandir(origin):
        entry: os.DirEntry
        # Avoid directories that are specifically marked as 'avoid'
        if not (entry.name in avoid and entry.is_dir()):
            shutil.move(entry.path, bin_path)

    for entry in COPY_FILES:
        entry: Path
        shutil.copy(str(entry.resolve()), destination)

    copy_tree(
        str(EXAMPLE_PATH.resolve()),
        str((destination / "examples").resolve())
    )

    create_bin_config(bin_path)

    # remove temp for this build mode
    shutil.rmtree(origin)


if __name__ == "__main__":
    parse_input()
    cleanup_and_create_tmp_folder()
    fetch_pbl_build()

    # creating the output directories
    for i in (DIST_PATH, BUILD_PATH):
        if not os.path.exists(str(i.resolve())):
            os.makedirs(str(i.resolve()), exist_ok=True)

    # we need the cli for the binaries, so we will attempt to import it and
    # raise an error if it's not available
    try:
        import parac_ext_cli
    except Exception as e:
        raise ImportError(
            "Failed to locate child module 'parac_ext_cli'. "
            "This module has to be installed to utilise the CLI version of "
            "Para-C"
        ) from e

    # we have to parse them, since they need the prefixes added to work with
    # the pyinstaller run configuration
    parse_avoid_and_hidden_imports()

    # afterwards, we are going to compile the compiler itself
    run_config = [
        str(ENTRY_PATH.resolve()),
        "--log-level",
        "DEBUG",
        "--name",
        "parac",
        "--icon",
        str(ICON_PATH.resolve()),
        *AVOID_MODULES,
        *HIDDEN_IMPORT
    ]

    # running pyinstaller - the output will appear in ./dist and ./build
    PyInstaller.__main__.run(run_config)

    create_parac_modules("dist")
    create_parac_modules("build")

    cleanup_and_remove_tmp_folder()
