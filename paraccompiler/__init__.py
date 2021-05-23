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

import click

WIN: bool = click.utils.WIN

from .logger import __all__ as __logger_all__
from .logger import *
from .exceptions import __all__ as __exceptions_all__
from .exceptions import *
from .utils import __all__ as __utils_all__
from .utils import *
from .compiler import __all__ as __compiler_all__
from .compiler import *
from .__main__ import __all__ as __main_all__
from .__main__ import *

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
    *__logger_all__,
    *__exceptions_all__,
    *__utils_all__,
    *__main_all__,
    *__compiler_all__
]

import logging
import colorama

colorama.init(autoreset=True)
logging.getLogger(__name__).addHandler(logging.NullHandler())
