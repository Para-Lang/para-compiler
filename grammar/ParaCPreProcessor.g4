/*
 * Pre-Processor Grammar file
 * -> Seperates the basic Para-C code from the preprocessor statements,
 *    meaning only Pre-Processor parts are going to be registered, while any
 *    other syntax and content is ignored
 */

grammar ParaCPreProcessor;

// Entry Point for an entire file
compilationUnit
    :   translationUnit? EOF
    ;

translationUnit
    :   externalItem+
    ;

externalItem
    :   preProcessorDirective
    |   nonPreProcessorItemSequence
    |   Newline
    ;

nonPreProcessorItemSequence
    :   nonPreProcessorItem+
    ;

preProcessorDirective
    :   includeDirective
    |   selectionPreProcessorDirective
    |   complexDefineDirective
    |   errorDirective
    |   pragmaDirective
    |   lineDirective
    |   undefDirective
    ;

// selection pre processor directives
// #if smth
// /* code */
// #elif smth
// /* code */
// #else
// /* code */
selectionPreProcessorDirective
    :   startOfSelectionBlock selectionDirectiveAlternatives* selectionElseDirective? endIfDirective
    ;

startOfSelectionBlock
    :   (ifDirective | ifDefinedDirective | ifNotDefinedDirective) selectionBlock
    ;

selectionDirectiveAlternatives
    :   (elIfDirective | elIfDefinedDirective | elIfNotDefinedDirective) selectionBlock
    ;

selectionElseDirective
    :   elseDirective selectionBlock
    ;

selectionBlock
    :   (nonPreProcessorItemSequence | Newline)* selectionPreProcessorDirective*
    ;

includeDirective
    :   fileIncludeDirective
    |   computedIncludeDirective
    ;

// #include "header.h" / #include <header.h>
fileIncludeDirective
    :   (libIncludeDirective | stringIncludeDirective)
    ;

// #include MACRO_H
computedIncludeDirective
    :   Include Whitespace+ Identifier preProcessorEnd
    ;

// Selection Directives

ifNotDefinedDirective
    :   IfNotDefined Whitespace+ Identifier preProcessorEnd
    ;

ifDefinedDirective
    :   IfDefined Whitespace+ Identifier preProcessorEnd
    ;

elIfNotDefinedDirective
    :   ElIfNotDefined Whitespace+ Identifier preProcessorEnd
    ;

elIfDefinedDirective
    :   ElIfDefined Whitespace+ Identifier preProcessorEnd
    ;

ifDirective
    :   If anySequence preProcessorEnd
    ;

elIfDirective
    :   ElseIf anySequence preProcessorEnd
    ;

elseDirective
    :   Else preProcessorEnd
    ;

endIfDirective
    :   EndIf preProcessorEnd
    ;

// End of Selection Directives

pragmaDirective
    :   Pragma (Whitespace+ (GCCParacPrefix | PragmaParacPrefix | Identifier))+ preProcessorEnd
    ;

errorDirective
    :   Error anySequence preProcessorEnd
    ;

undefDirective
    :   Undefine Whitespace+ Identifier preProcessorEnd
    ;

// Since a define accepts almost ANY character the rules here need to be
// special to avoid causing the lexer to possibly miss newlines/includes or
// include comments into the directive
complexDefineDirective
    :   Define Whitespace+ Identifier (Whitespace+ anySequence)? preProcessorEnd
    ;

libIncludeDirective
    :   Include Whitespace+ LibStringLiteral preProcessorEnd
    ;

stringIncludeDirective
    :   Include Whitespace+ StringLiteral preProcessorEnd
    ;

lineDirective
    :   Line Whitespace+ DigitSequence Whitespace+ StringLiteral? preProcessorEnd
    ;

// Other

nonPreProcessorItem
    :   anySequence
    ;

anySequence
    :   (Identifier | DigitSequence | StringLiteral | NonPreProcessorItemSequence | Whitespace)+
    ;

preProcessorEnd
    :   Whitespace* (Newline | EOF)
    ;

// Lexer Rules (tokens / token rules)

fragment
PreProcessorBegin : '#' Whitespace*;
Include : PreProcessorBegin 'include';
Define : PreProcessorBegin 'define';
Undefine : PreProcessorBegin 'undef';
If : PreProcessorBegin 'if';
Else : PreProcessorBegin 'else';
IfDefined : PreProcessorBegin 'ifdef';
IfNotDefined : PreProcessorBegin 'ifndef';
ElIfNotDefined : PreProcessorBegin 'elifndef';
ElIfDefined : PreProcessorBegin 'elifdef';
ElseIf : PreProcessorBegin 'elif';
EndIf : PreProcessorBegin 'endif';
Error : PreProcessorBegin 'error';
Pragma : PreProcessorBegin 'pragma';
Line : PreProcessorBegin 'line';
GCCParacPrefix : 'GCC';
PragmaParacPrefix : 'PARAC';

Identifier
    :   IdentifierNondigit
        (   IdentifierNondigit
        |   Digit
        )*
    ;

fragment
IdentifierNondigit
    :   Nondigit
    |   UniversalCharacterName
    //|   // other implementation-defined characters...
    ;

LibStringLiteral
    :   '<' SCharSequence? '>'
    ;

StringLiteral
    :   '"' SCharSequence? '"'
    ;

DigitSequence
    :   Digit+
    ;

fragment
SCharSequence
    :   SChar+
    ;

fragment
SChar
    :   ~["\\\r\n]
    |   EscapeSequence
    |   '\\\n'   // Added line
    |   '\\\r\n' // Added line
    ;

fragment
EscapeSequence
    :   SimpleEscapeSequence
    |   OctalEscapeSequence
    |   HexadecimalEscapeSequence
    |   UniversalCharacterName
    ;

fragment
SimpleEscapeSequence
    :   '\\' ['"?abfnrtv\\]
    ;

fragment
OctalEscapeSequence
    :   '\\' OctalDigit OctalDigit? OctalDigit?
    ;

fragment
HexadecimalEscapeSequence
    :   '\\x' HexadecimalDigit+
    ;

fragment
Nondigit
    :   [a-zA-Z_]
    ;

fragment
Digit
    :   [0-9]
    ;

fragment
UniversalCharacterName
    :   '\\u' HexQuad
    |   '\\U' HexQuad HexQuad
    ;

fragment
HexQuad
    :   HexadecimalDigit HexadecimalDigit HexadecimalDigit HexadecimalDigit
    ;

fragment
OctalDigit
    :   [0-7]
    ;

fragment
HexadecimalDigit
    :   [0-9a-fA-F]
    ;

// ignore the following asm blocks:
/*
    asm
    {
        mfspr x, 286;
    }
 */
AsmBlock
    :   'asm' ~'{'* '{' ~'}'* '}'
	-> skip
    ;

Whitespace
    :   [ \t]+
    ;

Newline
    :   ('\r' '\n'? | '\n')
    ;

NonPreProcessorItemSequence
    :   ~[# \r\n]+
    ;
