# Generated from ./grammar/ParaCPreProcessor.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\5\2(\n\2\3\2\3\2\3\3\6\3-\n\3\r\3\16\3.\3\4\3\4\5")
        buf.write("\4\63\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6")
        buf.write("?\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\7\13K")
        buf.write("\n\13\f\13\16\13N\13\13\3\13\5\13Q\n\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\7\17`\n")
        buf.write("\17\f\17\16\17c\13\17\3\20\3\20\5\20g\n\20\3\21\3\21\3")
        buf.write("\22\3\22\3\23\3\23\3\23\2\2\24\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$\2\5\4\2\4\5\b\b\4\2\6\7\t\t\3\2\21")
        buf.write("\22\2k\2\'\3\2\2\2\4,\3\2\2\2\6\62\3\2\2\2\b\64\3\2\2")
        buf.write("\2\n>\3\2\2\2\f@\3\2\2\2\16B\3\2\2\2\20D\3\2\2\2\22F\3")
        buf.write("\2\2\2\24H\3\2\2\2\26T\3\2\2\2\30W\3\2\2\2\32Z\3\2\2\2")
        buf.write("\34a\3\2\2\2\36f\3\2\2\2 h\3\2\2\2\"j\3\2\2\2$l\3\2\2")
        buf.write("\2&(\5\4\3\2\'&\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7\2\2\3")
        buf.write("*\3\3\2\2\2+-\5\6\4\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./")
        buf.write("\3\2\2\2/\5\3\2\2\2\60\63\5\n\6\2\61\63\5\b\5\2\62\60")
        buf.write("\3\2\2\2\62\61\3\2\2\2\63\7\3\2\2\2\64\65\7\3\2\2\65\t")
        buf.write("\3\2\2\2\66?\5\36\20\2\67?\5$\23\28?\5\24\13\29?\5\f\7")
        buf.write("\2:?\5\20\t\2;?\5\16\b\2<?\5 \21\2=?\5\22\n\2>\66\3\2")
        buf.write("\2\2>\67\3\2\2\2>8\3\2\2\2>9\3\2\2\2>:\3\2\2\2>;\3\2\2")
        buf.write("\2><\3\2\2\2>=\3\2\2\2?\13\3\2\2\2@A\7\17\2\2A\r\3\2\2")
        buf.write("\2BC\7\f\2\2C\17\3\2\2\2DE\7\r\2\2E\21\3\2\2\2FG\7\16")
        buf.write("\2\2G\23\3\2\2\2HL\5\26\f\2IK\5\30\r\2JI\3\2\2\2KN\3\2")
        buf.write("\2\2LJ\3\2\2\2LM\3\2\2\2MP\3\2\2\2NL\3\2\2\2OQ\5\32\16")
        buf.write("\2PO\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\7\13\2\2S\25\3\2\2")
        buf.write("\2TU\t\2\2\2UV\5\34\17\2V\27\3\2\2\2WX\t\3\2\2XY\5\34")
        buf.write("\17\2Y\31\3\2\2\2Z[\7\n\2\2[\\\5\34\17\2\\\33\3\2\2\2")
        buf.write("]`\5\b\5\2^`\5\24\13\2_]\3\2\2\2_^\3\2\2\2`c\3\2\2\2a")
        buf.write("_\3\2\2\2ab\3\2\2\2b\35\3\2\2\2ca\3\2\2\2dg\5\"\22\2e")
        buf.write("g\5$\23\2fd\3\2\2\2fe\3\2\2\2g\37\3\2\2\2hi\7\23\2\2i")
        buf.write("!\3\2\2\2jk\t\4\2\2k#\3\2\2\2lm\7\20\2\2m%\3\2\2\2\13")
        buf.write("\'.\62>LP_af")
        return buf.getvalue()


