# coding=utf-8
""" C-compiler functions for managing the c compiler """
import json
import os
import logging
from pathlib import Path

from .pathtools import decode_if_bytes, ensure_pathlib_path
from ..exceptions import FilePermissionError, CCompilerNotFoundError
from ..logging import get_rich_console as console

__all__ = [
    "is_c_compiler_ready",
    "cli_initialise_c_compiler"
]

logger = logging.getLogger(__name__)


def is_c_compiler_ready() -> bool:
    """
    Returns whether the Para-C Compiler is correctly
    initialised and the c-compiler can be found
    """
    from .. import const
    if const.C_COM_EXISTENCE_OVERWRITE:
        return True

    if os.access(const.CONFIG_PATH, os.R_OK):
        with open(const.CONFIG_PATH, "r") as file:
            config: dict = json.loads(file.read())
            if config.get('c-compiler-path'):
                # if executable
                return os.access(config['c-compiler-path'], os.X_OK)
    return False


def cli_initialise_c_compiler() -> None:
    """
    Initialises the Para-C compiler and creates the config file.
    Will prompt the user to enter the compiler path
    """
    from .. import const
    _input = console().input(
        "[bold bright_cyan]"
        " > Please enter the path for the C-compiler: "
        "[/bold bright_cyan]"
    )
    console().print('\n', end="")
    path: Path = ensure_pathlib_path(_input)

    # it exists
    if not os.access(path, os.F_OK):
        raise CCompilerNotFoundError(
            f"The passed path '{path}' for the executable does not exist"
        )

    # is executable
    if not os.access(path, os.X_OK):
        raise FilePermissionError(
            f"The passed path '{path}' for the executable can't be executed."
            " Possibly missing Permissions?"
        )

    config = const.DEFAULT_CONFIG
    config['c-compiler-path'] = str(path)

    with open(const.CONFIG_PATH, "w+") as file:
        file.write(json.dumps(config, indent=4))

    logger.info(
        "Validated path and successfully created compiler-config.json"
    )
