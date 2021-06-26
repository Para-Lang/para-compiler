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
    |   logicalPreProcessorDirective
    |   ComplexDefineDirective
    |   PragmaDirective
    |   UndefDirective
    ;

// logical pre processor directives
// #if smth
// /* code */
// #elif smth
// /* code */
// #else
// /* code */
logicalPreProcessorDirective
    :   startSelectionBlock logicalDirectiveAlternatives* logicalElseDirective? EndifDirective
    ;

startSelectionBlock
    :   (IfDirective | IfDefinedDirective | IfNotDefinedDirective) logicalPreProcessorDirective?
    ;

logicalDirectiveAlternatives
    :   (ElIfDirective | ElIfDefinedDirective | ElIfNotDefinedDirective) logicalPreProcessorDirective?
    ;

logicalElseDirective
    :   ElseDirective logicalPreProcessorDirective
    ;

includeDirective
    :   fileIncludeDirective
    |   computedIncludeDirective
    ;

// #include "header.h" / #include <header.h>
fileIncludeDirective
    :   (LibIncludeLiteral | StringIncludeLiteral)
    ;

// #include MACRO_H
computedIncludeDirective
    :   ComputedIncludeLiteral
    ;

// Lexer Rules (tokens / token rules)

NonPreProcessorItemBlock
    :   ~[#\r\n]+
        -> skip
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
    :   '//' ~[\r\n]*
    ;

// Due to token recognition the lexer rules already contain the keywords
// to avoid the lexer recongnising certain other tokens inside the
// preprocessor

IfNotDefinedDirective
    :   IfNotDefined Identifier
    ;

IfDefinedDirective
    :   IfDefined Identifier
    ;

ElIfNotDefinedDirective
    :   ElIfNotDefined Identifier
    ;

ElIfDefinedDirective
    :   ElIfDefined Identifier
    ;

IfDirective
    :   If ~[\r\n]*
    ;

ElIfDirective
    :   ElseIf ~[\r\n]*
    ;

ElseDirective
    :   Else
    ;

EndifDirective
    :   EndIf
    ;

PragmaDirective
    :   Pragma (GCCParacPrefix | PragmaParacPrefix | Identifier)
        (Whitespace+ Identifier)+
    ;

UndefDirective
    :   Undefine Identifier
    ;

// Since a define accepts almost ANY character the rules here need to be
// special to avoid causing the lexer to possibly miss newlines/includes or
// include comments into the directive
ComplexDefineDirective
    :   Define Identifier '('? ~[\r\n]* ')'?
    ;

ComputedIncludeLiteral
    :   Include Identifier
    ;

LibIncludeLiteral
    :   Include '<' IncludeLiteral+ '>'
    ;

StringIncludeLiteral
    :   Include '"' IncludeLiteral+ '"'
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
ElIfNotDefined : PreProcessorBegin 'elifnotdef' Whitespace+;

fragment
ElIfDefined : PreProcessorBegin 'elifdef' Whitespace+;

fragment
ElseIf : PreProcessorBegin 'elif' Whitespace+;

fragment
EndIf : PreProcessorBegin 'endif' Whitespace?;

fragment
Error : PreProcessorBegin 'error' Whitespace+;

fragment
Pragma : PreProcessorBegin 'pragma' Whitespace+;

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
        -> skip
    ;
