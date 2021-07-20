# Generated from ./grammar/ParaCPreProcessor.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\32")
        buf.write("\u0149\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\3\2\3\2\7\2R\n\2\f\2\16\2U\13\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\7\23\u00ca\n\23\f\23\16\23\u00cd\13\23\3\24")
        buf.write("\3\24\5\24\u00d1\n\24\3\25\3\25\5\25\u00d5\n\25\3\25\3")
        buf.write("\25\3\26\3\26\5\26\u00db\n\26\3\26\3\26\3\27\6\27\u00e0")
        buf.write("\n\27\r\27\16\27\u00e1\3\30\6\30\u00e5\n\30\r\30\16\30")
        buf.write("\u00e6\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00f0\n")
        buf.write("\31\3\32\3\32\3\32\3\32\5\32\u00f6\n\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\5\34\u00fe\n\34\3\34\5\34\u0101\n\34\3")
        buf.write("\35\3\35\3\35\3\35\6\35\u0107\n\35\r\35\16\35\u0108\3")
        buf.write("\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u0119")
        buf.write("\n \3!\3!\3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3$\3$\7$\u0129")
        buf.write("\n$\f$\16$\u012c\13$\3$\3$\7$\u0130\n$\f$\16$\u0133\13")
        buf.write("$\3$\3$\3$\3$\3%\6%\u013a\n%\r%\16%\u013b\3&\3&\5&\u0140")
        buf.write("\n&\3&\5&\u0143\n&\3\'\6\'\u0146\n\'\r\'\16\'\u0147\2")
        buf.write("\2(\3\2\5\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f")
        buf.write("\31\r\33\16\35\17\37\20!\21#\22%\23\'\2)\24+\25-\26/\2")
        buf.write("\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\27I\30K\31")
        buf.write("M\32\3\2\f\6\2\f\f\17\17$$^^\f\2$$))AA^^cdhhppttvvxx\5")
        buf.write("\2C\\aac|\3\2\62;\3\2\629\5\2\62;CHch\3\2}}\3\2\177\177")
        buf.write("\4\2\13\13\"\"\6\2\f\f\17\17\"\"%%\2\u0152\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\3O\3\2\2\2\5V\3\2\2\2\7_\3\2\2\2\tg\3\2\2\2\13")
        buf.write("n\3\2\2\2\rr\3\2\2\2\17x\3\2\2\2\21\177\3\2\2\2\23\u0087")
        buf.write("\3\2\2\2\25\u0091\3\2\2\2\27\u009a\3\2\2\2\31\u00a0\3")
        buf.write("\2\2\2\33\u00a7\3\2\2\2\35\u00ae\3\2\2\2\37\u00b6\3\2")
        buf.write("\2\2!\u00bc\3\2\2\2#\u00c0\3\2\2\2%\u00c6\3\2\2\2\'\u00d0")
        buf.write("\3\2\2\2)\u00d2\3\2\2\2+\u00d8\3\2\2\2-\u00df\3\2\2\2")
        buf.write("/\u00e4\3\2\2\2\61\u00ef\3\2\2\2\63\u00f5\3\2\2\2\65\u00f7")
        buf.write("\3\2\2\2\67\u00fa\3\2\2\29\u0102\3\2\2\2;\u010a\3\2\2")
        buf.write("\2=\u010c\3\2\2\2?\u0118\3\2\2\2A\u011a\3\2\2\2C\u011f")
        buf.write("\3\2\2\2E\u0121\3\2\2\2G\u0123\3\2\2\2I\u0139\3\2\2\2")
        buf.write("K\u0142\3\2\2\2M\u0145\3\2\2\2OS\7%\2\2PR\5I%\2QP\3\2")
        buf.write("\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\4\3\2\2\2US\3\2\2")
        buf.write("\2VW\5\3\2\2WX\7k\2\2XY\7p\2\2YZ\7e\2\2Z[\7n\2\2[\\\7")
        buf.write("w\2\2\\]\7f\2\2]^\7g\2\2^\6\3\2\2\2_`\5\3\2\2`a\7f\2\2")
        buf.write("ab\7g\2\2bc\7h\2\2cd\7k\2\2de\7p\2\2ef\7g\2\2f\b\3\2\2")
        buf.write("\2gh\5\3\2\2hi\7w\2\2ij\7p\2\2jk\7f\2\2kl\7g\2\2lm\7h")
        buf.write("\2\2m\n\3\2\2\2no\5\3\2\2op\7k\2\2pq\7h\2\2q\f\3\2\2\2")
        buf.write("rs\5\3\2\2st\7g\2\2tu\7n\2\2uv\7u\2\2vw\7g\2\2w\16\3\2")
        buf.write("\2\2xy\5\3\2\2yz\7k\2\2z{\7h\2\2{|\7f\2\2|}\7g\2\2}~\7")
        buf.write("h\2\2~\20\3\2\2\2\177\u0080\5\3\2\2\u0080\u0081\7k\2\2")
        buf.write("\u0081\u0082\7h\2\2\u0082\u0083\7p\2\2\u0083\u0084\7f")
        buf.write("\2\2\u0084\u0085\7g\2\2\u0085\u0086\7h\2\2\u0086\22\3")
        buf.write("\2\2\2\u0087\u0088\5\3\2\2\u0088\u0089\7g\2\2\u0089\u008a")
        buf.write("\7n\2\2\u008a\u008b\7k\2\2\u008b\u008c\7h\2\2\u008c\u008d")
        buf.write("\7p\2\2\u008d\u008e\7f\2\2\u008e\u008f\7g\2\2\u008f\u0090")
        buf.write("\7h\2\2\u0090\24\3\2\2\2\u0091\u0092\5\3\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7n\2\2\u0094\u0095\7k\2\2\u0095\u0096")
        buf.write("\7h\2\2\u0096\u0097\7f\2\2\u0097\u0098\7g\2\2\u0098\u0099")
        buf.write("\7h\2\2\u0099\26\3\2\2\2\u009a\u009b\5\3\2\2\u009b\u009c")
        buf.write("\7g\2\2\u009c\u009d\7n\2\2\u009d\u009e\7k\2\2\u009e\u009f")
        buf.write("\7h\2\2\u009f\30\3\2\2\2\u00a0\u00a1\5\3\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7p\2\2\u00a3\u00a4\7f\2\2\u00a4\u00a5")
        buf.write("\7k\2\2\u00a5\u00a6\7h\2\2\u00a6\32\3\2\2\2\u00a7\u00a8")
        buf.write("\5\3\2\2\u00a8\u00a9\7g\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7t\2\2\u00ad\34")
        buf.write("\3\2\2\2\u00ae\u00af\5\3\2\2\u00af\u00b0\7r\2\2\u00b0")
        buf.write("\u00b1\7t\2\2\u00b1\u00b2\7c\2\2\u00b2\u00b3\7i\2\2\u00b3")
        buf.write("\u00b4\7o\2\2\u00b4\u00b5\7c\2\2\u00b5\36\3\2\2\2\u00b6")
        buf.write("\u00b7\5\3\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7k\2\2\u00b9")
        buf.write("\u00ba\7p\2\2\u00ba\u00bb\7g\2\2\u00bb \3\2\2\2\u00bc")
        buf.write("\u00bd\7I\2\2\u00bd\u00be\7E\2\2\u00be\u00bf\7E\2\2\u00bf")
        buf.write("\"\3\2\2\2\u00c0\u00c1\7R\2\2\u00c1\u00c2\7C\2\2\u00c2")
        buf.write("\u00c3\7T\2\2\u00c3\u00c4\7C\2\2\u00c4\u00c5\7E\2\2\u00c5")
        buf.write("$\3\2\2\2\u00c6\u00cb\5\'\24\2\u00c7\u00ca\5\'\24\2\u00c8")
        buf.write("\u00ca\5=\37\2\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2")
        buf.write("\u00ca\u00cd\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3")
        buf.write("\2\2\2\u00cc&\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d1")
        buf.write("\5;\36\2\u00cf\u00d1\5? \2\u00d0\u00ce\3\2\2\2\u00d0\u00cf")
        buf.write("\3\2\2\2\u00d1(\3\2\2\2\u00d2\u00d4\7>\2\2\u00d3\u00d5")
        buf.write("\5/\30\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00d7\7@\2\2\u00d7*\3\2\2\2\u00d8")
        buf.write("\u00da\7$\2\2\u00d9\u00db\5/\30\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd\7")
        buf.write("$\2\2\u00dd,\3\2\2\2\u00de\u00e0\5=\37\2\u00df\u00de\3")
        buf.write("\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2.\3\2\2\2\u00e3\u00e5\5\61\31\2\u00e4\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e7\3\2\2\2\u00e7\60\3\2\2\2\u00e8\u00f0\n\2\2\2\u00e9")
        buf.write("\u00f0\5\63\32\2\u00ea\u00eb\7^\2\2\u00eb\u00f0\7\f\2")
        buf.write("\2\u00ec\u00ed\7^\2\2\u00ed\u00ee\7\17\2\2\u00ee\u00f0")
        buf.write("\7\f\2\2\u00ef\u00e8\3\2\2\2\u00ef\u00e9\3\2\2\2\u00ef")
        buf.write("\u00ea\3\2\2\2\u00ef\u00ec\3\2\2\2\u00f0\62\3\2\2\2\u00f1")
        buf.write("\u00f6\5\65\33\2\u00f2\u00f6\5\67\34\2\u00f3\u00f6\59")
        buf.write("\35\2\u00f4\u00f6\5? \2\u00f5\u00f1\3\2\2\2\u00f5\u00f2")
        buf.write("\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write("\64\3\2\2\2\u00f7\u00f8\7^\2\2\u00f8\u00f9\t\3\2\2\u00f9")
        buf.write("\66\3\2\2\2\u00fa\u00fb\7^\2\2\u00fb\u00fd\5C\"\2\u00fc")
        buf.write("\u00fe\5C\"\2\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2")
        buf.write("\u00fe\u0100\3\2\2\2\u00ff\u0101\5C\"\2\u0100\u00ff\3")
        buf.write("\2\2\2\u0100\u0101\3\2\2\2\u01018\3\2\2\2\u0102\u0103")
        buf.write("\7^\2\2\u0103\u0104\7z\2\2\u0104\u0106\3\2\2\2\u0105\u0107")
        buf.write("\5E#\2\u0106\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0106")
        buf.write("\3\2\2\2\u0108\u0109\3\2\2\2\u0109:\3\2\2\2\u010a\u010b")
        buf.write("\t\4\2\2\u010b<\3\2\2\2\u010c\u010d\t\5\2\2\u010d>\3\2")
        buf.write("\2\2\u010e\u010f\7^\2\2\u010f\u0110\7w\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u0119\5A!\2\u0112\u0113\7^\2\2\u0113\u0114")
        buf.write("\7W\2\2\u0114\u0115\3\2\2\2\u0115\u0116\5A!\2\u0116\u0117")
        buf.write("\5A!\2\u0117\u0119\3\2\2\2\u0118\u010e\3\2\2\2\u0118\u0112")
        buf.write("\3\2\2\2\u0119@\3\2\2\2\u011a\u011b\5E#\2\u011b\u011c")
        buf.write("\5E#\2\u011c\u011d\5E#\2\u011d\u011e\5E#\2\u011eB\3\2")
        buf.write("\2\2\u011f\u0120\t\6\2\2\u0120D\3\2\2\2\u0121\u0122\t")
        buf.write("\7\2\2\u0122F\3\2\2\2\u0123\u0124\7c\2\2\u0124\u0125\7")
        buf.write("u\2\2\u0125\u0126\7o\2\2\u0126\u012a\3\2\2\2\u0127\u0129")
        buf.write("\n\b\2\2\u0128\u0127\3\2\2\2\u0129\u012c\3\2\2\2\u012a")
        buf.write("\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012d\3\2\2\2")
        buf.write("\u012c\u012a\3\2\2\2\u012d\u0131\7}\2\2\u012e\u0130\n")
        buf.write("\t\2\2\u012f\u012e\3\2\2\2\u0130\u0133\3\2\2\2\u0131\u012f")
        buf.write("\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0134\u0135\7\177\2\2\u0135\u0136\3\2\2")
        buf.write("\2\u0136\u0137\b$\2\2\u0137H\3\2\2\2\u0138\u013a\t\n\2")
        buf.write("\2\u0139\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0139")
        buf.write("\3\2\2\2\u013b\u013c\3\2\2\2\u013cJ\3\2\2\2\u013d\u013f")
        buf.write("\7\17\2\2\u013e\u0140\7\f\2\2\u013f\u013e\3\2\2\2\u013f")
        buf.write("\u0140\3\2\2\2\u0140\u0143\3\2\2\2\u0141\u0143\7\f\2\2")
        buf.write("\u0142\u013d\3\2\2\2\u0142\u0141\3\2\2\2\u0143L\3\2\2")
        buf.write("\2\u0144\u0146\n\13\2\2\u0145\u0144\3\2\2\2\u0146\u0147")
        buf.write("\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("N\3\2\2\2\27\2S\u00c9\u00cb\u00d0\u00d4\u00da\u00e1\u00e6")
        buf.write("\u00ef\u00f5\u00fd\u0100\u0108\u0118\u012a\u0131\u013b")
        buf.write("\u013f\u0142\u0147\3\b\2\2")
        return buf.getvalue()


class ParaCPreProcessorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Include = 1
    Define = 2
    Undefine = 3
    If = 4
    Else = 5
    IfDefined = 6
    IfNotDefined = 7
    ElIfNotDefined = 8
    ElIfDefined = 9
    ElseIf = 10
    EndIf = 11
    Error = 12
    Pragma = 13
    Line = 14
    GCCParacPrefix = 15
    PragmaParacPrefix = 16
    Identifier = 17
    LibStringLiteral = 18
    StringLiteral = 19
    DigitSequence = 20
    AsmBlock = 21
    Whitespace = 22
    Newline = 23
    NonPreProcessorItemSequence = 24

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'GCC'", "'PARAC'" ]

    symbolicNames = [ "<INVALID>",
            "Include", "Define", "Undefine", "If", "Else", "IfDefined", 
            "IfNotDefined", "ElIfNotDefined", "ElIfDefined", "ElseIf", "EndIf", 
            "Error", "Pragma", "Line", "GCCParacPrefix", "PragmaParacPrefix", 
            "Identifier", "LibStringLiteral", "StringLiteral", "DigitSequence", 
            "AsmBlock", "Whitespace", "Newline", "NonPreProcessorItemSequence" ]

    ruleNames = [ "PreProcessorBegin", "Include", "Define", "Undefine", 
                  "If", "Else", "IfDefined", "IfNotDefined", "ElIfNotDefined", 
                  "ElIfDefined", "ElseIf", "EndIf", "Error", "Pragma", "Line", 
                  "GCCParacPrefix", "PragmaParacPrefix", "Identifier", "IdentifierNondigit", 
                  "LibStringLiteral", "StringLiteral", "DigitSequence", 
                  "SCharSequence", "SChar", "EscapeSequence", "SimpleEscapeSequence", 
                  "OctalEscapeSequence", "HexadecimalEscapeSequence", "Nondigit", 
                  "Digit", "UniversalCharacterName", "HexQuad", "OctalDigit", 
                  "HexadecimalDigit", "AsmBlock", "Whitespace", "Newline", 
                  "NonPreProcessorItemSequence" ]

    grammarFileName = "ParaCPreProcessor.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


