# coding=utf-8
""" Compiler for the Para-C programming language"""

__title__ = "paraccompiler"
__description__ = "Para-C compiler written in Python"
__url__ = "https://github.com/Luna-Klatzer/Para-C/"
__author__ = "Luna Klatzer"
__author_email__ = "luna.klatzer@gmail.com"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "v0.1.dev1"
__code_name__ = ""
__release__ = f"{__code_name__} {__version__}"
__copyright__ = "Luna Klatzer"

import sys
import pathlib

# argv[0] returns the path of the starting script
RUN_SCRIPT_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.resolve()

# Adding the working directory (location of compiler-cli.py)
sys.path.append(str(RUN_SCRIPT_DIR))

# Main imports
from . import logging
from . import utils
from . import para_exceptions
from . import core

# Importing the files that are used in the Pre-Processor and Compiler
from .core import abc  # Abstract Classes

# Importing from the added path the preprocessor
import preprocessor

from . import __main__
from .__main__ import *

# Module Imports
from .logging import *
from .para_exceptions import *
from .core import *
from .utils import *

__all__ = [
    '__title__',
    '__description__',
    '__url__',
    '__author__',
    '__author_email__',
    '__license__',
    '__version__',
    '__code_name__',
    '__release__',
    '__copyright__',
    'abc',
    'preprocessor',
    'utils',
    'logging',
    'logger',
    *core.__all__,
    *para_exceptions.__all__,
    *__main__.__all__,
    'WIN',
    'CONFIG_PATH',
    'RUN_SCRIPT_DIR',
    'VALID_FILE_ENDINGS',
    'DEFAULT_LOG_PATH',
    'DEFAULT_DIST_PATH',
    'DEFAULT_BUILD_PATH',
    'DEFAULT_CONFIG',
    'INIT_OVERWRITE'
]

import logging as lib_logging
import click
import colorama
from typing import List


lib_logging.getLogger(__name__).addHandler(lib_logging.NullHandler())
colorama.init(autoreset=True)

WIN: bool = click.utils.WIN
SEPARATOR: str = "\\" if WIN else "/"
CONFIG_PATH: str = f"{RUN_SCRIPT_DIR}{SEPARATOR}compile-config.json"
VALID_FILE_ENDINGS: List[str] = [".para", ".parah", ".c", ".h", ".ph"]
DEFAULT_LOG_PATH: str = "./para.log"
DEFAULT_BUILD_PATH: str = "./build"
DEFAULT_DIST_PATH: str = "./dist"
# If the init overwrite is true =>
# Existence check for the c-compiler will always return True
INIT_OVERWRITE: bool = False
DEFAULT_CONFIG: dict = {
    "c-compiler-path": ""
}
INVALID_UNIX_FILE_NAME_CHARS: List[str] = ['/', '<', '>', '\0', '|', ':', '&']
INVALID_WIN_FILE_NAME_CHARS: List[str] = [
    '<', '>', ':', '"', '/', '\\', '|', '?', '*'
]

# Main-Class
ParacCompiler = core.compiler.ParacCompiler
