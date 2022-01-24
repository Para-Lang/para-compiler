# coding=utf-8
""" Logger management file for formatting and specific exception and  """
import logging
from types import FunctionType
from typing import Optional

logger = logging.getLogger(__name__)

__all__ = [
    'log_msg'
]


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
