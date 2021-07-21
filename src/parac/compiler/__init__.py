# coding=utf-8
""" Compiler for the Para-C programming language"""

from pathlib import Path

# argv[0] returns the path of the starting script
BASE_DIR: Path = Path(__file__).parent.parent.resolve()

# Main imports
from . import logging
from . import utils
from . import para_exceptions
from . import core

# Importing the files that are used in the Pre-Processor and Compiler
from .core import abc  # Abstract Classes

from . import __main__
from .__main__ import *

# Module Imports
from .logging import *
from .para_exceptions import *
from .core import *
from .utils import *

__all__ = [
    'abc',
    'utils',
    'logging',
    'logger',
    *core.__all__,
    *para_exceptions.__all__,
    *__main__.__all__,
    'WIN',
    'CONFIG_PATH',
    'BASE_DIR',
    'VALID_FILE_ENDINGS',
    'DEFAULT_LOG_PATH',
    'DEFAULT_DIST_PATH',
    'DEFAULT_BUILD_PATH',
    'DEFAULT_CONFIG',
    'INIT_OVERWRITE'
]

import click
import colorama
from typing import List


colorama.init(autoreset=True)

WIN: bool = click.utils.WIN
SEPARATOR: str = "\\" if WIN else "/"
CONFIG_PATH: str = f"{BASE_DIR}{SEPARATOR}compile-config.json"
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
