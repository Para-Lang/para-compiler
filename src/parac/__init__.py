# coding=utf-8
""" Init file for managing both compiler and preprocessor """

__title__ = "parac"
__description__ = "Para-C Module"
__url__ = "https://github.com/Para-C/Para-C/"
__author__ = "Luna Klatzer"
__author_email__ = "luna.klatzer@gmail.com"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "v0.1.dev2"
__code_name__ = ""
__release__ = f"{__code_name__} {__version__}"
__copyright__ = "Luna Klatzer"

from .const import *
from . import const
from .exceptions import *
from . import exceptions
from . import abc
from . import logging
from . import util
from . import compiler
from . import preprocessor

MODULES = [
    "const",
    "exceptions",
    "abc",
    "logging",
    "util"
    "compiler",
    "preprocessor"
]

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
    'compiler',
    'preprocessor',
    'BASE_DIR',
    'C_LIB_PATH',
    'WIN',
    'CONFIG_PATH',
    'VALID_FILE_ENDINGS',
    'DEFAULT_LOG_PATH',
    'DEFAULT_DIST_PATH',
    'DEFAULT_BUILD_PATH',
    'DEFAULT_CONFIG',
    'C_COM_EXISTENCE_OVERWRITE',
    'RUNTIME_COMPILER',
    *exceptions.__all__,
    *const.__all__,
    *MODULES
]

import logging as lib_logging
import colorama

colorama.init(autoreset=True)
lib_logging.getLogger(__name__).addHandler(lib_logging.NullHandler())

# An instance of the compiler, which should be generally used in the module
# due to the logging logic
RUNTIME_COMPILER: compiler.ParacCompiler = compiler.ParacCompiler()
