""" Compiler for the Para-C programming language"""
__title__ = "parac_compiler"
__author__ = "Luna Klatzer"
__license__ = "GNU GENERAL PUBLIC LICENSE v3.0"
__version__ = "0.1"
__copyright__ = "Luna Klatzer"

import logging
from typing import Optional
from types import FunctionType


def log_msg(level: str, msg: str, *args, **kwargs) -> None:
    """ Logs the specified message using the logger module and regular print

    :param level: The logging level which should be used
    :param msg: The msg that should be printed
    :param args: The args that should be passed to the logging call
    :param kwargs: The kwargs that should be passed to the logging call
    """
    log_level: Optional[FunctionType] = getattr(logger, level)
    if callable(log_level):
        log_level(msg=msg, *args, **kwargs)
    print(msg)


from .__main__ import *


logging.getLogger(__name__).addHandler(logging.NullHandler())
