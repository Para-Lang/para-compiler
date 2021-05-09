""" Compiler for the Para-C programming language"""
__title__ = "paraccompiler"
__author__ = "Luna Klatzer"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "0.1"
__copyright__ = "Luna Klatzer"

from .exceptions import *
from .utils import *
from .__main__ import *


logging.getLogger(__name__).addHandler(logging.NullHandler())
