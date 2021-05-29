# coding=utf-8
""" Utility in the Para-C Compiler"""
import functools
import json
import logging
import sys
import warnings
import os
from sys import exit

from click.utils import WIN
from os import PathLike
from typing import Union, Type
from functools import wraps

from .exceptions import CCompilerError, AbortError
from .logger import get_rich_console as console, log_traceback

__all__ = [
    'INIT_OVERWRITE',
    'SEPARATOR',
    'COMPILER_DIR',
    'c_compiler_initialised',
    'initialise',
    'deprecated',
    'decode_if_bytes',
    'cleanup_path',
    'abortable',
    'requires_init'
]

logger = logging.getLogger(__name__)

# If the overwrite is true then the check for the c-compiler will always return True
INIT_OVERWRITE: bool = False
SEPARATOR = "\\" if WIN else "/"
COMPILER_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
CONFIG_PATH = ""
DEFAULT_CONFIG = {
    "c-compiler-path": ""
}


def c_compiler_initialised() -> bool:
    """ Returns whether the Para-C Compiler is correctly initialised and the c-compiler can be found """
    if INIT_OVERWRITE:
        return True

    global COMPILER_DIR
    COMPILER_DIR = cleanup_path(COMPILER_DIR)
    global CONFIG_PATH
    CONFIG_PATH = f"{COMPILER_DIR}{SEPARATOR}compile-config-examples.json"

    if os.access(CONFIG_PATH, os.R_OK):
        with open(CONFIG_PATH, "r") as file:
            config: dict = json.loads(file.read())
            if config.get('c-compiler-path'):
                # executable
                return os.access(config['c-compiler-path'], os.X_OK)
    return False


def initialise() -> None:
    """ Initialises the Para-C compiler and creates the config-examples file. Will prompt the user to enter the compiler path """
    _input = console().input(
        " [bright_yellow]> [bright_white]Please enter the path for the C-compiler: "
    )
    console().print('')
    path = cleanup_path(decode_if_bytes(_input))

    # exists
    if not os.access(_input, os.X_OK):
        raise CCompilerError(
            f"The passed path '{path}' for the executable does not exist"
        )

    # executable
    if not os.access(_input, os.X_OK):
        raise CCompilerError(
            f"The passed path '{path}' for the executable can't be executed."
            " Possibly missing Permissions?"
        )

    config = DEFAULT_CONFIG
    config['c-compiler-path'] = path
    with open(CONFIG_PATH, "w+") as file:
        file.write(json.dumps(config, indent=4))

    logger.info("Validated path and successfully created compile-config-examples.json")


def abortable(_func=None, *, step: str = "Process"):
    """
    Marks the function as abort-able and adds traceback logging to it.
    If re-raise is False it will exit the program
    """
    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            from .__main__ import abort_banner, log_banner
            try:
                return func(*args, **kwargs)
            except AbortError as e:
                abort_banner(step)
                exit(1)

            except Exception as e:
                from .__main__ import pcompiler
                if not pcompiler.log_initialised:
                    pcompiler.init_logging_session()

                log_banner()
                log_traceback(
                    level="critical",
                    brief="Exception in the compilation setup",
                    exc_info=sys.exc_info()
                )

                raise AbortError(e) from e

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


def requires_init(_func=None):
    """ Checks whether the compiler is initialised before calling the function """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            if not c_compiler_initialised() and not INIT_OVERWRITE:
                console().print('')
                logger.warning(
                    "C-Compiler path is not initialised! If you do not have a working compiler installed, "
                    "please refer to an installation page for your operation system (MinGW, cygwin)"
                )
                logger.info("Initialising Para-C compiler due to missing configuration\n")
                initialise()
                logger.info("Setup may continue\n")
            return func(*args, **kwargs)

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


def deprecated(_func, *, instead=None):
    """ Warns the user about a function or tool that is deprecated and shouldn't be used anymore """

    def _decorator(func):
        @wraps(func)
        def _decorated(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)  # turn off filter
            if instead:
                fmt = "{0.__name__} is deprecated, use {1} instead."
            else:
                fmt = '{0.__name__} is deprecated.'

            warnings.warn(fmt.format(func, instead), stacklevel=3, category=DeprecationWarning)
            warnings.simplefilter('default', DeprecationWarning)  # reset filter
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
