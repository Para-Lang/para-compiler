# coding=utf-8
""" Exceptions in the Para-C Compiler """
from enum import IntEnum
from typing import NewType, Optional

from .logger import log_msg

__all__ = [
    'ErrorCodes',

    'ParacCompilerError', 'CCompilerError',

    'UserInputError', 'EntryFileAccessError', 'EntryFilePermissionError',
    'EntryFileNotFoundError', 'IsDirectoryError', 'InvalidArgumentsError',

    'LexerError',

    'ParserError',

    'LogicalError',

    'LinkerError',

    'AbortError',
]

ErrorCode = NewType('ErrorCode', int)


class ErrorCodes(IntEnum):
    """ Error codes in the Para-C module """
    # 1** - INTERNAL ERRORS
    INTERNAL_ERROR = ErrorCode(100)
    INTERRUPT = ErrorCode(101)
    CONFIG_NOT_FOUND = ErrorCode(102)
    # -----------

    # 2** - USER INPUT ERRORS
    USER_INPUT_ERROR = ErrorCode(200)
    FILE_PERM_ERROR = ErrorCode(201)
    FILE_NOT_FOUND = ErrorCode(202)
    IS_DIR = ErrorCode(203)
    INVALID_CLI_ARGS = ErrorCode(204)
    # -----------

    # 3** - LEXER ERRORS
    LEXER_ERROR = ErrorCode(300)
    # -----------

    # 4** - PARSER ERRORS
    PARSER_ERROR = ErrorCode(400)
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
    COMPILER = ErrorCode(902)
    # -----------


class ParacCompilerError(Exception):
    """
    Base Exception in the Para-C compiler!

    All other exceptions inherit from this base class
    """
    error_msg = None
    _default_code = ErrorCodes.INTERNAL_ERROR

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


class CCompilerError(ParacCompilerError):
    """ General Exception for issues handling the C-compiler """
    error_msg = "Failed to properly interact with the C-compiler"
    _default_code = ErrorCodes.COMPILER


class UserInputError(ParacCompilerError):
    """
    Exception while trying to validate and use the specified user input
    """
    error_msg = "The given user input was invalid and couldn't be processed"
    _default_code = ErrorCodes.USER_INPUT_ERROR


class EntryFileAccessError(ParacCompilerError):
    """ General Exception for accessing a file """
    error_msg = "Failed to access entry-file"
    _default_code = ErrorCodes.USER_INPUT_ERROR


class EntryFilePermissionError(EntryFileAccessError):
    """ Failed to open or write to the specified file provided """
    error_msg = "Missing file access permissions"
    _default_code = ErrorCodes.FILE_PERM_ERROR


class EntryFileNotFoundError(EntryFileAccessError, FileNotFoundError):
    """ File does not exist """
    error_msg = "Specified Entry File does not exist"
    _default_code = ErrorCodes.FILE_NOT_FOUND


class IsDirectoryError(EntryFileAccessError):
    """ Specified file is a directory """
    error_msg = "Specified file is a directory"
    _default_code = ErrorCodes.IS_DIR


class InvalidArgumentsError(ParacCompilerError, RuntimeError):
    """
    Exception that indicates the wrong usages of arguments or flags resulting
    in an error
    """
    error_msg = "The passed arguments are invalid"
    _default_code = ErrorCodes.INVALID_CLI_ARGS


class LexerError(ParacCompilerError):
    """
    Exception in the Lexer, which parses and validates passed files
    """
    error_msg = "The Lexer encountered an error while walking through the " \
                "file and tokenizing"
    _default_code = ErrorCodes.LEXER_ERROR


class ParserError(ParacCompilerError):
    """
    Exception in the Parser, which parses the tokens and generates the logic
    tree
    """
    error_msg = "The Parser encountered an error while processing"
    _default_code = ErrorCodes.PARSER_ERROR


class LogicalError(ParacCompilerError):
    """
    Exception in the Compiler, caused by a logical issue inside a file
    """
    error_msg = "The Compiler encountered an logical error while processing"
    _default_code = ErrorCodes.LOGICAL_ERROR


class LinkerError(ParacCompilerError):
    """
    Exception in the Linker, which binds the files and checks
    the dependencies and implementation
    """
    error_msg = "The Linker encountered an error while linking the files"
    _default_code = ErrorCodes.LINKER_ERROR


class AbortError(ParacCompilerError, RuntimeError):
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
            exception: Optional[BaseException] = None
    ):
        if exception:
            if hasattr(exception, 'code'):
                code = exception.code

        super().__init__(code=code, *args)

        log_msg(
            level='critical',
            msg=f"Aborting setup with error code "
                f"{repr(self.code)}" if hasattr(self, 'code') else ""
        )
