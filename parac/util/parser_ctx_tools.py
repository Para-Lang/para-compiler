# coding=utf-8
""" Management tools for the Parser Context Instances """
from antlr4 import InputStream, ParserRuleContext
from antlr4.Token import CommonToken


def get_input_stream_from_ctx(antlr4_ctx: ParserRuleContext) -> InputStream:
    """ Fetches the input stream from the passed context instance """
    return antlr4_ctx.start.getTokenSource().inputStream


def get_original_text(antlr4_ctx: ParserRuleContext) -> str:
    """ Fetches the original text from the passed context instance """
    input_stream = get_input_stream_from_ctx(antlr4_ctx)
    return input_stream.getText(
        antlr4_ctx.start.start, antlr4_ctx.stop.stop
    )


def get_original_text_from_token(token: CommonToken) -> str:
    """ Fetches the original text from the passed token instance """
    input_stream: InputStream = token.source[1]
    return input_stream.getText(
        token.start, token.stop
    )
