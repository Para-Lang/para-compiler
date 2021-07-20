# coding=utf-8
""" Init file for managing both compiler and preprocessor """

__title__ = "parac"
__description__ = "Para-C Module"
__url__ = "https://github.com/Para-C/Para-C/"
__author__ = "Luna Klatzer"
__author_email__ = "luna.klatzer@gmail.com"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "v0.1.dev1"
__code_name__ = ""
__release__ = f"{__code_name__} {__version__}"
__copyright__ = "Luna Klatzer"

from . import compiler
from . import preprocessor

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
    'preprocessor'
]

import logging as lib_logging

lib_logging.getLogger(__name__).addHandler(lib_logging.NullHandler())
