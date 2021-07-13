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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\3\2\5\2\"\n\2\3\2\3\2\3\3\6\3")
        buf.write("\'\n\3\r\3\16\3(\3\4\3\4\5\4-\n\4\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6\67\n\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3")
        buf.write("\n\7\nA\n\n\f\n\16\nD\13\n\3\n\5\nG\n\n\3\n\3\n\3\13\3")
        buf.write("\13\5\13M\n\13\3\f\3\f\5\fQ\n\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\5\16X\n\16\3\17\3\17\3\20\3\20\3\20\2\2\21\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36\2\5\4\2\4\5\b\b\4\2\6\7")
        buf.write("\t\t\3\2\20\21\2[\2!\3\2\2\2\4&\3\2\2\2\6,\3\2\2\2\b.")
        buf.write("\3\2\2\2\n\66\3\2\2\2\f8\3\2\2\2\16:\3\2\2\2\20<\3\2\2")
        buf.write("\2\22>\3\2\2\2\24J\3\2\2\2\26N\3\2\2\2\30R\3\2\2\2\32")
        buf.write("W\3\2\2\2\34Y\3\2\2\2\36[\3\2\2\2 \"\5\4\3\2! \3\2\2\2")
        buf.write("!\"\3\2\2\2\"#\3\2\2\2#$\7\2\2\3$\3\3\2\2\2%\'\5\6\4\2")
        buf.write("&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)\5\3\2\2\2*")
        buf.write("-\5\n\6\2+-\5\b\5\2,*\3\2\2\2,+\3\2\2\2-\7\3\2\2\2./\7")
        buf.write("\3\2\2/\t\3\2\2\2\60\67\5\32\16\2\61\67\5\36\20\2\62\67")
        buf.write("\5\22\n\2\63\67\5\f\7\2\64\67\5\16\b\2\65\67\5\20\t\2")
        buf.write("\66\60\3\2\2\2\66\61\3\2\2\2\66\62\3\2\2\2\66\63\3\2\2")
        buf.write("\2\66\64\3\2\2\2\66\65\3\2\2\2\67\13\3\2\2\289\7\16\2")
        buf.write("\29\r\3\2\2\2:;\7\f\2\2;\17\3\2\2\2<=\7\r\2\2=\21\3\2")
        buf.write("\2\2>B\5\24\13\2?A\5\26\f\2@?\3\2\2\2AD\3\2\2\2B@\3\2")
        buf.write("\2\2BC\3\2\2\2CF\3\2\2\2DB\3\2\2\2EG\5\30\r\2FE\3\2\2")
        buf.write("\2FG\3\2\2\2GH\3\2\2\2HI\7\13\2\2I\23\3\2\2\2JL\t\2\2")
        buf.write("\2KM\5\22\n\2LK\3\2\2\2LM\3\2\2\2M\25\3\2\2\2NP\t\3\2")
        buf.write("\2OQ\5\22\n\2PO\3\2\2\2PQ\3\2\2\2Q\27\3\2\2\2RS\7\n\2")
        buf.write("\2ST\5\22\n\2T\31\3\2\2\2UX\5\34\17\2VX\5\36\20\2WU\3")
        buf.write("\2\2\2WV\3\2\2\2X\33\3\2\2\2YZ\t\4\2\2Z\35\3\2\2\2[\\")
        buf.write("\7\17\2\2\\\37\3\2\2\2\13!(,\66BFLPW")
        return buf.getvalue()


