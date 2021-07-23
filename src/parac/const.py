# coding=utf-8
""" Constant values used in the module """
from typing import List
from pathlib import Path
import click
import os

__all__ = [
    "BASE_DIR",
    "C_LIB_PATH",
    "DIST_VERSION",
    "MODULE_VERSION",
    "C_COM_EXISTENCE_OVERWRITE",
    "DEFAULT_CONFIG",
    "DEFAULT_BUILD_PATH",
    "DEFAULT_DIST_PATH",
    "DEFAULT_LOG_PATH",
    "VALID_FILE_ENDINGS",
    "CONFIG_PATH",
    "SEPARATOR",
    "INVALID_UNIX_FILE_NAME_CHARS",
    "INVALID_WIN_FILE_NAME_CHARS",
    "WIN",
    "WORK_DIR"
]

# Base dir / root folder
BASE_DIR: Path = Path(
    os.path.dirname(os.path.realpath(__file__))
).parent.parent.resolve()
# Path to the binary folder or in dev mode /src/
BIN_DIR: Path = Path(
    os.path.dirname(os.path.realpath(__file__))
).parent.resolve()

# Directory where the script was executed
WORK_DIR: Path = Path(os.getcwd()).resolve()

# If the lib folder is in the bin folder or /src/ folder then it's the module
# runtime, else if in the source folder then it's the dist runtime aka. the
# pyinstaller compiled runtime
if os.path.exists(BIN_DIR / "lib"):
    DIST_VERSION: bool = False
    MODULE_VERSION: bool = True
    C_LIB_PATH: Path = BIN_DIR / "lib"
elif os.path.exists(BASE_DIR / "lib"):
    DIST_VERSION: bool = True
    MODULE_VERSION: bool = False
    C_LIB_PATH: Path = BASE_DIR / "lib"

    if not os.path.exists(BASE_DIR / "compiler-config.json"):
        raise RuntimeError(
            f"compiler-config.json not found! "
            f"Expected {BASE_DIR / 'compiler-config.json'}"
        )
else:
    raise RuntimeError("Cannot locate lib folder")


WIN: bool = click.utils.WIN
SEPARATOR: str = "\\" if WIN else "/"
CONFIG_PATH: Path = (BASE_DIR / "compiler-config.json").resolve()
VALID_FILE_ENDINGS: List[str] = [".para", ".parah", ".c", ".h", ".ph"]
DEFAULT_LOG_PATH: Path = (WORK_DIR / "para.log").resolve()
DEFAULT_BUILD_PATH: Path = (WORK_DIR / "build").resolve()
DEFAULT_DIST_PATH: Path = (WORK_DIR / "dist").resolve()
# If the init overwrite is true =>
# Existence check for the c-compiler will always return True
C_COM_EXISTENCE_OVERWRITE: bool = False
DEFAULT_CONFIG: dict = {
    "c-compiler-path": "",
    "lib-path": "./lib/"
}
INVALID_UNIX_FILE_NAME_CHARS: List[str] = [
    '/', '<', '>', '\0', '|', ':', '&'
]
INVALID_WIN_FILE_NAME_CHARS: List[str] = [
    '<', '>', ':', '"', '/', '\\', '|', '?', '*'
]
