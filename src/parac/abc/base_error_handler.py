# coding=utf-8
""" File containing the abstract base error listener """
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Union, TYPE_CHECKING

from antlr4.Token import CommonToken
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import (InputMismatchException,
                                 FailedPredicateException,
                                 RecognitionException,
                                 LexerNoViableAltException,
                                 NoViableAltException)
from ..exceptions import ParaCSyntaxError


if TYPE_CHECKING:
    from ..compiler.parser.python.ParaCParser import ParaCParser
    from ..preprocessor import ParaCPreProcessorParser


__all__ = [
    'BaseErrorListener',
]


class BaseErrorListener(ErrorListener, ABC):
    """
    Abstract class serving as the base for the error listeners in Para-C, which
    are used with Antlr4.

    Possible Antlr4 errors:

    - RecognitionException:
        The superclass of all exceptions thrown by an ANTLR-generated
        recognizer. It’s a subclass of RuntimeException to avoid the hassles
        of checked exceptions. This exception records where the recognizer
        (lexer or parser) was in the input, where it was in the ATN (internal
        graph data structure representing the grammar), the rule invocation
        stack, and what kind of problem occurred.
    - NoViableAltException:
        Indicates that the parser could not decide which of two or more paths
        to take by looking at the remaining input. This exception tracks the
        starting token of the offending input and also knows where the parser
        was in the various paths when the error occurred.
    - LexerNoViableAltException:
        The equivalent of NoViableAltException but for lexers only.
    - InputMismatchException:
        The current input Token does not match what the parser expected.
    - FailedPredicateException:
        A semantic predicate that evaluates to false during prediction renders
        the surrounding alternative nonviable. Prediction occurs when a rule
        is predicting which alternative to take. If all viable paths
        disappear, parser will throw NoViableAltException. This predicate
        gets thrown by the parser when a semantic predicate evaluates to
        false outside of prediction, during the normal parsing process of
        matching tokens and calling rules.
    """

    @abstractmethod
    def __init__(self):
        self.errors = [

        ]

    @abstractmethod
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

    @abstractmethod
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

    @abstractmethod
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

    @abstractmethod
    def syntaxError(
            self,
            recognizer: Union[ParaCParser, ParaCPreProcessorParser],
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
        an error inside the given input.
        """
        self.errors.append(
            ParaCSyntaxError(
                recognizer,
                offendingSymbol,
                line,
                column,
                msg
            )
        )
