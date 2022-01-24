# coding=utf-8
""" Constant values used in the module """
import os
from pathlib import Path
from typing import List, Union, Optional

__all__ = [
    "BASE_DIR",
    "C_LIB_PATH",
    "DIST_COMPILED_VERSION",
    "MODULE_VERSION",
    "C_COM_EXISTENCE_OVERWRITE",
    "DEFAULT_BUILD_PATH",
    "DEFAULT_DIST_PATH",
    "DEFAULT_LOG_PATH",
    "VALID_FILE_ENDINGS",
    "BIN_CONFIG_PATH",
    "initialise_default_paths",
]

# -- Signatures ---------------------------------------------------------------
BASE_DIR: Path
C_LIB_PATH: Optional[Path]
DIST_COMPILED_VERSION: bool
MODULE_VERSION: bool
C_COM_EXISTENCE_OVERWRITE: bool
DEFAULT_BUILD_PATH: Path
DEFAULT_DIST_PATH: Path
DEFAULT_LOG_PATH: Path
VALID_FILE_ENDINGS: List[str]
BIN_CONFIG_PATH: Path


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

# Initialising the default paths based on the work_dir
initialise_default_paths(os.getcwd())

# Base dir / root folder
# If module version -> ./ (valid)
# If compiled version -> ./bin (will be changed with version check)
BASE_DIR = Path(
    os.path.dirname(os.path.realpath(__file__))
).parent.resolve()

# If 'empty-bin-config.json' exists -> compiled binary mode
if os.path.exists(BASE_DIR / "bin" / "empty-bin-config.json"):
    DIST_COMPILED_VERSION = True
    MODULE_VERSION = False
    C_LIB_PATH = BASE_DIR / "bin" / "libpbl.a"
else:
    DIST_COMPILED_VERSION = False
    MODULE_VERSION = True
    C_LIB_PATH = None

# Config path for empty-bin-config.json
BIN_CONFIG_PATH = (BASE_DIR / "empty-bin-config.json").resolve()

# Valid file endings for Para
VALID_FILE_ENDINGS = [".para", ".parah", ".c", ".h", ".ph"]

# If the init overwrite is true =>
# Existence check for the c-compiler will always return True
C_COM_EXISTENCE_OVERWRITE = False
