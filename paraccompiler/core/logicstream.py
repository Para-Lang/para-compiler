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

logger = logging.getLogger(__name__)


class ParacLogicStream:
    """
    Logic Stream, which represents a stream of logic tokens, which can be used
    to convert the Para-C components into C-components, which can be converted
    into native C
    """
    ...


class CLogicStream:
    """
    Logic Stream, which represents a stream of logic tokens that are in native
    C and can be converted into that using gen_c_source
    """
