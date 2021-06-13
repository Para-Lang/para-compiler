# coding=utf-8
""" Implementation for the antlr generated lexer, parser and tokenizer """
from os import PathLike
from typing import Union
import antlr4
from antlr4.error.ErrorListener import ErrorListener

from . import ParaCLexer
from . import ParaCListener
from . import ParaCParser


class Listener(ParaCListener.ParaCListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaCListener and then define the wanted
    behaviour inside a compilation.
    """
    def enterExpr(self, ctx):
        print(">")

    def exitExpr(self, ctx):
        print("<")

    def enterOperation(self, ctx):
        print(">")

    def exitOperation(self, ctx):
        print("<")

    def enterEveryRule(self, ctx):
        print(">")

    def exitRule(self, ctx):
        print("<")


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
        ...


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
    # Parsing the lexer and generating a token stream
    stream = antlr4.CommonTokenStream(lexer)

    # Parser which should generate the logic trees
    parser = ParaCParser.ParaCParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.expression()

    # Listener which will perform certain actions based on the 'events'
    # received during walking through the file
    printer = Listener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(printer, tree)

    return tree
