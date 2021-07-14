# Generated from ./grammar/ParaCPreProcessor.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParaCPreProcessorParser import ParaCPreProcessorParser
else:
    from ParaCPreProcessorParser import ParaCPreProcessorParser

# This class defines a complete listener for a parse tree produced by ParaCPreProcessorParser.
class ParaCPreProcessorListener(ParseTreeListener):

    # Enter a parse tree produced by ParaCPreProcessorParser#compilationUnit.
    def enterCompilationUnit(self, ctx:ParaCPreProcessorParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#compilationUnit.
    def exitCompilationUnit(self, ctx:ParaCPreProcessorParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#translationUnit.
    def enterTranslationUnit(self, ctx:ParaCPreProcessorParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#translationUnit.
    def exitTranslationUnit(self, ctx:ParaCPreProcessorParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#externalItem.
    def enterExternalItem(self, ctx:ParaCPreProcessorParser.ExternalItemContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#externalItem.
    def exitExternalItem(self, ctx:ParaCPreProcessorParser.ExternalItemContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#nonPreProcessorItemSequence.
    def enterNonPreProcessorItemSequence(self, ctx:ParaCPreProcessorParser.NonPreProcessorItemSequenceContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#nonPreProcessorItemSequence.
    def exitNonPreProcessorItemSequence(self, ctx:ParaCPreProcessorParser.NonPreProcessorItemSequenceContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#preProcessorDirective.
    def enterPreProcessorDirective(self, ctx:ParaCPreProcessorParser.PreProcessorDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#preProcessorDirective.
    def exitPreProcessorDirective(self, ctx:ParaCPreProcessorParser.PreProcessorDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#selectionPreProcessorDirective.
    def enterSelectionPreProcessorDirective(self, ctx:ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#selectionPreProcessorDirective.
    def exitSelectionPreProcessorDirective(self, ctx:ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#startOfSelectionBlock.
    def enterStartOfSelectionBlock(self, ctx:ParaCPreProcessorParser.StartOfSelectionBlockContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#startOfSelectionBlock.
    def exitStartOfSelectionBlock(self, ctx:ParaCPreProcessorParser.StartOfSelectionBlockContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#selectionDirectiveAlternatives.
    def enterSelectionDirectiveAlternatives(self, ctx:ParaCPreProcessorParser.SelectionDirectiveAlternativesContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#selectionDirectiveAlternatives.
    def exitSelectionDirectiveAlternatives(self, ctx:ParaCPreProcessorParser.SelectionDirectiveAlternativesContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#selectionElseDirective.
    def enterSelectionElseDirective(self, ctx:ParaCPreProcessorParser.SelectionElseDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#selectionElseDirective.
    def exitSelectionElseDirective(self, ctx:ParaCPreProcessorParser.SelectionElseDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#selectionBlock.
    def enterSelectionBlock(self, ctx:ParaCPreProcessorParser.SelectionBlockContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#selectionBlock.
    def exitSelectionBlock(self, ctx:ParaCPreProcessorParser.SelectionBlockContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#includeDirective.
    def enterIncludeDirective(self, ctx:ParaCPreProcessorParser.IncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#includeDirective.
    def exitIncludeDirective(self, ctx:ParaCPreProcessorParser.IncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#fileIncludeDirective.
    def enterFileIncludeDirective(self, ctx:ParaCPreProcessorParser.FileIncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#fileIncludeDirective.
    def exitFileIncludeDirective(self, ctx:ParaCPreProcessorParser.FileIncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#computedIncludeDirective.
    def enterComputedIncludeDirective(self, ctx:ParaCPreProcessorParser.ComputedIncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#computedIncludeDirective.
    def exitComputedIncludeDirective(self, ctx:ParaCPreProcessorParser.ComputedIncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#ifNotDefinedDirective.
    def enterIfNotDefinedDirective(self, ctx:ParaCPreProcessorParser.IfNotDefinedDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#ifNotDefinedDirective.
    def exitIfNotDefinedDirective(self, ctx:ParaCPreProcessorParser.IfNotDefinedDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#ifDefinedDirective.
    def enterIfDefinedDirective(self, ctx:ParaCPreProcessorParser.IfDefinedDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#ifDefinedDirective.
    def exitIfDefinedDirective(self, ctx:ParaCPreProcessorParser.IfDefinedDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#elIfNotDefinedDirective.
    def enterElIfNotDefinedDirective(self, ctx:ParaCPreProcessorParser.ElIfNotDefinedDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#elIfNotDefinedDirective.
    def exitElIfNotDefinedDirective(self, ctx:ParaCPreProcessorParser.ElIfNotDefinedDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#elIfDefinedDirective.
    def enterElIfDefinedDirective(self, ctx:ParaCPreProcessorParser.ElIfDefinedDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#elIfDefinedDirective.
    def exitElIfDefinedDirective(self, ctx:ParaCPreProcessorParser.ElIfDefinedDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#ifDirective.
    def enterIfDirective(self, ctx:ParaCPreProcessorParser.IfDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#ifDirective.
    def exitIfDirective(self, ctx:ParaCPreProcessorParser.IfDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#elIfDirective.
    def enterElIfDirective(self, ctx:ParaCPreProcessorParser.ElIfDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#elIfDirective.
    def exitElIfDirective(self, ctx:ParaCPreProcessorParser.ElIfDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#elseDirective.
    def enterElseDirective(self, ctx:ParaCPreProcessorParser.ElseDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#elseDirective.
    def exitElseDirective(self, ctx:ParaCPreProcessorParser.ElseDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#endIfDirective.
    def enterEndIfDirective(self, ctx:ParaCPreProcessorParser.EndIfDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#endIfDirective.
    def exitEndIfDirective(self, ctx:ParaCPreProcessorParser.EndIfDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#pragmaDirective.
    def enterPragmaDirective(self, ctx:ParaCPreProcessorParser.PragmaDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#pragmaDirective.
    def exitPragmaDirective(self, ctx:ParaCPreProcessorParser.PragmaDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#errorDirective.
    def enterErrorDirective(self, ctx:ParaCPreProcessorParser.ErrorDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#errorDirective.
    def exitErrorDirective(self, ctx:ParaCPreProcessorParser.ErrorDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#undefDirective.
    def enterUndefDirective(self, ctx:ParaCPreProcessorParser.UndefDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#undefDirective.
    def exitUndefDirective(self, ctx:ParaCPreProcessorParser.UndefDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#complexDefineDirective.
    def enterComplexDefineDirective(self, ctx:ParaCPreProcessorParser.ComplexDefineDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#complexDefineDirective.
    def exitComplexDefineDirective(self, ctx:ParaCPreProcessorParser.ComplexDefineDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#libIncludeDirective.
    def enterLibIncludeDirective(self, ctx:ParaCPreProcessorParser.LibIncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#libIncludeDirective.
    def exitLibIncludeDirective(self, ctx:ParaCPreProcessorParser.LibIncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#stringIncludeDirective.
    def enterStringIncludeDirective(self, ctx:ParaCPreProcessorParser.StringIncludeDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#stringIncludeDirective.
    def exitStringIncludeDirective(self, ctx:ParaCPreProcessorParser.StringIncludeDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#lineDirective.
    def enterLineDirective(self, ctx:ParaCPreProcessorParser.LineDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#lineDirective.
    def exitLineDirective(self, ctx:ParaCPreProcessorParser.LineDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#nonPreProcessorItem.
    def enterNonPreProcessorItem(self, ctx:ParaCPreProcessorParser.NonPreProcessorItemContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#nonPreProcessorItem.
    def exitNonPreProcessorItem(self, ctx:ParaCPreProcessorParser.NonPreProcessorItemContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#anySequence.
    def enterAnySequence(self, ctx:ParaCPreProcessorParser.AnySequenceContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#anySequence.
    def exitAnySequence(self, ctx:ParaCPreProcessorParser.AnySequenceContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#preProcessorEnd.
    def enterPreProcessorEnd(self, ctx:ParaCPreProcessorParser.PreProcessorEndContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#preProcessorEnd.
    def exitPreProcessorEnd(self, ctx:ParaCPreProcessorParser.PreProcessorEndContext):
        pass



del ParaCPreProcessorParser