# coding=utf-8
"""
CLI Script for building the compiler and generating the binaries that may be
used.
"""
import argparse
import json
import os
import platform
import shutil
import time
from pathlib import Path
from typing import List, Literal, Optional

import PyInstaller.__main__
import requests

# File constant
COMPATIBLE_VERSION: str = "v0.1.dev6"

# Input regex
IN_REGEX: str = "(--[A-z0-9]+=[A-z0-9]+)"

# Path Constants
BASE_PATH: Path = Path(os.getcwd())
DIST_PATH: Path = BASE_PATH / "dist"
BUILD_PATH: Path = BASE_PATH / "build"
ENTRY_PATH: Path = BASE_PATH / "dummy-entry.py"
EXAMPLE_PATH: Path = BASE_PATH / "example"
ICON_PATH: Path = BASE_PATH / "img" / "paralang.ico"

# C Compiler and PBL Config
C_COMPILER = "gcc"
C_LIB_IDENTIFIER = "libpbl.a"
LIB_PBL = f"https://github.com/Para-Lang/Para-Base-Library/releases/download/{COMPATIBLE_VERSION}/{C_LIB_IDENTIFIER}"
C_LIB_TEMP_DESTINATION = BASE_PATH / "tmp" / C_LIB_IDENTIFIER

# Target system
TARGET: str = platform.system()
IS_WIN: bool = os.name == "nt"
IS_POSIX: bool = os.name == 'posix'

# Raise error if the operating system is invalid
if not any((IS_WIN, IS_POSIX)):
    raise RuntimeError(
        f"Unsupported operating system (os.name): {os.name}"
    )

# Global destination paths
# The global destination for Posix / Linux / MacOS systems - None if invalid OS
POSIX_GLOBAL_DEST: Optional[Path] = \
    Path("~/.local/bin/Para").resolve() \
    if TARGET == "" \
    else None
# The global destination for NT / Windows systems - None if invalid OS
NT_GLOBAL_DEST: Optional[Path] = \
    Path("C:\\Program Files (x86)\\Para\\").resolve() \
    if TARGET == "windows" \
    else None
# Global destination, which is depending on the current operating system
GLOBAL_DEST: Optional[Path] = \
    POSIX_GLOBAL_DEST if IS_POSIX else NT_GLOBAL_DEST

