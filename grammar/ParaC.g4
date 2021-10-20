/*
    The C Antlr 4 grammar was taken as base and reference for this file

    URL: https://github.com/core/grammars-v4/blob/master/c/C.g4

    This means here the BSD Licence will apply here for all content

    [The "BSD licence"]
    Copyright (c) 2021 Luna-Klatzer
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:
    1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
    3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
    IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
    OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
    IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
    INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
    NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
    THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/** C 2011 grammar built from the C11 Spec */
grammar ParaC;


primaryExpression
    :   Identifier
    |   Constant
    |   StringLiteral+
    |   '(' expression ')'
    |   lambdaFunction
    ;

lambdaFunction
    :   '(' WS* parameterList? WS* ')' WS* lambdaBody
    ;

lambdaBody
    :    expressionLambda
    |    statementLambda
    ;

expressionLambda
    :   '=>' WS* expression
    ;

statementLambda
    :   '=>' WS* compoundStatement
    ;

postfixExpression
    :   (
        'spawn'? WS* primaryExpression
        // type identifier = (type) { .name = value };
        |   '(' WS* typeName WS* ')' WS* '{' WS* initializerList WS* ','? WS* '}'
    ) WS* ('[' WS* expression WS* ']'
    | '(' WS* argumentExpressionList? WS* ')'
    | ('.' | '->') WS* Identifier
    | ('++' | '--')
    )*
    ;

argumentExpressionList
    :   assignmentExpression WS* (',' WS* assignmentExpression WS*)*
    ;

unaryExpression
    :   ('++' |  '--' |  'sizeof')* WS*
    (postfixExpression
    |   unaryOperator WS* castOrConvertExpression
    |   ('sizeof' | 'alignof') WS* '(' WS* typeName WS* ')'
    )
    ;

unaryOperator
    :   '&' | '*' | '+' | '-' | '~' | '!'
    ;

castOrConvertExpression
    :   '(' WS* typeName WS* ')' WS* castOrConvertExpression
    |   castOrConvertExpression WS* 'as' WS* typeName
    |   unaryExpression
    |   DigitSequence // for
    ;

multiplicativeExpression
    :   castOrConvertExpression WS* (('*'|'/'|'%') WS* castOrConvertExpression WS*)*
    ;

additiveExpression
    :   multiplicativeExpression WS* (('+'|'-') WS* multiplicativeExpression WS*)*
    ;

shiftExpression
    :   additiveExpression WS* (('<<'|'>>') WS* additiveExpression WS*)*
    ;

relationalExpression
    :   shiftExpression WS* (('<'|'>'|'<='|'>=') WS* shiftExpression WS*)*
    ;

equalityExpression
    :   relationalExpression WS* (('=='| '!=') WS* relationalExpression WS*)*
    ;

andExpression
    :   equalityExpression WS* ( '&' WS* equalityExpression WS*)*
    ;

exclusiveOrExpression
    :   andExpression WS* ('^' WS* andExpression WS*)*
    ;

inclusiveOrExpression
    :   exclusiveOrExpression WS* ('|' WS* exclusiveOrExpression WS*)*
    ;

logicalAndExpression
    :   inclusiveOrExpression WS* ('&&' WS* inclusiveOrExpression WS*)*
    ;

logicalOrExpression
    :   logicalAndExpression WS* ( '||' WS* logicalAndExpression WS*)*
    ;

conditionalExpression
    :   logicalOrExpression WS* ('?' WS* expression WS* ':' WS* conditionalExpression WS*)?
    ;

assignmentExpression
    :   conditionalExpression
    |   unaryExpression WS* assignmentOperator WS* assignmentExpression
    |   DigitSequence // for
    ;

assignmentOperator
    :   '=' | '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
    ;

expression
    :   assignmentExpression WS* (',' WS* assignmentExpression WS*)*
    ;

constantExpression
    :   conditionalExpression
    ;

declaration
    :   declarationSpecifiers WS* initDeclaratorList? endOfItem
    |   staticAssertDeclaration
    ;

declarationSpecifiers
    :   (declarationSpecifier WS*)+
    ;

declarationSpecifier
    :   storageClassSpecifier
    |   typeSpecifier
    |   typeQualifier
    |   functionSpecifier
    |   alignmentSpecifier
    ;

initDeclaratorList
    :   initDeclarator WS* (',' WS* initDeclarator WS*)*
    ;

