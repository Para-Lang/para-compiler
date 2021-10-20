# coding=utf-8
""" Logger management file for formatting and specific exception and  """
import logging
import os
import shutil
import sys
import traceback
import re
from logging import StreamHandler
from pathlib import Path

from rich.console import Console
from typing import Optional, Callable, Tuple, Type, Union, Literal
from types import FunctionType, TracebackType
from rich.theme import Theme

__all__ = [
    'OVERWRITE_AVOID_PRINT_BANNER',
    'CLICK_FORMAT_IGNORE_REGEX',
    'set_avoid_print_banner_overwrite',
    'custom_theme',
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
    'print_result_banner',
    'cli_create_prompt',
    'cli_format_default',
    'logger'
]

_bracket_s = re.escape('[')
_bracket_e = re.escape(']')
CLICK_FORMAT_IGNORE_REGEX: str = \
    f"{_bracket_s}[^{_bracket_s}{_bracket_e}]*?{_bracket_e}"
# If this flag is set to True no banners will be printed
# and instead only newlines
OVERWRITE_AVOID_PRINT_BANNER: bool = False
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
    global OVERWRITE_AVOID_PRINT_BANNER
    OVERWRITE_AVOID_PRINT_BANNER = value


def get_terminal_size() -> Optional[int]:
    """ Gets the terminal size """
    from . import const

    width: Optional[int] = None
    if "PYCHARM_HOSTED" in os.environ:
        width = 150
    elif const.WIN:  # pragma: no cover
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
    from . import const
    return "windows" if const.WIN else "auto"


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
    """
    Specific Logging Stream Handler for Para-C designed to implement rich
    """

    def __init__(self, *args, **kwargs):
        self.warnings = 0
        self.errors = 0
        super().__init__(*args, **kwargs)

    @property
    def console(self) -> Union[Console, None]:
        """ Fetches the Console if it is initialised """
        return get_rich_console()

    def emit(self, record: logging.LogRecord):
        """
        Emit a record using rich and the set c-implementation

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.
        If exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        try:
            if record.levelno in (logging.CRITICAL, logging.ERROR):
                self.errors += 1
            elif record.levelno == logging.WARNING:
                self.warnings += 1

            msg = self.format(record)
            # Writing with the rich print method which implements
            # its own stream-handler (console out handler)
            self.console.print(msg, highlight=False, justify="left")
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)


logger = logging.getLogger(__name__)


class ParacFileHandler(logging.FileHandler):
    """
    Default FileHandler for the logging file handling in the Para-C compiler
    """

    def __init__(
            self,
            filename: Union[str, os.PathLike, Path] = None,
            encoding: str = 'utf-8',
            mode: str = 'w',
            *args,
            **kwargs
    ):
        from . import const
        if filename is None:
            filename = str(const.DEFAULT_LOG_PATH)

        super().__init__(
            filename=filename,
            encoding=encoding,
            mode=mode,
            *args,
            **kwargs
        )

    def emit(self, record: logging.LogRecord):
        """ Emits the record """
        record.msg = re.sub(
            CLICK_FORMAT_IGNORE_REGEX,
            '',
            record.msg,
            flags=re.DOTALL
        )
        super().emit(record)


class ParacFormatter(logging.Formatter):
    """
    Default Formatter class for the custom formatted logging output of the
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
            '[bold white]'
            '[%(levelname)s] - (%(asctime)s):'
            '[/bold white]'
            '[white] %(message)s[/white]'
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

    def format(self, record: logging.LogRecord):
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
        return f"{cls.bold.replace('m', '')};" \
               f"{value.strip().replace(cls.base, '').replace('m', '')}m"

    @classmethod
    def make_italic(cls, value: str) -> str:
        """ Adds to the ANSI formatting the italic prefix """
        return f"{cls.italic.replace('m', '')};" \
               f"{value.strip().replace(cls.base, '').replace('m', '')}m"


ansi_col = TerminalANSIColor()


def print_init_banner() -> None:
    """
    Creates the init screen string that can be printed

    Required init_rich_console to be called before it!
    """
    from . import __version__

    if get_rich_console() is None:
        raise RuntimeError(
            "Rich console was not initialised. Use init_rich_console to"
            " utilise this function"
        )

    if OVERWRITE_AVOID_PRINT_BANNER:
        return get_rich_console().print("\n", end="")

    base_str = f"Para-C Compiler | {__version__} | Docs: para-c.readthedocs.io"

    get_rich_console().rule(style="bright_white rule.line")
    get_rich_console().print(
        f"[bold bright_cyan]{base_str}[/bold bright_cyan]",
        justify="center"
    )
    get_rich_console().rule(style="bright_white rule.line")


def print_abort_banner(process: str) -> None:
    """
    Prints a simple colored Exception banner showing it crashed / was aborted

    Required init_rich_console to be called before it!
    """
    if get_rich_console() is None:
        raise RuntimeError(
            "Rich console was not initialised. Use init_rich_console to"
            " utilise this function"
        )

    if OVERWRITE_AVOID_PRINT_BANNER:
        return get_rich_console().print("\n", end="")

    get_rich_console().rule(
        f"\n[bold red]Aborted {process}[/bold red]\n",
        style="red rule.line"
    )


def print_result_banner(
        name: str = "Compilation", success: bool = True
) -> None:
    """
    Prints a simple colored banner screen showing the process finished and a
    result is available

    Required init_rich_console to be called before it!

    :param name: The name that should be printed before the ' Result'
    :param success: If success if True then the banner will be in green
    """
    if get_rich_console() is None:
        raise RuntimeError(
            "Rich console was not initialised. Use init_rich_console to"
            " utilise this function"
        )

    if OVERWRITE_AVOID_PRINT_BANNER:
        return get_rich_console().print("\n", end="")

    col = 'bright_cyan' if success else 'red'
    get_rich_console().rule(
        f"\n[bold {col}]{name} Result[/bold {col}]\n",
        style="green rule.line"
    )
    get_rich_console().print("\n", end="")


def print_log_banner(name: str = "Compiler", newline: bool = True) -> None:
    """
    Prints a simple colored banner screen showing the logs are active and
    the process started.

    Required init_rich_console to be called before it!
    """
    if get_rich_console() is None:
        raise RuntimeError(
            "Rich console was not initialised. Use init_rich_console to"
            " utilise this function"
        )

    if OVERWRITE_AVOID_PRINT_BANNER:
        return get_rich_console().print("\n", end="")

    if newline:
        get_rich_console().print("\n", end="")
    get_rich_console().rule(
        f"[bold bright_cyan]{name} Logs[white]\n",
        style="bright_white rule.line"
    )


def cli_format_default(string: str) -> str:
    """ Creates a colored string for a command default """
    return f"{ansi_col.bright_green}{string}" \
           f"{ansi_col.make_bold(ansi_col.bright_cyan)}"


def cli_create_prompt(string: str) -> str:
    """
    Creates a colored prompt string for a click.prompt() call
    (Uses ansi instead of rich because of compatibility issues)
    """
    return f'{ansi_col.make_bold(ansi_col.bright_cyan)} > {string}'

