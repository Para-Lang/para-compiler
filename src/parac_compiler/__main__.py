""" Main file of the Para-Compiler"""
import click
import logging
import pyfiglet

from . import __version__, log_msg

logger = logging.getLogger(__name__)


def init_screen() -> None:
    """ 'Initialises' the compiler and logs a message """
    click.secho(f"\nPara-C Compiler v{__version__} Pre-Release\n", fg='white', bold=True)


@click.command()
@click.option(
    '--file',
    prompt='Specify the entry-point of your program (path)',
    help='The entry-point of the program where the compiler should start the compilation process.'
)
@click.option(
    '--output',
    default='parac.log',
    prompt='Specify where the console .log file should be created (path):',
    help='Path of the output .log file where the compilation process is logged. If None or False it will not generate '
         'any output.'
)
def run(file, output) -> None:
    """ Basic cli run command for running the main compiler """
    log_output = output == "None" or output == "False"
