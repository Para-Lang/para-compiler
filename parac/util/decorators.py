# coding=utf-8
""" File containing utility decorators """
import functools
import logging
import sys
import warnings
from sys import exit
from functools import wraps

from ..exceptions import (InterruptError, ParacCompilerError,
                          InternalError)

from ..logging import (get_rich_console as console, log_traceback,
                       print_abort_banner, init_rich_console)
from .strtools import escape_ansi


__all__ = [
    'deprecated',
    'abortable',
    'requires_init',
    'cli_keep_open_callback',
    'escape_ansi_args'
]

logger = logging.getLogger(__name__)


def abortable(
        _func=None,
        *,
        reraise: bool,
        preserve_exception: bool = False,
        abort_on_internal_errors: bool = False,
        print_abort: bool = True,
        step: str = "Process"
):
    """
    Marks the function as abortable and adds traceback logging to it.

    Raised InterruptError will close the program entirely!

    :param _func: Function to apply the decorator
    :param reraise: If set to True, any exception will be reraised. If False,
     it will close the program and write the error onto the console.
    :param preserve_exception: If set to True, the original exception will be
     returned and not the wrapped exception using InternalError or
    InterruptError
    :param abort_on_internal_errors: If set to True when receiving an
     InternalError it will treat it as a call for aborting the process. This
     means it will stop the program and print the abort banner if print_abort
     is True.
    :param print_abort: If True, it will print the abort banner when closing
    :param step: The step that should be passed onto print_abort_banner.
     Only valid argument when print_abort is True
    """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            def _handle_abort(print_out: bool):
                if print_out:
                    print_abort_banner(step)
                exit(1)

            try:
                from .. import RUNTIME_COMPILER
                try:
                    return func(*args, **kwargs)
                except InterruptError:
                    _handle_abort(print_abort)

                except KeyboardInterrupt as e:
                    if preserve_exception:
                        raise e
                    else:
                        raise InterruptError(exc=e) from e

                except ParacCompilerError as e:
                    if not RUNTIME_COMPILER.log_initialised:
                        RUNTIME_COMPILER.init_logging_session()

                    log_traceback(
                        level="critical",
                        brief="Encountered unexpected exception while running",
                        exc_info=sys.exc_info()
                    )
                    if preserve_exception:
                        raise e
                    else:
                        raise InterruptError(exc=e) from e

                except Exception as e:
                    if not RUNTIME_COMPILER.log_initialised:
                        RUNTIME_COMPILER.init_logging_session()

                    if preserve_exception:
                        raise e
                    else:
                        raise InternalError(
                            "Encountered unexpected exception while running",
                            exc=e
                        ) from e

            except Exception as e:
                if abort_on_internal_errors and type(e) is InternalError:
                    _handle_abort(print_abort)
                elif reraise:
                    raise e
                else:
                    _handle_abort(print_abort)

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


def requires_init(_func=None):
    """
    Checks whether the compiler is initialised and only calls the function if
    it is, else it will trigger a warning and prompt for initialisation
    """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            from .. import RUNTIME_COMPILER
            from .. import const
            from . import (is_c_compiler_ready, cli_initialise_c_compiler)

            if not is_c_compiler_ready() and \
                    not const.C_COM_EXISTENCE_OVERWRITE:
                if not RUNTIME_COMPILER.log_initialised:
                    RUNTIME_COMPILER.init_logging_session()

                init_rich_console()
                console().print('')
                logger.warning(
                    "C-Compiler path is not initialised! If you do not have a"
                    " working compiler installed, please refer to an "
                    "installation page for your operation system"
                    " (MinGW, cygwin)"
                )
                logger.info(
                    "Initialising Para-C compiler due to missing configuration"
                    "\n"
                )
                cli_initialise_c_compiler()
                logger.info("Setup may continue\n")
            return func(*args, **kwargs)

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


def deprecated(_func, *, instead=None):
    """
    Warns the user about a function or tool that is deprecated
    and shouldn't be used anymore
    """

    def _decorator(func):
        @wraps(func)
        def _decorated(*args, **kwargs):
            # turn off filter
            warnings.simplefilter('always', DeprecationWarning)
            if instead:
                fmt = "{0.__name__} is deprecated, use {1} instead."
            else:
                fmt = '{0.__name__} is deprecated.'

            warnings.warn(
                fmt.format(func, instead),
                stacklevel=3,
                category=DeprecationWarning
            )
            # reset filter
            warnings.simplefilter('default', DeprecationWarning)
            return func(*args, **kwargs)

        return _decorated

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


def cli_keep_open_callback(_func=None):
    """ Keeps the console open after finishing until the user presses a key """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            keep_open = kwargs.pop('keep_open')
            r = func(*args, **kwargs)

            # If keep_open is True -> the user passed --keep_open as an option
            # then the console will stay open until a key is pressed
            if keep_open:
                console().print("\n\n", end="")
                console().input("Press any key to close the process ...")
                console().print("")
            return r

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)


def escape_ansi_args(_func):
    """
    Calls the function but removes ansi colouring on the args and kwargs on str
    items if it exists
    """

    def _decorator(func):
        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            new_args = []
            for i in args:
                if type(i) is str:
                    new_args.append(escape_ansi(i))
                else:
                    new_args.append(i)

            new_kwargs = {}
            for key, value in kwargs.items():
                if type(value) is str:
                    value = escape_ansi(value)
                new_kwargs[key] = value

            return func(*new_args, **new_kwargs)

        return _wrapper

    if _func is None:
        return _decorator
    else:
        return _decorator(_func)
