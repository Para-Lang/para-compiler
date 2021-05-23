# coding=utf-8
""" Exceptions in the Para-C Compiler """
from typing import NewType
from enum import IntEnum
from . import log_msg

__all__ = [
    'ErrorCodes',
    'ParacCompilerError', 'CCompilerError',

    'EntryFileAccessError', 'EntryFilePermissionError', 'EntryFileNotFoundError', 'IsDirectoryError',

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

    # 2** - FILE ERRORS
    FILE_ERROR = ErrorCode(200)
    FILE_PERM_ERROR = ErrorCode(201)
    FILE_NOT_FOUND = ErrorCode(202)
    IS_DIR = ErrorCode(203)
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


class EntryFileAccessError(ParacCompilerError):
    """ General Exception for accessing a file """
    error_msg = "Failed to access entry-file"
    _default_code = ErrorCodes.FILE_ERROR


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


class AbortError(ParacCompilerError, RuntimeError):
    """ Exception used to signalise the compiler should abort its process and stop """
    error_msg = "Aborting the compilation process"

    def __init__(self, exception: BaseException, code: int = ErrorCodes.INTERRUPT, *args, **kwargs):
        if hasattr(exception, 'code'):
            code = exception.code

        super().__init__(code=code, *args)
        log_msg(
            level='critical',
            msg=f"Aborting setup {f'with error code {repr(self.code)}' if hasattr(self, 'code') else ''}"
        )
