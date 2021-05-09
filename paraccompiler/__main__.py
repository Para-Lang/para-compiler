""" Main file of the Para-Compiler"""
import shutil
import sys
import click
import logging
import os
from typing import Tuple, Dict

from . import __version__, log_msg, log_traceback, FileWritingPermissionError

logger = logging.getLogger(__name__)


def main() -> None:
    """ Main function for running the core compiler setup and compilation process """
    click.secho(f"\nPara-C Compiler v{__version__} Pre-Release\n", fg='white', bold=True)
    compiler = ParacCompiler()
    try:
        file, build_path, dist_path, args = setup()
    except Exception:
        log_traceback(
            brief=f"Exception in the compilation setup:",
            exc_info=sys.exc_info()
        )
        return log_msg('critical', "Aborting setup")
    compiler.compile_from_entry_file(file, build_path, dist_path)


def _dir_already_exists(folder: str) -> bool:
    """ Asks the user whether the build folder should be overwritten """
    _input = input(f"The {folder} folder already exists. Overwrite data? [True]: ")
    if _input == "":
        _input = "True"
    return _input.lower() == 'true'


def _validate_output(output_type: str, overwrite: bool) -> str:
    """
    Validates the Output-type and checks whether the specified output folder is available. If the folder already exists
    it will show a prompt to the user what should be done about the existing folder.
    """
    output = f"./{output_type}/"
    if not os.path.exists(output):
        os.mkdir(output)
    elif len(os.listdir(output)) > 0:
        # If the overwrite is set to False then a prompt will appear
        if overwrite is False:
            overwrite = _dir_already_exists(output_type)

        if overwrite:
            shutil.rmtree(output)
            os.mkdir(output)
        else:
            counter = 2
            while os.path.exists(f"./{output_type}_{counter}"):
                counter += 1
            output = f"./{output_type}_{counter}"
            os.mkdir(output)
    return output


@click.command()
@click.option(
    '--file',
    prompt='Specify the entry-point of your program',
    default='main.para',
    help='The entry-point of the program where the compiler should start the compilation process.'
)
@click.option(
    '--log',
    default='parac.log',
    prompt='Specify where the console .log file should be created',
    help='Path of the output .log file where program messages should be logged. '
         'If set to None it will not use a log file and only use the console as the output method'
)
@click.option(
    '--overwrite-build',
    default='False',
    help='If set to True the build folder will always be overwritten without consideration of pre-existing data'
)
@click.option(
    '--overwrite-dist',
    default='False',
    help='If set to True the dist folder will always be overwritten without consideration of pre-existing data'
)
def setup(file, log, overwrite_build, overwrite_dist):
    """ Para-C compiler which takes in .para files and compiles them to C or binary (executable)"""
    return ParacCompiler.validate_setup(file, log, overwrite_build == 'True', overwrite_dist == 'True')


class ParacCompiler:
    """ Main Class for the Para-C compiler containing the main functions """
    @staticmethod
    def validate_setup(
            entry_file: str,
            log_path: str,
            overwrite_build: bool,
            overwrite_dist: bool
    ) -> Tuple[str, str, str, Dict]:
        """
        Validates the provided setup parameter for the compilation process. In case of an error an
        exception will be raised and the process cancelled.

        :param entry_file: The entry-file of the program
        :param log_path: Path of the .log file were the logging module will output program messages. If set to None it
                         will not use a log file and only use the console as the output method
        :param overwrite_build: If set to true the build folder will be overwritten if it already exists
        :param overwrite_dist: If set to true the dist folder will be overwritten if it already exists
        :returns: The file name, the output build path, the output dist path and the arguments passed for the
                  compilation
        """
        _logger = logging.getLogger("paraccompiler")
        _logger.setLevel(logging.DEBUG)

        if log_path.lower() != 'none':
            if os.path.exists(log_path):
                raise FileWritingPermissionError(
                    "Failed to access the specified log file-path. Path already exists"
                )
            try:
                handler = logging.FileHandler(filename=f'./{log_path}', encoding='utf-8', mode='w')
            except PermissionError:
                raise FileWritingPermissionError("Failed to access the specified log file-path")
            handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
            _logger.addHandler(handler)

        build_output = _validate_output("build", overwrite_build)
        dist_output = _validate_output("dist", overwrite_dist)

        if not any([item in entry_file for item in ['\\', '/', '//']]):
            path = f"{os.getcwd()}\\{entry_file}"
        else:
            path = entry_file
        if not os.path.exists(path):
            raise FileNotFoundError(f"Failed to read file/path '{path}'! File does not exist!")

        return entry_file, build_output, dist_output, {}

    def compile_from_entry_file(self, file: str, build_path: str, dist_path: str):
        """ Compiles the specified entry-point file

        :param file: The file that should serve as the entry-point of the program where all files are imported
                     relatively and name_mangling is applied
        :param build_path: The build folder path where all compilation files should be placed
        :param dist_path: The dist folder path where all compilation files and distribution-ready should be placed
        """
        ...
