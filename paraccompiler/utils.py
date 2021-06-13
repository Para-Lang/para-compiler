# coding=utf-8
""" Utility in the Para-C Compiler"""
import functools
import logging
import re
import sys
import warnings
import os
from sys import exit

from click.utils import WIN
from os import PathLike
from typing import Union, Type
from functools import wraps

from .para_exceptions import AbortError
from .logger import (get_rich_console as console, log_traceback,
                     print_abort_banner, init_rich_console)

__all__ = [
    'SEPARATOR',
    'deprecated',
    'decode_if_bytes',
    'cleanup_path',
    'abortable',
    'requires_init',
    'keep_open_callback',
    'escape_ansi',
    'escape_ansi_param'
]

logger = logging.getLogger(__name__)

SEPARATOR = "\\" if WIN else "/"


def abortable(_func=None, *, print_abort: bool = True, step: str = "Process"):
    """
    Marks the function as abort-able and adds traceback logging to it.
    If re-raise is False it will exit the program
    """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except AbortError:
                if print_abort:
                    print_abort_banner(step)
                exit(1)

            except Exception as e:
                from .__main__ import para_compiler
                if not para_compiler.log_initialised:
                    para_compiler.init_logging_session()

                log_traceback(
                    level="critical",
                    brief="Exception in the compilation setup",
                    exc_info=sys.exc_info()
                )
                raise AbortError(exception=e) from e

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


def requires_init(_func=None):
    """
    Checks whether the compiler is initialised and only calls the function if
    it is, else it will trigger a warning and prompt for initialisation
    """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            from . import (is_c_compiler_ready, INIT_OVERWRITE,
                           initialise_c_compiler)
            if not is_c_compiler_ready() and not INIT_OVERWRITE:
                from . import para_compiler
                if not para_compiler.log_initialised:
                    para_compiler.init_logging_session()

                init_rich_console()
                console().print('')
                logger.warning(
                    "C-Compiler path is not initialised! If you do not have a"
                    " working compiler installed, please refer to an "
                    "installation page for your operation system"
                    " (MinGW, cygwin)"
                )
                logger.info(
                    "Initialising Para-C compiler due to missing configuration"
                    "\n"
                )
                initialise_c_compiler()
                logger.info("Setup may continue\n")
            return func(*args, **kwargs)

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


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


def decode_if_bytes(byte_like: Union[str, bytes, PathLike, Type]):
    """ Decodes the passed PathLike if it is in bytes """
    if type(byte_like) is str:
        return byte_like
    elif type(byte_like) is bytes or isinstance(bytes, byte_like):
        return byte_like.decode()
    else:
        return byte_like


def cleanup_path(_p: str) -> str:
    """ Cleans the path for the specific current os """
    if WIN:
        _p = _p.replace("/", SEPARATOR).replace("\\\\", SEPARATOR)
    else:
        # UNIX path
        _p = _p.replace("\\", SEPARATOR).replace("\\\\", SEPARATOR)

    if _p.startswith(f".{SEPARATOR}"):
        _p = os.getcwd() + _p[1:]  # Replacing . with current directory
    return _p


def keep_open_callback(_func=None):
    """ Keeps the console open after finishing until the user presses a key """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            keep_open = kwargs.pop('keep_open')
            r = func(*args, **kwargs)

            # If keep_open is True -> the user passed --keep_open as an option
            # then the console will stay open until a key is pressed
            if keep_open:
                console().print("\n\n", end="")
                console().input("Press any key to continue ...")
                console().print("", end="\n")
            return r

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


def escape_ansi(string: str) -> str:
    """ Removes ansi colouring in the passed string """
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', string)


def escape_ansi_param(_func):
    """
    Calls the function but removes ansi colouring on the args and kwargs on str
    items if it exists
    """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            new_args = []
            for i in args:
                if type(i) is str:
                    new_args.append(escape_ansi(i))
                else:
                    new_args.append(i)

            new_kwargs = {}
            for key, value in kwargs.items():
                if type(value) is str:
                    value = escape_ansi(value)
                new_kwargs[key] = value

            return func(*new_args, **new_kwargs)

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)
