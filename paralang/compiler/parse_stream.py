# coding=utf-8
"""
File containing the ParaQualifiedParseStream and CParseStream, which represents a
stream of logic components. A ParaQualifiedParseStream can be converted into a
CParseStream and processed into native C.
"""
import logging

__all__ = [
    'ParaQualifiedParseStream',
    'CParseStream'
]

from typing import List, Any

from ..abc import ParaParseToken, CParseToken, ParseStream

logger = logging.getLogger(__name__)


class ParaQualifiedParseStream(ParseStream):
    """
    Logic Stream, which represents a stream of logic tokens, which can be used
    to convert the Para components into C-components, which can be converted
    into native C.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def content(self) -> List[ParaParseToken]:
        """
        Returns the content of the list. Type-hinted alias for list(self).

        Only contains the pure content
        """
        return list(self)

    def get_start(self) -> ParaParseToken:
        """ Gets the first item of the stream """
        return self[0]

    def get_end(self) -> ParaParseToken:
        """ Gets the last item of the stream """
        return self[-1]

    def append_antlr_ctx(self, _ctx: Any) -> None:
        """ Appends a new ctx instance to the stream """
        super().append_antlr_ctx(_ctx)


class CParseStream(ParseStream):
    """
    Logic Stream, which represents a stream of logic tokens that are in native
    C - can be converted into native C code using the Para Base Library
    """

    def __init__(
            self,
            generator_parent: ParaQualifiedParseStream,
            *args,
            **kwargs
    ):
        self._generator_parent = generator_parent
        super().__init__(*args, **kwargs)

    @property
    def generator_parent(self) -> ParaQualifiedParseStream:
        """
        Parent of this Stream aka. the original Para token stream, which
        was used to create this stream
        """
        return self._generator_parent

    @property
    def content(self) -> List[CParseToken]:
        """
        Returns the content of the list. Type-hinted alias for list(self).

        Only contains the pure content
        """
        return list(self)

    def get_parent_item(self, index: int) -> ParaParseToken:
        """
        Fetches an item from the Para stream parent based on the index
        """
        return self._generator_parent[index]

    def get_start(self) -> CParseToken:
        """ Gets the first item of the stream """
        return self[0]

    def get_end(self) -> CParseToken:
        """ Gets the last item of the stream """
        return self[-1]

    def append_antlr_ctx(self, _ctx: Any) -> None:
        """ Appends a new ctx instance to the stream """
        super().append_antlr_ctx(_ctx)
