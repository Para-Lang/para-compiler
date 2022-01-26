# Generated from ./ParaPreProcessor.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParaPreProcessorParser import ParaPreProcessorParser
else:
    from ParaPreProcessorParser import ParaPreProcessorParser

# This class defines a complete listener for a parse tree produced by ParaPreProcessorParser.
class ParaPreProcessorListener(ParseTreeListener):

    # Enter a parse tree produced by ParaPreProcessorParser#compilationUnit.
    def enterCompilationUnit(self, ctx:ParaPreProcessorParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#compilationUnit.
    def exitCompilationUnit(self, ctx:ParaPreProcessorParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#translationUnit.
    def enterTranslationUnit(self, ctx:ParaPreProcessorParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#translationUnit.
    def exitTranslationUnit(self, ctx:ParaPreProcessorParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#externalItem.
    def enterExternalItem(self, ctx:ParaPreProcessorParser.ExternalItemContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#externalItem.
    def exitExternalItem(self, ctx:ParaPreProcessorParser.ExternalItemContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#nonPreProcessorItemSequence.
    def enterNonPreProcessorItemSequence(self, ctx:ParaPreProcessorParser.NonPreProcessorItemSequenceContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#nonPreProcessorItemSequence.
    def exitNonPreProcessorItemSequence(self, ctx:ParaPreProcessorParser.NonPreProcessorItemSequenceContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#preProcessorDirective.
    def enterPreProcessorDirective(self, ctx:ParaPreProcessorParser.PreProcessorDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#preProcessorDirective.
    def exitPreProcessorDirective(self, ctx:ParaPreProcessorParser.PreProcessorDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#selectionPreProcessorDirective.
    def enterSelectionPreProcessorDirective(self, ctx:ParaPreProcessorParser.SelectionPreProcessorDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#selectionPreProcessorDirective.
    def exitSelectionPreProcessorDirective(self, ctx:ParaPreProcessorParser.SelectionPreProcessorDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#startOfSelectionBlock.
    def enterStartOfSelectionBlock(self, ctx:ParaPreProcessorParser.StartOfSelectionBlockContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#startOfSelectionBlock.
    def exitStartOfSelectionBlock(self, ctx:ParaPreProcessorParser.StartOfSelectionBlockContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#selectionDirectiveAlternatives.
    def enterSelectionDirectiveAlternatives(self, ctx:ParaPreProcessorParser.SelectionDirectiveAlternativesContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#selectionDirectiveAlternatives.
    def exitSelectionDirectiveAlternatives(self, ctx:ParaPreProcessorParser.SelectionDirectiveAlternativesContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#selectionElseDirective.
    def enterSelectionElseDirective(self, ctx:ParaPreProcessorParser.SelectionElseDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#selectionElseDirective.
    def exitSelectionElseDirective(self, ctx:ParaPreProcessorParser.SelectionElseDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#selectionBlock.
    def enterSelectionBlock(self, ctx:ParaPreProcessorParser.SelectionBlockContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#selectionBlock.
    def exitSelectionBlock(self, ctx:ParaPreProcessorParser.SelectionBlockContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#includeDirective.
    def enterIncludeDirective(self, ctx:ParaPreProcessorParser.IncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#includeDirective.
    def exitIncludeDirective(self, ctx:ParaPreProcessorParser.IncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#fileIncludeDirective.
    def enterFileIncludeDirective(self, ctx:ParaPreProcessorParser.FileIncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#fileIncludeDirective.
    def exitFileIncludeDirective(self, ctx:ParaPreProcessorParser.FileIncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#computedIncludeDirective.
    def enterComputedIncludeDirective(self, ctx:ParaPreProcessorParser.ComputedIncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#computedIncludeDirective.
    def exitComputedIncludeDirective(self, ctx:ParaPreProcessorParser.ComputedIncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#ifNotDefinedDirective.
    def enterIfNotDefinedDirective(self, ctx:ParaPreProcessorParser.IfNotDefinedDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#ifNotDefinedDirective.
    def exitIfNotDefinedDirective(self, ctx:ParaPreProcessorParser.IfNotDefinedDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#ifDefinedDirective.
    def enterIfDefinedDirective(self, ctx:ParaPreProcessorParser.IfDefinedDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#ifDefinedDirective.
    def exitIfDefinedDirective(self, ctx:ParaPreProcessorParser.IfDefinedDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#elIfNotDefinedDirective.
    def enterElIfNotDefinedDirective(self, ctx:ParaPreProcessorParser.ElIfNotDefinedDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#elIfNotDefinedDirective.
    def exitElIfNotDefinedDirective(self, ctx:ParaPreProcessorParser.ElIfNotDefinedDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#elIfDefinedDirective.
    def enterElIfDefinedDirective(self, ctx:ParaPreProcessorParser.ElIfDefinedDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#elIfDefinedDirective.
    def exitElIfDefinedDirective(self, ctx:ParaPreProcessorParser.ElIfDefinedDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#ifDirective.
    def enterIfDirective(self, ctx:ParaPreProcessorParser.IfDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#ifDirective.
    def exitIfDirective(self, ctx:ParaPreProcessorParser.IfDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#elIfDirective.
    def enterElIfDirective(self, ctx:ParaPreProcessorParser.ElIfDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#elIfDirective.
    def exitElIfDirective(self, ctx:ParaPreProcessorParser.ElIfDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#elseDirective.
    def enterElseDirective(self, ctx:ParaPreProcessorParser.ElseDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#elseDirective.
    def exitElseDirective(self, ctx:ParaPreProcessorParser.ElseDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#endIfDirective.
    def enterEndIfDirective(self, ctx:ParaPreProcessorParser.EndIfDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#endIfDirective.
    def exitEndIfDirective(self, ctx:ParaPreProcessorParser.EndIfDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#pragmaDirective.
    def enterPragmaDirective(self, ctx:ParaPreProcessorParser.PragmaDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#pragmaDirective.
    def exitPragmaDirective(self, ctx:ParaPreProcessorParser.PragmaDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#errorDirective.
    def enterErrorDirective(self, ctx:ParaPreProcessorParser.ErrorDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#errorDirective.
    def exitErrorDirective(self, ctx:ParaPreProcessorParser.ErrorDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#undefDirective.
    def enterUndefDirective(self, ctx:ParaPreProcessorParser.UndefDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#undefDirective.
    def exitUndefDirective(self, ctx:ParaPreProcessorParser.UndefDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#complexDefineDirective.
    def enterComplexDefineDirective(self, ctx:ParaPreProcessorParser.ComplexDefineDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#complexDefineDirective.
    def exitComplexDefineDirective(self, ctx:ParaPreProcessorParser.ComplexDefineDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#libIncludeDirective.
    def enterLibIncludeDirective(self, ctx:ParaPreProcessorParser.LibIncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#libIncludeDirective.
    def exitLibIncludeDirective(self, ctx:ParaPreProcessorParser.LibIncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#stringIncludeDirective.
    def enterStringIncludeDirective(self, ctx:ParaPreProcessorParser.StringIncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#stringIncludeDirective.
    def exitStringIncludeDirective(self, ctx:ParaPreProcessorParser.StringIncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#lineDirective.
    def enterLineDirective(self, ctx:ParaPreProcessorParser.LineDirectiveContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#lineDirective.
    def exitLineDirective(self, ctx:ParaPreProcessorParser.LineDirectiveContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#nonPreProcessorItem.
    def enterNonPreProcessorItem(self, ctx:ParaPreProcessorParser.NonPreProcessorItemContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#nonPreProcessorItem.
    def exitNonPreProcessorItem(self, ctx:ParaPreProcessorParser.NonPreProcessorItemContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#anySequence.
    def enterAnySequence(self, ctx:ParaPreProcessorParser.AnySequenceContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#anySequence.
    def exitAnySequence(self, ctx:ParaPreProcessorParser.AnySequenceContext):
        pass


    # Enter a parse tree produced by ParaPreProcessorParser#preProcessorEnd.
    def enterPreProcessorEnd(self, ctx:ParaPreProcessorParser.PreProcessorEndContext):
        pass

    # Exit a parse tree produced by ParaPreProcessorParser#preProcessorEnd.
    def exitPreProcessorEnd(self, ctx:ParaPreProcessorParser.PreProcessorEndContext):
        pass



del ParaPreProcessorParser