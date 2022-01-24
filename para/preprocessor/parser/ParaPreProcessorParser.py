# Generated from ./ParaPreProcessor.g4 by ANTLR 4.9.2
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
        buf.write("\u0128\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\5\2B\n\2\3\2\3\2\3\3\6\3G\n\3\r\3")
        buf.write("\16\3H\3\4\3\4\3\4\5\4N\n\4\3\5\6\5Q\n\5\r\5\16\5R\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6\\\n\6\3\7\3\7\7\7`\n\7\f")
        buf.write("\7\16\7c\13\7\3\7\5\7f\n\7\3\7\3\7\3\b\3\b\3\b\5\bm\n")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\5\tt\n\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\13\3\13\7\13}\n\13\f\13\16\13\u0080\13\13\3\13\7\13\u0083")
        buf.write("\n\13\f\13\16\13\u0086\13\13\3\f\3\f\5\f\u008a\n\f\3\r")
        buf.write("\3\r\5\r\u008e\n\r\3\16\3\16\6\16\u0092\n\16\r\16\16\16")
        buf.write("\u0093\3\16\3\16\3\16\3\17\3\17\6\17\u009b\n\17\r\17\16")
        buf.write("\17\u009c\3\17\3\17\3\17\3\20\3\20\6\20\u00a4\n\20\r\20")
        buf.write("\16\20\u00a5\3\20\3\20\3\20\3\21\3\21\6\21\u00ad\n\21")
        buf.write("\r\21\16\21\u00ae\3\21\3\21\3\21\3\22\3\22\6\22\u00b6")
        buf.write("\n\22\r\22\16\22\u00b7\3\22\3\22\3\22\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\6\27\u00cd\n\27\r\27\16\27\u00ce\3\27\6\27")
        buf.write("\u00d2\n\27\r\27\16\27\u00d3\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\6\31\u00de\n\31\r\31\16\31\u00df\3\31")
        buf.write("\3\31\3\31\3\32\3\32\6\32\u00e7\n\32\r\32\16\32\u00e8")
        buf.write("\3\32\3\32\6\32\u00ed\n\32\r\32\16\32\u00ee\3\32\5\32")
        buf.write("\u00f2\n\32\3\32\3\32\3\33\3\33\6\33\u00f8\n\33\r\33\16")
        buf.write("\33\u00f9\3\33\3\33\3\33\3\34\3\34\6\34\u0101\n\34\r\34")
        buf.write("\16\34\u0102\3\34\3\34\3\34\3\35\3\35\6\35\u010a\n\35")
        buf.write("\r\35\16\35\u010b\3\35\3\35\6\35\u0110\n\35\r\35\16\35")
        buf.write("\u0111\3\35\5\35\u0115\n\35\3\35\3\35\3\36\3\36\3\37\6")
        buf.write("\37\u011c\n\37\r\37\16\37\u011d\3 \7 \u0121\n \f \16 ")
        buf.write("\u0124\13 \3 \3 \3 \2\2!\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>\2\4\6\2\21\21\23\24")
        buf.write("\26\26\30\30\3\3\27\27\2\u0130\2A\3\2\2\2\4F\3\2\2\2\6")
        buf.write("M\3\2\2\2\bP\3\2\2\2\n[\3\2\2\2\f]\3\2\2\2\16l\3\2\2\2")
        buf.write("\20s\3\2\2\2\22w\3\2\2\2\24~\3\2\2\2\26\u0089\3\2\2\2")
        buf.write("\30\u008d\3\2\2\2\32\u008f\3\2\2\2\34\u0098\3\2\2\2\36")
        buf.write("\u00a1\3\2\2\2 \u00aa\3\2\2\2\"\u00b3\3\2\2\2$\u00bc\3")
        buf.write("\2\2\2&\u00c0\3\2\2\2(\u00c4\3\2\2\2*\u00c7\3\2\2\2,\u00ca")
        buf.write("\3\2\2\2.\u00d7\3\2\2\2\60\u00db\3\2\2\2\62\u00e4\3\2")
        buf.write("\2\2\64\u00f5\3\2\2\2\66\u00fe\3\2\2\28\u0107\3\2\2\2")
        buf.write(":\u0118\3\2\2\2<\u011b\3\2\2\2>\u0122\3\2\2\2@B\5\4\3")
        buf.write("\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7\2\2\3D\3\3\2\2\2")
        buf.write("EG\5\6\4\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2\2I\5")
        buf.write("\3\2\2\2JN\5\n\6\2KN\5\b\5\2LN\7\27\2\2MJ\3\2\2\2MK\3")
        buf.write("\2\2\2ML\3\2\2\2N\7\3\2\2\2OQ\5:\36\2PO\3\2\2\2QR\3\2")
        buf.write("\2\2RP\3\2\2\2RS\3\2\2\2S\t\3\2\2\2T\\\5\26\f\2U\\\5\f")
        buf.write("\7\2V\\\5\62\32\2W\\\5.\30\2X\\\5,\27\2Y\\\58\35\2Z\\")
        buf.write("\5\60\31\2[T\3\2\2\2[U\3\2\2\2[V\3\2\2\2[W\3\2\2\2[X\3")
        buf.write("\2\2\2[Y\3\2\2\2[Z\3\2\2\2\\\13\3\2\2\2]a\5\16\b\2^`\5")
        buf.write("\20\t\2_^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2be\3\2")
        buf.write("\2\2ca\3\2\2\2df\5\22\n\2ed\3\2\2\2ef\3\2\2\2fg\3\2\2")
        buf.write("\2gh\5*\26\2h\r\3\2\2\2im\5$\23\2jm\5\36\20\2km\5\34\17")
        buf.write("\2li\3\2\2\2lj\3\2\2\2lk\3\2\2\2mn\3\2\2\2no\5\24\13\2")
        buf.write("o\17\3\2\2\2pt\5&\24\2qt\5\"\22\2rt\5 \21\2sp\3\2\2\2")
        buf.write("sq\3\2\2\2sr\3\2\2\2tu\3\2\2\2uv\5\24\13\2v\21\3\2\2\2")
        buf.write("wx\5(\25\2xy\5\24\13\2y\23\3\2\2\2z}\5\b\5\2{}\7\27\2")
        buf.write("\2|z\3\2\2\2|{\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3")
        buf.write("\2\2\2\177\u0084\3\2\2\2\u0080~\3\2\2\2\u0081\u0083\5")
        buf.write("\f\7\2\u0082\u0081\3\2\2\2\u0083\u0086\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0084\u0085\3\2\2\2\u0085\25\3\2\2\2\u0086\u0084")
        buf.write("\3\2\2\2\u0087\u008a\5\30\r\2\u0088\u008a\5\32\16\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u0088\3\2\2\2\u008a\27\3\2\2\2\u008b")
        buf.write("\u008e\5\64\33\2\u008c\u008e\5\66\34\2\u008d\u008b\3\2")
        buf.write("\2\2\u008d\u008c\3\2\2\2\u008e\31\3\2\2\2\u008f\u0091")
        buf.write("\7\3\2\2\u0090\u0092\7\26\2\2\u0091\u0090\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2")
        buf.write("\u0094\u0095\3\2\2\2\u0095\u0096\7\21\2\2\u0096\u0097")
        buf.write("\5> \2\u0097\33\3\2\2\2\u0098\u009a\7\t\2\2\u0099\u009b")
        buf.write("\7\26\2\2\u009a\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u009f\7\21\2\2\u009f\u00a0\5> \2\u00a0\35\3\2\2")
        buf.write("\2\u00a1\u00a3\7\b\2\2\u00a2\u00a4\7\26\2\2\u00a3\u00a2")
        buf.write("\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5")
        buf.write("\u00a6\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a8\7\21\2")
        buf.write("\2\u00a8\u00a9\5> \2\u00a9\37\3\2\2\2\u00aa\u00ac\7\n")
        buf.write("\2\2\u00ab\u00ad\7\26\2\2\u00ac\u00ab\3\2\2\2\u00ad\u00ae")
        buf.write("\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae\u00af\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b1\7\21\2\2\u00b1\u00b2\5> \2")
        buf.write("\u00b2!\3\2\2\2\u00b3\u00b5\7\13\2\2\u00b4\u00b6\7\26")
        buf.write("\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b5")
        buf.write("\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9")
        buf.write("\u00ba\7\21\2\2\u00ba\u00bb\5> \2\u00bb#\3\2\2\2\u00bc")
        buf.write("\u00bd\7\6\2\2\u00bd\u00be\5<\37\2\u00be\u00bf\5> \2\u00bf")
        buf.write("%\3\2\2\2\u00c0\u00c1\7\f\2\2\u00c1\u00c2\5<\37\2\u00c2")
        buf.write("\u00c3\5> \2\u00c3\'\3\2\2\2\u00c4\u00c5\7\7\2\2\u00c5")
        buf.write("\u00c6\5> \2\u00c6)\3\2\2\2\u00c7\u00c8\7\r\2\2\u00c8")
        buf.write("\u00c9\5> \2\u00c9+\3\2\2\2\u00ca\u00d1\7\17\2\2\u00cb")
        buf.write("\u00cd\7\26\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00ce\3\2\2")
        buf.write("\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00d2\7\21\2\2\u00d1\u00cc\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\u00d6\5> \2\u00d6-\3\2\2\2")
        buf.write("\u00d7\u00d8\7\16\2\2\u00d8\u00d9\5<\37\2\u00d9\u00da")
        buf.write("\5> \2\u00da/\3\2\2\2\u00db\u00dd\7\5\2\2\u00dc\u00de")
        buf.write("\7\26\2\2\u00dd\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e1\u00e2\7\21\2\2\u00e2\u00e3\5> \2\u00e3\61\3\2\2")
        buf.write("\2\u00e4\u00e6\7\4\2\2\u00e5\u00e7\7\26\2\2\u00e6\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8")
        buf.write("\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00f1\7\21\2")
        buf.write("\2\u00eb\u00ed\7\26\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee")
        buf.write("\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\u00f0\3\2\2\2\u00f0\u00f2\5<\37\2\u00f1\u00ec\3\2\2\2")
        buf.write("\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\5")
        buf.write("> \2\u00f4\63\3\2\2\2\u00f5\u00f7\7\3\2\2\u00f6\u00f8")
        buf.write("\7\26\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00fc\7\22\2\2\u00fc\u00fd\5> \2\u00fd\65\3\2\2")
        buf.write("\2\u00fe\u0100\7\3\2\2\u00ff\u0101\7\26\2\2\u0100\u00ff")
        buf.write("\3\2\2\2\u0101\u0102\3\2\2\2\u0102\u0100\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\7\23\2")
        buf.write("\2\u0105\u0106\5> \2\u0106\67\3\2\2\2\u0107\u0109\7\20")
        buf.write("\2\2\u0108\u010a\7\26\2\2\u0109\u0108\3\2\2\2\u010a\u010b")
        buf.write("\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c")
        buf.write("\u010d\3\2\2\2\u010d\u010f\7\24\2\2\u010e\u0110\7\26\2")
        buf.write("\2\u010f\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u010f")
        buf.write("\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114\3\2\2\2\u0113")
        buf.write("\u0115\7\23\2\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2")
        buf.write("\2\u0115\u0116\3\2\2\2\u0116\u0117\5> \2\u01179\3\2\2")
        buf.write("\2\u0118\u0119\5<\37\2\u0119;\3\2\2\2\u011a\u011c\t\2")
        buf.write("\2\2\u011b\u011a\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011b")
        buf.write("\3\2\2\2\u011d\u011e\3\2\2\2\u011e=\3\2\2\2\u011f\u0121")
        buf.write("\7\26\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2")
        buf.write("\u0124\u0122\3\2\2\2\u0125\u0126\t\3\2\2\u0126?\3\2\2")
        buf.write("\2\"AHMR[aels|~\u0084\u0089\u008d\u0093\u009c\u00a5\u00ae")
        buf.write("\u00b7\u00ce\u00d3\u00df\u00e8\u00ee\u00f1\u00f9\u0102")
        buf.write("\u010b\u0111\u0114\u011d\u0122")
        return buf.getvalue()


