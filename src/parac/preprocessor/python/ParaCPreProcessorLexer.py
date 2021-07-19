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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\33")
        buf.write("\u0169\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\7\2X\n\2\f\2")
        buf.write("\16\2[\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\7\23\u00d0\n\23\f\23\16")
        buf.write("\23\u00d3\13\23\3\24\3\24\5\24\u00d7\n\24\3\25\3\25\5")
        buf.write("\25\u00db\n\25\3\25\3\25\3\26\3\26\5\26\u00e1\n\26\3\26")
        buf.write("\3\26\3\27\6\27\u00e6\n\27\r\27\16\27\u00e7\3\30\6\30")
        buf.write("\u00eb\n\30\r\30\16\30\u00ec\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u00f6\n\31\3\32\3\32\3\32\3\32\5\32\u00fc")
        buf.write("\n\32\3\33\3\33\3\33\3\34\3\34\3\34\5\34\u0104\n\34\3")
        buf.write("\34\5\34\u0107\n\34\3\35\3\35\3\35\3\35\6\35\u010d\n\35")
        buf.write("\r\35\16\35\u010e\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \5 \u011f\n \3!\3!\3!\3!\3!\3\"\3\"\3#\3")
        buf.write("#\3$\3$\3$\3$\3$\7$\u012f\n$\f$\16$\u0132\13$\3$\3$\7")
        buf.write("$\u0136\n$\f$\16$\u0139\13$\3$\3$\3$\3$\3%\3%\5%\u0141")
        buf.write("\n%\3%\3%\3&\3&\3&\3&\7&\u0149\n&\f&\16&\u014c\13&\3&")
        buf.write("\3&\3&\3\'\3\'\3\'\3\'\6\'\u0155\n\'\r\'\16\'\u0156\3")
        buf.write("(\6(\u015a\n(\r(\16(\u015b\3)\3)\5)\u0160\n)\3)\5)\u0163")
        buf.write("\n)\3*\6*\u0166\n*\r*\16*\u0167\3\u014a\2+\3\2\5\3\7\4")
        buf.write("\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35")
        buf.write("\17\37\20!\21#\22%\23\'\2)\24+\25-\26/\2\61\2\63\2\65")
        buf.write("\2\67\29\2;\2=\2?\2A\2C\2E\2G\27I\30K\2M\2O\31Q\32S\33")
        buf.write("\3\2\r\6\2\f\f\17\17$$^^\f\2$$))AA^^cdhhppttvvxx\5\2C")
        buf.write("\\aac|\3\2\62;\3\2\629\5\2\62;CHch\3\2}}\3\2\177\177\4")
        buf.write("\2\f\f\17\17\4\2\13\13\"\"\6\2\f\f\17\17\"\"%%\2\u0173")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2)")
        buf.write("\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\3U\3\2\2\2\5\\\3\2\2\2")
        buf.write("\7e\3\2\2\2\tm\3\2\2\2\13t\3\2\2\2\rx\3\2\2\2\17~\3\2")
        buf.write("\2\2\21\u0085\3\2\2\2\23\u008d\3\2\2\2\25\u0097\3\2\2")
        buf.write("\2\27\u00a0\3\2\2\2\31\u00a6\3\2\2\2\33\u00ad\3\2\2\2")
        buf.write("\35\u00b4\3\2\2\2\37\u00bc\3\2\2\2!\u00c2\3\2\2\2#\u00c6")
        buf.write("\3\2\2\2%\u00cc\3\2\2\2\'\u00d6\3\2\2\2)\u00d8\3\2\2\2")
        buf.write("+\u00de\3\2\2\2-\u00e5\3\2\2\2/\u00ea\3\2\2\2\61\u00f5")
        buf.write("\3\2\2\2\63\u00fb\3\2\2\2\65\u00fd\3\2\2\2\67\u0100\3")
        buf.write("\2\2\29\u0108\3\2\2\2;\u0110\3\2\2\2=\u0112\3\2\2\2?\u011e")
        buf.write("\3\2\2\2A\u0120\3\2\2\2C\u0125\3\2\2\2E\u0127\3\2\2\2")
        buf.write("G\u0129\3\2\2\2I\u0140\3\2\2\2K\u0144\3\2\2\2M\u0150\3")
        buf.write("\2\2\2O\u0159\3\2\2\2Q\u0162\3\2\2\2S\u0165\3\2\2\2UY")
        buf.write("\7%\2\2VX\5O(\2WV\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2")
        buf.write("\2Z\4\3\2\2\2[Y\3\2\2\2\\]\5\3\2\2]^\7k\2\2^_\7p\2\2_")
        buf.write("`\7e\2\2`a\7n\2\2ab\7w\2\2bc\7f\2\2cd\7g\2\2d\6\3\2\2")
        buf.write("\2ef\5\3\2\2fg\7f\2\2gh\7g\2\2hi\7h\2\2ij\7k\2\2jk\7p")
        buf.write("\2\2kl\7g\2\2l\b\3\2\2\2mn\5\3\2\2no\7w\2\2op\7p\2\2p")
        buf.write("q\7f\2\2qr\7g\2\2rs\7h\2\2s\n\3\2\2\2tu\5\3\2\2uv\7k\2")
        buf.write("\2vw\7h\2\2w\f\3\2\2\2xy\5\3\2\2yz\7g\2\2z{\7n\2\2{|\7")
        buf.write("u\2\2|}\7g\2\2}\16\3\2\2\2~\177\5\3\2\2\177\u0080\7k\2")
        buf.write("\2\u0080\u0081\7h\2\2\u0081\u0082\7f\2\2\u0082\u0083\7")
        buf.write("g\2\2\u0083\u0084\7h\2\2\u0084\20\3\2\2\2\u0085\u0086")
        buf.write("\5\3\2\2\u0086\u0087\7k\2\2\u0087\u0088\7h\2\2\u0088\u0089")
        buf.write("\7p\2\2\u0089\u008a\7f\2\2\u008a\u008b\7g\2\2\u008b\u008c")
        buf.write("\7h\2\2\u008c\22\3\2\2\2\u008d\u008e\5\3\2\2\u008e\u008f")
        buf.write("\7g\2\2\u008f\u0090\7n\2\2\u0090\u0091\7k\2\2\u0091\u0092")
        buf.write("\7h\2\2\u0092\u0093\7p\2\2\u0093\u0094\7f\2\2\u0094\u0095")
        buf.write("\7g\2\2\u0095\u0096\7h\2\2\u0096\24\3\2\2\2\u0097\u0098")
        buf.write("\5\3\2\2\u0098\u0099\7g\2\2\u0099\u009a\7n\2\2\u009a\u009b")
        buf.write("\7k\2\2\u009b\u009c\7h\2\2\u009c\u009d\7f\2\2\u009d\u009e")
        buf.write("\7g\2\2\u009e\u009f\7h\2\2\u009f\26\3\2\2\2\u00a0\u00a1")
        buf.write("\5\3\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4")
        buf.write("\7k\2\2\u00a4\u00a5\7h\2\2\u00a5\30\3\2\2\2\u00a6\u00a7")
        buf.write("\5\3\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa")
        buf.write("\7f\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7h\2\2\u00ac\32")
        buf.write("\3\2\2\2\u00ad\u00ae\5\3\2\2\u00ae\u00af\7g\2\2\u00af")
        buf.write("\u00b0\7t\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7q\2\2\u00b2")
        buf.write("\u00b3\7t\2\2\u00b3\34\3\2\2\2\u00b4\u00b5\5\3\2\2\u00b5")
        buf.write("\u00b6\7r\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7c\2\2\u00b8")
        buf.write("\u00b9\7i\2\2\u00b9\u00ba\7o\2\2\u00ba\u00bb\7c\2\2\u00bb")
        buf.write("\36\3\2\2\2\u00bc\u00bd\5\3\2\2\u00bd\u00be\7n\2\2\u00be")
        buf.write("\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7g\2\2\u00c1")
        buf.write(" \3\2\2\2\u00c2\u00c3\7I\2\2\u00c3\u00c4\7E\2\2\u00c4")
        buf.write("\u00c5\7E\2\2\u00c5\"\3\2\2\2\u00c6\u00c7\7R\2\2\u00c7")
        buf.write("\u00c8\7C\2\2\u00c8\u00c9\7T\2\2\u00c9\u00ca\7C\2\2\u00ca")
        buf.write("\u00cb\7E\2\2\u00cb$\3\2\2\2\u00cc\u00d1\5\'\24\2\u00cd")
        buf.write("\u00d0\5\'\24\2\u00ce\u00d0\5=\37\2\u00cf\u00cd\3\2\2")
        buf.write("\2\u00cf\u00ce\3\2\2\2\u00d0\u00d3\3\2\2\2\u00d1\u00cf")
        buf.write("\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2&\3\2\2\2\u00d3\u00d1")
        buf.write("\3\2\2\2\u00d4\u00d7\5;\36\2\u00d5\u00d7\5? \2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7(\3\2\2\2\u00d8\u00da")
        buf.write("\7>\2\2\u00d9\u00db\5/\30\2\u00da\u00d9\3\2\2\2\u00da")
        buf.write("\u00db\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd\7@\2\2")
        buf.write("\u00dd*\3\2\2\2\u00de\u00e0\7$\2\2\u00df\u00e1\5/\30\2")
        buf.write("\u00e0\u00df\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3")
        buf.write("\2\2\2\u00e2\u00e3\7$\2\2\u00e3,\3\2\2\2\u00e4\u00e6\5")
        buf.write("=\37\2\u00e5\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7\u00e5")
        buf.write("\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8.\3\2\2\2\u00e9\u00eb")
        buf.write("\5\61\31\2\u00ea\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\60\3\2\2\2\u00ee")
        buf.write("\u00f6\n\2\2\2\u00ef\u00f6\5\63\32\2\u00f0\u00f1\7^\2")
        buf.write("\2\u00f1\u00f6\7\f\2\2\u00f2\u00f3\7^\2\2\u00f3\u00f4")
        buf.write("\7\17\2\2\u00f4\u00f6\7\f\2\2\u00f5\u00ee\3\2\2\2\u00f5")
        buf.write("\u00ef\3\2\2\2\u00f5\u00f0\3\2\2\2\u00f5\u00f2\3\2\2\2")
        buf.write("\u00f6\62\3\2\2\2\u00f7\u00fc\5\65\33\2\u00f8\u00fc\5")
        buf.write("\67\34\2\u00f9\u00fc\59\35\2\u00fa\u00fc\5? \2\u00fb\u00f7")
        buf.write("\3\2\2\2\u00fb\u00f8\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc\64\3\2\2\2\u00fd\u00fe\7^\2\2\u00fe")
        buf.write("\u00ff\t\3\2\2\u00ff\66\3\2\2\2\u0100\u0101\7^\2\2\u0101")
        buf.write("\u0103\5C\"\2\u0102\u0104\5C\"\2\u0103\u0102\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0107\5C\"\2")
        buf.write("\u0106\u0105\3\2\2\2\u0106\u0107\3\2\2\2\u01078\3\2\2")
        buf.write("\2\u0108\u0109\7^\2\2\u0109\u010a\7z\2\2\u010a\u010c\3")
        buf.write("\2\2\2\u010b\u010d\5E#\2\u010c\u010b\3\2\2\2\u010d\u010e")
        buf.write("\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f")
        buf.write(":\3\2\2\2\u0110\u0111\t\4\2\2\u0111<\3\2\2\2\u0112\u0113")
        buf.write("\t\5\2\2\u0113>\3\2\2\2\u0114\u0115\7^\2\2\u0115\u0116")
        buf.write("\7w\2\2\u0116\u0117\3\2\2\2\u0117\u011f\5A!\2\u0118\u0119")
        buf.write("\7^\2\2\u0119\u011a\7W\2\2\u011a\u011b\3\2\2\2\u011b\u011c")
        buf.write("\5A!\2\u011c\u011d\5A!\2\u011d\u011f\3\2\2\2\u011e\u0114")
        buf.write("\3\2\2\2\u011e\u0118\3\2\2\2\u011f@\3\2\2\2\u0120\u0121")
        buf.write("\5E#\2\u0121\u0122\5E#\2\u0122\u0123\5E#\2\u0123\u0124")
        buf.write("\5E#\2\u0124B\3\2\2\2\u0125\u0126\t\6\2\2\u0126D\3\2\2")
        buf.write("\2\u0127\u0128\t\7\2\2\u0128F\3\2\2\2\u0129\u012a\7c\2")
        buf.write("\2\u012a\u012b\7u\2\2\u012b\u012c\7o\2\2\u012c\u0130\3")
        buf.write("\2\2\2\u012d\u012f\n\b\2\2\u012e\u012d\3\2\2\2\u012f\u0132")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131")
        buf.write("\u0133\3\2\2\2\u0132\u0130\3\2\2\2\u0133\u0137\7}\2\2")
        buf.write("\u0134\u0136\n\t\2\2\u0135\u0134\3\2\2\2\u0136\u0139\3")
        buf.write("\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013a")
        buf.write("\3\2\2\2\u0139\u0137\3\2\2\2\u013a\u013b\7\177\2\2\u013b")
        buf.write("\u013c\3\2\2\2\u013c\u013d\b$\2\2\u013dH\3\2\2\2\u013e")
        buf.write("\u0141\5K&\2\u013f\u0141\5M\'\2\u0140\u013e\3\2\2\2\u0140")
        buf.write("\u013f\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\b%\2\2")
        buf.write("\u0143J\3\2\2\2\u0144\u0145\7\61\2\2\u0145\u0146\7,\2")
        buf.write("\2\u0146\u014a\3\2\2\2\u0147\u0149\13\2\2\2\u0148\u0147")
        buf.write("\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u014b\3\2\2\2\u014a")
        buf.write("\u0148\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014d\u014e\7,\2\2\u014e\u014f\7\61\2\2\u014fL\3\2\2")
        buf.write("\2\u0150\u0151\7\61\2\2\u0151\u0152\7\61\2\2\u0152\u0154")
        buf.write("\3\2\2\2\u0153\u0155\n\n\2\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157N\3\2\2\2\u0158\u015a\t\13\2\2\u0159\u0158\3\2\2")
        buf.write("\2\u015a\u015b\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015cP\3\2\2\2\u015d\u015f\7\17\2\2\u015e\u0160")
        buf.write("\7\f\2\2\u015f\u015e\3\2\2\2\u015f\u0160\3\2\2\2\u0160")
        buf.write("\u0163\3\2\2\2\u0161\u0163\7\f\2\2\u0162\u015d\3\2\2\2")
        buf.write("\u0162\u0161\3\2\2\2\u0163R\3\2\2\2\u0164\u0166\n\f\2")
        buf.write("\2\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0168\3\2\2\2\u0168T\3\2\2\2\32\2Y\u00cf")
        buf.write("\u00d1\u00d6\u00da\u00e0\u00e7\u00ec\u00f5\u00fb\u0103")
        buf.write("\u0106\u010e\u011e\u0130\u0137\u0140\u014a\u0156\u015b")
        buf.write("\u015f\u0162\u0167\3\b\2\2")
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
    Comment = 22
    Whitespace = 23
    Newline = 24
    NonPreProcessorItemSequence = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'GCC'", "'PARAC'" ]

    symbolicNames = [ "<INVALID>",
            "Include", "Define", "Undefine", "If", "Else", "IfDefined", 
            "IfNotDefined", "ElIfNotDefined", "ElIfDefined", "ElseIf", "EndIf", 
            "Error", "Pragma", "Line", "GCCParacPrefix", "PragmaParacPrefix", 
            "Identifier", "LibStringLiteral", "StringLiteral", "DigitSequence", 
            "AsmBlock", "Comment", "Whitespace", "Newline", "NonPreProcessorItemSequence" ]

    ruleNames = [ "PreProcessorBegin", "Include", "Define", "Undefine", 
                  "If", "Else", "IfDefined", "IfNotDefined", "ElIfNotDefined", 
                  "ElIfDefined", "ElseIf", "EndIf", "Error", "Pragma", "Line", 
                  "GCCParacPrefix", "PragmaParacPrefix", "Identifier", "IdentifierNondigit", 
                  "LibStringLiteral", "StringLiteral", "DigitSequence", 
                  "SCharSequence", "SChar", "EscapeSequence", "SimpleEscapeSequence", 
                  "OctalEscapeSequence", "HexadecimalEscapeSequence", "Nondigit", 
                  "Digit", "UniversalCharacterName", "HexQuad", "OctalDigit", 
                  "HexadecimalDigit", "AsmBlock", "Comment", "BlockComment", 
                  "LineComment", "Whitespace", "Newline", "NonPreProcessorItemSequence" ]

    grammarFileName = "ParaCPreProcessor.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


