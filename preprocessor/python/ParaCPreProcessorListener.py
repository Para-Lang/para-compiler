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


    # Enter a parse tree produced by ParaCPreProcessorParser#logicalPreProcessorDirective.
    def enterLogicalPreProcessorDirective(self, ctx:ParaCPreProcessorParser.LogicalPreProcessorDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#logicalPreProcessorDirective.
    def exitLogicalPreProcessorDirective(self, ctx:ParaCPreProcessorParser.LogicalPreProcessorDirectiveContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#startSelectionBlock.
    def enterStartSelectionBlock(self, ctx:ParaCPreProcessorParser.StartSelectionBlockContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#startSelectionBlock.
    def exitStartSelectionBlock(self, ctx:ParaCPreProcessorParser.StartSelectionBlockContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#logicalDirectiveAlternatives.
    def enterLogicalDirectiveAlternatives(self, ctx:ParaCPreProcessorParser.LogicalDirectiveAlternativesContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#logicalDirectiveAlternatives.
    def exitLogicalDirectiveAlternatives(self, ctx:ParaCPreProcessorParser.LogicalDirectiveAlternativesContext):
        pass


    # Enter a parse tree produced by ParaCPreProcessorParser#logicalElseDirective.
    def enterLogicalElseDirective(self, ctx:ParaCPreProcessorParser.LogicalElseDirectiveContext):
        pass

    # Exit a parse tree produced by ParaCPreProcessorParser#logicalElseDirective.
    def exitLogicalElseDirective(self, ctx:ParaCPreProcessorParser.LogicalElseDirectiveContext):
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



del ParaCPreProcessorParser