class ParaPreProcessorParser ( Parser ):

    grammarFileName = "ParaPreProcessor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "Include", "Define", "Undefine", "If", 
                      "Else", "IfDefined", "IfNotDefined", "ElIfNotDefined", 
                      "ElIfDefined", "ElseIf", "EndIf", "Error", "Pragma", 
                      "Line", "Identifier", "LibStringLiteral", "StringLiteral", 
                      "DigitSequence", "AsmBlock", "Whitespace", "Newline", 
                      "NonPreProcessorItemSequence" ]

    RULE_compilationUnit = 0
    RULE_translationUnit = 1
    RULE_externalItem = 2
    RULE_nonPreProcessorItemSequence = 3
    RULE_preProcessorDirective = 4
    RULE_selectionPreProcessorDirective = 5
    RULE_startOfSelectionBlock = 6
    RULE_selectionDirectiveAlternatives = 7
    RULE_selectionElseDirective = 8
    RULE_selectionBlock = 9
    RULE_includeDirective = 10
    RULE_fileIncludeDirective = 11
    RULE_computedIncludeDirective = 12
    RULE_ifNotDefinedDirective = 13
    RULE_ifDefinedDirective = 14
    RULE_elIfNotDefinedDirective = 15
    RULE_elIfDefinedDirective = 16
    RULE_ifDirective = 17
    RULE_elIfDirective = 18
    RULE_elseDirective = 19
    RULE_endIfDirective = 20
    RULE_pragmaDirective = 21
    RULE_errorDirective = 22
    RULE_undefDirective = 23
    RULE_complexDefineDirective = 24
    RULE_libIncludeDirective = 25
    RULE_stringIncludeDirective = 26
    RULE_lineDirective = 27
    RULE_nonPreProcessorItem = 28
    RULE_anySequence = 29
    RULE_preProcessorEnd = 30

    ruleNames =  [ "compilationUnit", "translationUnit", "externalItem", 
                   "nonPreProcessorItemSequence", "preProcessorDirective", 
                   "selectionPreProcessorDirective", "startOfSelectionBlock", 
                   "selectionDirectiveAlternatives", "selectionElseDirective", 
                   "selectionBlock", "includeDirective", "fileIncludeDirective", 
                   "computedIncludeDirective", "ifNotDefinedDirective", 
                   "ifDefinedDirective", "elIfNotDefinedDirective", "elIfDefinedDirective", 
                   "ifDirective", "elIfDirective", "elseDirective", "endIfDirective", 
                   "pragmaDirective", "errorDirective", "undefDirective", 
                   "complexDefineDirective", "libIncludeDirective", "stringIncludeDirective", 
                   "lineDirective", "nonPreProcessorItem", "anySequence", 
                   "preProcessorEnd" ]

    EOF = Token.EOF
    Include=1
    Define=2
    Undefine=3
    If=4
    Else=5
    IfDefined=6
    IfNotDefined=7
    ElIfNotDefined=8
    ElIfDefined=9
    ElseIf=10
    EndIf=11
    Error=12
    Pragma=13
    Line=14
    Identifier=15
    LibStringLiteral=16
    StringLiteral=17
    DigitSequence=18
    AsmBlock=19
    Whitespace=20
    Newline=21
    NonPreProcessorItemSequence=22

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
            return self.getToken(ParaPreProcessorParser.EOF, 0)

        def translationUnit(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.TranslationUnitContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = ParaPreProcessorParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaPreProcessorParser.Include) | (1 << ParaPreProcessorParser.Define) | (1 << ParaPreProcessorParser.Undefine) | (1 << ParaPreProcessorParser.If) | (1 << ParaPreProcessorParser.IfDefined) | (1 << ParaPreProcessorParser.IfNotDefined) | (1 << ParaPreProcessorParser.Error) | (1 << ParaPreProcessorParser.Pragma) | (1 << ParaPreProcessorParser.Line) | (1 << ParaPreProcessorParser.Identifier) | (1 << ParaPreProcessorParser.StringLiteral) | (1 << ParaPreProcessorParser.DigitSequence) | (1 << ParaPreProcessorParser.Whitespace) | (1 << ParaPreProcessorParser.Newline) | (1 << ParaPreProcessorParser.NonPreProcessorItemSequence))) != 0):
                self.state = 62
                self.translationUnit()


            self.state = 65
            self.match(ParaPreProcessorParser.EOF)
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
                return self.getTypedRuleContexts(ParaPreProcessorParser.ExternalItemContext)
            else:
                return self.getTypedRuleContext(ParaPreProcessorParser.ExternalItemContext,i)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_translationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTranslationUnit" ):
                listener.enterTranslationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTranslationUnit" ):
                listener.exitTranslationUnit(self)




    def translationUnit(self):

        localctx = ParaPreProcessorParser.TranslationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_translationUnit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                self.externalItem()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaPreProcessorParser.Include) | (1 << ParaPreProcessorParser.Define) | (1 << ParaPreProcessorParser.Undefine) | (1 << ParaPreProcessorParser.If) | (1 << ParaPreProcessorParser.IfDefined) | (1 << ParaPreProcessorParser.IfNotDefined) | (1 << ParaPreProcessorParser.Error) | (1 << ParaPreProcessorParser.Pragma) | (1 << ParaPreProcessorParser.Line) | (1 << ParaPreProcessorParser.Identifier) | (1 << ParaPreProcessorParser.StringLiteral) | (1 << ParaPreProcessorParser.DigitSequence) | (1 << ParaPreProcessorParser.Whitespace) | (1 << ParaPreProcessorParser.Newline) | (1 << ParaPreProcessorParser.NonPreProcessorItemSequence))) != 0)):
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
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorDirectiveContext,0)


        def nonPreProcessorItemSequence(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.NonPreProcessorItemSequenceContext,0)


        def Newline(self):
            return self.getToken(ParaPreProcessorParser.Newline, 0)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_externalItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExternalItem" ):
                listener.enterExternalItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExternalItem" ):
                listener.exitExternalItem(self)




    def externalItem(self):

        localctx = ParaPreProcessorParser.ExternalItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_externalItem)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ParaPreProcessorParser.Include, ParaPreProcessorParser.Define, ParaPreProcessorParser.Undefine, ParaPreProcessorParser.If, ParaPreProcessorParser.IfDefined, ParaPreProcessorParser.IfNotDefined, ParaPreProcessorParser.Error, ParaPreProcessorParser.Pragma, ParaPreProcessorParser.Line]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.preProcessorDirective()
                pass
            elif token in [ParaPreProcessorParser.Identifier, ParaPreProcessorParser.StringLiteral, ParaPreProcessorParser.DigitSequence, ParaPreProcessorParser.Whitespace, ParaPreProcessorParser.NonPreProcessorItemSequence]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.nonPreProcessorItemSequence()
                pass
            elif token in [ParaPreProcessorParser.Newline]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(ParaPreProcessorParser.Newline)
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


    class NonPreProcessorItemSequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nonPreProcessorItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaPreProcessorParser.NonPreProcessorItemContext)
            else:
                return self.getTypedRuleContext(ParaPreProcessorParser.NonPreProcessorItemContext,i)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_nonPreProcessorItemSequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonPreProcessorItemSequence" ):
                listener.enterNonPreProcessorItemSequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonPreProcessorItemSequence" ):
                listener.exitNonPreProcessorItemSequence(self)




    def nonPreProcessorItemSequence(self):

        localctx = ParaPreProcessorParser.NonPreProcessorItemSequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nonPreProcessorItemSequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 77
                    self.nonPreProcessorItem()

                else:
                    raise NoViableAltException(self)
                self.state = 80 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            return self.getTypedRuleContext(ParaPreProcessorParser.IncludeDirectiveContext,0)


        def selectionPreProcessorDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.SelectionPreProcessorDirectiveContext,0)


        def complexDefineDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.ComplexDefineDirectiveContext,0)


        def errorDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.ErrorDirectiveContext,0)


        def pragmaDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PragmaDirectiveContext,0)


        def lineDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.LineDirectiveContext,0)


        def undefDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.UndefDirectiveContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_preProcessorDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreProcessorDirective" ):
                listener.enterPreProcessorDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreProcessorDirective" ):
                listener.exitPreProcessorDirective(self)




    def preProcessorDirective(self):

        localctx = ParaPreProcessorParser.PreProcessorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_preProcessorDirective)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ParaPreProcessorParser.Include]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.includeDirective()
                pass
            elif token in [ParaPreProcessorParser.If, ParaPreProcessorParser.IfDefined, ParaPreProcessorParser.IfNotDefined]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.selectionPreProcessorDirective()
                pass
            elif token in [ParaPreProcessorParser.Define]:
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.complexDefineDirective()
                pass
            elif token in [ParaPreProcessorParser.Error]:
                self.enterOuterAlt(localctx, 4)
                self.state = 85
                self.errorDirective()
                pass
            elif token in [ParaPreProcessorParser.Pragma]:
                self.enterOuterAlt(localctx, 5)
                self.state = 86
                self.pragmaDirective()
                pass
            elif token in [ParaPreProcessorParser.Line]:
                self.enterOuterAlt(localctx, 6)
                self.state = 87
                self.lineDirective()
                pass
            elif token in [ParaPreProcessorParser.Undefine]:
                self.enterOuterAlt(localctx, 7)
                self.state = 88
                self.undefDirective()
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


    class SelectionPreProcessorDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def startOfSelectionBlock(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.StartOfSelectionBlockContext,0)


        def endIfDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.EndIfDirectiveContext,0)


        def selectionDirectiveAlternatives(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaPreProcessorParser.SelectionDirectiveAlternativesContext)
            else:
                return self.getTypedRuleContext(ParaPreProcessorParser.SelectionDirectiveAlternativesContext,i)


        def selectionElseDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.SelectionElseDirectiveContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_selectionPreProcessorDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionPreProcessorDirective" ):
                listener.enterSelectionPreProcessorDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionPreProcessorDirective" ):
                listener.exitSelectionPreProcessorDirective(self)




    def selectionPreProcessorDirective(self):

        localctx = ParaPreProcessorParser.SelectionPreProcessorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_selectionPreProcessorDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.startOfSelectionBlock()
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaPreProcessorParser.ElIfNotDefined) | (1 << ParaPreProcessorParser.ElIfDefined) | (1 << ParaPreProcessorParser.ElseIf))) != 0):
                self.state = 92
                self.selectionDirectiveAlternatives()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ParaPreProcessorParser.Else:
                self.state = 98
                self.selectionElseDirective()


            self.state = 101
            self.endIfDirective()
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
            return self.getTypedRuleContext(ParaPreProcessorParser.SelectionBlockContext,0)


        def ifDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.IfDirectiveContext,0)


        def ifDefinedDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.IfDefinedDirectiveContext,0)


        def ifNotDefinedDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.IfNotDefinedDirectiveContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_startOfSelectionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartOfSelectionBlock" ):
                listener.enterStartOfSelectionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartOfSelectionBlock" ):
                listener.exitStartOfSelectionBlock(self)




    def startOfSelectionBlock(self):

        localctx = ParaPreProcessorParser.StartOfSelectionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_startOfSelectionBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ParaPreProcessorParser.If]:
                self.state = 103
                self.ifDirective()
                pass
            elif token in [ParaPreProcessorParser.IfDefined]:
                self.state = 104
                self.ifDefinedDirective()
                pass
            elif token in [ParaPreProcessorParser.IfNotDefined]:
                self.state = 105
                self.ifNotDefinedDirective()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 108
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
            return self.getTypedRuleContext(ParaPreProcessorParser.SelectionBlockContext,0)


        def elIfDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.ElIfDirectiveContext,0)


        def elIfDefinedDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.ElIfDefinedDirectiveContext,0)


        def elIfNotDefinedDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.ElIfNotDefinedDirectiveContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_selectionDirectiveAlternatives

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionDirectiveAlternatives" ):
                listener.enterSelectionDirectiveAlternatives(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionDirectiveAlternatives" ):
                listener.exitSelectionDirectiveAlternatives(self)




    def selectionDirectiveAlternatives(self):

        localctx = ParaPreProcessorParser.SelectionDirectiveAlternativesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_selectionDirectiveAlternatives)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ParaPreProcessorParser.ElseIf]:
                self.state = 110
                self.elIfDirective()
                pass
            elif token in [ParaPreProcessorParser.ElIfDefined]:
                self.state = 111
                self.elIfDefinedDirective()
                pass
            elif token in [ParaPreProcessorParser.ElIfNotDefined]:
                self.state = 112
                self.elIfNotDefinedDirective()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 115
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

        def elseDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.ElseDirectiveContext,0)


        def selectionBlock(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.SelectionBlockContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_selectionElseDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionElseDirective" ):
                listener.enterSelectionElseDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionElseDirective" ):
                listener.exitSelectionElseDirective(self)




    def selectionElseDirective(self):

        localctx = ParaPreProcessorParser.SelectionElseDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_selectionElseDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.elseDirective()
            self.state = 118
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

        def nonPreProcessorItemSequence(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaPreProcessorParser.NonPreProcessorItemSequenceContext)
            else:
                return self.getTypedRuleContext(ParaPreProcessorParser.NonPreProcessorItemSequenceContext,i)


        def Newline(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Newline)
            else:
                return self.getToken(ParaPreProcessorParser.Newline, i)

        def selectionPreProcessorDirective(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ParaPreProcessorParser.SelectionPreProcessorDirectiveContext)
            else:
                return self.getTypedRuleContext(ParaPreProcessorParser.SelectionPreProcessorDirectiveContext,i)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_selectionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectionBlock" ):
                listener.enterSelectionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectionBlock" ):
                listener.exitSelectionBlock(self)




    def selectionBlock(self):

        localctx = ParaPreProcessorParser.SelectionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_selectionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaPreProcessorParser.Identifier) | (1 << ParaPreProcessorParser.StringLiteral) | (1 << ParaPreProcessorParser.DigitSequence) | (1 << ParaPreProcessorParser.Whitespace) | (1 << ParaPreProcessorParser.Newline) | (1 << ParaPreProcessorParser.NonPreProcessorItemSequence))) != 0):
                self.state = 122
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ParaPreProcessorParser.Identifier, ParaPreProcessorParser.StringLiteral, ParaPreProcessorParser.DigitSequence, ParaPreProcessorParser.Whitespace, ParaPreProcessorParser.NonPreProcessorItemSequence]:
                    self.state = 120
                    self.nonPreProcessorItemSequence()
                    pass
                elif token in [ParaPreProcessorParser.Newline]:
                    self.state = 121
                    self.match(ParaPreProcessorParser.Newline)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaPreProcessorParser.If) | (1 << ParaPreProcessorParser.IfDefined) | (1 << ParaPreProcessorParser.IfNotDefined))) != 0):
                self.state = 127
                self.selectionPreProcessorDirective()
                self.state = 132
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
            return self.getTypedRuleContext(ParaPreProcessorParser.FileIncludeDirectiveContext,0)


        def computedIncludeDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.ComputedIncludeDirectiveContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_includeDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeDirective" ):
                listener.enterIncludeDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeDirective" ):
                listener.exitIncludeDirective(self)




    def includeDirective(self):

        localctx = ParaPreProcessorParser.IncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_includeDirective)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.fileIncludeDirective()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 134
                self.computedIncludeDirective()
                pass


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

        def libIncludeDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.LibIncludeDirectiveContext,0)


        def stringIncludeDirective(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.StringIncludeDirectiveContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_fileIncludeDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileIncludeDirective" ):
                listener.enterFileIncludeDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileIncludeDirective" ):
                listener.exitFileIncludeDirective(self)




    def fileIncludeDirective(self):

        localctx = ParaPreProcessorParser.FileIncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_fileIncludeDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 137
                self.libIncludeDirective()
                pass

            elif la_ == 2:
                self.state = 138
                self.stringIncludeDirective()
                pass


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

        def Include(self):
            return self.getToken(ParaPreProcessorParser.Include, 0)

        def Identifier(self):
            return self.getToken(ParaPreProcessorParser.Identifier, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_computedIncludeDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComputedIncludeDirective" ):
                listener.enterComputedIncludeDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComputedIncludeDirective" ):
                listener.exitComputedIncludeDirective(self)




    def computedIncludeDirective(self):

        localctx = ParaPreProcessorParser.ComputedIncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_computedIncludeDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(ParaPreProcessorParser.Include)
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 147
            self.match(ParaPreProcessorParser.Identifier)
            self.state = 148
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfNotDefinedDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IfNotDefined(self):
            return self.getToken(ParaPreProcessorParser.IfNotDefined, 0)

        def Identifier(self):
            return self.getToken(ParaPreProcessorParser.Identifier, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_ifNotDefinedDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfNotDefinedDirective" ):
                listener.enterIfNotDefinedDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfNotDefinedDirective" ):
                listener.exitIfNotDefinedDirective(self)




    def ifNotDefinedDirective(self):

        localctx = ParaPreProcessorParser.IfNotDefinedDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_ifNotDefinedDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(ParaPreProcessorParser.IfNotDefined)
            self.state = 152 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 151
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 154 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 156
            self.match(ParaPreProcessorParser.Identifier)
            self.state = 157
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfDefinedDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IfDefined(self):
            return self.getToken(ParaPreProcessorParser.IfDefined, 0)

        def Identifier(self):
            return self.getToken(ParaPreProcessorParser.Identifier, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_ifDefinedDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfDefinedDirective" ):
                listener.enterIfDefinedDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfDefinedDirective" ):
                listener.exitIfDefinedDirective(self)




    def ifDefinedDirective(self):

        localctx = ParaPreProcessorParser.IfDefinedDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ifDefinedDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ParaPreProcessorParser.IfDefined)
            self.state = 161 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 160
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 163 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 165
            self.match(ParaPreProcessorParser.Identifier)
            self.state = 166
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElIfNotDefinedDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ElIfNotDefined(self):
            return self.getToken(ParaPreProcessorParser.ElIfNotDefined, 0)

        def Identifier(self):
            return self.getToken(ParaPreProcessorParser.Identifier, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_elIfNotDefinedDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElIfNotDefinedDirective" ):
                listener.enterElIfNotDefinedDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElIfNotDefinedDirective" ):
                listener.exitElIfNotDefinedDirective(self)




    def elIfNotDefinedDirective(self):

        localctx = ParaPreProcessorParser.ElIfNotDefinedDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elIfNotDefinedDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(ParaPreProcessorParser.ElIfNotDefined)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 169
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 174
            self.match(ParaPreProcessorParser.Identifier)
            self.state = 175
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElIfDefinedDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ElIfDefined(self):
            return self.getToken(ParaPreProcessorParser.ElIfDefined, 0)

        def Identifier(self):
            return self.getToken(ParaPreProcessorParser.Identifier, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_elIfDefinedDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElIfDefinedDirective" ):
                listener.enterElIfDefinedDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElIfDefinedDirective" ):
                listener.exitElIfDefinedDirective(self)




    def elIfDefinedDirective(self):

        localctx = ParaPreProcessorParser.ElIfDefinedDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_elIfDefinedDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ParaPreProcessorParser.ElIfDefined)
            self.state = 179 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 183
            self.match(ParaPreProcessorParser.Identifier)
            self.state = 184
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def If(self):
            return self.getToken(ParaPreProcessorParser.If, 0)

        def anySequence(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.AnySequenceContext,0)


        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_ifDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfDirective" ):
                listener.enterIfDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfDirective" ):
                listener.exitIfDirective(self)




    def ifDirective(self):

        localctx = ParaPreProcessorParser.IfDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_ifDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ParaPreProcessorParser.If)
            self.state = 187
            self.anySequence()
            self.state = 188
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElIfDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ElseIf(self):
            return self.getToken(ParaPreProcessorParser.ElseIf, 0)

        def anySequence(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.AnySequenceContext,0)


        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_elIfDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElIfDirective" ):
                listener.enterElIfDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElIfDirective" ):
                listener.exitElIfDirective(self)




    def elIfDirective(self):

        localctx = ParaPreProcessorParser.ElIfDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_elIfDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(ParaPreProcessorParser.ElseIf)
            self.state = 191
            self.anySequence()
            self.state = 192
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Else(self):
            return self.getToken(ParaPreProcessorParser.Else, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_elseDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseDirective" ):
                listener.enterElseDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseDirective" ):
                listener.exitElseDirective(self)




    def elseDirective(self):

        localctx = ParaPreProcessorParser.ElseDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_elseDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(ParaPreProcessorParser.Else)
            self.state = 195
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndIfDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EndIf(self):
            return self.getToken(ParaPreProcessorParser.EndIf, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_endIfDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndIfDirective" ):
                listener.enterEndIfDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndIfDirective" ):
                listener.exitEndIfDirective(self)




    def endIfDirective(self):

        localctx = ParaPreProcessorParser.EndIfDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_endIfDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(ParaPreProcessorParser.EndIf)
            self.state = 198
            self.preProcessorEnd()
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

        def Pragma(self):
            return self.getToken(ParaPreProcessorParser.Pragma, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Identifier)
            else:
                return self.getToken(ParaPreProcessorParser.Identifier, i)

        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_pragmaDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragmaDirective" ):
                listener.enterPragmaDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragmaDirective" ):
                listener.exitPragmaDirective(self)




    def pragmaDirective(self):

        localctx = ParaPreProcessorParser.PragmaDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_pragmaDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ParaPreProcessorParser.Pragma)
            self.state = 207 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 202 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 201
                        self.match(ParaPreProcessorParser.Whitespace)
                        self.state = 204 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==ParaPreProcessorParser.Whitespace):
                            break

                    self.state = 206
                    self.match(ParaPreProcessorParser.Identifier)

                else:
                    raise NoViableAltException(self)
                self.state = 209 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 211
            self.preProcessorEnd()
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

        def Error(self):
            return self.getToken(ParaPreProcessorParser.Error, 0)

        def anySequence(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.AnySequenceContext,0)


        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_errorDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterErrorDirective" ):
                listener.enterErrorDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitErrorDirective" ):
                listener.exitErrorDirective(self)




    def errorDirective(self):

        localctx = ParaPreProcessorParser.ErrorDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_errorDirective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ParaPreProcessorParser.Error)
            self.state = 214
            self.anySequence()
            self.state = 215
            self.preProcessorEnd()
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

        def Undefine(self):
            return self.getToken(ParaPreProcessorParser.Undefine, 0)

        def Identifier(self):
            return self.getToken(ParaPreProcessorParser.Identifier, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_undefDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUndefDirective" ):
                listener.enterUndefDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUndefDirective" ):
                listener.exitUndefDirective(self)




    def undefDirective(self):

        localctx = ParaPreProcessorParser.UndefDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_undefDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(ParaPreProcessorParser.Undefine)
            self.state = 219 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 218
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 221 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 223
            self.match(ParaPreProcessorParser.Identifier)
            self.state = 224
            self.preProcessorEnd()
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

        def Define(self):
            return self.getToken(ParaPreProcessorParser.Define, 0)

        def Identifier(self):
            return self.getToken(ParaPreProcessorParser.Identifier, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def anySequence(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.AnySequenceContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_complexDefineDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplexDefineDirective" ):
                listener.enterComplexDefineDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplexDefineDirective" ):
                listener.exitComplexDefineDirective(self)




    def complexDefineDirective(self):

        localctx = ParaPreProcessorParser.ComplexDefineDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_complexDefineDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(ParaPreProcessorParser.Define)
            self.state = 228 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 227
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 230 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 232
            self.match(ParaPreProcessorParser.Identifier)
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 234 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 233
                        self.match(ParaPreProcessorParser.Whitespace)

                    else:
                        raise NoViableAltException(self)
                    self.state = 236 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                self.state = 238
                self.anySequence()


            self.state = 241
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LibIncludeDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Include(self):
            return self.getToken(ParaPreProcessorParser.Include, 0)

        def LibStringLiteral(self):
            return self.getToken(ParaPreProcessorParser.LibStringLiteral, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_libIncludeDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLibIncludeDirective" ):
                listener.enterLibIncludeDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLibIncludeDirective" ):
                listener.exitLibIncludeDirective(self)




    def libIncludeDirective(self):

        localctx = ParaPreProcessorParser.LibIncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_libIncludeDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(ParaPreProcessorParser.Include)
            self.state = 245 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 244
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 247 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 249
            self.match(ParaPreProcessorParser.LibStringLiteral)
            self.state = 250
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringIncludeDirectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Include(self):
            return self.getToken(ParaPreProcessorParser.Include, 0)

        def StringLiteral(self):
            return self.getToken(ParaPreProcessorParser.StringLiteral, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_stringIncludeDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringIncludeDirective" ):
                listener.enterStringIncludeDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringIncludeDirective" ):
                listener.exitStringIncludeDirective(self)




    def stringIncludeDirective(self):

        localctx = ParaPreProcessorParser.StringIncludeDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stringIncludeDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(ParaPreProcessorParser.Include)
            self.state = 254 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 253
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 256 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 258
            self.match(ParaPreProcessorParser.StringLiteral)
            self.state = 259
            self.preProcessorEnd()
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

        def Line(self):
            return self.getToken(ParaPreProcessorParser.Line, 0)

        def DigitSequence(self):
            return self.getToken(ParaPreProcessorParser.DigitSequence, 0)

        def preProcessorEnd(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.PreProcessorEndContext,0)


        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def StringLiteral(self):
            return self.getToken(ParaPreProcessorParser.StringLiteral, 0)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_lineDirective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineDirective" ):
                listener.enterLineDirective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineDirective" ):
                listener.exitLineDirective(self)




    def lineDirective(self):

        localctx = ParaPreProcessorParser.LineDirectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_lineDirective)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(ParaPreProcessorParser.Line)
            self.state = 263 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 262
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 265 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ParaPreProcessorParser.Whitespace):
                    break

            self.state = 267
            self.match(ParaPreProcessorParser.DigitSequence)
            self.state = 269 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 268
                    self.match(ParaPreProcessorParser.Whitespace)

                else:
                    raise NoViableAltException(self)
                self.state = 271 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ParaPreProcessorParser.StringLiteral:
                self.state = 273
                self.match(ParaPreProcessorParser.StringLiteral)


            self.state = 276
            self.preProcessorEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NonPreProcessorItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def anySequence(self):
            return self.getTypedRuleContext(ParaPreProcessorParser.AnySequenceContext,0)


        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_nonPreProcessorItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonPreProcessorItem" ):
                listener.enterNonPreProcessorItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonPreProcessorItem" ):
                listener.exitNonPreProcessorItem(self)




    def nonPreProcessorItem(self):

        localctx = ParaPreProcessorParser.NonPreProcessorItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_nonPreProcessorItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.anySequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnySequenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Identifier)
            else:
                return self.getToken(ParaPreProcessorParser.Identifier, i)

        def DigitSequence(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.DigitSequence)
            else:
                return self.getToken(ParaPreProcessorParser.DigitSequence, i)

        def StringLiteral(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.StringLiteral)
            else:
                return self.getToken(ParaPreProcessorParser.StringLiteral, i)

        def NonPreProcessorItemSequence(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.NonPreProcessorItemSequence)
            else:
                return self.getToken(ParaPreProcessorParser.NonPreProcessorItemSequence, i)

        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_anySequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnySequence" ):
                listener.enterAnySequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnySequence" ):
                listener.exitAnySequence(self)




    def anySequence(self):

        localctx = ParaPreProcessorParser.AnySequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_anySequence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 280
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ParaPreProcessorParser.Identifier) | (1 << ParaPreProcessorParser.StringLiteral) | (1 << ParaPreProcessorParser.DigitSequence) | (1 << ParaPreProcessorParser.Whitespace) | (1 << ParaPreProcessorParser.NonPreProcessorItemSequence))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()

                else:
                    raise NoViableAltException(self)
                self.state = 283 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PreProcessorEndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Newline(self):
            return self.getToken(ParaPreProcessorParser.Newline, 0)

        def EOF(self):
            return self.getToken(ParaPreProcessorParser.EOF, 0)

        def Whitespace(self, i:int=None):
            if i is None:
                return self.getTokens(ParaPreProcessorParser.Whitespace)
            else:
                return self.getToken(ParaPreProcessorParser.Whitespace, i)

        def getRuleIndex(self):
            return ParaPreProcessorParser.RULE_preProcessorEnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreProcessorEnd" ):
                listener.enterPreProcessorEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreProcessorEnd" ):
                listener.exitPreProcessorEnd(self)




    def preProcessorEnd(self):

        localctx = ParaPreProcessorParser.PreProcessorEndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_preProcessorEnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ParaPreProcessorParser.Whitespace:
                self.state = 285
                self.match(ParaPreProcessorParser.Whitespace)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
            _la = self._input.LA(1)
            if not(_la==ParaPreProcessorParser.EOF or _la==ParaPreProcessorParser.Newline):
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





