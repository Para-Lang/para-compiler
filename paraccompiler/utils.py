""" Utility in the Para-C Compiler"""
import logging
from functools import wraps
import warnings

__all__ = [
    'deprecated'
]

logger = logging.getLogger(__name__)


def deprecated(instead=None):
    """ Warns the user about a function or tool that is deprecated and shouldn't be used anymore """
    def actual_decorator(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)  # turn off filter
            if instead:
                fmt = "{0.__name__} is deprecated, use {1} instead."
            else:
                fmt = '{0.__name__} is deprecated.'

            warnings.warn(fmt.format(func, instead), stacklevel=3, category=DeprecationWarning)
            warnings.simplefilter('default', DeprecationWarning)  # reset filter
            return func(*args, **kwargs)

        return decorated

    return actual_decorator
