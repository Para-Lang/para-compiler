# coding=utf-8
""" Exceptions in the Para-C Compiler """
from __future__ import annotations

from enum import IntEnum
from types import TracebackType
from typing import NewType, Union, Type, TYPE_CHECKING, List

from .logging import log_msg

if TYPE_CHECKING:
    from .compiler.parser.python.ParaCParser import ParaCParser

__all__ = [
    'ErrorCodes', 'ParacCompilerError',

    'InternalError', 'InternalErrorInfo', 'InterruptError',
    'FailedToProcessError',

    'UserInputError', 'FileAccessError', 'FilePermissionError',
    'FileNotFoundError', 'IsDirectoryError', 'InvalidArgumentsError',
    'ConfigNotFoundError', 'CCompilerNotFoundError',

    'LexerError',

    'ParserError',

    'ParaCSyntaxError', 'ParaCSyntaxErrorCollection',

    'LogicalError',

    'LinkerError',

    'UnassociatedError', 'UnknownError'
]

ErrorCode = NewType('ErrorCode', int)


class ErrorCodes(IntEnum):
    """ Error codes in the Para-C module """
    # 99 - Base Error
    BASE_ERROR = ErrorCode(99)

    # 1** - INTERNAL ERRORS
    INTERNAL_ERROR = ErrorCode(100)
    INTERRUPT = ErrorCode(101)
    FAILED_TO_PROCESS = ErrorCode(102)
    # -----------

    # 2** - USER INPUT ERRORS
    USER_INPUT_ERROR = ErrorCode(200)
    FILE_ACCESS_ERROR = ErrorCode(201)
    FILE_PERM_ERROR = ErrorCode(202)
    FILE_NOT_FOUND = ErrorCode(203)
    IS_DIR = ErrorCode(204)
    INVALID_CLI_ARGS = ErrorCode(205)
    CONFIG_NOT_FOUND = ErrorCode(206)
    C_COMPILER_NOT_FOUND = ErrorCode(207)
    # -----------

    # 3** - LEXER ERRORS
    LEXER_ERROR = ErrorCode(300)
    # -----------

    # 4** - PARSER ERRORS
    PARSER_ERROR = ErrorCode(400)
    SYNTAX_ERROR = ErrorCode(401)
    # -----------

    # 5** - LOGICAL ERRORS
    LOGICAL_ERROR = ErrorCode(500)
    # -----------

    # 6** - LINKER ERRORS
    LINKER_ERROR = ErrorCode(600)
    # -----------

    # 9** - OTHER
    OTHER = ErrorCode(900)
    UNKNOWN = ErrorCode(901)
    # -----------


class ParacCompilerError(Exception):
    """
    Base Exception in the Para-C compiler!

    All other exceptions inherit from this base class
    """
    error_msg = None
    _default_code = ErrorCodes.BASE_ERROR

    def __init__(self, *args, code: int = None):
        if code is None:
            code = getattr(self, '_default_code')

        self._code = code
        if self.error_msg is None or args:
            if args:
                self.error_msg = ", ".join([str(arg) for arg in args])
            else:
                self.error_msg = "Exception occurred in the Para-C compiler"

        super().__init__(self.error_msg)

    @property
    def code(self) -> ErrorCode:
        """ Returns the exception code """
        return self._code


# 1** - INTERNAL ERRORS

class InternalErrorInfo:
    """ Class storing info about an exception causing an InternalError """
    
    def __init__(
            self,
            exc_type: Type[Exception],
            exc_value: Exception,
            exc_tb: TracebackType
    ):
        self._exc_type = exc_type
        self._exc_value = exc_value
        self._exc_tb = exc_tb
    
    @property
    def exc_type(self) -> Type[Exception]:
        """ Exception Type """
        return self._exc_type

    @property
    def exc_value(self) -> Exception:
        """ Exception Instance """
        return self._exc_value

    @property
    def exc_tb(self) -> TracebackType:
        """ Traceback of Exception Instance """
        return self._exc_tb


