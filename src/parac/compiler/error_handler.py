# coding=utf-8
""" Error handler for the parser and lexer of the core compiler """
import logging
from typing import Union

from antlr4.Token import CommonToken
from antlr4.error.Errors import (InputMismatchException,
                                 FailedPredicateException,
                                 RecognitionException,
                                 LexerNoViableAltException,
                                 NoViableAltException)
from .parser.python.ParaCParser import ParaCParser

from ..abc.base_error_handler import BaseErrorListener

__all__ = [
    'ParacErrorListener',
]

logger = logging.getLogger(__name__)


class ParacErrorListener(BaseErrorListener):
    """ Error-Listener for the Para-C compiler """

    def __init__(self):
        super().__init__()

    def reportAmbiguity(
            self,
            recognizer,
            dfa,
            startIndex,
            stopIndex,
            exact,
            ambigAlts,
            configs
    ) -> None:
        """
        This method is called by the parser when a full-context prediction
        results in an ambiguity.
        """
        ...

    def reportAttemptingFullContext(
            self,
            recognizer,
            dfa,
            startIndex,
            stopIndex,
            conflictingAlts,
            configs
    ) -> None:
        """
        This method is called when an SLL conflict occurs and the parser is
        about to use the full context information to make an LL decision.
        """
        ...

    def reportContextSensitivity(
            self,
            recognizer,
            dfa,
            startIndex,
            stopIndex,
            prediction,
            configs
    ) -> None:
        """
        This method is called by the parser when a full-context prediction
        has a unique result.
        """
        ...

    def syntaxError(
            self,
            recognizer: ParaCParser,
            offendingSymbol: CommonToken,
            line: int,
            column: int,
            msg: str,
            e: Union[
                RecognitionException,
                NoViableAltException,
                LexerNoViableAltException,
                InputMismatchException,
                FailedPredicateException
            ]
    ) -> None:
        """
        Method which will be called if the ANTLR4 Lexer or Parser detect
        an error inside the program
        """
        super().syntaxError(
            recognizer, offendingSymbol, line, column, msg, e
        )
