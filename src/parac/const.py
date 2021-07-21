# coding=utf-8
""" Constant values used in the module """
from typing import List
from pathlib import Path
import click
import os

__all__ = [
    "BASE_DIR",
    "C_LIB_PATH",
    "INIT_OVERWRITE",
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

BASE_DIR: Path = Path(__file__).parent.parent.resolve()
# Directory where the script was executed
WORK_DIR: Path = Path(os.getcwd()).resolve()
C_LIB_PATH: Path = BASE_DIR / "lib"

WIN: bool = click.utils.WIN
SEPARATOR: str = "\\" if WIN else "/"
CONFIG_PATH: Path = (BASE_DIR / "compile-config.json").resolve()
VALID_FILE_ENDINGS: List[str] = [".para", ".parah", ".c", ".h", ".ph"]
DEFAULT_LOG_PATH: Path = (WORK_DIR / "para.log").resolve()
DEFAULT_BUILD_PATH: Path = (WORK_DIR / "build").resolve()
DEFAULT_DIST_PATH: Path = (WORK_DIR / "dist").resolve()
# If the init overwrite is true =>
# Existence check for the c-compiler will always return True
INIT_OVERWRITE: bool = False
DEFAULT_CONFIG: dict = {
    "c-compiler-path": ""
}
INVALID_UNIX_FILE_NAME_CHARS: List[str] = [
    '/', '<', '>', '\0', '|', ':', '&'
]
INVALID_WIN_FILE_NAME_CHARS: List[str] = [
    '<', '>', ':', '"', '/', '\\', '|', '?', '*'
]
