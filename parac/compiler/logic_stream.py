# coding=utf-8
"""
File containing the ParacLogicStream and CLogicStream, which represents a
stream of logic components. A ParacLogicStream can be converted into a
CLogicStream and processed into native C.
"""
import logging

__all__ = [
    'ParacLogicStream',
    'CLogicStream'
]

from typing import List, Any

from ..abc import ParacLogicToken, CLogicToken, LogicStream

logger = logging.getLogger(__name__)


class ParacLogicStream(LogicStream):
    """
    Logic Stream, which represents a stream of logic tokens, which can be used
    to convert the Para-C components into C-components, which can be converted
    into native C.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def content(self) -> List[ParacLogicToken]:
        """
        Returns the content of the list. Type-hinted alias for list(self).

        Only contains the pure content
        """
        return list(self)

    def get_start(self) -> ParacLogicToken:
        """ Gets the first item of the stream """
        return self[0]

    def get_end(self) -> ParacLogicToken:
        """ Gets the last item of the stream """
        return self[-1]

    def append_antlr_ctx(self, _ctx: Any) -> None:
        """ Appends a new ctx instance to the stream """
        super().append_antlr_ctx(_ctx)


class CLogicStream(LogicStream):
    """
    Logic Stream, which represents a stream of logic tokens that are in native
    C.
    """

    def __init__(self, generator_parent: ParacLogicStream, *args, **kwargs):
        self._generator_parent = generator_parent
        super().__init__(*args, **kwargs)

    @property
    def generator_parent(self) -> ParacLogicStream:
        """
        Parent of this Stream aka. the original Para-C token stream, which
        was used to create this stream
        """
        return self._generator_parent

    @property
    def content(self) -> List[CLogicToken]:
        """
        Returns the content of the list. Type-hinted alias for list(self).

        Only contains the pure content
        """
        return list(self)

    def get_parent_item(self, index: int) -> ParacLogicToken:
        """
        Fetches an item from the Para-C stream parent based on the index
        """
        return self._generator_parent[index]

    def get_start(self) -> CLogicToken:
        """ Gets the first item of the stream """
        return self[0]

    def get_end(self) -> CLogicToken:
        """ Gets the last item of the stream """
        return self[-1]

    def append_antlr_ctx(self, _ctx: Any) -> None:
        """ Appends a new ctx instance to the stream """
        super().append_antlr_ctx(_ctx)
