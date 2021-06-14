# coding=utf-8
"""
File containing the class which will be used to track and run a compilation.
The compile unit will track variables, stack, logic and general compiling
information which is only related to the specified file.
"""


__all__ = [
    'CompileUnit'
]


class CompileUnit:
    """
    Class used inside the listener which 'listens' to events / registers
    tokens, which will keep track of variables, the stack, logic and
    general compiling information which is only related to the specified file.

    Dependencies will be managed using the CompilationContext, which will keep
    track of all files and in the end process the resulting dependencies and
    whether they work
    """
    ...
