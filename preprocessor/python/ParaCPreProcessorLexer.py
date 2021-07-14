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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u0266\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\6\2y\n\2\r\2\16\2z\3\3\6\3~\n\3\r\3\16\3\177")
        buf.write("\3\4\3\4\3\4\7\4\u0085\n\4\f\4\16\4\u0088\13\4\3\5\3\5")
        buf.write("\3\5\3\5\7\5\u008e\n\5\f\5\16\5\u0091\13\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\7\6\u009a\n\6\f\6\16\6\u009d\13\6\3\7")
        buf.write("\3\7\3\7\3\7\5\7\u00a3\n\7\3\b\3\b\3\b\3\b\5\b\u00a9\n")
        buf.write("\b\3\t\3\t\3\t\3\t\5\t\u00af\n\t\3\n\3\n\3\n\3\n\5\n\u00b5")
        buf.write("\n\n\3\13\3\13\7\13\u00b9\n\13\f\13\16\13\u00bc\13\13")
        buf.write("\3\13\3\13\5\13\u00c0\n\13\3\f\3\f\7\f\u00c4\n\f\f\f\16")
        buf.write("\f\u00c7\13\f\3\f\3\f\5\f\u00cb\n\f\3\r\3\r\3\r\5\r\u00d0")
        buf.write("\n\r\3\16\3\16\3\16\5\16\u00d5\n\16\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00db\n\17\3\17\6\17\u00de\n\17\r\17\16\17\u00df")
        buf.write("\3\17\3\17\6\17\u00e4\n\17\r\17\16\17\u00e5\3\17\3\17")
        buf.write("\5\17\u00ea\n\17\3\20\3\20\6\20\u00ee\n\20\r\20\16\20")
        buf.write("\u00ef\3\20\3\20\5\20\u00f4\n\20\3\21\3\21\3\21\3\21\5")
        buf.write("\21\u00fa\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u0101\n\22")
        buf.write("\3\22\3\22\5\22\u0105\n\22\3\23\5\23\u0108\n\23\3\23\7")
        buf.write("\23\u010b\n\23\f\23\16\23\u010e\13\23\3\23\5\23\u0111")
        buf.write("\n\23\3\24\3\24\3\24\3\24\5\24\u0117\n\24\3\25\3\25\3")
        buf.write("\25\3\25\5\25\u011d\n\25\3\26\3\26\3\26\3\26\5\26\u0123")
        buf.write("\n\26\3\27\3\27\6\27\u0127\n\27\r\27\16\27\u0128\3\27")
        buf.write("\3\27\5\27\u012d\n\27\3\27\3\27\5\27\u0131\n\27\3\30\3")
        buf.write("\30\7\30\u0135\n\30\f\30\16\30\u0138\13\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\6\31\u0144\n\31")
        buf.write("\r\31\16\31\u0145\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\32\6\32\u0151\n\32\r\32\16\32\u0152\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\6\33\u015d\n\33\r\33\16\33")
        buf.write("\u015e\3\34\3\34\3\34\3\34\3\34\6\34\u0166\n\34\r\34\16")
        buf.write("\34\u0167\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35\u0171")
        buf.write("\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\6\36\u017b")
        buf.write("\n\36\r\36\16\36\u017c\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\6\37\u0188\n\37\r\37\16\37\u0189\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \6 \u0197\n \r \16 \u0198\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\3!\6!\u01a5\n!\r!\16!\u01a6\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\6\"\u01b0\n\"\r\"\16\"\u01b1")
        buf.write("\3#\3#\3#\3#\3#\3#\3#\3#\5#\u01bc\n#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\6\'\u01df\n\'\r\'\16")
        buf.write("\'\u01e0\3(\3(\3(\3(\3(\3(\3(\3(\6(\u01eb\n(\r(\16(\u01ec")
        buf.write("\3)\3)\3)\5)\u01f2\n)\3*\3*\5*\u01f6\n*\3+\3+\5+\u01fa")
        buf.write("\n+\3+\3+\3,\3,\5,\u0200\n,\3,\3,\3-\6-\u0205\n-\r-\16")
        buf.write("-\u0206\3.\3.\3.\3.\3.\3.\3.\5.\u0210\n.\3/\3/\3/\3/\5")
        buf.write("/\u0216\n/\3\60\3\60\3\60\3\61\3\61\3\61\5\61\u021e\n")
        buf.write("\61\3\61\5\61\u0221\n\61\3\62\3\62\3\62\3\62\6\62\u0227")
        buf.write("\n\62\r\62\16\62\u0228\3\63\3\63\3\64\3\64\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u0239\n\65")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\67\3\67\38\38\39\39\39\39")
        buf.write("\39\79\u0249\n9\f9\169\u024c\139\39\39\79\u0250\n9\f9")
        buf.write("\169\u0253\139\39\39\39\39\3:\6:\u025a\n:\r:\16:\u025b")
        buf.write("\3:\3:\3;\3;\5;\u0262\n;\3;\5;\u0265\n;\3\u008f\2<\3\3")
        buf.write("\5\2\7\2\t\2\13\2\r\4\17\5\21\6\23\7\25\b\27\t\31\n\33")
        buf.write("\13\35\f\37\r!\16#\17%\2\'\20)\21+\22-\23/\2\61\2\63\2")
        buf.write("\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2K\2M\2O\2Q\2S\2U")
        buf.write("\24W\25Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\26s\27u\30")
        buf.write("\3\2\r\3\2%%\4\2\f\f\17\17\6\2\f\f\17\17$$^^\f\2$$))A")
        buf.write("A^^cdhhppttvvxx\5\2C\\aac|\3\2\62;\3\2\629\5\2\62;CHc")
        buf.write("h\3\2}}\3\2\177\177\4\2\13\13\"\"\2\u0287\2\3\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\3x\3\2\2\2\5}\3")
        buf.write("\2\2\2\7\u0081\3\2\2\2\t\u0089\3\2\2\2\13\u0095\3\2\2")
        buf.write("\2\r\u009e\3\2\2\2\17\u00a4\3\2\2\2\21\u00aa\3\2\2\2\23")
        buf.write("\u00b0\3\2\2\2\25\u00b6\3\2\2\2\27\u00c1\3\2\2\2\31\u00cc")
        buf.write("\3\2\2\2\33\u00d1\3\2\2\2\35\u00d6\3\2\2\2\37\u00eb\3")
        buf.write("\2\2\2!\u00f5\3\2\2\2#\u00fb\3\2\2\2%\u0107\3\2\2\2\'")
        buf.write("\u0112\3\2\2\2)\u0118\3\2\2\2+\u011e\3\2\2\2-\u0124\3")
        buf.write("\2\2\2/\u0132\3\2\2\2\61\u0139\3\2\2\2\63\u0147\3\2\2")
        buf.write("\2\65\u0154\3\2\2\2\67\u0160\3\2\2\29\u0169\3\2\2\2;\u0172")
        buf.write("\3\2\2\2=\u017e\3\2\2\2?\u018b\3\2\2\2A\u019a\3\2\2\2")
        buf.write("C\u01a8\3\2\2\2E\u01b3\3\2\2\2G\u01bd\3\2\2\2I\u01c6\3")
        buf.write("\2\2\2K\u01d0\3\2\2\2M\u01d8\3\2\2\2O\u01e2\3\2\2\2Q\u01f1")
        buf.write("\3\2\2\2S\u01f5\3\2\2\2U\u01f7\3\2\2\2W\u01fd\3\2\2\2")
        buf.write("Y\u0204\3\2\2\2[\u020f\3\2\2\2]\u0215\3\2\2\2_\u0217\3")
        buf.write("\2\2\2a\u021a\3\2\2\2c\u0222\3\2\2\2e\u022a\3\2\2\2g\u022c")
        buf.write("\3\2\2\2i\u0238\3\2\2\2k\u023a\3\2\2\2m\u023f\3\2\2\2")
        buf.write("o\u0241\3\2\2\2q\u0243\3\2\2\2s\u0259\3\2\2\2u\u0264\3")
        buf.write("\2\2\2wy\n\2\2\2xw\3\2\2\2yz\3\2\2\2zx\3\2\2\2z{\3\2\2")
        buf.write("\2{\4\3\2\2\2|~\n\3\2\2}|\3\2\2\2~\177\3\2\2\2\177}\3")
        buf.write("\2\2\2\177\u0080\3\2\2\2\u0080\6\3\2\2\2\u0081\u0086\5")
        buf.write("S*\2\u0082\u0085\5S*\2\u0083\u0085\5g\64\2\u0084\u0082")
        buf.write("\3\2\2\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\b\3\2\2\2\u0088")
        buf.write("\u0086\3\2\2\2\u0089\u008a\7\61\2\2\u008a\u008b\7,\2\2")
        buf.write("\u008b\u008f\3\2\2\2\u008c\u008e\13\2\2\2\u008d\u008c")
        buf.write("\3\2\2\2\u008e\u0091\3\2\2\2\u008f\u0090\3\2\2\2\u008f")
        buf.write("\u008d\3\2\2\2\u0090\u0092\3\2\2\2\u0091\u008f\3\2\2\2")
        buf.write("\u0092\u0093\7,\2\2\u0093\u0094\7\61\2\2\u0094\n\3\2\2")
        buf.write("\2\u0095\u0096\7\61\2\2\u0096\u0097\7\61\2\2\u0097\u009b")
        buf.write("\3\2\2\2\u0098\u009a\5\5\3\2\u0099\u0098\3\2\2\2\u009a")
        buf.write("\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c\f\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\5=\37")
        buf.write("\2\u009f\u00a2\5\7\4\2\u00a0\u00a3\5u;\2\u00a1\u00a3\7")
        buf.write("\2\2\3\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\16")
        buf.write("\3\2\2\2\u00a4\u00a5\5;\36\2\u00a5\u00a8\5\7\4\2\u00a6")
        buf.write("\u00a9\5u;\2\u00a7\u00a9\7\2\2\3\u00a8\u00a6\3\2\2\2\u00a8")
        buf.write("\u00a7\3\2\2\2\u00a9\20\3\2\2\2\u00aa\u00ab\5? \2\u00ab")
        buf.write("\u00ae\5\7\4\2\u00ac\u00af\5u;\2\u00ad\u00af\7\2\2\3\u00ae")
        buf.write("\u00ac\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\22\3\2\2\2\u00b0")
        buf.write("\u00b1\5A!\2\u00b1\u00b4\5\7\4\2\u00b2\u00b5\5u;\2\u00b3")
        buf.write("\u00b5\7\2\2\3\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2")
        buf.write("\u00b5\24\3\2\2\2\u00b6\u00ba\5\67\34\2\u00b7\u00b9\5")
        buf.write("\5\3\2\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bf\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bd\u00c0\5u;\2\u00be\u00c0\7\2\2\3\u00bf")
        buf.write("\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\26\3\2\2\2\u00c1")
        buf.write("\u00c5\5C\"\2\u00c2\u00c4\5\5\3\2\u00c3\u00c2\3\2\2\2")
        buf.write("\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3")
        buf.write("\2\2\2\u00c6\u00ca\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00cb")
        buf.write("\5u;\2\u00c9\u00cb\7\2\2\3\u00ca\u00c8\3\2\2\2\u00ca\u00c9")
        buf.write("\3\2\2\2\u00cb\30\3\2\2\2\u00cc\u00cf\59\35\2\u00cd\u00d0")
        buf.write("\5u;\2\u00ce\u00d0\7\2\2\3\u00cf\u00cd\3\2\2\2\u00cf\u00ce")
        buf.write("\3\2\2\2\u00d0\32\3\2\2\2\u00d1\u00d4\5E#\2\u00d2\u00d5")
        buf.write("\5u;\2\u00d3\u00d5\7\2\2\3\u00d4\u00d2\3\2\2\2\u00d4\u00d3")
        buf.write("\3\2\2\2\u00d5\34\3\2\2\2\u00d6\u00da\5I%\2\u00d7\u00db")
        buf.write("\5M\'\2\u00d8\u00db\5O(\2\u00d9\u00db\5\7\4\2\u00da\u00d7")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3\2\2\2\u00db")
        buf.write("\u00e3\3\2\2\2\u00dc\u00de\5s:\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e1\3\2\2\2\u00e1\u00e2\5\7\4\2\u00e2\u00e4\3")
        buf.write("\2\2\2\u00e3\u00dd\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e3")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7")
        buf.write("\u00ea\5u;\2\u00e8\u00ea\7\2\2\3\u00e9\u00e7\3\2\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea\36\3\2\2\2\u00eb\u00ed\5G$\2\u00ec")
        buf.write("\u00ee\5\5\3\2\u00ed\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f3\3")
        buf.write("\2\2\2\u00f1\u00f4\5u;\2\u00f2\u00f4\7\2\2\3\u00f3\u00f1")
        buf.write("\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4 \3\2\2\2\u00f5\u00f6")
        buf.write("\5\65\33\2\u00f6\u00f9\5\7\4\2\u00f7\u00fa\5u;\2\u00f8")
        buf.write("\u00fa\7\2\2\3\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2")
        buf.write("\u00fa\"\3\2\2\2\u00fb\u00fc\5\63\32\2\u00fc\u0100\5\7")
        buf.write("\4\2\u00fd\u00fe\5s:\2\u00fe\u00ff\5%\23\2\u00ff\u0101")
        buf.write("\3\2\2\2\u0100\u00fd\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0104\3\2\2\2\u0102\u0105\5u;\2\u0103\u0105\7\2\2\3\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105$\3\2\2\2\u0106")
        buf.write("\u0108\7*\2\2\u0107\u0106\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u010c\3\2\2\2\u0109\u010b\5\5\3\2\u010a\u0109\3")
        buf.write("\2\2\2\u010b\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d")
        buf.write("\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010f")
        buf.write("\u0111\7+\2\2\u0110\u010f\3\2\2\2\u0110\u0111\3\2\2\2")
        buf.write("\u0111&\3\2\2\2\u0112\u0113\5\61\31\2\u0113\u0116\5\7")
        buf.write("\4\2\u0114\u0117\5u;\2\u0115\u0117\7\2\2\3\u0116\u0114")
        buf.write("\3\2\2\2\u0116\u0115\3\2\2\2\u0117(\3\2\2\2\u0118\u0119")
        buf.write("\5\61\31\2\u0119\u011c\5U+\2\u011a\u011d\5u;\2\u011b\u011d")
        buf.write("\7\2\2\3\u011c\u011a\3\2\2\2\u011c\u011b\3\2\2\2\u011d")
        buf.write("*\3\2\2\2\u011e\u011f\5\61\31\2\u011f\u0122\5W,\2\u0120")
        buf.write("\u0123\5u;\2\u0121\u0123\7\2\2\3\u0122\u0120\3\2\2\2\u0122")
        buf.write("\u0121\3\2\2\2\u0123,\3\2\2\2\u0124\u0126\5K&\2\u0125")
        buf.write("\u0127\5g\64\2\u0126\u0125\3\2\2\2\u0127\u0128\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\3")
        buf.write("\2\2\2\u012a\u012c\5s:\2\u012b\u012d\5W,\2\u012c\u012b")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u0130\3\2\2\2\u012e")
        buf.write("\u0131\5u;\2\u012f\u0131\7\2\2\3\u0130\u012e\3\2\2\2\u0130")
        buf.write("\u012f\3\2\2\2\u0131.\3\2\2\2\u0132\u0136\7%\2\2\u0133")
        buf.write("\u0135\5s:\2\u0134\u0133\3\2\2\2\u0135\u0138\3\2\2\2\u0136")
        buf.write("\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\60\3\2\2\2\u0138")
        buf.write("\u0136\3\2\2\2\u0139\u013a\5/\30\2\u013a\u013b\7k\2\2")
        buf.write("\u013b\u013c\7p\2\2\u013c\u013d\7e\2\2\u013d\u013e\7n")
        buf.write("\2\2\u013e\u013f\7w\2\2\u013f\u0140\7f\2\2\u0140\u0141")
        buf.write("\7g\2\2\u0141\u0143\3\2\2\2\u0142\u0144\5s:\2\u0143\u0142")
        buf.write("\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0143\3\2\2\2\u0145")
        buf.write("\u0146\3\2\2\2\u0146\62\3\2\2\2\u0147\u0148\5/\30\2\u0148")
        buf.write("\u0149\7f\2\2\u0149\u014a\7g\2\2\u014a\u014b\7h\2\2\u014b")
        buf.write("\u014c\7k\2\2\u014c\u014d\7p\2\2\u014d\u014e\7g\2\2\u014e")
        buf.write("\u0150\3\2\2\2\u014f\u0151\5s:\2\u0150\u014f\3\2\2\2\u0151")
        buf.write("\u0152\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2")
        buf.write("\u0153\64\3\2\2\2\u0154\u0155\5/\30\2\u0155\u0156\7w\2")
        buf.write("\2\u0156\u0157\7p\2\2\u0157\u0158\7f\2\2\u0158\u0159\7")
        buf.write("g\2\2\u0159\u015a\7h\2\2\u015a\u015c\3\2\2\2\u015b\u015d")
        buf.write("\5s:\2\u015c\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015c")
        buf.write("\3\2\2\2\u015e\u015f\3\2\2\2\u015f\66\3\2\2\2\u0160\u0161")
        buf.write("\5/\30\2\u0161\u0162\7k\2\2\u0162\u0163\7h\2\2\u0163\u0165")
        buf.write("\3\2\2\2\u0164\u0166\5s:\2\u0165\u0164\3\2\2\2\u0166\u0167")
        buf.write("\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("8\3\2\2\2\u0169\u016a\5/\30\2\u016a\u016b\7g\2\2\u016b")
        buf.write("\u016c\7n\2\2\u016c\u016d\7u\2\2\u016d\u016e\7g\2\2\u016e")
        buf.write("\u0170\3\2\2\2\u016f\u0171\5s:\2\u0170\u016f\3\2\2\2\u0170")
        buf.write("\u0171\3\2\2\2\u0171:\3\2\2\2\u0172\u0173\5/\30\2\u0173")
        buf.write("\u0174\7k\2\2\u0174\u0175\7h\2\2\u0175\u0176\7f\2\2\u0176")
        buf.write("\u0177\7g\2\2\u0177\u0178\7h\2\2\u0178\u017a\3\2\2\2\u0179")
        buf.write("\u017b\5s:\2\u017a\u0179\3\2\2\2\u017b\u017c\3\2\2\2\u017c")
        buf.write("\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d<\3\2\2\2\u017e")
        buf.write("\u017f\5/\30\2\u017f\u0180\7k\2\2\u0180\u0181\7h\2\2\u0181")
        buf.write("\u0182\7p\2\2\u0182\u0183\7f\2\2\u0183\u0184\7g\2\2\u0184")
        buf.write("\u0185\7h\2\2\u0185\u0187\3\2\2\2\u0186\u0188\5s:\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a>\3\2\2\2\u018b\u018c\5/\30")
        buf.write("\2\u018c\u018d\7g\2\2\u018d\u018e\7n\2\2\u018e\u018f\7")
        buf.write("k\2\2\u018f\u0190\7h\2\2\u0190\u0191\7p\2\2\u0191\u0192")
        buf.write("\7f\2\2\u0192\u0193\7g\2\2\u0193\u0194\7h\2\2\u0194\u0196")
        buf.write("\3\2\2\2\u0195\u0197\5s:\2\u0196\u0195\3\2\2\2\u0197\u0198")
        buf.write("\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("@\3\2\2\2\u019a\u019b\5/\30\2\u019b\u019c\7g\2\2\u019c")
        buf.write("\u019d\7n\2\2\u019d\u019e\7k\2\2\u019e\u019f\7h\2\2\u019f")
        buf.write("\u01a0\7f\2\2\u01a0\u01a1\7g\2\2\u01a1\u01a2\7h\2\2\u01a2")
        buf.write("\u01a4\3\2\2\2\u01a3\u01a5\5s:\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7B\3\2\2\2\u01a8\u01a9\5/\30\2\u01a9\u01aa\7g\2\2")
        buf.write("\u01aa\u01ab\7n\2\2\u01ab\u01ac\7k\2\2\u01ac\u01ad\7h")
        buf.write("\2\2\u01ad\u01af\3\2\2\2\u01ae\u01b0\5s:\2\u01af\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2D\3\2\2\2\u01b3\u01b4\5/\30\2\u01b4")
        buf.write("\u01b5\7g\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7\7f\2\2\u01b7")
        buf.write("\u01b8\7k\2\2\u01b8\u01b9\7h\2\2\u01b9\u01bb\3\2\2\2\u01ba")
        buf.write("\u01bc\5s:\2\u01bb\u01ba\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("F\3\2\2\2\u01bd\u01be\5/\30\2\u01be\u01bf\7g\2\2\u01bf")
        buf.write("\u01c0\7t\2\2\u01c0\u01c1\7t\2\2\u01c1\u01c2\7q\2\2\u01c2")
        buf.write("\u01c3\7t\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\5s:\2\u01c5")
        buf.write("H\3\2\2\2\u01c6\u01c7\5/\30\2\u01c7\u01c8\7r\2\2\u01c8")
        buf.write("\u01c9\7t\2\2\u01c9\u01ca\7c\2\2\u01ca\u01cb\7i\2\2\u01cb")
        buf.write("\u01cc\7o\2\2\u01cc\u01cd\7c\2\2\u01cd\u01ce\3\2\2\2\u01ce")
        buf.write("\u01cf\5s:\2\u01cfJ\3\2\2\2\u01d0\u01d1\5/\30\2\u01d1")
        buf.write("\u01d2\7n\2\2\u01d2\u01d3\7k\2\2\u01d3\u01d4\7p\2\2\u01d4")
        buf.write("\u01d5\7g\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7\5s:\2\u01d7")
        buf.write("L\3\2\2\2\u01d8\u01d9\5/\30\2\u01d9\u01da\7I\2\2\u01da")
        buf.write("\u01db\7E\2\2\u01db\u01dc\7E\2\2\u01dc\u01de\3\2\2\2\u01dd")
        buf.write("\u01df\5s:\2\u01de\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1N\3\2\2\2\u01e2")
        buf.write("\u01e3\5/\30\2\u01e3\u01e4\7R\2\2\u01e4\u01e5\7C\2\2\u01e5")
        buf.write("\u01e6\7T\2\2\u01e6\u01e7\7C\2\2\u01e7\u01e8\7E\2\2\u01e8")
        buf.write("\u01ea\3\2\2\2\u01e9\u01eb\5s:\2\u01ea\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ec\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2")
        buf.write("\u01edP\3\2\2\2\u01ee\u01f2\5e\63\2\u01ef\u01f2\5g\64")
        buf.write("\2\u01f0\u01f2\7\60\2\2\u01f1\u01ee\3\2\2\2\u01f1\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2R\3\2\2\2\u01f3\u01f6")
        buf.write("\5e\63\2\u01f4\u01f6\5i\65\2\u01f5\u01f3\3\2\2\2\u01f5")
        buf.write("\u01f4\3\2\2\2\u01f6T\3\2\2\2\u01f7\u01f9\7>\2\2\u01f8")
        buf.write("\u01fa\5Y-\2\u01f9\u01f8\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01fc\7@\2\2\u01fcV\3\2\2\2\u01fd")
        buf.write("\u01ff\7$\2\2\u01fe\u0200\5Y-\2\u01ff\u01fe\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0202\7$\2\2")
        buf.write("\u0202X\3\2\2\2\u0203\u0205\5[.\2\u0204\u0203\3\2\2\2")
        buf.write("\u0205\u0206\3\2\2\2\u0206\u0204\3\2\2\2\u0206\u0207\3")
        buf.write("\2\2\2\u0207Z\3\2\2\2\u0208\u0210\n\4\2\2\u0209\u0210")
        buf.write("\5]/\2\u020a\u020b\7^\2\2\u020b\u0210\7\f\2\2\u020c\u020d")
        buf.write("\7^\2\2\u020d\u020e\7\17\2\2\u020e\u0210\7\f\2\2\u020f")
        buf.write("\u0208\3\2\2\2\u020f\u0209\3\2\2\2\u020f\u020a\3\2\2\2")
        buf.write("\u020f\u020c\3\2\2\2\u0210\\\3\2\2\2\u0211\u0216\5_\60")
        buf.write("\2\u0212\u0216\5a\61\2\u0213\u0216\5c\62\2\u0214\u0216")
        buf.write("\5i\65\2\u0215\u0211\3\2\2\2\u0215\u0212\3\2\2\2\u0215")
        buf.write("\u0213\3\2\2\2\u0215\u0214\3\2\2\2\u0216^\3\2\2\2\u0217")
        buf.write("\u0218\7^\2\2\u0218\u0219\t\5\2\2\u0219`\3\2\2\2\u021a")
        buf.write("\u021b\7^\2\2\u021b\u021d\5m\67\2\u021c\u021e\5m\67\2")
        buf.write("\u021d\u021c\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u0220\3")
        buf.write("\2\2\2\u021f\u0221\5m\67\2\u0220\u021f\3\2\2\2\u0220\u0221")
        buf.write("\3\2\2\2\u0221b\3\2\2\2\u0222\u0223\7^\2\2\u0223\u0224")
        buf.write("\7z\2\2\u0224\u0226\3\2\2\2\u0225\u0227\5o8\2\u0226\u0225")
        buf.write("\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0226\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229d\3\2\2\2\u022a\u022b\t\6\2\2\u022b")
        buf.write("f\3\2\2\2\u022c\u022d\t\7\2\2\u022dh\3\2\2\2\u022e\u022f")
        buf.write("\7^\2\2\u022f\u0230\7w\2\2\u0230\u0231\3\2\2\2\u0231\u0239")
        buf.write("\5k\66\2\u0232\u0233\7^\2\2\u0233\u0234\7W\2\2\u0234\u0235")
        buf.write("\3\2\2\2\u0235\u0236\5k\66\2\u0236\u0237\5k\66\2\u0237")
        buf.write("\u0239\3\2\2\2\u0238\u022e\3\2\2\2\u0238\u0232\3\2\2\2")
        buf.write("\u0239j\3\2\2\2\u023a\u023b\5o8\2\u023b\u023c\5o8\2\u023c")
        buf.write("\u023d\5o8\2\u023d\u023e\5o8\2\u023el\3\2\2\2\u023f\u0240")
        buf.write("\t\b\2\2\u0240n\3\2\2\2\u0241\u0242\t\t\2\2\u0242p\3\2")
        buf.write("\2\2\u0243\u0244\7c\2\2\u0244\u0245\7u\2\2\u0245\u0246")
        buf.write("\7o\2\2\u0246\u024a\3\2\2\2\u0247\u0249\n\n\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024a\u024b\3\2\2\2\u024b\u024d\3\2\2\2\u024c\u024a\3")
        buf.write("\2\2\2\u024d\u0251\7}\2\2\u024e\u0250\n\13\2\2\u024f\u024e")
        buf.write("\3\2\2\2\u0250\u0253\3\2\2\2\u0251\u024f\3\2\2\2\u0251")
        buf.write("\u0252\3\2\2\2\u0252\u0254\3\2\2\2\u0253\u0251\3\2\2\2")
        buf.write("\u0254\u0255\7\177\2\2\u0255\u0256\3\2\2\2\u0256\u0257")
        buf.write("\b9\2\2\u0257r\3\2\2\2\u0258\u025a\t\f\2\2\u0259\u0258")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u0259\3\2\2\2\u025b")
        buf.write("\u025c\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e\b:\2\2")
        buf.write("\u025et\3\2\2\2\u025f\u0261\7\17\2\2\u0260\u0262\7\f\2")
        buf.write("\2\u0261\u0260\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0265")
        buf.write("\3\2\2\2\u0263\u0265\7\f\2\2\u0264\u025f\3\2\2\2\u0264")
        buf.write("\u0263\3\2\2\2\u0265v\3\2\2\2C\2z\177\u0084\u0086\u008f")
        buf.write("\u009b\u00a2\u00a8\u00ae\u00b4\u00ba\u00bf\u00c5\u00ca")
        buf.write("\u00cf\u00d4\u00da\u00df\u00e5\u00e9\u00ef\u00f3\u00f9")
        buf.write("\u0100\u0104\u0107\u010c\u0110\u0116\u011c\u0122\u0128")
        buf.write("\u012c\u0130\u0136\u0145\u0152\u015e\u0167\u0170\u017c")
        buf.write("\u0189\u0198\u01a6\u01b1\u01bb\u01e0\u01ec\u01f1\u01f5")
        buf.write("\u01f9\u01ff\u0206\u020f\u0215\u021d\u0220\u0228\u0238")
        buf.write("\u024a\u0251\u025b\u0261\u0264\3\b\2\2")
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
    EndIfDirective = 9
    PragmaDirective = 10
    ErrorDirective = 11
    UndefDirective = 12
    ComplexDefineDirective = 13
    ComputedIncludeLiteral = 14
    LibIncludeDirective = 15
    StringIncludeDirective = 16
    LineDirective = 17
    LibStringLiteral = 18
    StringLiteral = 19
    AsmBlock = 20
    Whitespace = 21
    Newline = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NonPreProcessorItemBlock", "IfNotDefinedDirective", "IfDefinedDirective", 
            "ElIfNotDefinedDirective", "ElIfDefinedDirective", "IfDirective", 
            "ElIfDirective", "ElseDirective", "EndIfDirective", "PragmaDirective", 
            "ErrorDirective", "UndefDirective", "ComplexDefineDirective", 
            "ComputedIncludeLiteral", "LibIncludeDirective", "StringIncludeDirective", 
            "LineDirective", "LibStringLiteral", "StringLiteral", "AsmBlock", 
            "Whitespace", "Newline" ]

    ruleNames = [ "NonPreProcessorItemBlock", "LiteralBlock", "Identifier", 
                  "BlockComment", "LineComment", "IfNotDefinedDirective", 
                  "IfDefinedDirective", "ElIfNotDefinedDirective", "ElIfDefinedDirective", 
                  "IfDirective", "ElIfDirective", "ElseDirective", "EndIfDirective", 
                  "PragmaDirective", "ErrorDirective", "UndefDirective", 
                  "ComplexDefineDirective", "ComplexDefineItem", "ComputedIncludeLiteral", 
                  "LibIncludeDirective", "StringIncludeDirective", "LineDirective", 
                  "PreProcessorBegin", "Include", "Define", "Undefine", 
                  "If", "Else", "IfDefined", "IfNotDefined", "ElIfNotDefined", 
                  "ElIfDefined", "ElseIf", "EndIf", "Error", "Pragma", "Line", 
                  "GCCParacPrefix", "PragmaParacPrefix", "IncludeLiteral", 
                  "IdentifierNondigit", "LibStringLiteral", "StringLiteral", 
                  "SCharSequence", "SChar", "EscapeSequence", "SimpleEscapeSequence", 
                  "OctalEscapeSequence", "HexadecimalEscapeSequence", "Nondigit", 
                  "Digit", "UniversalCharacterName", "HexQuad", "OctalDigit", 
                  "HexadecimalDigit", "AsmBlock", "Whitespace", "Newline" ]

    grammarFileName = "ParaCPreProcessor.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


