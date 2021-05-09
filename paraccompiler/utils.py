""" Utility in the Para-C Compiler"""
import logging
import traceback
from typing import Optional, Callable, Tuple, Type
from types import FunctionType, TracebackType
from functools import wraps
import warnings


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


def log_traceback(
        exc_info: Tuple[Type[BaseException], BaseException, TracebackType],
        level: Optional[str] = 'error',
        brief: Optional[str] = None
) -> None:
    """
    Logs the traceback of the latest exception

    :param level: Logger level for the exception
    :param brief: Small message that will be logged before the traceback
    :param exc_info: The exc_info containing the exception and the traceback
    """
    tb = traceback.format_exception(
        etype=exc_info[0],
        value=exc_info[1],
        tb=exc_info[2]
    )

    log_level: Callable = getattr(logger, level, None)
    if log_level is None and not callable(log_level):
        raise ValueError("The passed level does not exist in the logging module!")

    tb_str = "".join(frame for frame in tb)
    brief = brief if brief is not None else ""
    msg = f"{brief}\n\n{tb_str}\n"

    # Fetches and prints the current traceback with the passed message
    log_level(msg)
    print(msg)


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
