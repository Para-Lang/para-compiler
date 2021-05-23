# coding=utf-8
""" Main file of the Para-Compiler"""
import shutil
import time
import click
import colorama
import logging
import os
from os import PathLike
from sys import exit
from rich.progress import Progress
from typing import Tuple, Union, Literal

from . import __version__, __title__
from .compiler import CompilationProcess, FinishedProcess, ParacCompiler, DEFAULT_BUILD_PATH, DEFAULT_DIST_PATH
from .logger import output_console as console, ansi_col
from .utils import c_compiler_initialised, initialise, abortable, requires_init

__all__ = [
    'compiler',
    'create_process',
    'run_output_dir_validation',
    'run_process_with_logging',
    'cli',
    'parac_compile',
    'ParacCLI',
    'error_banner',
    'log_banner',
    'finish_banner'
]

logger = logging.getLogger(__name__)
colorama.init(autoreset=True)
compiler = ParacCompiler()
log_banner_used = False


@abortable(reraise=True, step="Setup")
def create_process(
        file: str,
        log_path: str,
        build_path: str,
        dist_path: str,
        level: Union[Literal[50, 40, 30, 20, 10], int]
) -> CompilationProcess:
    """ Creates a compilation process and returns it """
    compiler.init_logging_session(log_path, level)
    log_banner()
    p = CompilationProcess.create_from_args(file, build_path, dist_path)
    return p


def init_banner() -> None:
    """ Creates the init screen string that can be printed """
    base_str = f"Para-C Compiler{' ' * 5}"

    console.rule(style="white rule.line")
    console.print(
        f"[bold bright_white]{base_str}[/bold bright_white][bold cyan]{__version__}[/bold cyan]",
        justify="center"
    )
    console.rule(style="white rule.line")


def error_banner(process: str) -> None:
    """ Prints a simple colored Exception banner showing it crashed / was aborted """
    console.rule(f"\n[bold red]Aborted {process}[/bold red]\n", style="red rule.line")


def finish_banner() -> None:
    """ Prints a simple colored banner screen showing it succeeded and finished """
    console.rule(f"\n[bold green]Finished Compilation[/bold green]\n", style="green rule.line")


def log_banner() -> None:
    """ Prints a simple colored banner screen showing the logs are active and the process started """
    # Avoiding the log_banner is displayed twice
    global log_banner_used
    if log_banner_used:
        return
    console.rule(f"\n[bold cyan]Compiler Logs[white]\n", style="white rule.line")
    log_banner_used = True


def _create_prompt(string: str) -> str:
    """Creates a colored prompt for a click.prompt() call (Uses ansi instead of rich because of compatibility issues)"""
    return f'{ansi_col.cyan} > {ansi_col.bright_white}{string}'


@abortable
def _dir_already_exists(folder: str) -> bool:
    """ Asks the user whether the build folder should be overwritten """
    _input = console.input(
        f"[bright_yellow] > [bright_white]The {folder} folder already exists. Overwrite data? (y\\N): "
    ).lower() == 'y'
    return _input


def _validate_output(output_type: str, default_path: Union[str, PathLike], overwrite: bool) -> str:
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
            while os.path.exists(f"{os.getcwd()}/{output_type}_{counter}"):
                counter += 1
            output = f"{os.getcwd()}/{output_type}_{counter}"
            os.mkdir(output)
    return output


def run_output_dir_validation(overwrite_build: bool, overwrite_dist: bool) -> Tuple[str, str]:
    """ Validates whether the output folder /build/ and /dist/ can be used

    :param overwrite_build: If set to True if a build folder already exists it will be deleted and overwritten
    :param overwrite_dist: If set to True if a dist folder already exists it will be deleted and overwritten
    """
    build_path = _validate_output("build", DEFAULT_BUILD_PATH, overwrite_build)
    dist_path = _validate_output("dist", DEFAULT_DIST_PATH, overwrite_dist)
    return build_path, dist_path


def run_process_with_logging(p: CompilationProcess) -> FinishedProcess:
    """ Runs the compilation process with console logs and formatting """
    # Some testing for now
    with Progress(console=console, refresh_per_second=30) as progress:
        main_task = progress.add_task("[green]Processing...", total=100)

        logger.info(f"Entry-Point: {p.entry_file}")
        progress.update(main_task, advance=50)
        time.sleep(1)
        logger.info("Fetching files...")

        time.sleep(1)
        progress.update(main_task, advance=100)

    finish_banner()
    return FinishedProcess(p)


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
def cli(*args, **kwargs):
    """ Console Line Interface for the Para-C Compiler """
    ParacCLI.cli(*args, **kwargs)


@cli.command(name='init')
def parac_init():
    """ Console Line Interface for the Initialisation of the Para-C compiler and the configuration of the c-compiler """
    ParacCLI.parac_init()


@cli.command(name='compile')
@click.option(
    '-f',
    '--file',
    prompt=_create_prompt('Specify the entry-point of your program'),
    default='main.para',
    type=str,
    help='The entry-point of the program where the compiler should start the compilation process.'
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
def parac_compile(*args, **kwargs):
    """ Compile a Para-C program to C or executable """
    ParacCLI.parac_compile(*args, **kwargs)


@cli.command(name='run')
@click.option(
    '-f',
    '--file',
    prompt=_create_prompt('Specify the entry-point of your program'),
    default='main.para',
    type=str,
    help='The entry-point of the program where the compiler should start the compilation process.'
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
def parac_run(*args, **kwargs):
    """ Compile a Para-C program and runs it """
    ParacCLI.parac_run(*args, **kwargs)


class ParacCLI:
    """ CLI for the main Para-C Compiler process """

    @staticmethod
    @abortable
    def cli(ctx: click.Context, version, *args, **kwargs):
        """ Main entry point of the cli. Either returns version or prints the init_banner of the Compiler """
        compiler.init_logging_session()  # Creating simple console logging without a file handler
        if version:
            click.echo(' '.join([__title__.title(), __version__]))
            exit()
        else:
            init_banner()
            click.echo('')

        if not ctx.invoked_subcommand:
            click.echo(ctx.get_help())

    @staticmethod
    @abortable
    def parac_init():
        """ Initialises the Para-C compiler """
        logger.info(f"{'Reinitialising' if c_compiler_initialised() else 'Initialising'} Para-C Compiler")
        initialise()

    @staticmethod
    @abortable
    @requires_init
    def parac_compile(
            file: str,
            log: str,
            overwrite_build: bool,
            overwrite_dist: bool,
            debug: bool
    ) -> FinishedProcess:
        """ CLI interface for the parac_compile command. Will create a compilation-process and run it """
        build_path, dist_path = run_output_dir_validation(overwrite_build, overwrite_dist)

        p: CompilationProcess = abortable(create_process, step="Setup")(
            file, log, build_path, dist_path, logging.DEBUG if debug else logging.INFO
        )
        return run_process_with_logging(p)

    @staticmethod
    @abortable
    @requires_init
    def parac_run(
            file: str,
            log: str,
            overwrite_build: bool,
            overwrite_dist: bool,
            debug: bool
    ) -> None:
        """ CLI interface for compiling and running a program. """
        p = ParacCLI.parac_compile(file, log, overwrite_build, overwrite_dist, debug)
        # TODO! Run the process. Requires GCC Integration
