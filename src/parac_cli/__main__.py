# coding=utf-8
""" Main file of the Para-Compiler"""
import time
import asyncio
from pathlib import Path
from typing import Union
import click
import colorama
import logging
from os import PathLike
from rich.progress import Progress

from parac import RUNTIME_COMPILER
from parac.exceptions import InvalidArgumentsError
from parac.util import (cli_keep_open_callback, escape_ansi_args,
                        requires_init, is_c_compiler_ready,
                        cli_initialise_c_compiler, abortable)
from parac.logging import (get_rich_console as console, print_result_banner,
                           cli_create_prompt, cli_format_default,
                           init_rich_console, print_init_banner)
from parac.compiler import (ProgramCompilationProcess,
                            BasicProcess, FinishedProcess)
from .utils import cli_run_output_dir_validation, cli_resolve_path

__all__ = [
    'cli_create_process',
    'cli_run_output_dir_validation',
    'cli_run_process_with_logging',
    'cli_entry',
    'cli_parac_compile',
    'ParacCLI'
]

logger = logging.getLogger(__name__)
colorama.init(autoreset=True)


@abortable(step="Setup", reraise=True, preserve_exception=True)
def cli_create_process(
        file: Union[str, PathLike, Path],
        encoding: str,
        log_path: Union[str, PathLike, Path],
        build_path: Union[str, PathLike, Path],
        dist_path: Union[str, PathLike, Path]
) -> ProgramCompilationProcess:
    """
    Creates a compilation process, which can be used for compiling Para-C code
    and returns it.
    Activates logging on default
    """
    if not RUNTIME_COMPILER.log_initialised:
        RUNTIME_COMPILER.init_logging_session(log_path)

    # Resolving path and stripping whitespaces
    file: str = cli_resolve_path(file).strip()
    build_path: str = cli_resolve_path(build_path).strip()
    dist_path: str = cli_resolve_path(dist_path).strip()
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
    if not RUNTIME_COMPILER.log_initialised:
        RUNTIME_COMPILER.init_logging_session(log_path)

    return BasicProcess(file, encoding)


async def run_process(p: ProgramCompilationProcess) -> FinishedProcess:
    """
    Runs the process and returns the finished compilation process
    Calls p.compile(), adds additional formatting and returns the result
    """
    finished_process = await p.compile()
    if RUNTIME_COMPILER.log_initialised:
        print_result_banner()
    return finished_process


async def cli_run_process_with_logging(
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
    if RUNTIME_COMPILER.log_initialised:
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
def cli_entry(*args, **kwargs):
    """
    Console Line Interface for the Para-C Compiler
    \f
    Entry point for the CLI. This should be called when wanting to start the
    cli. It will utilise the args passed to the program as the click arguments
    """
    ParacCLI.cli(*args, **kwargs)


@cli_entry.command(name="c-init")
@click.option("--keep-open", is_flag=True)
@abortable(reraise=False)
def parac_c_init(*args, **kwargs):
    """
    Console Line Interface for the configuration of the C-compiler
    """
    ParacCLI.parac_c_init(*args, **kwargs)


@cli_entry.command(name="compile")
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
    default=cli_format_default("./parac.log"),
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
def cli_parac_compile(*args, **kwargs):
    """ Compile a Para-C program to C or executable """
    ParacCLI.parac_compile(*args, **kwargs)


@cli_entry.command(name="run")
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
    default=cli_format_default("./parac.log"),
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


@cli_entry.command(name="syntax-check")
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
    default=cli_format_default("./parac.log"),
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
            from parac import __version__, __title__
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
        if not RUNTIME_COMPILER.log_initialised:
            RUNTIME_COMPILER.init_logging_session(print_banner=False)
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
        if not RUNTIME_COMPILER.log_initialised:
            RUNTIME_COMPILER.init_logging_session(
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
        build_path, dist_path = cli_run_output_dir_validation(
            overwrite_build,
            overwrite_dist
        )

        # Creates a CompilationProcess which represents a process that can
        # be finished but does not need to be finished
        p: ProgramCompilationProcess = abortable(
            cli_create_process,
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
        return asyncio.run(cli_run_process_with_logging(p))

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
        if not RUNTIME_COMPILER.log_initialised:
            RUNTIME_COMPILER.init_logging_session(
                log,
                level=logging.DEBUG if debug else logging.INFO,
                banner_name="Syntax Check"
            )

        p = create_basic_process(file, encoding, log)

        # Exception won't be reraised and directly logged to the console
        result = asyncio.run(p.validate_syntax(enable_out=True))

        errors = RUNTIME_COMPILER.stream_handler.errors
        warnings = RUNTIME_COMPILER.stream_handler.warnings
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
