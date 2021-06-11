# coding=utf-8
""" Implementation for the antlr generated lexer, parser and tokeniser """
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
    def enterRule(self, ctx):
        print(">")

    def exitRule(self, ctx):
        print("<")


class ParacErrorListener(ErrorListener):
    """ Error-Listener for the Para-C compiler """

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        ...


def parse_file(file_path: Union[str, PathLike], encoding: str = 'ascii'):
    """ Parses the specified file and returns the parsed tree """
    input_stream = antlr4.FileStream(file_path, encoding)
    error_listener = ParacErrorListener()
    lexer = ParaCLexer.ParaCLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = antlr4.CommonTokenStream(lexer)
    parser = ParaCParser.ParaCParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    tree = parser.expression()

    printer = Listener()
    walker = antlr4.ParseTreeWalker()
    walker.walk(printer, tree)

    return tree
