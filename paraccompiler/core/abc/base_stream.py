# coding=utf-8
""" File containing the ABC class for a LogicStream """

from abc import abstractmethod, ABC
from typing import List

from .base_tokens import LogicToken


__all__ = [
    'LogicStream'
]


class LogicStream(list, ABC):
    """
    Logic Stream class which acts like a list, which implements special
    functions for interacting with the stream
    """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    @abstractmethod
    def content(self) -> List[LogicToken]:
        """
        Returns the content of the list. Type-hinted alias for list(self).

        Only contains the pure content
        """
        return list(self)

    @abstractmethod
    def get_start(self) -> LogicToken:
        """ Gets the first item of the stream """
        return self[0]

    @abstractmethod
    def get_end(self) -> LogicToken:
        """ Gets the last item of the stream """
        return self[-1]