class ParaCPreProcessorParser ( Parser ):

    grammarFileName = "ParaCPreProcessor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NonPreProcessorItemBlock", "IfNotDefinedDirective", 
                      "IfDefinedDirective", "ElIfNotDefinedDirective", "ElIfDefinedDirective", 
                      "IfDirective", "ElIfDirective", "ElseDirective", "EndIfDirective", 
                      "PragmaDirective", "ErrorDirective", "UndefDirective", 
                      "ComplexDefineDirective", "ComputedIncludeLiteral", 
                      "LibIncludeDirective", "StringIncludeDirective", "LineDirective", 
                      "LibStringLiteral", "StringLiteral", "AsmBlock", "Whitespace", 
                      "Newline" ]

    RULE_compilationUnit = 0
    RULE_translationUnit = 1
    RULE_externalItem = 2
    RULE_coreLanguageItem = 3
    RULE_preProcessorDirective = 4
    RULE_complexDefineDirective = 5
    RULE_pragmaDirective = 6
    RULE_errorDirective = 7
    RULE_undefDirective = 8
    RULE_selectionPreProcessorDirective = 9
    RULE_startOfSelectionBlock = 10
    RULE_selectionDirectiveAlternatives = 11
    RULE_selectionElseDirective = 12
    RULE_selectionBlock = 13
    RULE_includeDirective = 14
    RULE_lineDirective = 15
    RULE_fileIncludeDirective = 16
    RULE_computedIncludeDirective = 17

    ruleNames =  [ "compilationUnit", "translationUnit", "externalItem", 
                   "coreLanguageItem", "preProcessorDirective", "complexDefineDirective", 
                   "pragmaDirective", "errorDirective", "undefDirective", 
                   "selectionPreProcessorDirective", "startOfSelectionBlock", 
                   "selectionDirectiveAlternatives", "selectionElseDirective", 
                   "selectionBlock", "includeDirective", "lineDirective", 
                   "fileIncludeDirective", "computedIncludeDirective" ]

    EOF = Token.EOF
    NonPreProcessorItemBlock=1
    IfNotDefinedDirective=2
    IfDefinedDirective=3
    ElIfNotDefinedDirective=4
    ElIfDefinedDirective=5
    IfDirective=6
    ElIfDirective=7
    ElseDirective=8
    EndIfDirective=9
    PragmaDirective=10
    ErrorDirective=11
    UndefDirective=12
    ComplexDefineDirective=13
    ComputedIncludeLiteral=14
    LibIncludeDirective=15
    StringIncludeDirective=16
    LineDirective=17
    LibStringLiteral=18
    StringLiteral=19
    AsmBlock=20
    Whitespace=21
    Newline=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ParaCPreProcessorParser.EOF, 0)

        def translationUnit(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.TranslationUnitContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = ParaCPreProcessorParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.NonPreProcessorItemBlock) | (1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective) | (1 << ParaCPreProcessorParser.PragmaDirective) | (1 << ParaCPreProcessorParser.ErrorDirective) | (1 << ParaCPreProcessorParser.UndefDirective) | (1 << ParaCPreProcessorParser.ComplexDefineDirective) | (1 << ParaCPreProcessorParser.ComputedIncludeLiteral) | (1 << ParaCPreProcessorParser.LibIncludeDirective) | (1 << ParaCPreProcessorParser.StringIncludeDirective) | (1 << ParaCPreProcessorParser.LineDirective))) != 0):
                self.state = 36
                self.translationUnit()


            self.state = 39
            self.match(ParaCPreProcessorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TranslationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def externalItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaCPreProcessorParser.ExternalItemContext)
            else:
                return self.getTypedRuleContext(ParaCPreProcessorParser.ExternalItemContext,i)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_translationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslationUnit" ):
                listener.enterTranslationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslationUnit" ):
                listener.exitTranslationUnit(self)




    def translationUnit(self):

        localctx = ParaCPreProcessorParser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_translationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 41
                self.externalItem()
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.NonPreProcessorItemBlock) | (1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective) | (1 << ParaCPreProcessorParser.PragmaDirective) | (1 << ParaCPreProcessorParser.ErrorDirective) | (1 << ParaCPreProcessorParser.UndefDirective) | (1 << ParaCPreProcessorParser.ComplexDefineDirective) | (1 << ParaCPreProcessorParser.ComputedIncludeLiteral) | (1 << ParaCPreProcessorParser.LibIncludeDirective) | (1 << ParaCPreProcessorParser.StringIncludeDirective) | (1 << ParaCPreProcessorParser.LineDirective))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExternalItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def preProcessorDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.PreProcessorDirectiveContext,0)


        def coreLanguageItem(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.CoreLanguageItemContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_externalItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternalItem" ):
                listener.enterExternalItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternalItem" ):
                listener.exitExternalItem(self)




    def externalItem(self):

        localctx = ParaCPreProcessorParser.ExternalItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_externalItem)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ParaCPreProcessorParser.IfNotDefinedDirective, ParaCPreProcessorParser.IfDefinedDirective, ParaCPreProcessorParser.IfDirective, ParaCPreProcessorParser.PragmaDirective, ParaCPreProcessorParser.ErrorDirective, ParaCPreProcessorParser.UndefDirective, ParaCPreProcessorParser.ComplexDefineDirective, ParaCPreProcessorParser.ComputedIncludeLiteral, ParaCPreProcessorParser.LibIncludeDirective, ParaCPreProcessorParser.StringIncludeDirective, ParaCPreProcessorParser.LineDirective]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.preProcessorDirective()
                pass
            elif token in [ParaCPreProcessorParser.NonPreProcessorItemBlock]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.coreLanguageItem()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoreLanguageItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NonPreProcessorItemBlock(self):
            return self.getToken(ParaCPreProcessorParser.NonPreProcessorItemBlock, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_coreLanguageItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoreLanguageItem" ):
                listener.enterCoreLanguageItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoreLanguageItem" ):
                listener.exitCoreLanguageItem(self)




    def coreLanguageItem(self):

        localctx = ParaCPreProcessorParser.CoreLanguageItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_coreLanguageItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(ParaCPreProcessorParser.NonPreProcessorItemBlock)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreProcessorDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def includeDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.IncludeDirectiveContext,0)


        def computedIncludeDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.ComputedIncludeDirectiveContext,0)


        def selectionPreProcessorDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext,0)


        def complexDefineDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.ComplexDefineDirectiveContext,0)


        def errorDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.ErrorDirectiveContext,0)


        def pragmaDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.PragmaDirectiveContext,0)


        def lineDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.LineDirectiveContext,0)


        def undefDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.UndefDirectiveContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_preProcessorDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreProcessorDirective" ):
                listener.enterPreProcessorDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreProcessorDirective" ):
                listener.exitPreProcessorDirective(self)




    def preProcessorDirective(self):

        localctx = ParaCPreProcessorParser.PreProcessorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_preProcessorDirective)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.includeDirective()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.computedIncludeDirective()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.selectionPreProcessorDirective()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.complexDefineDirective()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.errorDirective()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.pragmaDirective()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.lineDirective()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 59
                self.undefDirective()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexDefineDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ComplexDefineDirective(self):
            return self.getToken(ParaCPreProcessorParser.ComplexDefineDirective, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_complexDefineDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexDefineDirective" ):
                listener.enterComplexDefineDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexDefineDirective" ):
                listener.exitComplexDefineDirective(self)




    def complexDefineDirective(self):

        localctx = ParaCPreProcessorParser.ComplexDefineDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_complexDefineDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ParaCPreProcessorParser.ComplexDefineDirective)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PragmaDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PragmaDirective(self):
            return self.getToken(ParaCPreProcessorParser.PragmaDirective, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_pragmaDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragmaDirective" ):
                listener.enterPragmaDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragmaDirective" ):
                listener.exitPragmaDirective(self)




    def pragmaDirective(self):

        localctx = ParaCPreProcessorParser.PragmaDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pragmaDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ParaCPreProcessorParser.PragmaDirective)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ErrorDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ErrorDirective(self):
            return self.getToken(ParaCPreProcessorParser.ErrorDirective, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_errorDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErrorDirective" ):
                listener.enterErrorDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErrorDirective" ):
                listener.exitErrorDirective(self)




    def errorDirective(self):

        localctx = ParaCPreProcessorParser.ErrorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_errorDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ParaCPreProcessorParser.ErrorDirective)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UndefDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UndefDirective(self):
            return self.getToken(ParaCPreProcessorParser.UndefDirective, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_undefDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUndefDirective" ):
                listener.enterUndefDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUndefDirective" ):
                listener.exitUndefDirective(self)




    def undefDirective(self):

        localctx = ParaCPreProcessorParser.UndefDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_undefDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ParaCPreProcessorParser.UndefDirective)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionPreProcessorDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def startOfSelectionBlock(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.StartOfSelectionBlockContext,0)


        def EndIfDirective(self):
            return self.getToken(ParaCPreProcessorParser.EndIfDirective, 0)

        def selectionDirectiveAlternatives(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaCPreProcessorParser.SelectionDirectiveAlternativesContext)
            else:
                return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionDirectiveAlternativesContext,i)


        def selectionElseDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionElseDirectiveContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_selectionPreProcessorDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionPreProcessorDirective" ):
                listener.enterSelectionPreProcessorDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionPreProcessorDirective" ):
                listener.exitSelectionPreProcessorDirective(self)




    def selectionPreProcessorDirective(self):

        localctx = ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_selectionPreProcessorDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.startOfSelectionBlock()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.ElIfNotDefinedDirective) | (1 << ParaCPreProcessorParser.ElIfDefinedDirective) | (1 << ParaCPreProcessorParser.ElIfDirective))) != 0):
                self.state = 71
                self.selectionDirectiveAlternatives()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ParaCPreProcessorParser.ElseDirective:
                self.state = 77
                self.selectionElseDirective()


            self.state = 80
            self.match(ParaCPreProcessorParser.EndIfDirective)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartOfSelectionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectionBlock(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionBlockContext,0)


        def IfDirective(self):
            return self.getToken(ParaCPreProcessorParser.IfDirective, 0)

        def IfDefinedDirective(self):
            return self.getToken(ParaCPreProcessorParser.IfDefinedDirective, 0)

        def IfNotDefinedDirective(self):
            return self.getToken(ParaCPreProcessorParser.IfNotDefinedDirective, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_startOfSelectionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartOfSelectionBlock" ):
                listener.enterStartOfSelectionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartOfSelectionBlock" ):
                listener.exitStartOfSelectionBlock(self)




    def startOfSelectionBlock(self):

        localctx = ParaCPreProcessorParser.StartOfSelectionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_startOfSelectionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 83
            self.selectionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionDirectiveAlternativesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectionBlock(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionBlockContext,0)


        def ElIfDirective(self):
            return self.getToken(ParaCPreProcessorParser.ElIfDirective, 0)

        def ElIfDefinedDirective(self):
            return self.getToken(ParaCPreProcessorParser.ElIfDefinedDirective, 0)

        def ElIfNotDefinedDirective(self):
            return self.getToken(ParaCPreProcessorParser.ElIfNotDefinedDirective, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_selectionDirectiveAlternatives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionDirectiveAlternatives" ):
                listener.enterSelectionDirectiveAlternatives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionDirectiveAlternatives" ):
                listener.exitSelectionDirectiveAlternatives(self)




    def selectionDirectiveAlternatives(self):

        localctx = ParaCPreProcessorParser.SelectionDirectiveAlternativesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_selectionDirectiveAlternatives)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.ElIfNotDefinedDirective) | (1 << ParaCPreProcessorParser.ElIfDefinedDirective) | (1 << ParaCPreProcessorParser.ElIfDirective))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 86
            self.selectionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionElseDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ElseDirective(self):
            return self.getToken(ParaCPreProcessorParser.ElseDirective, 0)

        def selectionBlock(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionBlockContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_selectionElseDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionElseDirective" ):
                listener.enterSelectionElseDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionElseDirective" ):
                listener.exitSelectionElseDirective(self)




    def selectionElseDirective(self):

        localctx = ParaCPreProcessorParser.SelectionElseDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_selectionElseDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ParaCPreProcessorParser.ElseDirective)
            self.state = 89
            self.selectionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def coreLanguageItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaCPreProcessorParser.CoreLanguageItemContext)
            else:
                return self.getTypedRuleContext(ParaCPreProcessorParser.CoreLanguageItemContext,i)


        def selectionPreProcessorDirective(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext)
            else:
                return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext,i)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_selectionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionBlock" ):
                listener.enterSelectionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionBlock" ):
                listener.exitSelectionBlock(self)




    def selectionBlock(self):

        localctx = ParaCPreProcessorParser.SelectionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_selectionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.NonPreProcessorItemBlock) | (1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective))) != 0):
                self.state = 93
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ParaCPreProcessorParser.NonPreProcessorItemBlock]:
                    self.state = 91
                    self.coreLanguageItem()
                    pass
                elif token in [ParaCPreProcessorParser.IfNotDefinedDirective, ParaCPreProcessorParser.IfDefinedDirective, ParaCPreProcessorParser.IfDirective]:
                    self.state = 92
                    self.selectionPreProcessorDirective()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fileIncludeDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.FileIncludeDirectiveContext,0)


        def computedIncludeDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.ComputedIncludeDirectiveContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_includeDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeDirective" ):
                listener.enterIncludeDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeDirective" ):
                listener.exitIncludeDirective(self)




    def includeDirective(self):

        localctx = ParaCPreProcessorParser.IncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_includeDirective)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ParaCPreProcessorParser.LibIncludeDirective, ParaCPreProcessorParser.StringIncludeDirective]:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.fileIncludeDirective()
                pass
            elif token in [ParaCPreProcessorParser.ComputedIncludeLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.computedIncludeDirective()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LineDirective(self):
            return self.getToken(ParaCPreProcessorParser.LineDirective, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_lineDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineDirective" ):
                listener.enterLineDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineDirective" ):
                listener.exitLineDirective(self)




    def lineDirective(self):

        localctx = ParaCPreProcessorParser.LineDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lineDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(ParaCPreProcessorParser.LineDirective)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FileIncludeDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LibIncludeDirective(self):
            return self.getToken(ParaCPreProcessorParser.LibIncludeDirective, 0)

        def StringIncludeDirective(self):
            return self.getToken(ParaCPreProcessorParser.StringIncludeDirective, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_fileIncludeDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileIncludeDirective" ):
                listener.enterFileIncludeDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileIncludeDirective" ):
                listener.exitFileIncludeDirective(self)




    def fileIncludeDirective(self):

        localctx = ParaCPreProcessorParser.FileIncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_fileIncludeDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not(_la==ParaCPreProcessorParser.LibIncludeDirective or _la==ParaCPreProcessorParser.StringIncludeDirective):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComputedIncludeDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ComputedIncludeLiteral(self):
            return self.getToken(ParaCPreProcessorParser.ComputedIncludeLiteral, 0)

        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_computedIncludeDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComputedIncludeDirective" ):
                listener.enterComputedIncludeDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComputedIncludeDirective" ):
                listener.exitComputedIncludeDirective(self)




    def computedIncludeDirective(self):

        localctx = ParaCPreProcessorParser.ComputedIncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_computedIncludeDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(ParaCPreProcessorParser.ComputedIncludeLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