class InternalError(ParacCompilerError):
    """
    Encountered an error in the internal compiler structure. This is an
    indication for a heavy bug or issue blocking correct processing.
    """
    error_msg = "Failed due to internal error! Please checks the logs and " \
                "report the issue if the issue can't be resolved!"
    _default_code = ErrorCodes.INTERNAL_ERROR

    def __init__(
            self,
            *args,
            exc: Union[Exception, ParacCompilerError],
            code: int = _default_code,
    ):
        if exc:
            if hasattr(exc, 'code'):
                code = exc.code
        else:
            code = self._default_code  # always default to INTERRUPT

        self._origin = InternalErrorInfo(
            type(exc),
            exc,
            exc.__traceback__
        )
        super().__init__(code=code, *args)

    @property
    def origin(self) -> InternalErrorInfo:
        """
        InternalErrorInfo for the original Exception causing the InternalError
        """
        return self._origin


class InterruptError(InternalError, RuntimeError):
    """
    Exception used to signalise the compiler should abort its process
    and stop
    """
    error_msg = "Aborting the compilation process"
    _default_code = ErrorCodes.INTERRUPT

    def __init__(
            self,
            *args,
            code: int = _default_code,
            exc: Union[Exception, KeyboardInterrupt] = None,
            print_abort_code: bool = True
    ):
        if exc:
            if hasattr(exc, 'code'):
                code = exc.code
        else:
            code = self._default_code  # always default to INTERRUPT

        self.origin_exc = exc
        super().__init__(code=code, *args)

        if print_abort_code:
            log_msg(
                level='critical',
                msg=f"Aborting setup with error code "
                    f"{repr(self.code)}" if hasattr(self, 'code') else ""
            )


class FailedToProcessError(InternalError):
    """
    A specific error that is raised inside a compilation process or
    Pre-Processor process, which represents a failure in processing the wanted
    input. This class replaces the actual error that would be logged and all
    error logs will be printed onto the console.
    """
    error_msg = "Failed to process the input! Check logs for information"
    _default_code = ErrorCodes.FAILED_TO_PROCESS

    def __init__(
            self,
            exc: Union[Exception, ParacCompilerError],
            code: int = _default_code,
    ):
        log_msg('error', str(exc))
        super().__init__(self.error_msg, exc=exc, code=code)


# 2** - USER INPUT ERRORS
class UserInputError(ParacCompilerError):
    """
    Exception while trying to validate and use the specified user input
    """
    error_msg = "The given user input was invalid and couldn't be processed"
    _default_code = ErrorCodes.USER_INPUT_ERROR


class FileAccessError(UserInputError):
    """ General Exception for accessing a file """
    error_msg = "Failed to access entry-file"
    _default_code = ErrorCodes.FILE_ACCESS_ERROR


class FilePermissionError(UserInputError):
    """ Failed to open or write to the specified file provided """
    error_msg = "Missing file access permissions"
    _default_code = ErrorCodes.FILE_PERM_ERROR


_in_FileNotFoundError = FileNotFoundError


class FileNotFoundError(UserInputError, _in_FileNotFoundError):
    """ File does not exist """
    error_msg = "Specified Entry File does not exist"
    _default_code = ErrorCodes.FILE_NOT_FOUND


class IsDirectoryError(UserInputError):
    """ Specified file is a directory """
    error_msg = "Specified file is a directory"
    _default_code = ErrorCodes.IS_DIR


class InvalidArgumentsError(UserInputError):
    """
    Exception that indicates the wrong usages of arguments or flags resulting
    in an error
    """
    error_msg = "The passed arguments are invalid"
    _default_code = ErrorCodes.INVALID_CLI_ARGS


class ConfigNotFoundError(UserInputError):
    """ The configuration file for the project was not found """
    error_msg = "Failed to find the configuration file for the project"
    _default_code = ErrorCodes.CONFIG_NOT_FOUND


class CCompilerNotFoundError(UserInputError):
    """ The C-compiler necessary for compilation was not found """
    error_msg = "Failed to locate C-compiler! Configuration path dest does " \
                "not exist"
    _default_code = ErrorCodes.C_COMPILER_NOT_FOUND


