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
    |   coreLanguageItem
    ;

coreLanguageItem
    :   NonPreProcessorItemBlock
    ;

preProcessorDirective
    :   includeDirective
    |   computedIncludeDirective
    |   selectionPreProcessorDirective
    |   complexDefineDirective
    |   errorDirective
    |   pragmaDirective
    |   lineDirective
    |   undefDirective
    ;

complexDefineDirective
    :   ComplexDefineDirective
    ;

pragmaDirective
    :   PragmaDirective
    ;

errorDirective
    :   ErrorDirective
    ;

undefDirective
    :   UndefDirective
    ;

// selection pre processor directives
// #if smth
// /* code */
// #elif smth
// /* code */
// #else
// /* code */
selectionPreProcessorDirective
    :   startOfSelectionBlock selectionDirectiveAlternatives* selectionElseDirective? EndIfDirective
    ;

startOfSelectionBlock
    :   (IfDirective | IfDefinedDirective | IfNotDefinedDirective) selectionBlock
    ;

selectionDirectiveAlternatives
    :   (ElIfDirective | ElIfDefinedDirective | ElIfNotDefinedDirective) selectionBlock
    ;

selectionElseDirective
    :   ElseDirective selectionBlock
    ;

selectionBlock
    :   (coreLanguageItem | selectionPreProcessorDirective)*
    ;

includeDirective
    :   fileIncludeDirective
    |   computedIncludeDirective
    ;

lineDirective
    :   LineDirective
    ;

// #include "header.h" / #include <header.h>
fileIncludeDirective
    :   (LibIncludeDirective | StringIncludeDirective)
    ;

// #include MACRO_H
computedIncludeDirective
    :   ComputedIncludeLiteral
    ;

// Lexer Rules (tokens / token rules)

NonPreProcessorItemBlock
    :   ~[#]+
    ;

fragment
LiteralBlock
    :   ~[\r\n]+
    ;

fragment
Identifier
    :   IdentifierNondigit
        (   IdentifierNondigit
        |   Digit
        )*
    ;

fragment
BlockComment
    :   '/*' .*? '*/'
    ;

fragment
LineComment
    :   '//' LiteralBlock*
    ;

// Due to token recognition the lexer rules already contain the keywords
// to avoid the lexer recongnising certain other tokens inside the
// preprocessor

IfNotDefinedDirective
    :   IfNotDefined Identifier (Newline | EOF)
    ;

IfDefinedDirective
    :   IfDefined Identifier (Newline | EOF)
    ;

ElIfNotDefinedDirective
    :   ElIfNotDefined Identifier (Newline | EOF)
    ;

ElIfDefinedDirective
    :   ElIfDefined Identifier (Newline | EOF)
    ;

IfDirective
    :   If LiteralBlock* (Newline | EOF)
    ;

ElIfDirective
    :   ElseIf LiteralBlock* (Newline | EOF)
    ;

ElseDirective
    :   Else (Newline | EOF)
    ;

EndIfDirective
    :   EndIf (Newline | EOF)
    ;

PragmaDirective
    :   Pragma (GCCParacPrefix | PragmaParacPrefix | Identifier)
        (Whitespace+ Identifier)+ (Newline | EOF)
    ;

ErrorDirective
    :   Error LiteralBlock+ (Newline | EOF)
    ;

UndefDirective
    :   Undefine Identifier (Newline | EOF)
    ;

// Since a define accepts almost ANY character the rules here need to be
// special to avoid causing the lexer to possibly miss newlines/includes or
// include comments into the directive
ComplexDefineDirective
    :   Define Identifier (Whitespace ComplexDefineItem)? (Newline | EOF)
    ;

fragment
ComplexDefineItem
    :   '('? LiteralBlock* ')'?
    ;

ComputedIncludeLiteral
    :   Include Identifier (Newline | EOF)
    ;

LibIncludeDirective
    :   Include LibStringLiteral (Newline | EOF)
    ;

StringIncludeDirective
    :   Include StringLiteral (Newline | EOF)
    ;

LineDirective
    :   Line Digit+ Whitespace (StringLiteral)? (Newline | EOF)
    ;

// Pre-Processor definitions
fragment
PreProcessorBegin : '#' Whitespace*;

fragment
Include : PreProcessorBegin 'include' Whitespace+;

fragment
Define : PreProcessorBegin 'define' Whitespace+;

fragment
Undefine : PreProcessorBegin 'undef' Whitespace+;

fragment
If : PreProcessorBegin 'if' Whitespace+;

fragment
Else : PreProcessorBegin 'else' Whitespace?;

fragment
IfDefined : PreProcessorBegin 'ifdef' Whitespace+;

fragment
IfNotDefined : PreProcessorBegin 'ifndef' Whitespace+;

fragment
ElIfNotDefined : PreProcessorBegin 'elifndef' Whitespace+;

fragment
ElIfDefined : PreProcessorBegin 'elifdef' Whitespace+;

fragment
ElseIf : PreProcessorBegin 'elif' Whitespace+;

fragment
EndIf : PreProcessorBegin 'endif' Whitespace?;

fragment
Error : PreProcessorBegin 'error' Whitespace;

fragment
Pragma : PreProcessorBegin 'pragma' Whitespace;

fragment
Line : PreProcessorBegin 'line' Whitespace;

fragment
GCCParacPrefix : PreProcessorBegin 'GCC' Whitespace+;

fragment
PragmaParacPrefix : PreProcessorBegin 'PARAC' Whitespace+;

fragment
IncludeLiteral
    :   Nondigit
    |   Digit
    |   '.'
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
        -> skip
    ;

Newline
    :   (  '\r' '\n'? | '\n')
    ;
