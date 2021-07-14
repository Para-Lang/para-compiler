# coding=utf-8
"""
Pre-Processor Module, containing the entire preprocessor including the
generated code for the preprocessor based on the ParaCPreProcessor.g4 grammar
file
"""
import os
import logging
import sys

from .python import (ParaCPreProcessorLexer, ParaCPreProcessorListener,
                     ParaCPreProcessorParser)
from . import __main__
from . import listener
from . import ctx
from . import logic_tokens
from .logic_tokens import *
from .__main__ import *

# Adding the working directory (location of compiler-cli.py)
sys.path.append(os.getcwd())


__all__ = [
    'ParaCPreProcessorLexer',
    'ParaCPreProcessorListener',
    'ParaCPreProcessorParser',
    'logic_tokens',
    'listener',
    'ctx',
    *logic_tokens.__all__,
    *ctx.__all__,
    *__main__.__all__
]

logging.getLogger(__name__).addHandler(logging.NullHandler())
