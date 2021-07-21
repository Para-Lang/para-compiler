# coding=utf-8
"""
Core Optimiser for the C code and Para-C code which will optimise the code
and manage imports and additional content using the __parac__.h file
"""

__all__ = [
    'Optimiser'
]

from ..ctx import FileCompilationContext
from ..process import ProgramCompilationContext


class Optimiser:
    """ Optimiser Class used to optimise the code """

    def optimise(
            self,
            ctx: ProgramCompilationContext,
            cu: FileCompilationContext
    ):
        """ Optimises the CompileUnit code """

