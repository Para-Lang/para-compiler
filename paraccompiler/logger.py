""" Logger management file for formatting and specific exception and  """
import logging
import traceback
from typing import Optional, Callable, Tuple, Type
from types import FunctionType, TracebackType

__all__ = [
    'TerminalColor',
    'tcol',
    'ParacFileHandler',
    'ParacFormatter',
    'log_traceback',
    'log_msg'
]

logger = logging.getLogger(__name__)


class TerminalColor:
    """ Cross-Platform Terminal Colors """
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
        return f"{cls.bold.replace('m', '')};{value.strip().replace(cls.base, '').replace('m', '')}m"

    @classmethod
    def make_italic(cls, value: str) -> str:
        """ Adds to the ANSI formatting the italic prefix """
        return f"{cls.italic.replace('m', '')};{value.strip().replace(cls.base, '').replace('m', '')}m"


tcol = TerminalColor()


class ParacFileHandler(logging.FileHandler):
    """ Default FileHandler for the file handling in the Para-C compiler """
    def __init__(self, filename=f'./parac.log', encoding='utf-8', mode='w', *args, **kwargs):
        super().__init__(filename=filename, encoding=encoding, mode=mode, *args, **kwargs)


class ParacFormatter(logging.Formatter):
    """ Default Formatter class for the custom formatted output of the Para-C compiler """
    level_formatting = {
        logging.CRITICAL: [
            f'{tcol.make_bold(tcol.bright_red)}[%(levelname)s]', f'{tcol.bright_red} - (%(asctime)s): %(message)s'
        ],
        logging.ERROR: [
            f'{tcol.make_bold(tcol.red)}[%(levelname)s]', f'{tcol.red} - (%(asctime)s): %(message)s'
        ],
        logging.WARNING: [
            f'{tcol.make_bold(tcol.bright_yellow)}[%(levelname)s]', f'{tcol.bright_yellow} - (%(asctime)s): %(message)s'
        ],
        logging.DEBUG: [
            f'{tcol.bright_yellow}[%(levelname)s]', f'{tcol.bright_yellow} - (%(asctime)s): %(message)s'
        ],
        logging.INFO: [
            f'{tcol.blue}[%(levelname)s]', f'{tcol.blue} - (%(asctime)s): %(message)s'
        ]
    }

    default = '[%(levelname)s] - (%(asctime)s): %(message)s'

    def __init__(self, file_mng: bool = False, fmt: Optional[str] = default, *args, **kwargs):
        self.file_mng = file_mng
        super().__init__(fmt=fmt, *args, **kwargs)

    def format(self, record):
        """ Class specific formatter function to add colouring and Para-C specific formatting """
        format_orig = getattr(self._style, '_fmt')
        # If the output goes into a file it will not use any formatting
        if not self.file_mng:
            self._style._fmt = tcol.reset.join(self.level_formatting[record.levelno])

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
        raise ValueError("The passed level does not exist in the logging module!")

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
