# coding=utf-8
""" Listener Class """
from __future__ import annotations

import logging
import antlr4
from typing import Optional

from .python import ParaListener
from .python import ParaParser
from ..parse_stream import ParaQualifiedParseStream

logger = logging.getLogger(__name__)


__all__ = [
    'Listener'
]


class Listener(ParaListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaListener and then define the wanted
    behaviour inside a compilation.
    """

    def __init__(
            self,
            antlr4_file_ctx: ParaParser.CompilationUnitContext
    ):
        self._antlr4_file_ctx: ParaParser.CompilationUnitContext = \
            antlr4_file_ctx
        self._prefer_logging: bool = False
        self._current_external_item = None
        self._parse_stream: Optional[ParaQualifiedParseStream] = None
        self._running = False

    @property
    def antlr4_file_ctx(self) -> ParaParser.CompilationUnitContext:
        """
        The antlr4 file ctx, which represents the entire file in a logic
        tree made up of tokens
        """
        return self._antlr4_file_ctx

    @property
    def running(self) -> bool:
        """ Returns whether at the moment a stream generation is being run """
        return self._running

    async def walk(
            self, prefer_logging: bool
    ) -> ParaQualifiedParseStream:
        """
        Walks through the parsed CompilationUnitContext and listens to the
        events / goes through the tokens and generates a logic stream.

        The FileCompilationContext can then be used inside the
        CompilationContext to be linked with other files and to finish
        the compilation for the program.

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """
        if self._running:
            raise RuntimeError("May not run two generations at the same time!")

        self._parse_stream = ParaQualifiedParseStream()
        self._running = True

        logger.debug(
            "Walking through parse tree and generating the logic stream"
        )
        self._prefer_logging: bool = prefer_logging

        walker = antlr4.ParseTreeWalker()
        walker.walk(self, self.antlr4_file_ctx)

        self._running = False
        return self._parse_stream

    # =========================================
    # Beginning of the file
    # =========================================
    def enterCompilationUnit(
            self,
            ctx: ParaParser.CompilationUnitContext
    ):
        """
        Enter a parse tree produced by ParaParser#compilationUnit.

        Is the base from where the tree is going to start (starts at the first
        token of the file and ends at the last token)
        """
        logger.debug("Starting file parsing")

    # =========================================
    # End of the file
    # =========================================
    def exitCompilationUnit(
            self,
            ctx: ParaParser.CompilationUnitContext
    ):
        """
        Exit a parse tree produced by ParaParser#compilationUnit.

        Is the point where the token stream will end. (EOF excluded)
        """
        logger.debug("Finished file parsing")


    # TODO! Implement listener functions and parsing algorithm
