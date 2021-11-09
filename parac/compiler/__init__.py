# coding=utf-8
"""
Para-C Compiler class, which is the main location, which stores functions
for parsing, compiling and handling files.
"""
from . import optimiser
from . import parser
from . import error_handler
from . import logic_stream
from . import ctx
from .process import *
from . import process
from .ctx import *
from . import compiler
from .compiler import *

__all__ = [
    *compiler.__all__,
    *ctx.__all__,
    *process.__all__,
    'optimiser',
    'parser',
    'error_handler',
    'logic_stream',
    'ctx',
    'compiler'
]

# Main-Class
ParacCompiler = compiler.ParacCompiler
