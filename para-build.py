# coding=utf-8
"""
CLI Script for building the compiler and generating the binaries that may be
used.

Steps of generating the binary output:
1. Fetch Para Base Library that is required for the compiler! Either

"""
import argparse
import os
import platform
import shutil
from pathlib import Path
from typing import List, Literal, Optional

import PyInstaller.__main__
import requests
import paralang_base
import paralang_cli

# Asserting that both versions are equal and compatible
if not paralang_cli.__version__ == paralang_base.__version__:
    raise RuntimeError(
        f"'paralang_cli' has version {paralang_cli.__version__}. "
        f"'paralang_base' requires '{paralang_base.__version__}!"
    )

# Compatible version
COMPATIBLE_VERSION: str = paralang_base.__version__

# Input regex
IN_REGEX: str = "(--[A-z0-9]+=[A-z0-9]+)"

# Path Constants
BASE_PATH: Path = Path(os.getcwd())
DIST_PATH: Path = BASE_PATH / "dist"
BUILD_PATH: Path = BASE_PATH / "build"
PYI_SPEC_FILE: Path = BASE_PATH / "scripts" / "scripts.spec"
ICON_PATH: Path = BASE_PATH / "img" / "para.ico"

# C Compiler and PBL Config
C_LIB_IDENTIFIER = "libpbl.a"
LIB_PBL = f"https://github.com/Para-Lang/Para-Base-Library/releases/download/{COMPATIBLE_VERSION}/{C_LIB_IDENTIFIER}"
C_LIB_TEMP_DESTINATION = BASE_PATH / "tmp" / C_LIB_IDENTIFIER

# Target system
PLATFORM: str = platform.system()
IS_WIN: bool = os.name == "nt"
IS_POSIX: bool = os.name == 'posix'
POSIX_GLOBAL_DEST: Path = Path("~/.local/bin/para/")
NT_GLOBAL_DEST: Optional[Path] = Path("C:\\Program Files (x86)\\para\\")

# Raise error if the operating system is invalid
if not any((IS_WIN, IS_POSIX)):
    raise RuntimeError(
        f"Unsupported operating system (os.name): {os.name}"
    )

# Required additional data files that have to be added
COPY_FILES: List[str] = []
with open("./INSTALL_FILES", "r+") as file:
    lines = file.readlines()
    for line in lines:
        line: str = line.replace("\n", "").replace("\r", "")
        COPY_FILES.append(line)


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
    Creates the required para module for the compiler

    :param output_type: The output_type, where the data should be fetched from
     and the environment installed.
    """
    # Copying the generated files to the tmp directory
    shutil.move(
        BASE_PATH / output_type / "para",
        str(tmp_binary_dir := BASE_PATH / "tmp" / output_type)
    )
    # The destination where the files should be copied to
    destination = (BASE_PATH / output_type / "para").resolve()
    # The destination path of the compiled files
    bin_path: Path = (destination / "bin").resolve()

    # Removing any previous data
    if os.path.exists(destination):
        shutil.rmtree(str(destination))

    # Creating the binary directories
    os.makedirs(str(bin_path), exist_ok=True)
    os.makedirs(str(bin_path / "lib"), exist_ok=True)

    # Copying the required library with the c-headers
    shutil.copy(
        C_LIB_TEMP_DESTINATION,
        bin_path / "lib" / C_LIB_IDENTIFIER
    )

    # All items are going to be copied to the bin path, since the output of
    # pyinstaller will already contain the binary as needed, so the rest of the
    # items will be from the Para module and managed by us
    for entry in os.scandir(tmp_binary_dir):
        entry: os.DirEntry
        # Avoid directories that are named "bin" and are a directory
        if not (entry.name == "bin" and entry.is_dir()):
            shutil.move(entry.path, bin_path)

    # Copies all extra specified files into the destination
    # e.g. images, text files ...
    for entry in COPY_FILES:
        entry: Path = Path(entry)
        dest: Path = (destination / entry).resolve()
        os.makedirs(str(dest.parent), exist_ok=True)
        if entry.is_dir():
            shutil.copytree(
                str(entry.resolve()),
                str(dest)
            )
        else:
            shutil.copy(
                str((BASE_PATH / entry).resolve()),
                str(dest)
            )

    # Move all extensions into the /bin/ folder as well
    for output_entry in os.scandir(BASE_PATH / output_type):
        output_entry: os.DirEntry
        output_entry: Path = Path(str(output_entry.path)).resolve()
        if output_entry.is_dir and output_entry.name != "para":
            # Go through every item in the output directory item
            for file_item in os.scandir(str(output_entry)):
                file_item: os.DirEntry
                file_item: Path = Path(str(file_item.path)).resolve()
                # Copying the file if it is ending with an '.exe'
                if file_item.name.endswith(".exe"):
                    shutil.copy(
                        str(file_item.resolve()),
                        str((bin_path / file_item.name).resolve())
                    )

    # Remove temp files after finishing and having moved everything to its
    # proper destination
    shutil.rmtree(tmp_binary_dir)


def install_global(optional_path: str):
    """
    Moves the content from the 'dist' folder into the OS-specific folder for
    program files.

    This will automatically fetch the proper destination based on the OS:
    - Linux: ~/.local/bin
    - macOS: ~/.local/bin
    - Windows: C:\\Program Files (x86)\

    :param optional_path: The optional path that may be specified where the
     dest files should be copied to.
    """
    try:
        path: Path
        origin = (DIST_PATH / "para").resolve()
        if optional_path:
            path: Path = Path(optional_path).resolve()
            shutil.copytree(
                src=origin,
                dst=str(path)
            )
        else:
            dest: Path = NT_GLOBAL_DEST if IS_WIN else POSIX_GLOBAL_DEST
            path: Path = Path(dest).resolve()
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
            "Failed to install para globally. Likely missing permissions"
        ) from e


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
             "install para into your binary folder, so you can access it "
             "directly after this script finished. (Adds to the path "
             "yourself)."
    )
    parser.add_argument(
        "--g-dest", type=str, default=None, required=False,
        help="Specifies the global destination folder where para should be"
             " moved to. This is only valid when '--install-global' is also "
             "specified otherwise the value is just ignored. "
    )
    args = parser.parse_args()

    cleanup_and_create_tmp_folder()
    fetch_pbl_build(args.libpbl, args.allow_download)

    # creating the output directories
    for i in (DIST_PATH, BUILD_PATH):
        if not os.path.exists(str(i.resolve())):
            os.makedirs(str(i.resolve()), exist_ok=True)

    # We need the extensions for the binaries, so we will attempt to import
    # them and raise an error if they are not available
    try:
        import paralang_cli
    except Exception as e:
        raise ImportError(
            "Failed to locate child module 'paralang_cli'. "
            "This module has to be installed to utilise the CLI version of "
            "Para"
        ) from e

    # Afterwards, we are going to compile the compiler CLi and extensions
    # itself
    run_config = [
        str(PYI_SPEC_FILE.resolve()),
        "--log-level",
        "DEBUG",
        "--icon",
        str(ICON_PATH)
    ]

    # Running pyinstaller - the output will appear in ./dist and ./build
    PyInstaller.__main__.run(run_config)

    # Installs from the sources the proper para environment
    install_para_module("dist")

    # if true, then attempt to install the executable globally
    if args.install_global:
        install_global(args.g_dest)

    # Cleanups the tmp files generated while running
    cleanup_and_remove_tmp_folder()
