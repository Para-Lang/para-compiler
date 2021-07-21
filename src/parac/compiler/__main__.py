# coding=utf-8
""" Main file of the Para-Compiler"""
import shutil
import time
import asyncio
from typing import Union, Tuple
import click
import colorama
import logging
import os
from os import PathLike
from rich.progress import Progress

from ..exceptions import InvalidArgumentsError
from ..const import DEFAULT_BUILD_PATH, DEFAULT_DIST_PATH
from ..util import (cli_keep_open_callback, escape_ansi_args,
                    requires_init, is_c_compiler_ready,
                    cli_initialise_c_compiler, abortable)
from ..logging import get_rich_console as console, print_result_banner, \
    cli_create_prompt, cli_format_default, init_rich_console, print_init_banner
from .compiler import ParacCompiler
from .process import ProgramCompilationProcess, BasicProcess, FinishedProcess

__all__ = [
    'para_compiler',
    'create_process',
    'run_output_dir_validation',
    'run_process_with_logging',
    'cli',
    'parac_compile',
    'ParacCLI'
]

logger = logging.getLogger(__name__)
colorama.init(autoreset=True)
para_compiler = ParacCompiler()


@abortable(step="Setup", reraise=True, preserve_exception=True)
def create_process(
        file: Union[str, PathLike],
        encoding: str,
        log_path: Union[str, PathLike],
        build_path: str,
        dist_path: str
) -> ProgramCompilationProcess:
    """
    Creates a compilation process, which can be used for compiling Para-C code
    and returns it.
    Activates logging on default
    """
    if not para_compiler.log_initialised:
        para_compiler.init_logging_session(log_path)

    return ProgramCompilationProcess(file, encoding, build_path, dist_path)


def create_basic_process(
        file: Union[str, PathLike],
        encoding: str,
        log_path: Union[str, PathLike]
) -> BasicProcess:
    """
    Creates a basic process, which can be used for syntax validation and
    returns it.
    Activates logging on default
    """
    if not para_compiler.log_initialised:
        para_compiler.init_logging_session(log_path)

    return BasicProcess(file, encoding)


@abortable(step="Validating Output", reraise=True)
def _err_dir_already_exists(folder: Union[str, PathLike]) -> bool:
    """ Asks the user whether the build folder should be overwritten """
    _input = console().input(
        f"[bright_yellow] > [bright_white]The {folder} "
        "folder already exists. Overwrite data? (y\\N): "
    ).lower() == 'y'
    return _input


