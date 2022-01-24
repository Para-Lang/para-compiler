# coding=utf-8
""" Logic Tree Listener for the Para Pre-Processor """
import logging
from typing import Optional

import antlr4

from .ctx import FilePreProcessorContext, ProgramPreProcessorContext
from .logic_stream import PreProcessorStream
from .logic_tokens import *
from .parser import (ParaPreProcessorListener,
                     ParaPreProcessorParser as Parser)

__all__ = [
    'Listener'
]

logger = logging.getLogger(__name__)


class Listener(ParaPreProcessorListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaPreProcessorListener and then define the
    wanted behaviour inside the preprocessor processing.
    """

    def __init__(
            self,
            antlr4_file_ctx: Parser.CompilationUnitContext,
            file_stream: antlr4.InputStream,
            relative_file_name: str,
            program_ctx: ProgramPreProcessorContext
    ):
        self._file_ctx = FilePreProcessorContext(
            relative_file_name, program_ctx
        )
        self.antlr4_file_ctx: Parser.CompilationUnitContext = antlr4_file_ctx
        self.file_stream: antlr4.InputStream = file_stream
        self._prefer_logging = False

        self._current_external_item: Optional[ExternalPreProcessorItem] = None

    @property
    def logic_stream(self) -> PreProcessorStream:
        """ Stream which stores the logical tokens for the passed file. """
        return self._file_ctx.logic_stream

    @property
    def file_ctx(self) -> FilePreProcessorContext:
        """ The file context for this class """
        return self._file_ctx

    async def walk_and_process_directives(
            self, prefer_logging: bool
    ) -> None:
        """
        Walks through the passed compilation unit context and processes it.
        The file_ctx will be populated and able to be used for finishing
        the preprocessor processing steps

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """
        logger.debug(
            "Walking through the logic tree and generating logic stream"
        )
        self._prefer_logging = prefer_logging

        walker = antlr4.ParseTreeWalker()
        walker.walk(self, self.antlr4_file_ctx)

    def enterCompilationUnit(
            self,
            ctx: Parser.CompilationUnitContext
    ):
        """
        Enter a parse tree produced by parser#compilationUnit.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitCompilationUnit(
            self,
            ctx: Parser.CompilationUnitContext
    ):
        """
        Exit a parse tree produced by parser#compilationUnit.
        """
        logger.debug(
            "Finished walk through logic tree and finished generation"
            " of logic stream"
        )

    def enterTranslationUnit(
            self,
            ctx: Parser.TranslationUnitContext
    ):
        """
        Enter a parse tree produced by parser#translationUnit.
        """
        ...

    def exitTranslationUnit(
            self,
            ctx: Parser.TranslationUnitContext
    ):
        """
        Exit a parse tree produced by parser#translationUnit.
        """
        ...

    def enterExternalItem(
            self,
            ctx: Parser.ExternalItemContext
    ):
        """
        Enter a parse tree produced by parser#externalItem.
        """
        item = ExternalPreProcessorItem(self._file_ctx, ctx)
        self._current_external_item = item
        self.logic_stream.append_antlr_ctx(item)

    def exitExternalItem(
            self,
            ctx: Parser.ExternalItemContext
    ):
        """
        Exit a parse tree produced by parser#externalItem.
        """
        # Resetting the value
        self._current_external_item = None

    def enterPreProcessorDirective(
            self,
            ctx: Parser.PreProcessorDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#preProcessorDirective.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitPreProcessorDirective(
            self,
            ctx: Parser.PreProcessorDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#preProcessorDirective.
        """
        ...

    def enterSelectionPreProcessorDirective(
            self,
            ctx: Parser.SelectionPreProcessorDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#selectionPreProcessorDirective.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitSelectionPreProcessorDirective(
            self,
            ctx: Parser.SelectionPreProcessorDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#selectionPreProcessorDirective.
        """
        ...

    def enterStartOfSelectionBlock(
            self,
            ctx: Parser.StartOfSelectionBlockContext
    ):
        """
        Enter a parse tree produced by parser#startSelectionBlock.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitStartOfSelectionBlock(
            self,
            ctx: Parser.StartOfSelectionBlockContext
    ):
        """
        Exit a parse tree produced by parser#startSelectionBlock.
        """
        ...

    def enterSelectionDirectiveAlternatives(
            self,
            ctx: Parser.SelectionDirectiveAlternativesContext
    ):
        """
        Enter a parse tree produced by parser#logicalDirectiveAlternatives.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitSelectionDirectiveAlternatives(
            self,
            ctx: Parser.SelectionDirectiveAlternativesContext
    ):
        """
        Exit a parse tree produced by parser#logicalDirectiveAlternatives.
        """
        ...

    def enterSelectionElseDirective(
            self,
            ctx: Parser.SelectionElseDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#logicalElseDirective.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitSelectionElseDirective(
            self,
            ctx: Parser.SelectionElseDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#logicalElseDirective.
        """
        ...

    def enterErrorDirective(
            self,
            ctx: Parser.ErrorDirectiveContext):
        """
        Enter a parse tree produced by ParaPreProcessorParser#errorDirective.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitErrorDirective(
            self,
            ctx: Parser.ErrorDirectiveContext):
        """
        Exit a parse tree produced by ParaPreProcessorParser#errorDirective.
        """
        ...

    def enterLineDirective(
            self,
            ctx: Parser.LineDirectiveContext):
        """
        Enter a parse tree produced by ParaPreProcessorParser#lineDirective.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitLineDirective(
            self,
            ctx: Parser.LineDirectiveContext):
        """
        Exit a parse tree produced by ParaPreProcessorParser#lineDirective.
        """
        ...

    def enterIncludeDirective(
            self,
            ctx: Parser.IncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#includeDirective.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitIncludeDirective(
            self,
            ctx: Parser.IncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#includeDirective.
        """
        ...

    def enterFileIncludeDirective(
            self,
            ctx: Parser.FileIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#fileIncludeDirective.
        """
        ...

    def exitFileIncludeDirective(
            self,
            ctx: Parser.FileIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#fileIncludeDirective.
        """
        ...

    def enterComputedIncludeDirective(
            self,
            ctx: Parser.ComputedIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#computedIncludeDirective.
        """
        ...

    def exitComputedIncludeDirective(
            self,
            ctx: Parser.ComputedIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#computedIncludeDirective.
        """
        ...

    def enterComplexDefineDirective(
            self,
            ctx: Parser.ComplexDefineDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#complexDefineDirective.
        """
        ...

    def exitComplexDefineDirective(
            self,
            ctx: Parser.ComplexDefineDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#complexDefineDirective.
        """
        ...

    def enterPragmaDirective(
            self,
            ctx: Parser.PragmaDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#pragmaDirective.
        """
        ...

    def exitPragmaDirective(
            self,
            ctx: Parser.PragmaDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#pragmaDirective.
        """
        ...

    def enterUndefDirective(
            self,
            ctx: Parser.UndefDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#undefDirective.
        """
        ...

    def exitUndefDirective(
            self,
            ctx: Parser.UndefDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#undefDirective.
        """
        ...

    def enterIfNotDefinedDirective(
            self,
            ctx: Parser.IfNotDefinedDirectiveContext
    ):
        """
        Enter a parse tree produced by
         ParaPreProcessorParser#ifNotDefinedDirective.
        """
        ...

    def exitIfNotDefinedDirective(
            self,
            ctx: Parser.IfNotDefinedDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaPreProcessorParser#ifNotDefinedDirective.
        """
        ...

    #
    def enterIfDefinedDirective(
            self,
            ctx: Parser.IfDefinedDirectiveContext
    ):
        """
        Enter a parse tree produced by
        ParaPreProcessorParser#ifDefinedDirective.
        """
        ...

    def exitIfDefinedDirective(
            self,
            ctx: Parser.IfDefinedDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaPreProcessorParser#ifDefinedDirective.
        """
        ...

    def enterElIfNotDefinedDirective(
            self,
            ctx: Parser.ElIfNotDefinedDirectiveContext
    ):
        """
        Enter a parse tree produced by
         ParaPreProcessorParser#elIfNotDefinedDirective.
        """
        ...

    def exitElIfNotDefinedDirective(
            self,
            ctx: Parser.ElIfNotDefinedDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaPreProcessorParser#elIfNotDefinedDirective.
        """
        ...

    def enterElIfDefinedDirective(
            self,
            ctx: Parser.ElIfDefinedDirectiveContext
    ):
        """
        Enter a parse tree produced by
        ParaPreProcessorParser#elIfDefinedDirective.
        """
        ...

    def exitElIfDefinedDirective(
            self,
            ctx: Parser.ElIfDefinedDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaPreProcessorParser#elIfDefinedDirective.
        """
        ...

    def enterIfDirective(
            self,
            ctx: Parser.IfDirectiveContext
    ):
        """
        Enter a parse tree produced by ParaPreProcessorParser#ifDirective.
        """
        ...

    def exitIfDirective(
            self,
            ctx: Parser.IfDirectiveContext
    ):
        """
        Exit a parse tree produced by ParaPreProcessorParser#ifDirective.
        """
        ...

    def enterElIfDirective(
            self,
            ctx: Parser.ElIfDirectiveContext
    ):
        """
        Enter a parse tree produced by ParaPreProcessorParser#elIfDirective.
        """
        ...

    def exitElIfDirective(
            self,
            ctx: Parser.ElIfDirectiveContext
    ):
        """
        Exit a parse tree produced by ParaPreProcessorParser#elIfDirective.
        """
        ...

    def enterElseDirective(
            self,
            ctx: Parser.ElseDirectiveContext
    ):
        """
        Enter a parse tree produced by ParaPreProcessorParser#elseDirective.
        """
        ...

    def exitElseDirective(
            self,
            ctx: Parser.ElseDirectiveContext
    ):
        """
        Exit a parse tree produced by ParaPreProcessorParser#elseDirective.
        """
        ...

    def enterEndIfDirective(
            self,
            ctx: Parser.EndIfDirectiveContext
    ):
        """
        Enter a parse tree produced by ParaPreProcessorParser#endIfDirective.
        """
        ...

    def exitEndIfDirective(
            self,
            ctx: Parser.EndIfDirectiveContext
    ):
        """
        Exit a parse tree produced by ParaPreProcessorParser#endIfDirective.
        """
        ...

    def enterLibIncludeDirective(
            self,
            ctx: Parser.LibIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by
        ParaPreProcessorParser#libIncludeDirective.
        """
        ...

    def exitLibIncludeDirective(
            self,
            ctx: Parser.LibIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaPreProcessorParser#libIncludeDirective.
        """
        ...

    def enterStringIncludeDirective(
            self,
            ctx: Parser.StringIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by
         ParaPreProcessorParser#stringIncludeDirective.
        """
        ...

    def exitStringIncludeDirective(
            self,
            ctx: Parser.StringIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by
        ParaPreProcessorParser#stringIncludeDirective.
        """
        ...

    def enterNonPreProcessorItem(
            self,
            ctx: Parser.NonPreProcessorItemContext
    ):
        """
        Enter a parse tree produced by
        ParaPreProcessorParser#nonPreProcessorItem.
        """
        self.logic_stream.append_antlr_ctx(ctx)

    def exitNonPreProcessorItem(
            self,
            ctx: Parser.NonPreProcessorItemContext
    ):
        """
        Exit a parse tree produced by
        ParaPreProcessorParser#nonPreProcessorItem.
        """
        ...

    def enterAnySequence(
            self,
            ctx: Parser.AnySequenceContext
    ):
        """
        Enter a parse tree produced by ParaPreProcessorParser#anySequence.
        """
        ...

    def exitAnySequence(
            self,
            ctx: Parser.AnySequenceContext
    ):
        """
        Exit a parse tree produced by ParaPreProcessorParser#anySequence.
        """
        ...

    def enterPreProcessorEnd(
            self,
            ctx: Parser.PreProcessorEndContext
    ):
        """
        Enter a parse tree produced by ParaPreProcessorParser#preProcessorEnd.
        """
        ...

    def exitPreProcessorEnd(
            self,
            ctx: Parser.PreProcessorEndContext
    ):
        """
        Exit a parse tree produced by ParaPreProcessorParser#preProcessorEnd.
        """
        ...
