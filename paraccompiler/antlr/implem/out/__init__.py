# coding=utf-8
""" Implementation for the antlr generated lexer, parser and tokenizer """
from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from os import PathLike
from typing import Union
import antlr4
from antlr4 import ParserRuleContext
from antlr4.error.ErrorListener import ErrorListener

from . import ParaCLexer
from . import ParaCListener
from . import ParaCParser


logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    # Assigning the variables to hold the imported classes for easier type
    # hinting and avoiding exceeding the line length
    _p = ParaCParser.ParaCParser
    ExpressionContext = _p.ExpressionContext
    FunctionDefinitionContext = _p.FunctionDefinitionContext
    AssignmentExpressionContext = _p.AssignmentExpressionContext


def log_parser_ctx(ctx: ParserRuleContext):
    """ Logs a Context and the associated information """
    items = ' '.join([i.symbol.text for i in ctx.children])
    logger.debug(
        f"Line {ctx.start.line} - {items}"
    )


class Listener(ParaCListener.ParaCListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaCListener and then define the wanted
    behaviour inside a compilation.
    """
    def enterPrimaryExpression(self, ctx: ExpressionContext):
        logger.debug("Enter Primary Expression")
        log_parser_ctx(ctx)

    def exitPrimaryExpression(self, ctx: ExpressionContext):
        logger.debug("Exit Primary Expression")

    def enterFunctionDefinition(self, ctx: FunctionDefinitionContext):
        logger.debug("Enter Function definition")
        log_parser_ctx(ctx)

    def exitFunctionDefinition(self, ctx: FunctionDefinitionContext):
        logger.debug("Exit Function definition")

    def enterAssignmentExpression(self, ctx: AssignmentExpressionContext):
        logger.debug("Enter Assignment expression")
        log_parser_ctx(ctx)

    def exitAssignmentExpression(self, ctx: AssignmentExpressionContext):
        logger.debug("Exit Assignment expression")


class ParacErrorListener(ErrorListener):
    """ Error-Listener for the Para-C compiler """

    def syntaxError(
            self,
            recognizer,
            offendingSymbol,
            line: int,
            column: int,
            msg: str,
            e):
        """
        Method which will be called if the ANTLR4 Lexer or Parser detect
        an error inside the program
        """
        logger.error(f"Error [{line}:{column}] > {msg}")


def parse_file(file_path: Union[str, PathLike], encoding: str = 'ascii'):
    """ Parses the specified file and returns the parsed tree """
    # Adding the File Stream based on the passed path
    input_stream = antlr4.FileStream(file_path, encoding)

    # Listener which will implement the ParaC exceptions
    error_listener = ParacErrorListener()

    # Initialising the lexer
    lexer = ParaCLexer.ParaCLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    logger.debug("Lexing the file and generating the tokens")
    # Parsing the lexer and generating a token stream
    stream = antlr4.CommonTokenStream(lexer)

    logger.debug("Parsing the tokens and generating the logic tree")
    # Parser which should generate the logic trees
    parser = ParaCParser.ParaCParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.primaryExpression()

    logger.debug("Walking through the tree")
    # Listener which will perform certain actions based on the 'events'
    # received during walking through the file
    listener = Listener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(listener, tree)

    return tree
