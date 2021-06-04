# coding=utf-8
"""
Core syntax analyser and tokenizer which mainly checks and validates the passed
code for correctness and if the logical input makes sense. This is at its core
a C-code analyser with additional Para-C keywords, grammar and logic added to
it
"""
from . import tokenizer
from . import syntax_analyser
from . import sematic_analyser