initDeclarator
    :   declarator WS* ('=' WS* initializer WS*)?
    ;

storageClassSpecifier
    :   'typedef'
    |   'extern'
    |   'static'
    |   'thread_local'
    |   'auto'
    |   'register'
    ;

arraySpecifier
    :   '[' WS* typeQualifierList? WS* assignmentExpression? WS* ']'
    |   '[' WS* 'static' WS* typeQualifierList? WS* assignmentExpression WS* ']'
    |   '[' WS* typeQualifierList WS* 'static' assignmentExpression WS* ']'
    |   '[' WS* typeQualifierList? WS* '*' WS* ']'
    ;

typeSpecifier
    :
    (   'void'
    |   'char'
    |   'short'
    |   'int'
    |   'status'
    |   'long'
    |   'float'
    |   'double'
    |   'signed'
    |   'lambda' WS* '<' WS* parameterTypeList WS* '>'
    |   'unsigned'
    |   'bool'
    |   'complex'
    )   arraySpecifier*
    |   atomicTypeSpecifier
    |   structOrUnionSpecifier
    |   enumSpecifier
    |   typedefName
    |   'typeof' WS* '(' WS* constantExpression WS* ')'
    |   typeSpecifier WS* pointer
    ;

structOrUnionSpecifier
    :   structOrUnion WS* (Identifier WS*)? '{' WS* structDeclarationList* WS* '}'
    |   structOrUnion WS* Identifier
    ;

structOrUnion
    :   'struct'
    |   'union'
    ;

structDeclarationList
    :   (WS* structDeclaration WS*)+
    ;

structDeclaration
    :   specifierQualifierList WS* structDeclaratorList? endOfItem
    |   staticAssertDeclaration
    ;

specifierQualifierList
    :   (typeSpecifier | typeQualifier) WS* specifierQualifierList?
    ;

structDeclaratorList
    :   structDeclarator WS* (',' WS* structDeclarator)*
    ;

structDeclarator
    :   declarator
    |   declarator? WS* ':' WS* constantExpression
    ;

enumSpecifier
    :   'enum' WS* Identifier? WS* '{' WS* enumeratorList WS* ','? WS* '}'
    |   'enum' WS* Identifier
    ;

enumeratorList
    :   enumerator WS* (',' WS* enumerator WS*)*
    ;

enumerator
    :   enumerationConstant WS* ('=' WS* constantExpression WS*)?
    ;

enumerationConstant
    :   Identifier
    ;

atomicTypeSpecifier
    :   'atomic' WS* '(' WS* typeName WS* ')' WS*
    ;

typeQualifier
    :   'const'
    |   'restrict'
    |   'volatile'
    |   'atomic'
    ;

functionSpecifier
    :   'noreturn'
    |   'entry'
    ;

alignmentSpecifier
    :   'alignas' WS* '(' WS* (typeName | constantExpression) WS* ')'
    ;

declarator
    :   pointer? WS* directDeclarator
    ;

directDeclarator
    :   Identifier
    |   '(' WS* declarator WS* ')'
    |   directDeclarator WS* '(' WS* parameterTypeList WS* ')'
    |   directDeclarator WS* '(' WS* identifierList? WS* ')'
    |   Identifier WS* ':' WS* DigitSequence  // bit field
    |   '(' WS* typeSpecifier? WS* pointer WS* directDeclarator WS* ')' // function pointer like: (__cdecl *f)
    ;


nestedParenthesesBlock
    :   (   ~('(' | ')')
        |   '(' WS* nestedParenthesesBlock WS* ')'
        )*
    ;

pointer
    :  (('*'|'^') WS* typeQualifierList? WS* )+ // ^ - Blocks language extension
    ;

typeQualifierList
    :   typeQualifier+
    ;

parameterTypeList
    :   parameterList WS* (',' WS* '...' WS*)?
    ;

parameterList
    :   parameterDeclaration WS* (',' WS* parameterDeclaration WS*)*
    ;

parameterDeclaration
    :   declarationSpecifiers WS* declarator #regularParameterDeclaration
    |   declarationSpecifiers WS* abstractDeclarator? #abstractParameterDeclaration
    ;

identifierList
    :   Identifier WS* (',' WS* Identifier WS*)*
    ;

typeName
    :   specifierQualifierList WS* abstractDeclarator?
    ;