# 3** - LEXER ERRORS
class LexerError(ParacCompilerError):
    """
    Exception in the Lexer, which parses and validates passed files
    """
    error_msg = "The Lexer encountered an error while walking through the " \
                "file and tokenizing"
    _default_code = ErrorCodes.LEXER_ERROR


# 4** - PARSER ERRORS
class ParserError(ParacCompilerError):
    """
    Exception in the Parser, which parses the tokens and generates the logic
    tree
    """
    error_msg = "The Parser encountered an error while processing"
    _default_code = ErrorCodes.PARSER_ERROR


class ParaCSyntaxError(ParserError, LexerError, SyntaxError):
    """
    Syntax-Exception signalising an issue with the code of the user
    """
    error_msg = "Encountered a syntax error while processing"
    _default_code = ErrorCodes.SYNTAX_ERROR

    def __init__(
            self,
            parac_parser: ParaCParser,
            offending_symbol,
            line: int,
            column: int,
            msg: str,
    ):
        self.error_ctx = parac_parser
        self.offending_symbol = offending_symbol
        self.line = line
        self.column = column
        self.msg = msg
        self.file = offending_symbol.source[1].name
        self.gen_str = self.create_error_log_msg()

        super().__init__(
            msg,
            code=self._default_code
        )

    def __str__(self):
        return self.gen_str

    def create_error_log_msg(self) -> str:
        """ Creates the log message for this Exception """
        from .util import get_original_text_from_token

        original_str: str = get_original_text_from_token(
            self.offending_symbol
        )
        gen_str: str = ''.join((
            f'In file \'{self.file}\'',
            '\n',
            original_str,
            '\n',
            '^' * (len(original_str) if original_str else 1),
            '\n',
            f'SyntaxError at line {self.line}: {self.msg}'
        ))
        return gen_str


class ParaCSyntaxErrorCollection(ParserError):
    """ Collection of ParaCSyntaxErrors """
    error_msg = "Encountered one or more syntax errors while processing"
    _default_code = ErrorCodes.SYNTAX_ERROR

    def __init__(
            self,
            errs: List[ParaCSyntaxError],
            log_errors: bool
    ):
        """
        :param errs: The list of syntax errors
        :param log_errors: If set to True it will log all exceptions on
         initialisation
        """
        self._errs: List[ParaCSyntaxError] = errs
        self._err_msgs: List[str] = list(str(e) for e in errs)

        # Logging for every instance the error
        if log_errors:
            for e in self.err_msgs:
                log_msg('critical', e)

        super().__init__()

    @property
    def errs(self) -> List[ParaCSyntaxError]:
        """ A list of the received SyntaxErrors """
        return self._errs

    @property
    def err_msgs(self) -> List[str]:
        """ A list of all messages of the SyntaxErrors """
        return self._err_msgs


# 5** - LOGICAL ERRORS
class LogicalError(ParacCompilerError):
    """
    Exception in the Compiler, caused by a logical issue inside a file
    """
    error_msg = "The Compiler encountered an logical error while processing"
    _default_code = ErrorCodes.LOGICAL_ERROR


# 6** - LINKER ERRORS
class LinkerError(ParacCompilerError):
    """
    Exception in the Linker, which binds the files and checks
    the dependencies and c-implementation
    """
    error_msg = "The Linker encountered an error while linking the files"
    _default_code = ErrorCodes.LINKER_ERROR


# 9** - OTHER
class UnassociatedError(ParacCompilerError):
    """ Unassociated error that does not match any specific category """
    error_msg = "Encountered an error while processing that can't be " \
                "categorised"
    _default_code = ErrorCodes.OTHER


class UnknownError(UnassociatedError):
    """ Encountered an unknown error """
    error_msg = "Encountered an unknown error while processing. Please check" \
                "logs for information. Report the issue if it can't be " \
                "resolved"
    _default_code = ErrorCodes.UNKNOWN
