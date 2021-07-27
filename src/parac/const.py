# coding=utf-8
""" Constant values used in the module """
from typing import List, Dict, Union
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
    "initialise_default_paths",
]

# -- Signatures ---------------------------------------------------------------
BASE_DIR: Path
C_LIB_PATH: Path
DIST_VERSION: bool
MODULE_VERSION: bool
C_COM_EXISTENCE_OVERWRITE: bool
DEFAULT_CONFIG: Dict[str, str]
DEFAULT_BUILD_PATH: Path
DEFAULT_DIST_PATH: Path
DEFAULT_LOG_PATH: Path
VALID_FILE_ENDINGS: List[str]
CONFIG_PATH: Path
SEPARATOR: str
INVALID_UNIX_FILE_NAME_CHARS: List[str]
INVALID_WIN_FILE_NAME_CHARS: List[str]
WIN: bool

# -- Initialisation Functions -------------------------------------------------


def initialise_default_paths(work_dir: Union[str, os.PathLike, Path]):
    """
    Initialises the default paths based on the passed work dir:
     - DEFAULT_LOG_PATH: ./para.log
     - DEFAULT_BUILD_PATH: ./build
     - DEFAULT_DIST_PATH: ./dist
    """
    work_dir = Path(str(work_dir)).resolve()

    global DEFAULT_LOG_PATH
    DEFAULT_LOG_PATH = (work_dir / "para.log").resolve()
    global DEFAULT_BUILD_PATH
    DEFAULT_BUILD_PATH = (work_dir / "build").resolve()
    global DEFAULT_DIST_PATH
    DEFAULT_DIST_PATH = (work_dir / "dist").resolve()


# -- Initialisation of Variables ----------------------------------------------

# Base dir / root folder
BASE_DIR = Path(
    os.path.dirname(os.path.realpath(__file__))
).parent.parent.resolve()

# Path to the binary folder or in dev mode /src/
BIN_DIR = Path(
    os.path.dirname(os.path.realpath(__file__))
).parent.resolve()

# Initialising the default paths based on the work_dir
initialise_default_paths(os.getcwd())

# If the lib folder is in the module (./src or ./bin) then it's module runtime,
# else if in the root folder then it's the dist runtime aka. the pyinstaller
# compiled runtime
if os.path.exists(BIN_DIR / "lib"):
    DIST_VERSION = False
    MODULE_VERSION = True
    C_LIB_PATH = BIN_DIR / "lib"
elif os.path.exists(BASE_DIR / "lib"):
    DIST_VERSION = True
    MODULE_VERSION = False
    C_LIB_PATH = BASE_DIR / "lib"

    if not os.path.exists(BASE_DIR / "compiler-config.json"):
        raise RuntimeError(
            f"compiler-config.json not found! "
            f"Expected {BASE_DIR / 'compiler-config.json'}"
        )
else:
    raise RuntimeError("Cannot locate lib folder")

# If true OS is Windows
WIN = click.utils.WIN

# Path Separator
SEPARATOR = "\\" if WIN else "/"

# Config path for compiler-config.json
CONFIG_PATH = (BASE_DIR / "compiler-config.json").resolve()

# Valid file endings for Para-C
VALID_FILE_ENDINGS = [".para", ".parah", ".c", ".h", ".ph"]

# If the init overwrite is true =>
# Existence check for the c-compiler will always return True
C_COM_EXISTENCE_OVERWRITE = False

# Default Config for compiler-config.json
DEFAULT_CONFIG = {
    "c-compiler-path": "",
    "lib-path": "./lib/"
}

# Invalid chars for a path (unix)
INVALID_UNIX_FILE_NAME_CHARS = [
    '/', '<', '>', '\0', '|', ':', '&'
]

# Invalid chars for a path (win)
INVALID_WIN_FILE_NAME_CHARS = [
    '<', '>', ':', '"', '/', '\\', '|', '?', '*'
]