abstractDeclarator
    :   pointer
    |   pointer? WS* directAbstractDeclarator
    ;

directAbstractDeclarator
    :   '(' WS* abstractDeclarator WS* ')'
    |   '[' WS* typeQualifierList? WS* assignmentExpression? WS* ']'
    |   '[' WS* 'static' WS* typeQualifierList? WS* assignmentExpression WS* ']'
    |   '[' WS* typeQualifierList WS* 'static' WS* assignmentExpression WS* ']'
    |   '[' WS* '*' WS* ']' // https://stackoverflow.com/questions/38775392/what-does-star-modifier-mean-in-c
    |   '(' WS* parameterTypeList? WS* ')'
    |   directAbstractDeclarator WS* '[' WS* typeQualifierList? WS* assignmentExpression? WS* ']'
    |   directAbstractDeclarator WS* '[' WS* 'static' WS* typeQualifierList? WS* assignmentExpression WS* ']'
    |   directAbstractDeclarator WS* '[' WS* typeQualifierList WS* 'static' WS* assignmentExpression WS* ']'
    |   directAbstractDeclarator WS* '[' WS* '*' WS* ']' // https://stackoverflow.com/questions/38775392/what-does-star-modifier-mean-in-c
    |   directAbstractDeclarator WS* '(' WS* parameterTypeList? WS* ')'
    ;

typedefName
    :   Identifier
    ;

initializer
    :   assignmentExpression
    |   '{' WS* initializerList? WS* ','? WS* '}' // array
    ;

initializerList
    :   designation? WS* initializer WS* (',' WS* designation? WS* initializer WS*)*
    ;

designation
    :   designatorList WS* '='
    ;

designatorList
    :   designator+
    ;

designator
    :   '[' WS* constantExpression WS* ']'
    |   '.' WS* Identifier
    ;

staticAssertDeclaration
    :   'static_assert' WS* '(' WS* constantExpression WS* ',' WS* StringLiteral+ WS* ')' endOfItem
    ;

statement
    :   labeledStatement
    |   compoundStatement
    |   expressionStatement
    |   tryExceptStatement
    |   selectionStatement
    |   iterationStatement
    |   jumpStatement
    |   (
            '(' WS* (logicalOrExpression WS* (',' WS* logicalOrExpression WS*)*)? WS*
            (':' WS* (logicalOrExpression WS* (',' WS* logicalOrExpression)*)?)* WS*
            ')' endOfItem
        )
    ;

labeledStatement
    :   'case' WS* constantExpression WS* ':' WS* statement
    |   'default' WS* ':' WS* statement
    ;

compoundStatement
    :   '{' WS* blockItemList? WS*'}'
    ;

blockItemList
    :   blockItem+
    ;

blockItem
    :   WS* (statement | declaration) WS*
    ;

expressionStatement
    :   expression? endOfItem
    ;

tryExceptStatement
    :   'try' WS* compoundStatement WS* exceptBlock+ WS* (finallyBlock WS* elseBlock? WS* | elseBlock WS* finallyBlock? WS* )?
    ;

exceptBlock
    :   'except' WS* '(' WS* (Identifier |  identifierList) WS* ')' WS* ('as' WS* Identifier)? WS* compoundStatement
    ;

finallyBlock
    :   'finally' WS* compoundStatement
    ;

elseBlock
    :   'else' WS* compoundStatement
    ;

selectionStatement
    :   'if' WS* '(' WS* expression WS* ')' WS* statement WS* ('else' WS* statement)?
    |   'switch' WS* '(' WS* expression WS* ')' WS* statement
    ;

iterationStatement
    :   While WS* '(' WS* expression WS* ')' WS* statement
    |   Do WS* statement WS* While WS* '(' WS* expression WS* ')' endOfItem
    |   For WS* '(' WS* forCondition WS* ')' WS* statement
    ;

//    |   'for' '(' expression? ';' expression?  ';' forUpdate? ')' statement
//    |   For '(' declaration  expression? ';' expression? ')' statement

forCondition
	:   (forDeclaration | expression?) endOfItem forExpression? endOfItem forExpression?
	;

forDeclaration
    :   declarationSpecifiers WS* initDeclaratorList?
    ;

forExpression
    :   assignmentExpression WS* (',' WS* assignmentExpression WS* )*
    ;

jumpStatement
    :   (('continue' | 'break')
    |   'return' WS* expression?
    )
    endOfItem
    ;

