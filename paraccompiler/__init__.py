# coding=utf-8
""" Compiler for the Para-C programming language"""

__title__ = "parac-compiler"
__description__ = "Para-C compiler written in Python"
__url__ = "https://github.com/Luna-Klatzer/Para-C/"
__author__ = "Luna Klatzer"
__author_email__ = "luna.klatzer@gmail.com"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "v0.1"
__code_name__ = ""
__release__ = f"{__code_name__} {__version__}"
__copyright__ = "Luna Klatzer"

# Main imports
from . import logger
from .logger import *
from . import exceptions
from .exceptions import *
from . import utils
from .utils import *
from . import compiler
from .compiler import *
from . import __main__
from .__main__ import *

# Module Imports
from . import tokenizer

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
    'tokenizer',
    'WIN',
    *logger.__all__,
    *exceptions.__all__,
    *utils.__all__,
    *__main__.__all__,
    *compiler.__all__
]

import logging
import click
import colorama

colorama.init(autoreset=True)
logging.getLogger(__name__).addHandler(logging.NullHandler())

WIN: bool = click.utils.WIN
