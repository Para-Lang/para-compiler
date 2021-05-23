# coding=utf-8
""" Utility in the Para-C Compiler"""
import json
import logging
import sys
import warnings
import os
from os import PathLike
from typing import Union, Type
from functools import wraps

from . import WIN
from .exceptions import CCompilerError
from .logger import output_console as console

__all__ = [
    'INIT_OVERWRITE',
    'SEPARATOR',
    'COMPILER_DIR',
    'c_compiler_initialised',
    'initialise',
    'deprecated',
    'decode_if_bytes',
    'cleanup_path'
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
    CONFIG_PATH = f"{COMPILER_DIR}{SEPARATOR}compile-config.json"

    if os.access(CONFIG_PATH, os.R_OK):
        with open(CONFIG_PATH, "r") as file:
            config: dict = json.loads(file.read())
            if config.get('c-compiler-path'):
                # executable
                return os.access(config['c-compiler-path'], os.X_OK)
    return False


def initialise() -> None:
    """ Initialises the Para-C compiler and creates the config file. Will prompt the user to enter the compiler path """
    logger.info("Initialising Para-C compiler due to missing configuration\n")
    _input = console.input(
        f" [bright_red]> [bright_white]Please enter the path for the C-compiler: "
    )
    path = cleanup_path(decode_if_bytes(_input))

    # exists
    if not os.access(_input, os.X_OK):
        raise CCompilerError(f"The passed path '{path}' for the executable does not exist")

    # executable
    if not os.access(_input, os.X_OK):
        raise CCompilerError(
            f"The passed path '{path}' for the executable can't be executed. Possibly missing Permissions?"
        )

    config = DEFAULT_CONFIG
    config['c-compiler-path'] = path
    with open(CONFIG_PATH, "w+") as file:
        file.write(json.dumps(config, indent=4))

    logger.info("Validated path and successfully created compile-config.json. Setup may continue\n")


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