// Entry Point for an entire file
compilationUnit
    :   translationUnit? EOF
    ;

translationUnit
    :   (externalItem | endOfItem | WS+)+
    ;

externalItem
    :   functionDefinition # externalFunctionDefinition
    |   declaration # externalDeclaration
    |   extensionTaskDefinition # externalExtTaskDefinition
    ;

functionDefinition
    :   functionDeclarationSpecifiers WS* declarator WS* declarationList? WS* compoundStatement  # standardFunctionDefinition
    |   functionDeclarationSpecifiers WS* declarator WS* declarationList? WS* expressionLambda endOfItem # simpleFunctionDefinition
    ;

functionDeclarationSpecifiers
    :   decoratorSpecifier* WS* declarationSpecifiers?
    ;

decoratorSpecifier
    :   '@' Identifier
    ;

// extension
extensionTaskDefinition
    :   'exttask' WS* Identifier WS* directDeclarator WS* declarationList? WS* extensionTaskParameterList
    ;

extensionTaskParameterList
    :   '{' WS* (extensionTaskParameter WS* (',' WS* extensionTaskParameter WS*)*)? '}'
    ;

extensionTaskParameter
    :   Identifier WS* ':' WS* primaryExpression
    ;

declarationList
    :   (declaration WS*)+
    ;

endOfItem
    :   Whitespace* ';' Whitespace*
    ;

// Lexer Rules (tokens / token rules)

// Built-In Types
Bool : 'bool';
Char : 'char';
Complex : 'complex'; // complex number
Double : 'double';
Entry : 'entry';
Float : 'float';
Imaginary : 'imaginary'; // imaginary number
Int : 'int';
Lambda : 'lambda';
Long : 'long';
Signed : 'signed';
Short : 'short';
Status : 'status';
Unsigned : 'unsigned';
Void : 'void';

// Declaration specifier
Const : 'const';
Volatile : 'volatile';
Atomic : 'atomic';

// General Built-In Keywords

// As keyword for built-in conversion
As : 'as';

// Storage Class Specifier
Auto : 'auto';
Register : 'register'; // DEPRECATED - SHADOWED MACRO
Static : 'static';
Extern : 'extern';

// switch
Switch : 'switch';
Case : 'case';
Default : 'default';

// switch / loop : 'break'
Break : 'break';

// loop: 'continue'
Continue : 'continue';

// do-while / while loop
Do : 'do';
While : 'while';

// selection statement - if
If : 'if';
Else : 'else';

// for - loop
For : 'for';

// Enum Variable
Enum : 'enum';

// Pointer specifier 'restrict'
Restrict : 'restrict';

// Function return
Return : 'return';

// Ext-Task declaration keyword
ExtensionTask : 'exttask';

// Ext-Task spawn keyword
Spawn : 'spawn';

// Struct keyword
Struct : 'struct';

// Sizeof - Compile-replacement expression
Sizeof : 'sizeof';

// Typeof - Compile-replacement expression
Typeof : 'typeof';

// Typedef - Custom Type definition
Typedef : 'typedef';

// Type Union
Union : 'union';

// Special keywords
Alignas : 'alignas';
Alignof : 'alignof';
Inline : 'inline';
Noreturn : 'noreturn';
StaticAssert : 'static_assert';
ThreadLocal : 'thread_local';

// Punctuators
LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';

// Byte shift Operators
LeftShift : '<<';
RightShift : '>>';

// Arithmic Operators
Plus : '+';
PlusPlus : '++';
Minus : '-';
MinusMinus : '--';
Star : '*';
Div : '/';
Mod : '%';

// Boolish Logical Operations
And : '&'; // byte and
Or : '|'; // byte or
AndAnd : '&&'; // logical and
OrOr : '||'; // logical or
Caret : '^'; // byte xor
Not : '!'; // logical not
Tilde : '~'; // byte not

// Decorator Apply Sign
DecoratorSign : '@';

// Lambda start
LambdaStartBlock : '=>';

// conditional expression
Question : '?';

// General colon
Colon : ':';

// semi-column -> statement end
Semi : ';';

// General comma
Comma : ',';

// assign
Assign : '=';

