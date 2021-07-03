# coding=utf-8
""" Compiler for the Para-C programming language"""

__title__ = "paraccompiler"
__description__ = "Para-C compiler written in Python"
__url__ = "https://github.com/Luna-Klatzer/Para-C/"
__author__ = "Luna Klatzer"
__author_email__ = "luna.klatzer@gmail.com"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "v0.0.1pre1"
__code_name__ = ""
__release__ = f"{__code_name__} {__version__}"
__copyright__ = "Luna Klatzer"

# Preprocessor Import
import sys
import os
# Adding the working directory (location of compiler-cli.py)
sys.path.append(os.getcwd())
# Importing from the added path the preprocessor
import preprocessor

# Main imports
from . import logger
from . import utils
from . import para_exceptions
from . import __main__
from .__main__ import *

# Module Imports
from .logger import *
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
    'WIN',
    'preprocessor',
    *logger.__all__,
    *para_exceptions.__all__,
    *utils.__all__,
    *__main__.__all__,
]

import logging
import click
import colorama

colorama.init(autoreset=True)
logging.getLogger(__name__).addHandler(logging.NullHandler())

WIN: bool = click.utils.WIN
