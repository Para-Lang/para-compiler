# coding=utf-8
"""
File containing the functions and class for the Pre-Processor parsing process
"""

import logging
from os import PathLike
from typing import Union
from click.utils import WIN
import antlr4

from .listener import Listener
from .ctx import ProgramPreProcessorContext
from .python.ParaCPreProcessorParser import ParaCPreProcessorParser
from .python.ParaCPreProcessorLexer import ParaCPreProcessorLexer

from .error_handler import PreProcessorErrorListener

__all__ = [
    'SEPARATOR',
    'PreProcessor',
    'PreProcessorProcessResult'
]

logger = logging.getLogger(__name__)

SEPARATOR = "\\" if WIN else "/"


class PreProcessorProcessResult:
    """
    The result of a Pre-Processor parse_and_process() call
    """


class PreProcessor:
    """
    The Pre-Processor, which handles directives in a Para-C file.

    The incoming files will be tokenized and parsed using Antlr4. The generated
    logic tree will be used by the Pre-Processor listener to generate a
    FilePreProcessorContext instance for the file and then process everything
    appropriately with the ProgramPreProcessorContext. After generation, the
    preprocessor will walk through and modify the file based on the directives.
    The output will be a file-stream / str, which can be used to write to a
    file or parsed to the main Para-C compiler for further processing.
    """

    @staticmethod
    def get_file_stream(
            path: Union[str, PathLike], encoding: str
    ) -> antlr4.FileStream:
        """ Fetches the FileStream from a file"""
        stream = antlr4.FileStream(path, encoding)
        stream.name = path.split(SEPARATOR)[-1]
        return stream

    @staticmethod
    def parse(
            input_stream: antlr4.FileStream,
            enable_out: bool = True
    ) -> ParaCPreProcessorParser.CompilationUnitContext:
        """
        Parses the passed input_stream using antlr4 and returns the
        compilation unit context which can be used with the listener to
        process the file and generate a logic stream

        :param input_stream: The token stream of the file
        :param enable_out: If set to True errors, warnings and info will be
                   logged onto the console using the local logger
                   instance. (Errors will then NOT be raised but only
                   logged)
        :returns: The compilationUnit (file) context
        """
        # Error handler which uses the default error strategy to handle the
        # incoming antlr4 errors
        error_listener = PreProcessorErrorListener(enable_out)

        # Initialising the lexer, which will tokenize the input_stream and
        # raise basic errors if needed
        lexer = ParaCPreProcessorLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        logger.debug("Lexing the file and generating the tokens")

        # Parsing the lexer and generating a token stream
        stream = antlr4.CommonTokenStream(lexer)

        logger.debug("Parsing the tokens and generating the logic tree")

        # Parser which generates based on the top entry rule the logic tree
        parser = ParaCPreProcessorParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        return parser.compilationUnit()

    @staticmethod
    def process_directives(
            ctx: ProgramPreProcessorContext,
            enable_out: bool = True
    ) -> PreProcessorProcessResult:
        """ Processing the directives populated in the passed ctx """
        ...

    @classmethod
    def parse_and_process(
            cls,
            ctx: ProgramPreProcessorContext,
            enable_out: bool = True
    ) -> PreProcessorProcessResult:
        """
        Parses the files and processes the directives inside of them. To
        generate the source file use ProgramPreProcessorContext.gen_source()

        This function only modifies the context

        :returns: A preprocessor result instance
        """
        from paraccompiler import get_relative_file_name

        stream = cls.get_file_stream(
            ctx.process.entry_file_path, ctx.encoding
        )
        relative_file_name = get_relative_file_name(
            file_name=stream.name,
            file_path=stream.fileName,
            base_path=ctx.work_dir
        )
        antlr4_file_ctx = cls.parse(stream, enable_out)
        
        listener = Listener(antlr4_file_ctx, stream, relative_file_name)
        listener.walk_and_process_directives(enable_out)
        ctx.set_entry_ctx(listener.get_file_ctx(), relative_file_name)

        return cls.process_directives(ctx)
