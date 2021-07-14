# coding=utf-8
""" Logic Stream for Pre-Processor Items """
from typing import List

from paraccompiler.core.abc import LogicStream
from preprocessor.abc import PreProcessorLogicToken


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
