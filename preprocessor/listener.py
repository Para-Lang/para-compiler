# coding=utf-8
""" Logic Tree Listener for the Para-C Pre-Processor """
from typing import List
import logging
import antlr4

from .abc import PreProcessorLogicToken
from .python import ParaCPreProcessorListener
from .ctx import FilePreProcessorContext
from .python import ParaCPreProcessorParser as parser

_p = parser.ParaCPreProcessorParser


__all__ = [
    'Listener'
]

logger = logging.getLogger(__name__)


class Listener(ParaCPreProcessorListener.ParaCPreProcessorListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaCPreProcessorListener and then define the
    wanted behaviour inside the preprocessor processing.
    """

    def __init__(
            self,
            antlr4_file_ctx: _p.CompilationUnitContext,
            file_stream: antlr4.FileStream,
            relative_file_name: str
    ):
        self._file_ctx = FilePreProcessorContext(relative_file_name)
        self.antlr4_file_ctx = antlr4_file_ctx
        self.file_stream = file_stream
        self._enable_out = False

    @property
    def logic_stream(self) -> List[PreProcessorLogicToken]:
        """ Stream which stores the logical tokens for the passed file. """
        return self._file_ctx.logic_stream

    def get_file_ctx(self) -> FilePreProcessorContext:
        """ Fetches the file context for this class """
        return self._file_ctx

    def walk_and_process_directives(self, enable_out: bool) -> None:
        """
        Walks through the passed compilation unit context and processes it.
        The file_ctx will be populated and able to be used for finishing
        the preprocessor processing steps

        :param enable_out: If set to True errors, warnings and info will be
                           logged onto the console using the local logger
                           instance. If an exception is raised or error is
                           encountered, it will be reraised with the
                           FailedToProcessError.
        """
        logger.debug(
            "Walking through the logic tree and generating the logic stream"
        )
        self._enable_out = enable_out

    def enterCompilationUnit(
            self,
            ctx: _p.CompilationUnitContext
    ):
        """
        Enter a parse tree produced by parser#compilationUnit.
        """
        ...

    def exitCompilationUnit(
            self,
            ctx: _p.CompilationUnitContext
    ):
        """
        Exit a parse tree produced by parser#compilationUnit.
        """
        ...

    def enterTranslationUnit(
            self,
            ctx: _p.TranslationUnitContext
    ):
        """
        Enter a parse tree produced by parser#translationUnit.
        """
        ...

    def exitTranslationUnit(
            self,
            ctx: _p.TranslationUnitContext
    ):
        """
        Exit a parse tree produced by parser#translationUnit.
        """
        ...

    def enterExternalItem(
            self,
            ctx: _p.ExternalItemContext
    ):
        """
        Enter a parse tree produced by parser#externalItem.
        """
        ...

    def exitExternalItem(
            self,
            ctx: _p.ExternalItemContext
    ):
        """
        Exit a parse tree produced by parser#externalItem.
        """
        ...

    def enterCoreLanguageItem(
            self,
            ctx: _p.CoreLanguageItemContext
    ):
        """
        Enter a parse tree produced by parser#coreLanguageItem.
        """
        ...

    def exitCoreLanguageItem(
            self,
            ctx: _p.CoreLanguageItemContext
    ):
        """
        Exit a parse tree produced by parser#coreLanguageItem.
        """
        ...

    def enterPreProcessorDirective(
            self,
            ctx: _p.PreProcessorDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#preProcessorDirective.
        """
        ...

    def exitPreProcessorDirective(
            self,
            ctx: _p.PreProcessorDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#preProcessorDirective.
        """
        ...

    def enterSelectionPreProcessorDirective(
            self,
            ctx: _p.SelectionPreProcessorDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#selectionPreProcessorDirective.
        """
        ...

    def exitSelectionPreProcessorDirective(
            self,
            ctx: _p.SelectionPreProcessorDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#selectionPreProcessorDirective.
        """
        ...

    def enterStartOfSelectionBlock(
            self,
            ctx: _p.StartOfSelectionBlockContext
    ):
        """
        Enter a parse tree produced by parser#startSelectionBlock.
        """
        ...

    def exitStartOfSelectionBlock(
            self,
            ctx: _p.StartOfSelectionBlockContext
    ):
        """
        Exit a parse tree produced by parser#startSelectionBlock.
        """
        ...

    def enterSelectionDirectiveAlternatives(
            self,
            ctx: _p.SelectionDirectiveAlternativesContext
    ):
        """
        Enter a parse tree produced by parser#logicalDirectiveAlternatives.
        """
        ...

    def exitSelectionDirectiveAlternatives(
            self,
            ctx: _p.SelectionDirectiveAlternativesContext
    ):
        """
        Exit a parse tree produced by parser#logicalDirectiveAlternatives.
        """
        ...

    def enterSelectionElseDirective(
            self,
            ctx: _p.SelectionElseDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#logicalElseDirective.
        """
        ...

    def exitSelectionElseDirective(
            self,
            ctx: _p.SelectionElseDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#logicalElseDirective.
        """
        ...

    def enterErrorDirective(
            self,
            ctx: _p.ErrorDirectiveContext):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#errorDirective.
        """
        ...

    def exitErrorDirective(
            self,
            ctx: _p.ErrorDirectiveContext):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#errorDirective.
        """
        ...

    def enterLineDirective(
            self,
            ctx: _p.LineDirectiveContext):
        """
        Enter a parse tree produced by ParaCPreProcessorParser#lineDirective.
        """
        ...

    def exitLineDirective(
            self,
            ctx: _p.LineDirectiveContext):
        """
        Exit a parse tree produced by ParaCPreProcessorParser#lineDirective.
        """
        ...

    def enterIncludeDirective(
            self,
            ctx: _p.IncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#includeDirective.
        """
        ...

    def exitIncludeDirective(
            self,
            ctx: _p.IncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#includeDirective.
        """
        ...

    def enterFileIncludeDirective(
            self,
            ctx: _p.FileIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#fileIncludeDirective.
        """
        ...

    def exitFileIncludeDirective(
            self,
            ctx: _p.FileIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#fileIncludeDirective.
        """
        ...

    def enterComputedIncludeDirective(
            self,
            ctx: _p.ComputedIncludeDirectiveContext
    ):
        """
        Enter a parse tree produced by parser#computedIncludeDirective.
        """
        ...

    def exitComputedIncludeDirective(
            self,
            ctx: _p.ComputedIncludeDirectiveContext
    ):
        """
        Exit a parse tree produced by parser#computedIncludeDirective.
        """
        ...

    def enterComplexDefineDirective(
            self,
            ctx: _p.ComplexDefineDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#complexDefineDirective.
        """
        ...

    def exitComplexDefineDirective(
            self,
            ctx: _p.ComplexDefineDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#complexDefineDirective.
        """
        ...

    def enterPragmaDirective(
            self,
            ctx: _p.PragmaDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#pragmaDirective.
        """
        ...

    def exitPragmaDirective(
            self,
            ctx: _p.PragmaDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#pragmaDirective.
        """
        ...

    def enterUndefDirective(
            self,
            ctx: _p.UndefDirectiveContext
    ):
        """
        Enter a parse tree produced by _p#undefDirective.
        """
        ...

    def exitUndefDirective(
            self,
            ctx: _p.UndefDirectiveContext
    ):
        """
        Exit a parse tree produced by _p#undefDirective.
        """
        ...
