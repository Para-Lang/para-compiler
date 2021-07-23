# coding=utf-8
""" Utility for the parac_cli module """
import os
import shutil
from os import PathLike
from pathlib import Path
from typing import Union, Tuple

from parac import DEFAULT_BUILD_PATH, DEFAULT_DIST_PATH, UserInputError
from parac.util import abortable, decode_if_bytes
from parac.logging import get_rich_console as console

__all__ = [
    "cli_err_dir_already_exists",
    "cli_run_output_dir_validation",
    "cli_check_destination",
    "cli_resolve_path"
]


def cli_resolve_path(path: Union[bytes, str, Path, PathLike]) -> str:
    """
    If the path is a pathlib.Path it will resolve it, including all symlinks
    and return it as a string, else it will be passed through decode_if_bytes,
    made to a pathlib.Path to resolve all symlinks and then returned as a
    string

    :raise UserInputError: If the inserted path can not be resolved due to an
    invalid format
    """
    if str(path.strip()) == "":
        raise UserInputError("Path can not be empty")
    if type(path) in (bytes, str, PathLike):
        try:
            path = Path(decode_if_bytes(path))
        # pathlib.Path raised error -> Invalid path
        except Exception as e:
            raise UserInputError("Path is in an invalid format") from e
    return str(path.resolve())


@abortable(step="Validating Output", reraise=True)
def cli_err_dir_already_exists(folder: Union[str, PathLike]) -> bool:
    """ Asks the user whether the build folder should be overwritten """
    _input = console().input(
        f"[bright_yellow] > [bright_white]The {folder} "
        "folder already exists. Overwrite data? (y\\N): "
    ).lower() == 'y'
    return _input


def cli_check_destination(
        output_type: str,
        default_path: Union[str, PathLike],
        overwrite: bool
) -> str:
    """
    Validates the destination and checks whether the specified output
    folder is available. If the folder already exists it will show a prompt
    to the user what should be done about the existing folder.

    :returns: The path to the folder
    """
    output = default_path
    if not os.path.exists(default_path):
        os.mkdir(default_path)
    elif len(os.listdir(default_path)) > 0:
        # If the overwrite is set to False then a prompt will appear
        if overwrite is False:
            overwrite = cli_err_dir_already_exists(output_type)

        if overwrite:
            shutil.rmtree(default_path)
            os.mkdir(default_path)
        else:
            counter = 2
            while os.path.exists(f"{os.getcwd()}/{output_type}_{counter}"):
                counter += 1
            output = f"{os.getcwd()}/{output_type}_{counter}"
            os.mkdir(output)
    return output


def cli_run_output_dir_validation(
        overwrite_build: bool,
        overwrite_dist: bool
) -> Tuple[str, str]:
    """ Validates whether the output folder /build/ and /dist/ can be used

    :param overwrite_build: If set to True if a build folder already exists
    it will be deleted and overwritten
    :param overwrite_dist: If set to True if a dist folder already exists
    it will be deleted and overwritten
    """
    build_path = cli_check_destination(
        "build",
        DEFAULT_BUILD_PATH,
        overwrite_build
    )
    dist_path = cli_check_destination(
        "dist",
        DEFAULT_DIST_PATH,
        overwrite_dist
    )
    return build_path, dist_path