def _check_destination(
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
            overwrite = _err_dir_already_exists(output_type)

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


def run_output_dir_validation(
        overwrite_build: bool,
        overwrite_dist: bool
) -> Tuple[str, str]:
    """ Validates whether the output folder /build/ and /dist/ can be used

    :param overwrite_build: If set to True if a build folder already exists
                            it will be deleted and overwritten
    :param overwrite_dist: If set to True if a dist folder already exists
                           it will be deleted and overwritten
    """
    build_path = _check_destination(
        "build",
        DEFAULT_BUILD_PATH,
        overwrite_build
    )
    dist_path = _check_destination(
        "dist",
        DEFAULT_DIST_PATH,
        overwrite_dist
    )
    return build_path, dist_path


async def run_process(p: ProgramCompilationProcess) -> FinishedProcess:
    """
    Runs the process and returns the finished compilation process
    Calls p.compile(), adds additional formatting and returns the result
    """
    finished_process = await p.compile()
    if para_compiler.log_initialised:
        print_result_banner()
    return finished_process


async def run_process_with_logging(
        p: ProgramCompilationProcess
) -> FinishedProcess:
    """ Runs the compilation process with console logs and formatting """
    finished_process = None

    # Some testing for now
    with Progress(console=console(), refresh_per_second=30) as progress:
        max_progress = 100
        current_progress = 0
        main_task = progress.add_task(
            "[green]Processing...",
            total=max_progress
        )

        async for p, status, level, end in \
                await p.compile_with_progress_iterator():
            if end is not None:
                finished_process = end
                progress.update(main_task, advance=p-current_progress)
            else:
                logger.log(level=level, msg=status)
                progress.update(main_task, advance=p-current_progress)
                current_progress = p

    console().print("\n", end="")
    if para_compiler.log_initialised:
        print_result_banner()
    return finished_process


@click.group(invoke_without_command=True)
@click.option("--keep-open", is_flag=True)
@click.option(
    "--version",
    is_flag=True,
    help="Prints the version of the compiler"
)
@click.option(
    "--help",
    is_flag=True,
    help="Show this message and exit."
)
@click.pass_context
@abortable(reraise=False)
def cli(*args, **kwargs):
    """ Console Line Interface for the Para-C Compiler """
    ParacCLI.cli(*args, **kwargs)


@cli.command(name="c-init")
@click.option("--keep-open", is_flag=True)
@abortable(reraise=False)
def parac_c_init(*args, **kwargs):
    """
    Console Line Interface for the configuration of the C-compiler
    """
    ParacCLI.parac_c_init(*args, **kwargs)


@cli.command(name="compile")
@click.option("--keep-open", is_flag=True)
@click.option(
    "-f",
    "--file",
    prompt=cli_create_prompt("Specify the entry-point of your program"),
    default=cli_format_default("entry.para"),
    type=str,
    help="The entry-point of the program where the compiler "
         "should start the compilation process."
)
@click.option(
    "--encoding",
    default="utf-8",
    type=str,
    help="The encoding the files should be opened with"
)
@click.option(
    "-l",
    "--log",
    default=cli_format_default("parac.log"),
    type=str,
    prompt=cli_create_prompt(
        "Specify where the console .log file should be created"
    ),
    help="Path of the output .log file where program messages should be logged"
         ". If set to None it will not use a log file and only use the console"
         " as the output method"
)
@click.option(
    "--overwrite-build",
    is_flag=True,
    type=bool,
    default=False,
    help="If set to True the build folder will always be overwritten "
         "without consideration of pre-existing data"
)
@click.option(
    "--overwrite-dist",
    is_flag=True,
    type=bool,
    default=False,
    help="If flag is set the dist folder will always be overwritten without "
         "consideration of pre-existing data"
)
@click.option(
    "--source/--no-source",
    is_flag=True,
    type=bool,
    default=True,
    help="If flag is set the compiler will compile the code down to native C"
         " (C11). If set with --executable, the executable will be also "
         "generated next the source C code."
)
@click.option(
    "--executable/--no-executable",
    type=bool,
    default=False,
    help="If flag is set the compiler will compile the native C code and "
         "directly generate an executable. If set with --source, the source C"
         "code will be also generated next the executable."
)
@click.option(
    "--debug/--no-debug",
    is_flag=True,
    type=bool,
    default=False,
    help="If set the compiler will add additional debug information"
)
@abortable(reraise=False)
def parac_compile(*args, **kwargs):
    """ Compile a Para-C program to C or executable """
    ParacCLI.parac_compile(*args, **kwargs)


@cli.command(name="run")
@click.option("--keep-open", is_flag=True)
@click.option(
    "-f",
    "--file",
    type=str,
    default=cli_format_default("entry.para"),
    prompt=cli_create_prompt("Specify the entry-point of your program"),
    help="The entry-point of the program where the compiler "
         "should start the compilation process."
)
@click.option(
    "--encoding",
    default="utf-8",
    type=str,
    help="The encoding the files should be opened with"
)
@click.option(
    "-l",
    "--log",
    type=str,
    default=cli_format_default("parac.log"),
    prompt=cli_create_prompt(
        "Specify where the console .log file should be created"),
    help="Path of the output .log file where program messages should be logged"
         ". If set to None it will not use a log file and only use the console"
         " as the output method"
)
@click.option(
    "--overwrite-build",
    is_flag=True,
    type=bool,
    default=False,
    help="If set to True the build folder will always be overwritten without "
         "consideration of pre-existing data"
)
@click.option(
    "--overwrite-dist",
    is_flag=True,
    type=bool,
    default=False,
    help="If flag is set the dist folder will always be overwritten without "
         "consideration of pre-existing data"
)
@click.option(
    "--debug/--no-debug",
    is_flag=True,
    type=bool,
    default=False,
    help="If set the compiler will add additional debug information"
)
@abortable(reraise=False)
def parac_run(*args, **kwargs):
    """
    Compiles a Para-C program and runs it (Creates build and dist as well)
    """
    ParacCLI.parac_run(*args, **kwargs)


@cli.command(name="syntax-check")
@click.option("--keep-open", is_flag=True)
@click.option(
    "-f",
    "--file",
    type=str,
    default=cli_format_default("entry.para"),
    prompt=cli_create_prompt("Specify the entry-point of your program"),
    help="The entry-point of the program where the compiler "
         "should start the compilation process."
)
@click.option(
    "--encoding",
    default="utf-8",
    type=str,
    help="The encoding the files should be opened with"
)
@click.option(
    "-l",
    "--log",
    type=str,
    default=cli_format_default("parac.log"),
    prompt=cli_create_prompt(
        "Specify where the console .log file should be created"),
    help="Path of the output .log file where program messages should be logged"
         ". If set to None it will not use a log file and only use the console"
         " as the output method"
)
@click.option(
    "--debug/--no-debug",
    is_flag=True,
    type=bool,
    default=False,
    help="If set the compiler will add additional debug information"
)
@abortable(reraise=False)
def parac_syntax_check(*args, **kwargs):
    """ Validates the syntax of a Para-C program and logs errors if needed """
    ParacCLI.parac_syntax_check(*args, **kwargs)


class ParacCLI:
    """ CLI for the main Para-C Compiler process """

    @staticmethod
    @abortable(reraise=True)
    @cli_keep_open_callback
    @escape_ansi_args
    def cli(ctx: click.Context, version, *args, **kwargs):
        """
        Main entry point of the cli.
        Either returns version or prints the init_banner of the Compiler
        """
        # If the console was not initialised yet, initialise it
        if console() is None:
            init_rich_console()

        out = console()
        if version:
            from .. import __version__, __title__
            return out.print(' '.join([__title__.title(), __version__]))
        else:
            print_init_banner()
            out.print('')

            # Sleeping to prevent that subcommands sending to stderr
            # causing the banner to be displayed at the end of the output
            time.sleep(.100)

        if not ctx.invoked_subcommand:
            out.print(ctx.get_help())

    @staticmethod
    @abortable(reraise=True)
    @cli_keep_open_callback
    @escape_ansi_args
    def parac_c_init():
        """ Initialises the C compiler """
        if not para_compiler.log_initialised:
            para_compiler.init_logging_session(print_banner=False)
        logger.info(
            'Reinitialising' if is_c_compiler_ready() else 'Initialising'
            " Para-C Compiler"
        )
        cli_initialise_c_compiler()

    @staticmethod
    @abortable(reraise=True)
    @cli_keep_open_callback
    @escape_ansi_args
    def parac_compile(
            file: str,
            encoding: str,
            log: str,
            overwrite_build: bool,
            overwrite_dist: bool,
            source: bool,
            executable: bool,
            debug: bool
    ) -> FinishedProcess:
        """
        CLI interface for the parac_compile command.
        Will create a compilation-process and run it
        """
        if not para_compiler.log_initialised:
            para_compiler.init_logging_session(
                log,
                level=logging.DEBUG if debug else logging.INFO,
            )

        if not source and not executable:
            raise InvalidArgumentsError(
                "--source and --executable can not be both set to False"
            )

        # Validating the output directories and whether they already exist
        # or might contain other content that would be overwritten. If that's
        # the case a prompt will appear asking the user to either answer yes
        # or no to overwriting it. If it's false a new directory with the same
        # name but a number added will be created e.g. build_2
        build_path, dist_path = run_output_dir_validation(
            overwrite_build,
            overwrite_dist
        )

        # Creates a CompilationProcess which represents a process that can
        # be finished but does not need to be finished
        p: ProgramCompilationProcess = abortable(
            create_process,
            step="Setup",
            reraise=True
        )(
            file,
            encoding,
            log,
            build_path,
            dist_path
        )
        # Running the process with additional formatting and logging
        return asyncio.run(run_process_with_logging(p))

    @staticmethod
    @abortable(reraise=True)
    @requires_init
    @cli_keep_open_callback
    @escape_ansi_args
    def parac_run(
            file: str,
            encoding: str,
            log: str,
            overwrite_build: bool,
            overwrite_dist: bool,
            debug: bool
    ) -> None:
        """ CLI interface for compiling and running a program. """
        p = ParacCLI.parac_compile(
            file,
            encoding,
            log,
            overwrite_build,
            overwrite_dist,
            debug
        )
        # TODO! Run the process. Requires GCC Integration

    @staticmethod
    @abortable(reraise=True)
    @cli_keep_open_callback
    @escape_ansi_args
    def parac_syntax_check(
            file: str,
            encoding: str,
            log: str,
            debug: bool
    ):
        """ Runs a syntax check on the specified file (imports excluded) """
        if not para_compiler.log_initialised:
            para_compiler.init_logging_session(
                log,
                level=logging.DEBUG if debug else logging.INFO,
                banner_name="Syntax Check"
            )

        p = create_basic_process(file, encoding, log)

        # Exception won't be reraised and directly logged to the console
        result = asyncio.run(p.validate_syntax(enable_out=True))

        errors = para_compiler.stream_handler.errors
        warnings = para_compiler.stream_handler.warnings
        if result is True:
            print_result_banner("Syntax Check")
            logger.info(
                "[bold bright_cyan]"
                "Syntax check finished successfully"
                "[/bold bright_cyan]"
            )
        else:
            print_result_banner("Syntax Check", success=False)
            logger.info(
                "[bold yellow]"
                "Syntax check detected "
                f"{'an error' if errors == 1 else 'multiple errors' }"
                "[/bold yellow]"
            )

        logger.info(
            "[bold yellow]"
            f"Warnings: {warnings}"
            "[/bold yellow]"
        )
        logger.info(
            "[bold red]"
            f"Errors: {errors}"
            "[/bold red]"
        )
