# coding=utf-8
""" Logger management file for formatting and specific exception and  """
import logging
import os
import shutil
import sys
import traceback
from logging import StreamHandler

from antlr4.error.ErrorListener import ErrorListener
from rich.console import Console
from typing import Optional, Callable, Tuple, Type, Union, Literal
from types import FunctionType, TracebackType

from rich.theme import Theme

from . import __version__

__all__ = [
    'AVOID_PRINT_BANNER_OVERWRITE',
    'set_avoid_print_banner_overwrite',
    'custom_theme',
    'ParacErrorListener',
    'ParacStreamHandler',
    'ParacFileHandler',
    'ParacFormatter',
    'output_console',
    'init_rich_console',
    'get_rich_console',
    'log_traceback',
    'log_msg',
    'ansi_col',
    'print_init_banner',
    'print_abort_banner',
    'print_log_banner',
    'print_finish_banner',
    'create_prompt',
    'format_default'
]

# If this is set to True no banners will be printed and instead only newlines
AVOID_PRINT_BANNER_OVERWRITE: bool = False
output_console: Optional[Console] = None
custom_theme = Theme({
    "info": "white",
    "warning": "bright_yellow",
    "error": "bold red",
    "critical": "bold bright_red",
    "repr.number": "bold bright_cyan"
})


def set_avoid_print_banner_overwrite(value: bool):
    """
    Sets the AVOID_PRINT_BANNER_OVERWRITE, which if True removes all banner
    printing
    """
    global AVOID_PRINT_BANNER_OVERWRITE
    AVOID_PRINT_BANNER_OVERWRITE = value


def get_terminal_size() -> Optional[int]:
    """ Gets the terminal size """
    from . import WIN
    width: Optional[int] = None
    if "PYCHARM_HOSTED" in os.environ:
        width = 150
    elif WIN:  # pragma: no cover
        width, _ = shutil.get_terminal_size()
    else:
        try:
            width, _ = os.get_terminal_size(sys.stdin.fileno())
        except (AttributeError, ValueError, OSError):
            try:
                width, _ = os.get_terminal_size(sys.stdout.fileno())
            except (AttributeError, ValueError, OSError):
                pass

    if width is None or width < 120:
        return 120
    else:
        return width


def _get_color_system() -> Union[Literal["windows", "auto"], str]:
    from . import WIN
    return "windows" if WIN else "auto"


def init_rich_console() -> None:
    """ Initialises the rich console used for special console formatting """

    global output_console
    output_console = Console(
        width=get_terminal_size(),
        color_system=_get_color_system(),
        theme=custom_theme
    )


def get_rich_console() -> Union[Console, None]:
    """
    Returns the output console which can be undefined if not initialised.
    This function is used instead of direct variable accessing to avoid the
    case that the console is initialised but the import still returns None.
    Therefore this function will return the local object and it should always
    return the object if it's initialised
    """
    return output_console


