# coding=utf-8
"""
Para-C (parac) Module for the Para-C Compiler and Pre-Processor. This contains
the source code for the full compiler and interface, which is used to create
and run Para-C code.

Copyright (C) 2021 Luna Klatzer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

__title__ = "parac"
__description__ = "Para-C Module"
__url__ = "https://github.com/Para-C/Para-C/"
__author__ = "Luna Klatzer"
__author_email__ = "luna.klatzer@gmail.com"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "v0.1.dev5"
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
