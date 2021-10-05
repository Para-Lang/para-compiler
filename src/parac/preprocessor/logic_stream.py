# coding=utf-8
""" Logic Stream for Pre-Processor Items """
from typing import List, Any
from cached_property import cached_property

from ..abc import LogicStream
from .logic_tokens import NonPreProcessorItem
from .abc import PreProcessorLogicToken


class PreProcessorStream(LogicStream):
    """
    Pre-Processor Stream, which represents a list of PreProcessorLogicToken
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def content(self) -> List[PreProcessorLogicToken]:
        """
        Returns the content of the list. Type-hinted alias for list(self).

        Only contains the pure content
        """
        return list(self)

    def get_start(self) -> PreProcessorLogicToken:
        """ Gets the first item of the stream """
        return self[0]

    def get_end(self) -> PreProcessorLogicToken:
        """ Gets the last item of the stream """
        return self[-1]

    def append_antlr_ctx(self, _ctx: Any) -> None:
        """ Appends a new ctx instance to the stream """
        super().append_antlr_ctx(_ctx)


class ProcessedFileStream(LogicStream):
    """
    Processed File Stream representing a file that was already processed and
    does not contain directives anymore, but only processed code.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @cached_property
    def file_string(self) -> str:
        """
        File-string, which is the merged version of the content of this stream
        """
        ...

        return str()

    @property
    def content(self) -> List[NonPreProcessorItem]:
        """
        Returns the content of the list. Type-hinted alias for list(self).

        Only contains the pure content
        """
        return list(self)

    def get_start(self) -> NonPreProcessorItem:
        """ Gets the first item of the stream """
        return self[0]

    def get_end(self) -> NonPreProcessorItem:
        """ Gets the last item of the stream """
        return self[-1]

    def append_antlr_ctx(self, _ctx: Any) -> None:
        """ Appends a new ctx instance to the stream """
        super().append_antlr_ctx(_ctx)
