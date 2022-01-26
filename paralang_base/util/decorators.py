# coding=utf-8
""" File containing utility decorators """
import functools
import logging
import sys
import warnings
from functools import wraps

__all__ = [
    'deprecated',
]

logger = logging.getLogger(__name__)


def deprecated(_func, *, instead=None):
    """
    Warns the user about a function or tool that is deprecated
    and shouldn't be used anymore
    """

    def _decorator(func):
        @wraps(func)
        def _decorated(*args, **kwargs):
            # turn off filter
            warnings.simplefilter('always', DeprecationWarning)
            if instead:
                fmt = "{0.__name__} is deprecated, use {1} instead."
            else:
                fmt = '{0.__name__} is deprecated.'

            warnings.warn(
                fmt.format(func, instead),
                stacklevel=3,
                category=DeprecationWarning
            )
            # reset filter
            warnings.simplefilter('default', DeprecationWarning)
            return func(*args, **kwargs)

        return _decorated

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)
