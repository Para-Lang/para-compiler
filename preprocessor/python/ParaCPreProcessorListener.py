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


    # Enter a parse tree produced by ParaCPreProcessorParser#coreLanguageItem.
    def enterCoreLanguageItem(self, ctx:ParaCPreProcessorParser.CoreLanguageItemContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#coreLanguageItem.
    def exitCoreLanguageItem(self, ctx:ParaCPreProcessorParser.CoreLanguageItemContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#preProcessorDirective.
    def enterPreProcessorDirective(self, ctx:ParaCPreProcessorParser.PreProcessorDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#preProcessorDirective.
    def exitPreProcessorDirective(self, ctx:ParaCPreProcessorParser.PreProcessorDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#complexDefineDirective.
    def enterComplexDefineDirective(self, ctx:ParaCPreProcessorParser.ComplexDefineDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#complexDefineDirective.
    def exitComplexDefineDirective(self, ctx:ParaCPreProcessorParser.ComplexDefineDirectiveContext):
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


    # Enter a parse tree produced by ParaCPreProcessorParser#lineDirective.
    def enterLineDirective(self, ctx:ParaCPreProcessorParser.LineDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#lineDirective.
    def exitLineDirective(self, ctx:ParaCPreProcessorParser.LineDirectiveContext):
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



del ParaCPreProcessorParser