class ParaCPreProcessorParser ( Parser ):

    grammarFileName = "ParaCPreProcessor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NonPreProcessorItemBlock", "IfNotDefinedDirective", 
                      "IfDefinedDirective", "ElIfNotDefinedDirective", "ElIfDefinedDirective", 
                      "IfDirective", "ElIfDirective", "ElseDirective", "EndifDirective", 
                      "PragmaDirective", "UndefDirective", "ComplexDefineDirective", 
                      "ComputedIncludeLiteral", "LibIncludeLiteral", "StringIncludeLiteral", 
                      "AsmBlock", "Whitespace", "Newline" ]

    RULE_compilationUnit = 0
    RULE_translationUnit = 1
    RULE_externalItem = 2
    RULE_coreLanguageItem = 3
    RULE_preProcessorDirective = 4
    RULE_complexDefineDirective = 5
    RULE_pragmaDirective = 6
    RULE_undefDirective = 7
    RULE_selectionPreProcessorDirective = 8
    RULE_startSelectionBlock = 9
    RULE_logicalDirectiveAlternatives = 10
    RULE_logicalElseDirective = 11
    RULE_includeDirective = 12
    RULE_fileIncludeDirective = 13
    RULE_computedIncludeDirective = 14

    ruleNames =  [ "compilationUnit", "translationUnit", "externalItem", 
                   "coreLanguageItem", "preProcessorDirective", "complexDefineDirective", 
                   "pragmaDirective", "undefDirective", "selectionPreProcessorDirective", 
                   "startSelectionBlock", "logicalDirectiveAlternatives", 
                   "logicalElseDirective", "includeDirective", "fileIncludeDirective", 
                   "computedIncludeDirective" ]

    EOF = Token.EOF
    NonPreProcessorItemBlock=1
    IfNotDefinedDirective=2
    IfDefinedDirective=3
    ElIfNotDefinedDirective=4
    ElIfDefinedDirective=5
    IfDirective=6
    ElIfDirective=7
    ElseDirective=8
    EndifDirective=9
    PragmaDirective=10
    UndefDirective=11
    ComplexDefineDirective=12
    ComputedIncludeLiteral=13
    LibIncludeLiteral=14
    StringIncludeLiteral=15
    AsmBlock=16
    Whitespace=17
    Newline=18

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
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.NonPreProcessorItemBlock) | (1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective) | (1 << ParaCPreProcessorParser.PragmaDirective) | (1 << ParaCPreProcessorParser.UndefDirective) | (1 << ParaCPreProcessorParser.ComplexDefineDirective) | (1 << ParaCPreProcessorParser.ComputedIncludeLiteral) | (1 << ParaCPreProcessorParser.LibIncludeLiteral) | (1 << ParaCPreProcessorParser.StringIncludeLiteral))) != 0):
                self.state = 30
                self.translationUnit()


            self.state = 33
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
            self.state = 36 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 35
                self.externalItem()
                self.state = 38 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.NonPreProcessorItemBlock) | (1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective) | (1 << ParaCPreProcessorParser.PragmaDirective) | (1 << ParaCPreProcessorParser.UndefDirective) | (1 << ParaCPreProcessorParser.ComplexDefineDirective) | (1 << ParaCPreProcessorParser.ComputedIncludeLiteral) | (1 << ParaCPreProcessorParser.LibIncludeLiteral) | (1 << ParaCPreProcessorParser.StringIncludeLiteral))) != 0)):
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
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ParaCPreProcessorParser.IfNotDefinedDirective, ParaCPreProcessorParser.IfDefinedDirective, ParaCPreProcessorParser.IfDirective, ParaCPreProcessorParser.PragmaDirective, ParaCPreProcessorParser.UndefDirective, ParaCPreProcessorParser.ComplexDefineDirective, ParaCPreProcessorParser.ComputedIncludeLiteral, ParaCPreProcessorParser.LibIncludeLiteral, ParaCPreProcessorParser.StringIncludeLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.preProcessorDirective()
                pass
            elif token in [ParaCPreProcessorParser.NonPreProcessorItemBlock]:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
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
            self.state = 44
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


        def pragmaDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.PragmaDirectiveContext,0)


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
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.includeDirective()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.computedIncludeDirective()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.selectionPreProcessorDirective()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.complexDefineDirective()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.pragmaDirective()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
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
            self.state = 54
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
            self.state = 56
            self.match(ParaCPreProcessorParser.PragmaDirective)
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
        self.enterRule(localctx, 14, self.RULE_undefDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
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

        def startSelectionBlock(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.StartSelectionBlockContext,0)


        def EndifDirective(self):
            return self.getToken(ParaCPreProcessorParser.EndifDirective, 0)

        def logicalDirectiveAlternatives(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaCPreProcessorParser.LogicalDirectiveAlternativesContext)
            else:
                return self.getTypedRuleContext(ParaCPreProcessorParser.LogicalDirectiveAlternativesContext,i)


        def logicalElseDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.LogicalElseDirectiveContext,0)


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
        self.enterRule(localctx, 16, self.RULE_selectionPreProcessorDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.startSelectionBlock()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.ElIfNotDefinedDirective) | (1 << ParaCPreProcessorParser.ElIfDefinedDirective) | (1 << ParaCPreProcessorParser.ElIfDirective))) != 0):
                self.state = 61
                self.logicalDirectiveAlternatives()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ParaCPreProcessorParser.ElseDirective:
                self.state = 67
                self.logicalElseDirective()


            self.state = 70
            self.match(ParaCPreProcessorParser.EndifDirective)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartSelectionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IfDirective(self):
            return self.getToken(ParaCPreProcessorParser.IfDirective, 0)

        def IfDefinedDirective(self):
            return self.getToken(ParaCPreProcessorParser.IfDefinedDirective, 0)

        def IfNotDefinedDirective(self):
            return self.getToken(ParaCPreProcessorParser.IfNotDefinedDirective, 0)

        def selectionPreProcessorDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_startSelectionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartSelectionBlock" ):
                listener.enterStartSelectionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartSelectionBlock" ):
                listener.exitStartSelectionBlock(self)




    def startSelectionBlock(self):

        localctx = ParaCPreProcessorParser.StartSelectionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_startSelectionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective))) != 0):
                self.state = 73
                self.selectionPreProcessorDirective()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalDirectiveAlternativesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ElIfDirective(self):
            return self.getToken(ParaCPreProcessorParser.ElIfDirective, 0)

        def ElIfDefinedDirective(self):
            return self.getToken(ParaCPreProcessorParser.ElIfDefinedDirective, 0)

        def ElIfNotDefinedDirective(self):
            return self.getToken(ParaCPreProcessorParser.ElIfNotDefinedDirective, 0)

        def selectionPreProcessorDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_logicalDirectiveAlternatives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalDirectiveAlternatives" ):
                listener.enterLogicalDirectiveAlternatives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalDirectiveAlternatives" ):
                listener.exitLogicalDirectiveAlternatives(self)




    def logicalDirectiveAlternatives(self):

        localctx = ParaCPreProcessorParser.LogicalDirectiveAlternativesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_logicalDirectiveAlternatives)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.ElIfNotDefinedDirective) | (1 << ParaCPreProcessorParser.ElIfDefinedDirective) | (1 << ParaCPreProcessorParser.ElIfDirective))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaCPreProcessorParser.IfNotDefinedDirective) | (1 << ParaCPreProcessorParser.IfDefinedDirective) | (1 << ParaCPreProcessorParser.IfDirective))) != 0):
                self.state = 77
                self.selectionPreProcessorDirective()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalElseDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ElseDirective(self):
            return self.getToken(ParaCPreProcessorParser.ElseDirective, 0)

        def selectionPreProcessorDirective(self):
            return self.getTypedRuleContext(ParaCPreProcessorParser.SelectionPreProcessorDirectiveContext,0)


        def getRuleIndex(self):
            return ParaCPreProcessorParser.RULE_logicalElseDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalElseDirective" ):
                listener.enterLogicalElseDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalElseDirective" ):
                listener.exitLogicalElseDirective(self)




    def logicalElseDirective(self):

        localctx = ParaCPreProcessorParser.LogicalElseDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_logicalElseDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(ParaCPreProcessorParser.ElseDirective)
            self.state = 81
            self.selectionPreProcessorDirective()
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
        self.enterRule(localctx, 24, self.RULE_includeDirective)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ParaCPreProcessorParser.LibIncludeLiteral, ParaCPreProcessorParser.StringIncludeLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.fileIncludeDirective()
                pass
            elif token in [ParaCPreProcessorParser.ComputedIncludeLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
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


    class FileIncludeDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LibIncludeLiteral(self):
            return self.getToken(ParaCPreProcessorParser.LibIncludeLiteral, 0)

        def StringIncludeLiteral(self):
            return self.getToken(ParaCPreProcessorParser.StringIncludeLiteral, 0)

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
        self.enterRule(localctx, 26, self.RULE_fileIncludeDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            _la = self._input.LA(1)
            if not(_la==ParaCPreProcessorParser.LibIncludeLiteral or _la==ParaCPreProcessorParser.StringIncludeLiteral):
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
        self.enterRule(localctx, 28, self.RULE_computedIncludeDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ParaCPreProcessorParser.ComputedIncludeLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