# Required additional data files that have to be added
COPY_FILES: List[Path] = [
    BASE_PATH / "img" / "paralang.ico",
    BASE_PATH / "img" / "paralang-banner.png",
    BASE_PATH / "img" / "paralang.png",
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
HIDDEN_IMPORT = ["para_ext_cli", "paralang"]


def create_bin_config(dest_dir: Path) -> None:
    """
    Creates the binaries' config file
    """
    conf = {
        "c-compiler": C_COMPILER,
        "target": TARGET,
        "version": COMPATIBLE_VERSION,
        "build-time": time.time()  # Unix timestamp
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


def _download_url(url: str) -> None:
    """
    Downloads the specified url

    :raises RuntimeError: If the request failed to execute
    """
    # Fetching the file and writing it to the temp destination
    r = requests.get(url, allow_redirects=True)
    if r.status_code != 200:
        raise RuntimeError(
            f"Failed to execute request! Received "
            f"'{r.status_code}' for endpoint {LIB_PBL}"
        )

    with open(C_LIB_TEMP_DESTINATION, "wb+") as f:
        f.write(r.content)


def fetch_pbl_build(lib_pbl: str, allow_download: bool = False) -> None:
    """
    Fetches the pbl build and stores it in the 'C_LIB_TEMP_DESTINATION'

    :param lib_pbl: The required path to the 'libpbl.a'. Can be a URL
    :param allow_download: If set to True, the lib_pbl parameter will be taken
     as a URL to download. (Only if the lib_pbl path wasn't found locally \
     though)
    """
    # If there is an independent build of libpbl, then try to fetch that
    if lib_pbl != LIB_PBL:
        # If the path does not exist and allow_download is false
        if not (p := Path(lib_pbl).resolve()).exists():
            if allow_download is False:
                raise ValueError(
                    f"Could not find '--libpbl' with value '{lib_pbl}'"
                )
            else:
                _download_url(lib_pbl)

        shutil.copy(p, C_LIB_TEMP_DESTINATION)
        return

    _download_url(lib_pbl)


def install_para_module(output_type: Literal["dist", "build"]) -> None:
    """
    Creates the required paralang module for the compiler

    :param output_type: The output_type, where the data should be fetched from
     and the environment installed.
    """
    # Copying the generated files to the tmp directory
    shutil.move(
        BASE_PATH / output_type / "paralang",
        str(origin := BASE_PATH / "tmp" / output_type)
    )

    # The destination where the files should be copied to
    destination = (BASE_PATH / output_type / "paralang").resolve()
    # The destination path of the compiled files
    bin_path: Path = (destination / "bin").resolve()

    # Removing any previous data
    if os.path.exists(destination):
        shutil.rmtree(str(destination))

    # Creating the binary directory
    os.makedirs(str(bin_path), exist_ok=True)

    # Copying the required library with the c-headers
    shutil.copy(
        C_LIB_TEMP_DESTINATION,
        bin_path / C_LIB_IDENTIFIER
    )

    # All items are going to be copied to the bin path, since the output of
    # pyinstaller will already contain the binary as needed, so the rest of the
    # items will be from the Para module and managed by us
    for entry in os.scandir(origin):
        entry: os.DirEntry
        # Avoid directories that are named "bin" and are a directory
        if not (entry.name == "bin" and entry.is_dir()):
            shutil.move(entry.path, bin_path)

    # Copies all extra specified files into the destination
    # e.g. images, text files ...
    for entry in COPY_FILES:
        entry: Path
        shutil.copy(str(entry.resolve()), destination)

    # Copies the examples into the destination folder
    shutil.copytree(
        str(EXAMPLE_PATH.resolve()),
        str((destination / "example").resolve())
    )

    # Creates the binary configuration file
    create_bin_config(bin_path)

    # Remove temp files after finishing and having moved everything to its
    # proper destination
    shutil.rmtree(origin)


def install_global(optional_path: str):
    """
    Moves the content from the 'dist' folder into the OS-specific folder for
    program files.

    This will automatically fetch the proper destination based on the OS:
    - Linux: ~/.local/bin
    - MacOS: ~/.local/bin
    - Windows: C:\Program Files (x86)\

    :param optional_path: The optional path that may be specified where the
     dest files should be copied to.
    """
    try:
        path: Path
        origin = (DIST_PATH / "paralang").resolve()
        if optional_path:
            path: Path = Path(optional_path).resolve()
            shutil.copytree(
                src=origin,
                dst=str(path)
            )
        else:
            path: Path = Path(GLOBAL_DEST).resolve()
            shutil.copytree(
                src=origin,
                dst=str(path)
            )
        print(
            f"\nInstalled Para {COMPATIBLE_VERSION} globally in: {path}\n\n"
            "For info on how to add the item to your path/create a bash alias,"
            " as well as general info, go here: "
            "https://para.readthedocs.io/en/latest/installation.html"
        )
    except IOError as e:
        raise RuntimeError(
            "Failed to install paralang globally. Likely missing permissions"
        ) from e


def setup_conan():
    """
    Setups the local conan environment and makes it ready for
    installation of MingW-w64 and CMake
    """
    ...


def install_c_env():
    """
    Installs the C-compile environment with CMake and MingW-w64
    """
    ...


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Para Build Script'
    )
    parser.add_argument(
        "--libpbl", nargs=1, default=LIB_PBL, type=str, required=False,
        help="The destination path to the 'libpbl.a' file. If this is a url "
             "that should be downloaded, please specify '--allow-download' "
             "(Defaults to default mirror on GitHub)."
    )
    parser.add_argument(
        "--allow-download", action="store_true", default=False, required=False,
        help="If the 'libpbl' parameter is a URL that may be downloaded, then "
             "this flag has to be set to avoid an error while processing!"
    )
    parser.add_argument(
        "--install-global", action="store_true", default=False,
        required=False,
        help="If this is specified, the script will attempt to directly "
             "install paralang into your binary folder, so you can access it "
             "directly after this script finished. (Adds to the path "
             "yourself)."
    )
    parser.add_argument(
        "--g-dest", type=str, default=None, required=False,
        help="Specifies the global destination folder where paralang should be "
             "moved to. This is only valid when '--install-global' is also "
             "specified otherwise the value is just ignored. "
    )
    args = parser.parse_args()

    cleanup_and_create_tmp_folder()
    fetch_pbl_build(args.libpbl, args.allow_download)

    # creating the output directories
    for i in (DIST_PATH, BUILD_PATH):
        if not os.path.exists(str(i.resolve())):
            os.makedirs(str(i.resolve()), exist_ok=True)

    # we need the cli for the binaries, so we will attempt to import it and
    # raise an error if it's not available
    try:
        import para_ext_cli
    except Exception as e:
        raise ImportError(
            "Failed to locate child module 'para_ext_cli'. "
            "This module has to be installed to utilise the CLI version of "
            "Para"
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
        "paralang",
        "--icon",
        str(ICON_PATH.resolve()),
        *AVOID_MODULES,
        *HIDDEN_IMPORT
    ]

    # Running pyinstaller - the output will appear in ./dist and ./build
    PyInstaller.__main__.run(run_config)

    # Installs from the sources the proper paralang-c environment
    install_para_module("dist")
    install_para_module("build")

    # If this is specified try to download the specified
    if args.install_global:
        install_global(args.g_dest)

    if IS_WIN:
        # Install CMake and MingW-w64
        setup_conan()
        install_c_env()

    # Cleanups the tmp files generated while running
    cleanup_and_remove_tmp_folder()