// arithmetic / byte assign
// '*=' | '/=' | '%=' | '+=' | '-=' | '<<=' | '>>=' | '&=' | '^=' | '|='
StarAssign : '*=';
DivAssign : '/=';
ModAssign : '%=';
PlusAssign : '+=';
MinusAssign : '-=';
LeftShiftAssign : '<<=';
RightShiftAssign : '>>=';
AndAssign : '&=';
XorAssign : '^=';
OrAssign : '|=';

// Value Comparison
Equal : '==';
NotEqual : '!=';
Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';

// pointer ->
Arrow : '->';

// struct property accessing
Dot : '.';

// Variadic macro
Ellipsis : '...';

Identifier
    :   IdentifierNondigit
        (   IdentifierNondigit
        |   Digit
        )*
    ;

fragment
ExtensionTaskBlock
    :   '{' [\u0000-\uFFFE]* '}'
    ;

fragment
IdentifierNondigit
    :   Nondigit
    |   UniversalCharacterName
    //|   // other c-implementation-defined characters...
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

Constant
    :   IntegerConstant
    |   FloatingConstant
    //|   EnumerationConstant
    |   CharacterConstant
    ;

fragment
IntegerConstant
    :   DecimalConstant IntegerSuffix?
    |   OctalConstant IntegerSuffix?
    |   HexadecimalConstant IntegerSuffix?
    |	BinaryConstant
    ;

fragment
BinaryConstant
	:	'0' [bB] [0-1]+
	;

fragment
DecimalConstant
    :   NonzeroDigit Digit*
    ;

fragment
OctalConstant
    :   '0' OctalDigit*
    ;

fragment
HexadecimalConstant
    :   HexadecimalPrefix HexadecimalDigit+
    ;

fragment
HexadecimalPrefix
    :   '0' [xX]
    ;

fragment
NonzeroDigit
    :   [1-9]
    ;

fragment
OctalDigit
    :   [0-7]
    ;

fragment
HexadecimalDigit
    :   [0-9a-fA-F]
    ;

fragment
IntegerSuffix
    :   UnsignedSuffix LongSuffix?
    |   UnsignedSuffix LongLongSuffix
    |   LongSuffix UnsignedSuffix?
    |   LongLongSuffix UnsignedSuffix?
    ;

fragment
UnsignedSuffix
    :   [uU]
    ;

fragment
LongSuffix
    :   [lL]
    ;

fragment
LongLongSuffix
    :   'll' | 'LL'
    ;

fragment
FloatingConstant
    :   DecimalFloatingConstant
    |   HexadecimalFloatingConstant
    ;

fragment
DecimalFloatingConstant
    :   FractionalConstant ExponentPart? FloatingSuffix?
    |   DigitSequence ExponentPart FloatingSuffix?
    ;

fragment
HexadecimalFloatingConstant
    :   HexadecimalPrefix (HexadecimalFractionalConstant | HexadecimalDigitSequence) BinaryExponentPart FloatingSuffix?
    ;

fragment
FractionalConstant
    :   DigitSequence? '.' DigitSequence
    |   DigitSequence '.'
    ;

fragment
ExponentPart
    :   [eE] Sign? DigitSequence
    ;

fragment
Sign
    :   [+-]
    ;

DigitSequence
    :   Digit+
    ;

fragment
HexadecimalFractionalConstant
    :   HexadecimalDigitSequence? '.' HexadecimalDigitSequence
    |   HexadecimalDigitSequence '.'
    ;

fragment
BinaryExponentPart
    :   [pP] Sign? DigitSequence
    ;

fragment
HexadecimalDigitSequence
    :   HexadecimalDigit+
    ;

fragment
FloatingSuffix
    :   [flFL]
    ;

fragment
CharacterConstant
    :   '\'' CCharSequence '\''
    |   'L\'' CCharSequence '\''
    |   'u\'' CCharSequence '\''
    |   'U\'' CCharSequence '\''
    ;

fragment
CCharSequence
    :   CChar+
    ;

fragment
CChar
    :   ~['\\\r\n]
    |   EscapeSequence
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

StringLiteral
    :   EncodingPrefix? '"' SCharSequence? '"'
    ;

fragment
EncodingPrefix
    :   'u8'
    |   'u'
    |   'U'
    |   'L'
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

Directive
    :   '#' ~[\r\n]*
        -> skip
    ;

WS
    :   Whitespace
    ;

Whitespace
    :   [ \t]+
    ;

Newline
    :   (  '\r' '\n'? | '\n')
        -> skip
    ;
