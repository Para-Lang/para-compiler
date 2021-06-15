# coding=utf-8
"""
File containing the class which will be used to track and run a compilation.
The compile unit will track variables, stack, logic and general compiling
information which is only related to the specified file.
"""


__all__ = [
    'FileCompilationContext',
    'CompilationContext'
]

from typing import Dict


class FileCompilationContext:
    """
    Class used inside the listener which 'listens' to events / registers
    tokens, which will keep track of variables, the stack, logic and
    general compiling information which is only related to the specified file.

    Dependencies will be managed using the CompilationContext, which will keep
    track of all files and in the end process the resulting dependencies and
    whether they work
    """
    ...


# TODO! Add proper logic and dependency management
class CompilationContext:
    """ Compilation Context """

    def __init__(self):
        ...

    def gen_str(self) -> Dict[str, str]:
        """
        Generates from the tokens stored inside the class the program strings,
        which will be named after the relative position in the output-dir
        """
        ...
