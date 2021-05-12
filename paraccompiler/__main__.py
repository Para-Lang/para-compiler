""" Main file of the Para-Compiler"""
import shutil
import sys
import click
import colorama
import logging
import os
import re
from sys import exit

from . import __version__, __title__, log_msg, log_traceback, AbortError
from .logger import tcol
from .compiler import CompilationProcess, ParacCompiler, DEFAULT_BUILD_PATH, DEFAULT_DIST_PATH

__all__ = [
    'create_process',
    'cli',
    'parac_compile'
]

logger = logging.getLogger(__name__)
colorama.init(autoreset=True)


def create_process(file: str, log_path: str, build_path: str, dist_path: str, level: int) -> CompilationProcess:
    """ Creates a compilation process and returns it """
    compiler = ParacCompiler()
    try:
        compiler.init_logging_session(log_path, level)
        click.echo(log_separator())
        p = CompilationProcess.create_from_args(file, build_path, dist_path)
    except Exception as e:
        if not compiler.log_initialised:
            compiler.init_logging_session("./para.log", logging.INFO)
        log_traceback(
            brief=f"Exception in the compilation setup",
            exc_info=sys.exc_info()
        )
        log_msg('critical', f"Aborting setup {f'with error_code {e.code}' if hasattr(e, 'code') else ''}")
        raise AbortError()
    else:
        return p


def init_banner() -> str:
    """ Creates the init screen string that can be printed """
    base_str = f"Para-C Compiler{' ' * 30}"
    append_str = ''.join((tcol.white, "-" * (len(base_str) + len(__version__)), tcol.reset))

    return '\n'.join((
        append_str,
        f"{tcol.make_bold(tcol.bright_white)}{base_str}{tcol.cyan}{__version__}{tcol.reset}",
        append_str
    ))


def log_separator() -> str:
    """ Creates the start log string that can be printed"""
    return f"\n{tcol.white}{'-' * 25} {tcol.cyan}Compiling logs{tcol.white} {'-' * 25}{tcol.reset}\n"


def _create_prompt(string: str) -> str:
    """ Creates a colored prompt for a click.prompt() call """
    return f'{tcol.cyan} > {tcol.bright_white}{string}'


def _dir_already_exists(folder: str) -> bool:
    """ Asks the user whether the build folder should be overwritten """
    try:
        _input = click.confirm(
            f"{tcol.bright_yellow} > {tcol.bright_white}The {folder} folder already exists. Overwrite data?"
        )
    except click.Abort:
        raise AbortError()
    except Exception as e:
        raise RuntimeError("Failed to process input") from e
    return _input


def _validate_output(output_type: str, default_path: str, overwrite: bool) -> str:
    """ Validates the Output-type and checks whether the specified output folder is available.
    If the folder already exists it will show a prompt to the user what should be done about the existing folder.

    :returns: The path to the folder
    """
    output = default_path
    if not os.path.exists(default_path):
        os.mkdir(default_path)
    elif len(os.listdir(default_path)) > 0:
        # If the overwrite is set to False then a prompt will appear
        if overwrite is False:
            overwrite = _dir_already_exists(output_type)

        if overwrite:
            shutil.rmtree(default_path)
            os.mkdir(default_path)
        else:
            counter = 2
            while os.path.exists(f"./{output_type}_{counter}"):
                counter += 1
            output = f"./{output_type}_{counter}"
            os.mkdir(output)
    return output


def _file_autocomplete(ctx, args, incomplete):
    file_match_re = r'^(?:[a-zA-Z]:)?[/\\]{0,2}(?:[./\\ ]{0,2}(?![/\\\n]|[.]{2})|[^<>:"|?*/\\ \n])+$'
    if incomplete.endswith('.para'):
        return []
    elif os.path.exists(incomplete) or os.path.exists(f'./{incomplete}'):
        return []
    elif not re.match(file_match_re, incomplete):
        return []

    return [f for f in os.listdir('.') if f.startswith(incomplete) and (f.endswith('.para') or f.endswith('.ph'))]


@click.group(invoke_without_command=True)
@click.option(
    '--version',
    is_flag=True,
    help='Prints the version of the compiler'
)
@click.option(
    '--help',
    is_flag=True,
    help='Prints this screen'
)
@click.pass_context
def cli(ctx: click.Context, version, **kwargs):
    """ Console Line Interface for the Para-C Compiler """
    if version:
        click.echo(' '.join([__title__.title(), __version__]))
        exit()
    else:
        click.echo(init_banner())
        click.echo('')

    if not ctx.invoked_subcommand:
        click.echo(ctx.get_help())


@cli.command(name='compile')
@click.option(
    '-f',
    '--file',
    prompt=_create_prompt('Specify the entry-point of your program'),
    default='main.para',
    type=str,
    help='The entry-point of the program where the compiler should start the compilation process.',
    autocompletion=_file_autocomplete
)
@click.option(
    '-l',
    '--log',
    default='parac.log',
    type=str,
    prompt=_create_prompt('Specify where the console .log file should be created'),
    help='Path of the output .log file where program messages should be logged. '
         'If set to None it will not use a log file and only use the console as the output method'
)
@click.option(
    '--overwrite-build',
    is_flag=True,
    type=bool,
    default=False,
    help='If set to True the build folder will always be overwritten without consideration of pre-existing data'
)
@click.option(
    '--overwrite-dist',
    is_flag=True,
    type=bool,
    default=False,
    help='If set to True the dist folder will always be overwritten without consideration of pre-existing data'
)
@click.option(
    '--debug/--no-debug',
    is_flag=True,
    default=False,
    help='If set the compiler will add additional debug information'
)
def parac_compile(
        file: str,
        log: str,
        overwrite_build: bool,
        overwrite_dist: bool,
        debug: bool
) -> None:
    """ Compile a Para-C program to C or executable """
    build_path = _validate_output("build", DEFAULT_BUILD_PATH, overwrite_build)
    dist_path = _validate_output("dist", DEFAULT_DIST_PATH, overwrite_dist)

    try:
        p = create_process(
            file, log, build_path, dist_path, logging.DEBUG if debug else logging.INFO
        )
    except AbortError:
        exit()
    click.echo(log_separator())
