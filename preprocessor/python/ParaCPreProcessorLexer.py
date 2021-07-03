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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("\u01d9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\3\2\6\2_\n\2\r\2\16\2`\3\2\3\2\3\3\3\3\3\3\7\3h\n")
        buf.write("\3\f\3\16\3k\13\3\3\4\3\4\3\4\3\4\7\4q\n\4\f\4\16\4t\13")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5}\n\5\f\5\16\5\u0080")
        buf.write("\13\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\n\3\n\7\n\u0090\n\n\f\n\16\n\u0093\13\n\3\13\3\13\7")
        buf.write("\13\u0097\n\13\f\13\16\13\u009a\13\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00a4\n\16\3\16\6\16\u00a7\n")
        buf.write("\16\r\16\16\16\u00a8\3\16\3\16\6\16\u00ad\n\16\r\16\16")
        buf.write("\16\u00ae\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u00b7\n\20")
        buf.write("\3\20\7\20\u00ba\n\20\f\20\16\20\u00bd\13\20\3\20\5\20")
        buf.write("\u00c0\n\20\3\21\3\21\3\21\3\22\3\22\3\22\6\22\u00c8\n")
        buf.write("\22\r\22\16\22\u00c9\3\22\3\22\3\23\3\23\3\23\6\23\u00d1")
        buf.write("\n\23\r\23\16\23\u00d2\3\23\3\23\3\24\3\24\7\24\u00d9")
        buf.write("\n\24\f\24\16\24\u00dc\13\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\6\25\u00e8\n\25\r\25\16\25\u00e9")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\6\26\u00f5")
        buf.write("\n\26\r\26\16\26\u00f6\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\6\27\u0101\n\27\r\27\16\27\u0102\3\30\3\30\3")
        buf.write("\30\3\30\3\30\6\30\u010a\n\30\r\30\16\30\u010b\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\5\31\u0115\n\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\6\32\u011f\n\32\r\32\16")
        buf.write("\32\u0120\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\6\33\u012c\n\33\r\33\16\33\u012d\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\6\34\u013d")
        buf.write("\n\34\r\34\16\34\u013e\3\35\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\6\35\u014b\n\35\r\35\16\35\u014c\3")
        buf.write("\36\3\36\3\36\3\36\3\36\3\36\3\36\6\36\u0156\n\36\r\36")
        buf.write("\16\36\u0157\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5")
        buf.write("\37\u0162\n\37\3 \3 \3 \3 \3 \3 \3 \3 \6 \u016c\n \r ")
        buf.write("\16 \u016d\3!\3!\3!\3!\3!\3!\3!\3!\3!\6!\u0179\n!\r!\16")
        buf.write("!\u017a\3\"\3\"\3\"\3\"\3\"\3\"\6\"\u0183\n\"\r\"\16\"")
        buf.write("\u0184\3#\3#\3#\3#\3#\3#\3#\3#\6#\u018f\n#\r#\16#\u0190")
        buf.write("\3$\3$\3$\5$\u0196\n$\3%\3%\5%\u019a\n%\3&\3&\3\'\3\'")
        buf.write("\3(\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01aa\n(\3)\3)\3)\3")
        buf.write(")\3)\3*\3*\3+\3+\3,\3,\3,\3,\3,\7,\u01ba\n,\f,\16,\u01bd")
        buf.write("\13,\3,\3,\7,\u01c1\n,\f,\16,\u01c4\13,\3,\3,\3,\3,\3")
        buf.write("-\6-\u01cb\n-\r-\16-\u01cc\3-\3-\3.\3.\5.\u01d3\n.\3.")
        buf.write("\5.\u01d6\n.\3.\3.\3r\2/\3\3\5\2\7\2\t\2\13\4\r\5\17\6")
        buf.write("\21\7\23\b\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21")
        buf.write("\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2")
        buf.write("E\2G\2I\2K\2M\2O\2Q\2S\2U\2W\22Y\23[\24\3\2\13\5\2\f\f")
        buf.write("\17\17%%\4\2\f\f\17\17\5\2C\\aac|\3\2\62;\3\2\629\5\2")
        buf.write("\62;CHch\3\2}}\3\2\177\177\4\2\13\13\"\"\2\u01e6\2\3\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2")
        buf.write("\3^\3\2\2\2\5d\3\2\2\2\7l\3\2\2\2\tx\3\2\2\2\13\u0081")
        buf.write("\3\2\2\2\r\u0084\3\2\2\2\17\u0087\3\2\2\2\21\u008a\3\2")
        buf.write("\2\2\23\u008d\3\2\2\2\25\u0094\3\2\2\2\27\u009b\3\2\2")
        buf.write("\2\31\u009d\3\2\2\2\33\u009f\3\2\2\2\35\u00b0\3\2\2\2")
        buf.write("\37\u00b3\3\2\2\2!\u00c1\3\2\2\2#\u00c4\3\2\2\2%\u00cd")
        buf.write("\3\2\2\2\'\u00d6\3\2\2\2)\u00dd\3\2\2\2+\u00eb\3\2\2\2")
        buf.write("-\u00f8\3\2\2\2/\u0104\3\2\2\2\61\u010d\3\2\2\2\63\u0116")
        buf.write("\3\2\2\2\65\u0122\3\2\2\2\67\u012f\3\2\2\29\u0140\3\2")
        buf.write("\2\2;\u014e\3\2\2\2=\u0159\3\2\2\2?\u0163\3\2\2\2A\u016f")
        buf.write("\3\2\2\2C\u017c\3\2\2\2E\u0186\3\2\2\2G\u0195\3\2\2\2")
        buf.write("I\u0199\3\2\2\2K\u019b\3\2\2\2M\u019d\3\2\2\2O\u01a9\3")
        buf.write("\2\2\2Q\u01ab\3\2\2\2S\u01b0\3\2\2\2U\u01b2\3\2\2\2W\u01b4")
        buf.write("\3\2\2\2Y\u01ca\3\2\2\2[\u01d5\3\2\2\2]_\n\2\2\2^]\3\2")
        buf.write("\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\2\2\2")
        buf.write("c\4\3\2\2\2di\5I%\2eh\5I%\2fh\5M\'\2ge\3\2\2\2gf\3\2\2")
        buf.write("\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\6\3\2\2\2ki\3\2\2\2")
        buf.write("lm\7\61\2\2mn\7,\2\2nr\3\2\2\2oq\13\2\2\2po\3\2\2\2qt")
        buf.write("\3\2\2\2rs\3\2\2\2rp\3\2\2\2su\3\2\2\2tr\3\2\2\2uv\7,")
        buf.write("\2\2vw\7\61\2\2w\b\3\2\2\2xy\7\61\2\2yz\7\61\2\2z~\3\2")
        buf.write("\2\2{}\n\3\2\2|{\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177")
        buf.write("\3\2\2\2\177\n\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\5\65")
        buf.write("\33\2\u0082\u0083\5\5\3\2\u0083\f\3\2\2\2\u0084\u0085")
        buf.write("\5\63\32\2\u0085\u0086\5\5\3\2\u0086\16\3\2\2\2\u0087")
        buf.write("\u0088\5\67\34\2\u0088\u0089\5\5\3\2\u0089\20\3\2\2\2")
        buf.write("\u008a\u008b\59\35\2\u008b\u008c\5\5\3\2\u008c\22\3\2")
        buf.write("\2\2\u008d\u0091\5/\30\2\u008e\u0090\n\3\2\2\u008f\u008e")
        buf.write("\3\2\2\2\u0090\u0093\3\2\2\2\u0091\u008f\3\2\2\2\u0091")
        buf.write("\u0092\3\2\2\2\u0092\24\3\2\2\2\u0093\u0091\3\2\2\2\u0094")
        buf.write("\u0098\5;\36\2\u0095\u0097\n\3\2\2\u0096\u0095\3\2\2\2")
        buf.write("\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3")
        buf.write("\2\2\2\u0099\26\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c")
        buf.write("\5\61\31\2\u009c\30\3\2\2\2\u009d\u009e\5=\37\2\u009e")
        buf.write("\32\3\2\2\2\u009f\u00a3\5A!\2\u00a0\u00a4\5C\"\2\u00a1")
        buf.write("\u00a4\5E#\2\u00a2\u00a4\5\5\3\2\u00a3\u00a0\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\u00ac\3\2\2\2")
        buf.write("\u00a5\u00a7\5Y-\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2")
        buf.write("\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00ab\5\5\3\2\u00ab\u00ad\3\2\2\2\u00ac")
        buf.write("\u00a6\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\34\3\2\2\2\u00b0\u00b1\5-\27")
        buf.write("\2\u00b1\u00b2\5\5\3\2\u00b2\36\3\2\2\2\u00b3\u00b4\5")
        buf.write("+\26\2\u00b4\u00b6\5\5\3\2\u00b5\u00b7\7*\2\2\u00b6\u00b5")
        buf.write("\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00bb\3\2\2\2\u00b8")
        buf.write("\u00ba\n\3\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2")
        buf.write("\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bf\3")
        buf.write("\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00c0\7+\2\2\u00bf\u00be")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0 \3\2\2\2\u00c1\u00c2")
        buf.write("\5)\25\2\u00c2\u00c3\5\5\3\2\u00c3\"\3\2\2\2\u00c4\u00c5")
        buf.write("\5)\25\2\u00c5\u00c7\7>\2\2\u00c6\u00c8\5G$\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\7@\2\2")
        buf.write("\u00cc$\3\2\2\2\u00cd\u00ce\5)\25\2\u00ce\u00d0\7$\2\2")
        buf.write("\u00cf\u00d1\5G$\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2")
        buf.write("\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d5\7$\2\2\u00d5&\3\2\2\2\u00d6\u00da")
        buf.write("\7%\2\2\u00d7\u00d9\5Y-\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("(\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\5\'\24\2\u00de")
        buf.write("\u00df\7k\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1\7e\2\2\u00e1")
        buf.write("\u00e2\7n\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7f\2\2\u00e4")
        buf.write("\u00e5\7g\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e8\5Y-\2\u00e7")
        buf.write("\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2")
        buf.write("\u00e9\u00ea\3\2\2\2\u00ea*\3\2\2\2\u00eb\u00ec\5\'\24")
        buf.write("\2\u00ec\u00ed\7f\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7")
        buf.write("h\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2")
        buf.write("\7g\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00f5\5Y-\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f6")
        buf.write("\u00f7\3\2\2\2\u00f7,\3\2\2\2\u00f8\u00f9\5\'\24\2\u00f9")
        buf.write("\u00fa\7w\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7f\2\2\u00fc")
        buf.write("\u00fd\7g\2\2\u00fd\u00fe\7h\2\2\u00fe\u0100\3\2\2\2\u00ff")
        buf.write("\u0101\5Y-\2\u0100\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103.\3\2\2\2\u0104")
        buf.write("\u0105\5\'\24\2\u0105\u0106\7k\2\2\u0106\u0107\7h\2\2")
        buf.write("\u0107\u0109\3\2\2\2\u0108\u010a\5Y-\2\u0109\u0108\3\2")
        buf.write("\2\2\u010a\u010b\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\60\3\2\2\2\u010d\u010e\5\'\24\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\u0110\7n\2\2\u0110\u0111\7u\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112\u0114\3\2\2\2\u0113\u0115\5Y-\2\u0114\u0113")
        buf.write("\3\2\2\2\u0114\u0115\3\2\2\2\u0115\62\3\2\2\2\u0116\u0117")
        buf.write("\5\'\24\2\u0117\u0118\7k\2\2\u0118\u0119\7h\2\2\u0119")
        buf.write("\u011a\7f\2\2\u011a\u011b\7g\2\2\u011b\u011c\7h\2\2\u011c")
        buf.write("\u011e\3\2\2\2\u011d\u011f\5Y-\2\u011e\u011d\3\2\2\2\u011f")
        buf.write("\u0120\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2")
        buf.write("\u0121\64\3\2\2\2\u0122\u0123\5\'\24\2\u0123\u0124\7k")
        buf.write("\2\2\u0124\u0125\7h\2\2\u0125\u0126\7p\2\2\u0126\u0127")
        buf.write("\7f\2\2\u0127\u0128\7g\2\2\u0128\u0129\7h\2\2\u0129\u012b")
        buf.write("\3\2\2\2\u012a\u012c\5Y-\2\u012b\u012a\3\2\2\2\u012c\u012d")
        buf.write("\3\2\2\2\u012d\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e")
        buf.write("\66\3\2\2\2\u012f\u0130\5\'\24\2\u0130\u0131\7g\2\2\u0131")
        buf.write("\u0132\7n\2\2\u0132\u0133\7k\2\2\u0133\u0134\7h\2\2\u0134")
        buf.write("\u0135\7p\2\2\u0135\u0136\7q\2\2\u0136\u0137\7v\2\2\u0137")
        buf.write("\u0138\7f\2\2\u0138\u0139\7g\2\2\u0139\u013a\7h\2\2\u013a")
        buf.write("\u013c\3\2\2\2\u013b\u013d\5Y-\2\u013c\u013b\3\2\2\2\u013d")
        buf.write("\u013e\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013f8\3\2\2\2\u0140\u0141\5\'\24\2\u0141\u0142\7g\2")
        buf.write("\2\u0142\u0143\7n\2\2\u0143\u0144\7k\2\2\u0144\u0145\7")
        buf.write("h\2\2\u0145\u0146\7f\2\2\u0146\u0147\7g\2\2\u0147\u0148")
        buf.write("\7h\2\2\u0148\u014a\3\2\2\2\u0149\u014b\5Y-\2\u014a\u0149")
        buf.write("\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014a\3\2\2\2\u014c")
        buf.write("\u014d\3\2\2\2\u014d:\3\2\2\2\u014e\u014f\5\'\24\2\u014f")
        buf.write("\u0150\7g\2\2\u0150\u0151\7n\2\2\u0151\u0152\7k\2\2\u0152")
        buf.write("\u0153\7h\2\2\u0153\u0155\3\2\2\2\u0154\u0156\5Y-\2\u0155")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0155\3\2\2\2")
        buf.write("\u0157\u0158\3\2\2\2\u0158<\3\2\2\2\u0159\u015a\5\'\24")
        buf.write("\2\u015a\u015b\7g\2\2\u015b\u015c\7p\2\2\u015c\u015d\7")
        buf.write("f\2\2\u015d\u015e\7k\2\2\u015e\u015f\7h\2\2\u015f\u0161")
        buf.write("\3\2\2\2\u0160\u0162\5Y-\2\u0161\u0160\3\2\2\2\u0161\u0162")
        buf.write("\3\2\2\2\u0162>\3\2\2\2\u0163\u0164\5\'\24\2\u0164\u0165")
        buf.write("\7g\2\2\u0165\u0166\7t\2\2\u0166\u0167\7t\2\2\u0167\u0168")
        buf.write("\7q\2\2\u0168\u0169\7t\2\2\u0169\u016b\3\2\2\2\u016a\u016c")
        buf.write("\5Y-\2\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016e\3\2\2\2\u016e@\3\2\2\2\u016f\u0170")
        buf.write("\5\'\24\2\u0170\u0171\7r\2\2\u0171\u0172\7t\2\2\u0172")
        buf.write("\u0173\7c\2\2\u0173\u0174\7i\2\2\u0174\u0175\7o\2\2\u0175")
        buf.write("\u0176\7c\2\2\u0176\u0178\3\2\2\2\u0177\u0179\5Y-\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017bB\3\2\2\2\u017c\u017d\5\'\24")
        buf.write("\2\u017d\u017e\7I\2\2\u017e\u017f\7E\2\2\u017f\u0180\7")
        buf.write("E\2\2\u0180\u0182\3\2\2\2\u0181\u0183\5Y-\2\u0182\u0181")
        buf.write("\3\2\2\2\u0183\u0184\3\2\2\2\u0184\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185D\3\2\2\2\u0186\u0187\5\'\24\2\u0187")
        buf.write("\u0188\7R\2\2\u0188\u0189\7C\2\2\u0189\u018a\7T\2\2\u018a")
        buf.write("\u018b\7C\2\2\u018b\u018c\7E\2\2\u018c\u018e\3\2\2\2\u018d")
        buf.write("\u018f\5Y-\2\u018e\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191F\3\2\2\2\u0192")
        buf.write("\u0196\5K&\2\u0193\u0196\5M\'\2\u0194\u0196\7\60\2\2\u0195")
        buf.write("\u0192\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2")
        buf.write("\u0196H\3\2\2\2\u0197\u019a\5K&\2\u0198\u019a\5O(\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u0198\3\2\2\2\u019aJ\3\2\2\2\u019b")
        buf.write("\u019c\t\4\2\2\u019cL\3\2\2\2\u019d\u019e\t\5\2\2\u019e")
        buf.write("N\3\2\2\2\u019f\u01a0\7^\2\2\u01a0\u01a1\7w\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01aa\5Q)\2\u01a3\u01a4\7^\2\2\u01a4")
        buf.write("\u01a5\7W\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a7\5Q)\2\u01a7")
        buf.write("\u01a8\5Q)\2\u01a8\u01aa\3\2\2\2\u01a9\u019f\3\2\2\2\u01a9")
        buf.write("\u01a3\3\2\2\2\u01aaP\3\2\2\2\u01ab\u01ac\5U+\2\u01ac")
        buf.write("\u01ad\5U+\2\u01ad\u01ae\5U+\2\u01ae\u01af\5U+\2\u01af")
        buf.write("R\3\2\2\2\u01b0\u01b1\t\6\2\2\u01b1T\3\2\2\2\u01b2\u01b3")
        buf.write("\t\7\2\2\u01b3V\3\2\2\2\u01b4\u01b5\7c\2\2\u01b5\u01b6")
        buf.write("\7u\2\2\u01b6\u01b7\7o\2\2\u01b7\u01bb\3\2\2\2\u01b8\u01ba")
        buf.write("\n\b\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2")
        buf.write("\u01bd\u01bb\3\2\2\2\u01be\u01c2\7}\2\2\u01bf\u01c1\n")
        buf.write("\t\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c5\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c5\u01c6\7\177\2\2\u01c6\u01c7\3\2\2")
        buf.write("\2\u01c7\u01c8\b,\2\2\u01c8X\3\2\2\2\u01c9\u01cb\t\n\2")
        buf.write("\2\u01ca\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ca")
        buf.write("\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01cf\b-\2\2\u01cfZ\3\2\2\2\u01d0\u01d2\7\17\2\2\u01d1")
        buf.write("\u01d3\7\f\2\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2")
        buf.write("\u01d3\u01d6\3\2\2\2\u01d4\u01d6\7\f\2\2\u01d5\u01d0\3")
        buf.write("\2\2\2\u01d5\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8")
        buf.write("\b.\2\2\u01d8\\\3\2\2\2*\2`gir~\u0091\u0098\u00a3\u00a8")
        buf.write("\u00ae\u00b6\u00bb\u00bf\u00c9\u00d2\u00da\u00e9\u00f6")
        buf.write("\u0102\u010b\u0114\u0120\u012d\u013e\u014c\u0157\u0161")
        buf.write("\u016d\u017a\u0184\u0190\u0195\u0199\u01a9\u01bb\u01c2")
        buf.write("\u01cc\u01d2\u01d5\3\b\2\2")
        return buf.getvalue()


class ParaCPreProcessorLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NonPreProcessorItemBlock = 1
    IfNotDefinedDirective = 2
    IfDefinedDirective = 3
    ElIfNotDefinedDirective = 4
    ElIfDefinedDirective = 5
    IfDirective = 6
    ElIfDirective = 7
    ElseDirective = 8
    EndifDirective = 9
    PragmaDirective = 10
    UndefDirective = 11
    ComplexDefineDirective = 12
    ComputedIncludeLiteral = 13
    LibIncludeLiteral = 14
    StringIncludeLiteral = 15
    AsmBlock = 16
    Whitespace = 17
    Newline = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NonPreProcessorItemBlock", "IfNotDefinedDirective", "IfDefinedDirective", 
            "ElIfNotDefinedDirective", "ElIfDefinedDirective", "IfDirective", 
            "ElIfDirective", "ElseDirective", "EndifDirective", "PragmaDirective", 
            "UndefDirective", "ComplexDefineDirective", "ComputedIncludeLiteral", 
            "LibIncludeLiteral", "StringIncludeLiteral", "AsmBlock", "Whitespace", 
            "Newline" ]

    ruleNames = [ "NonPreProcessorItemBlock", "Identifier", "BlockComment", 
                  "LineComment", "IfNotDefinedDirective", "IfDefinedDirective", 
                  "ElIfNotDefinedDirective", "ElIfDefinedDirective", "IfDirective", 
                  "ElIfDirective", "ElseDirective", "EndifDirective", "PragmaDirective", 
                  "UndefDirective", "ComplexDefineDirective", "ComputedIncludeLiteral", 
                  "LibIncludeLiteral", "StringIncludeLiteral", "PreProcessorBegin", 
                  "Include", "Define", "Undefine", "If", "Else", "IfDefined", 
                  "IfNotDefined", "ElIfNotDefined", "ElIfDefined", "ElseIf", 
                  "EndIf", "Error", "Pragma", "GCCParacPrefix", "PragmaParacPrefix", 
                  "IncludeLiteral", "IdentifierNondigit", "Nondigit", "Digit", 
                  "UniversalCharacterName", "HexQuad", "OctalDigit", "HexadecimalDigit", 
                  "AsmBlock", "Whitespace", "Newline" ]

    grammarFileName = "ParaCPreProcessor.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


