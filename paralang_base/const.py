# coding=utf-8
""" Constant values used in the module """
import os
import sys
from pathlib import Path
from typing import List, Union, Optional

__all__ = [
    "BASE_DIR",
    "C_LIB_PATH",
    "DIST_COMPILED_VERSION",
    "DEFAULT_BUILD_PATH",
    "DEFAULT_DIST_PATH",
    "DEFAULT_LOG_PATH",
    "VALID_FILE_ENDINGS",
    "initialise_default_paths",
]

# -- Signatures ---------------------------------------------------------------
BASE_DIR: Path
C_LIB_PATH: Optional[Path]
DIST_COMPILED_VERSION: bool
DEFAULT_BUILD_PATH: Path
DEFAULT_DIST_PATH: Path
DEFAULT_LOG_PATH: Path
VALID_FILE_ENDINGS: List[str]


# -- Initialisation Functions -------------------------------------------------


def initialise_default_paths(work_dir: Union[str, os.PathLike, Path]):
    """
    Initialises the default paths based on the passed work dir:
     - DEFAULT_LOG_PATH: ./paralang_base.log
     - DEFAULT_BUILD_PATH: ./build
     - DEFAULT_DIST_PATH: ./dist
    """
    work_dir = Path(str(work_dir)).resolve()

    global DEFAULT_LOG_PATH
    DEFAULT_LOG_PATH = (work_dir / "paralang_base.log").resolve()
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

if sys.argv[0].endswith("para.exe"):
    DIST_COMPILED_VERSION = True
    C_LIB_PATH: Optional[Path] = BASE_DIR / "bin" / "lib" / "libpbl.a"
else:
    DIST_COMPILED_VERSION = False
    C_LIB_PATH: Optional[Path] = None

    # TODO! Add the option to download 'libpbl' on installation of
    #  paralang_base

# Valid file endings for Para
VALID_FILE_ENDINGS = [".para", ".parah", ".c", ".h", ".ph"]
