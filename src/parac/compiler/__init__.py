# coding=utf-8
""" Compiler for the Para-C programming language """
from . import __main__
from .__main__ import *
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
    *__main__.__all__,
    'optimiser',
    'parser',
    'error_handler',
    'logic_stream',
    'ctx',
    'compiler'
]

# Main-Class
ParacCompiler = compiler.ParacCompiler
