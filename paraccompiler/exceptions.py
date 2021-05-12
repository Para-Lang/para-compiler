""" Exceptions in the Para-C Compiler """

__all__ = [
    'ParacCompilerError', 'FileWritingPermissionError', 'AbortError'
]


class ParacCompilerError(Exception):
    """
    Base Exception in the Para-C compiler!

    All other exceptions inherit from this base class
    """
    error_msg = None

    def __init__(self, *args):
        if self.error_msg is None or args:
            if args:
                self.error_msg = ", ".join([str(arg) for arg in args])
            else:
                self.error_msg = f"Exception occurred in the Para-C compiler"

        super().__init__(self.error_msg)

    def __str__(self):
        return repr(self)


class FileWritingPermissionError(ParacCompilerError):
    """ Failed to open or write to the specified file provided """
    error_msg = "Failed to access the specified file due to missing permissions"


class AbortError(RuntimeError, ParacCompilerError):
    """ Exception used to signalise the compiler should abort its process and stop """
    error_msg = "Aborting the compilation process"
