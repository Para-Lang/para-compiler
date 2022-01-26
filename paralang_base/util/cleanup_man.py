# coding=utf-8
"""
Cleanup Manager for creating specific context managers with cleanup functions
"""
from typing import Callable

__all__ = [
    "CleanUpManager"
]


class CleanUpManager:
    """
    Cleanup class used for managing cases where specific handing needs to be
    implemented and a cleanup method called in certain cases, but not
    necessarily all. This class will call after being used as a contextmanager
    the method passed during initialisation.

    Args and Kwargs can also be passed to the cleanup function by just passing
    a tuple and the dict to init as args: tuple and kwargs: dict

    These can also be manipulated inside the context manager block by setting
    f_args and f_kwargs
    """

    class Cancel(Exception):
        """
        Simple Puppet class for serving as a way to differentiate between
        exceptions
        """
        ...

    def __init__(self, f_cleanup: Callable, args: tuple, kwargs: dict):
        self.f_cleanup: Callable = f_cleanup
        self.f_args = args
        self.f_kwargs = kwargs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        cancelled: bool = issubclass(exc_type, self.__class__.Cancel)

        if not cancelled:
            self.f_cleanup(*self.f_args, **self.f_kwargs)
        else:
            if exc_value:
                raise exc_value  # re-raising exception

    def cancel(self):
        """
        Cancel the execution of the cleanup method after returning from the
        context manager
        """
        raise self.__class__.Cancel
