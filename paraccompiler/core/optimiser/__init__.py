# coding=utf-8
"""
Core Optimiser for the C code and Para-C code which will optimise the code
and manage imports and additional content using the __parac__.h file
"""
from ..compile_unit import CompileUnit
from ..compiler import CompilationContext


__all__ = [
    'Optimiser'
]


class Optimiser:
    """ Optimiser Class used to optimise the code """

    def optimise(self, ctx: CompilationContext, cu: CompileUnit):
        """ Optimises the CompileUnit code """

