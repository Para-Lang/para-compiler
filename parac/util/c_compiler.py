# coding=utf-8
""" C-compiler functions for managing the c compiler """
import json
import logging
import os


__all__ = [
    "is_c_compiler_ready",
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

    if os.access(const.BIN_CONFIG_PATH, os.R_OK):
        with open(const.BIN_CONFIG_PATH, "r") as file:
            config: dict = json.loads(file.read())
            if config.get('c-compiler-path'):
                # if executable
                return os.access(config['c-compiler-path'], os.X_OK)
    return False