class ParacStreamHandler(StreamHandler):
    """ Specific Stream Handler for Para-C designed to implement rich """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def console(self) -> Union[Console, None]:
        """ Fetches the Console if it is initialised """
        return get_rich_console()

    def emit(self, record):
        """
        Emit a record using rich and the set implementation

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.  If
        exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        try:
            msg = self.format(record)
            # Writing with the rich print method which implements
            # its own stream-handling
            self.console.print(msg, highlight=False, justify="left")
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)


logger = logging.getLogger(__name__)


class ParacFileHandler(logging.FileHandler):
    """ Default FileHandler for the file handling in the Para-C compiler """
    def __init__(
            self,
            filename='./parac.log',
            encoding='utf-8',
            mode='w',
            *args,
            **kwargs
    ):
        super().__init__(
            filename=filename,
            encoding=encoding,
            mode=mode,
            *args,
            **kwargs
        )


class ParacFormatter(logging.Formatter):
    """
    Default Formatter class for the custom formatted output of the
    Para-C compiler
    """
    level_formatting = {
        logging.CRITICAL: ''.join([
            '[bold bright_red bold]'
            '[%(levelname)s] - (%(asctime)s): %(message)s'
            '[/bold bright_red]'
        ]),
        logging.ERROR: ''.join([
            '[bold red bold]'
            '[%(levelname)s] - (%(asctime)s):'
            '[/bold red]'
            '[red] %(message)s[/red]'
        ]),
        logging.WARNING: ''.join([
            '[bold bright_yellow]'
            '[%(levelname)s] - (%(asctime)s):'
            '[/bold bright_yellow]',
            '[bright_yellow] %(message)s[/bright_yellow]'
        ]),
        logging.DEBUG: ''.join([
            '[bold yellow]'
            '[%(levelname)s] - (%(asctime)s):'
            '[/bold yellow]'
            '[yellow] %(message)s[/yellow]'
        ]),
        logging.INFO: ''.join([
            '[bold bright_cyan]'
            '[%(levelname)s] - (%(asctime)s):'
            '[/bold bright_cyan]',
            '[bright_cyan] %(message)s[/bright_cyan]'
        ])
    }

    default = '[%(levelname)s] - (%(asctime)s): %(message)s'

    def __init__(
            self,
            file_mng: bool = False,
            fmt: Optional[str] = default,
            *args,
            **kwargs
    ):
        self.file_mng = file_mng
        super().__init__(fmt=fmt, *args, **kwargs)

    def format(self, record):
        """
        Class specific formatter function to add colouring
        and Para-C specific formatting
        """
        format_orig = getattr(self._style, '_fmt')

        # If the output goes into a file it will not use any formatting
        if not self.file_mng:
            self._style._fmt = self.level_formatting[record.levelno]

        result = logging.Formatter.format(self, record)
        self._style._fmt = format_orig

        return result


def log_traceback(
        exc_info: Tuple[Type[BaseException], BaseException, TracebackType],
        level: Optional[str] = 'error',
        brief: Optional[str] = None
) -> None:
    """
    Logs the traceback of the latest exception

    :param level: Logger level for the exception
    :param brief: Small message that will be logged before the traceback
    :param exc_info: The exc_info containing the exception and the traceback
    """
    tb = traceback.format_exception(
        etype=exc_info[0],
        value=exc_info[1],
        tb=exc_info[2]
    )

    log_level: Callable = getattr(logger, level, None)
    if log_level is None and not callable(log_level):
        raise ValueError(
            "The passed level does not exist in the logging module!"
        )

    tb_str = "".join(frame for frame in tb)
    brief = brief if brief is not None else ""
    msg = f"{brief}\n\n{tb_str}\n"

    # Fetches and prints the current traceback with the passed message
    log_level(msg)


def log_msg(level: str, msg: str, *args, **kwargs) -> None:
    """ Logs the specified message using the logger module and regular print

    :param level: The logging level which should be used
    :param msg: The msg that should be printed
    :param args: The args that should be passed to the logging call
    :param kwargs: The kwargs that should be passed to the logging call
    """
    log_level: Optional[FunctionType] = getattr(logger, level)
    if callable(log_level):
        log_level(msg=msg, *args, **kwargs)


class TerminalANSIColor:
    """
    Cross-Platform Terminal Colors used for Click since rich can not
    interact with Click
    """
    base = "\033["
    default = f"{base}0m"
    reset = f"{base}0m"
    bold = f"{base}1m"
    italic = f"{base}3m"
    underline = f"{base}4m"
    blink = f"{base}5m"
    reverse = f"{base}7m"
    concealed = f"{base}8m"

    black = f"{base}30m"
    red = f"{base}31m"
    green = f"{base}32m"
    yellow = f"{base}33m"
    blue = f"{base}34m"
    purple = f"{base}35m"
    cyan = f"{base}36m"
    white = f"{base}37m"

    back_black = f"{base}40m"
    back_red = f"{base}41m"
    back_green = f"{base}42m"
    back_yellow = f"{base}43m"
    back_blue = f"{base}44m"
    back_magenta = f"{base}45m"
    back_cyan = f"{base}46m"
    back_white = f"{base}47m"

    bright_black = f"{base}30;90m"
    bright_red = f"{base}31;91m"
    bright_green = f"{base}32;92m"
    bright_yellow = f"{base}33;93m"
    bright_blue = f"{base}34;94m"
    bright_magenta = f"{base}35;95m"
    bright_cyan = f"{base}36;96m"
    bright_white = f"{base}37;97m"

    @classmethod
    def make_bold(cls, value: str) -> str:
        """ Adds to the ANSI formatting the bold prefix """
        return f"{cls.bold.replace('m', '')};"\
               f"{value.strip().replace(cls.base, '').replace('m', '')}m"

    @classmethod
    def make_italic(cls, value: str) -> str:
        """ Adds to the ANSI formatting the italic prefix """
        return f"{cls.italic.replace('m', '')};"\
               f"{value.strip().replace(cls.base, '').replace('m', '')}m"


ansi_col = TerminalANSIColor()


def print_init_banner() -> None:
    """ Creates the init screen string that can be printed """
    if AVOID_PRINT_BANNER_OVERWRITE:
        return get_rich_console().print("\n", end="")

    base_str = f"Para-C Compiler{' ' * 5}"

    get_rich_console().rule(style="bright_white rule.line")
    get_rich_console().print(
        f"[bold bright_cyan]{base_str}{__version__}[/bold bright_cyan]",
        justify="center"
    )
    get_rich_console().rule(style="bright_white rule.line")


def print_abort_banner(process: str) -> None:
    """
    Prints a simple colored Exception banner showing it crashed / was aborted
    """
    if AVOID_PRINT_BANNER_OVERWRITE:
        return get_rich_console().print("\n", end="")

    get_rich_console().rule(
        f"\n[bold red]Aborted {process}[/bold red]\n",
        style="red rule.line"
    )


def print_finish_banner() -> None:
    """
    Prints a simple colored banner screen showing it succeeded and finished
    """
    if AVOID_PRINT_BANNER_OVERWRITE:
        return get_rich_console().print("\n", end="")

    get_rich_console().rule(
        "\n[bold green]Finished Compilation[/bold green]\n",
        style="green rule.line"
    )


def print_log_banner() -> None:
    """
    Prints a simple colored banner screen showing the logs are active and
    the process started
    """
    if AVOID_PRINT_BANNER_OVERWRITE:
        return get_rich_console().print("\n", end="")

    output_console.print("\n", end="")
    output_console.rule(
        "[bold bright_cyan]Compiler Logs[white]\n",
        style="bright_white rule.line"
    )


def format_default(string: str) -> str:
    """ Creates a colored string for a command default """
    return f"{ansi_col.bright_green}{string}" \
           f"{ansi_col.make_bold(ansi_col.bright_cyan)}"


def create_prompt(string: str) -> str:
    """
    Creates a colored prompt string for a click.prompt() call
    (Uses ansi instead of rich because of compatibility issues)
    """
    return f'{ansi_col.make_bold(ansi_col.bright_cyan)} > {string}'


class ParacErrorListener(ErrorListener):
    """ Error-Listener for the Para-C compiler """

    def syntaxError(
            self,
            recognizer,
            offendingSymbol,
            line: int,
            column: int,
            msg: str,
            e):
        """
        Method which will be called if the ANTLR4 Lexer or Parser detect
        an error inside the program
        """
        logger.error(f"Error [{line}:{column}] > {msg}")
        # TODO! Add proper error handling

