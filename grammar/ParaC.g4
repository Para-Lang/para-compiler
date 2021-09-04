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
    |   'spawn' WS* Identifier
    |   Constant
    |   StringLiteral+
    |   '(' expression ')'
    |   genericSelection
    |   lambdaFunction
    |   '__extension__'? WS* '(' WS* compoundStatement WS* ')' // Blocks (GCC extension)
    |   '__builtin_va_arg' WS* '(' WS* unaryExpression WS* ',' WS* typeName WS* ')'
    |   '__builtin_offsetof' WS* '(' WS* typeName WS* ',' WS* unaryExpression WS* ')'
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

genericSelection
    :   '_Generic' WS* '(' WS* assignmentExpression WS* ',' WS* genericAssocList WS* ')'
    ;

genericAssocList
    :   genericAssociation WS* (',' WS* genericAssociation WS*)*
    ;

genericAssociation
    :   (typeName | 'default') WS* ':' WS* assignmentExpression
    ;

postfixExpression
    :
    (   primaryExpression
    |   '__extension__'? WS* '(' WS* typeName WS* ')' WS* '{' WS* initializerList WS* ','? WS* '}'
    )
    WS*
    ('[' WS* expression WS* ']'
    | '(' WS* argumentExpressionList? WS* ')'
    | ('.' | '->') WS* Identifier
    | ('++' | '--')
    )*
    ;

argumentExpressionList
    :   assignmentExpression WS* (',' WS* assignmentExpression WS*)*
    ;

unaryExpression
    :
    ('++' |  '--' |  'sizeof')* WS*
    (postfixExpression
    |   unaryOperator WS* castOrConvertExpression
    |   ('sizeof' | '_Alignof') WS* '(' WS* typeName WS* ')'
    |   '&&' WS* Identifier // GCC extension address of label
    )
    ;

unaryOperator
    :   '&' | '*' | '+' | '-' | '~' | '!'
    ;

castOrConvertExpression
    :   '__extension__'? WS* '(' WS* typeName WS* ')' WS* castOrConvertExpression
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
    |   entryPointSpecifier
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

entryPointSpecifier
    :   'entry' // Hinting the entry function for the program
    ;

storageClassSpecifier
    :   'typedef'
    |   'extern'
    |   'static'
    |   '_Thread_local'
    |   'auto'
    |   'register'
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
    |   '_Bool'
    |   '_Complex'
    |   '__m128'
    |   '__m128d'
    |   '__m128i'
    )
    |   '__extension__' WS* '(' WS* ('__m128' | '__m128d' | '__m128i') WS* ')'
    |   atomicTypeSpecifier
    |   structOrUnionSpecifier
    |   enumSpecifier
    |   typedefName
    |   ('__typeof__' | 'typeof') WS* '(' WS* constantExpression WS* ')' // GCC extension
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
    :   '_Atomic' WS* '(' WS* typeName WS* ')' WS*
    ;

typeQualifier
    :   'const'
    |   'restrict'
    |   'volatile'
    |   '_Atomic'
    ;

functionSpecifier
    :   ('inline'
    |   '_Noreturn'
    |   '__inline__' // GCC extension
    |   '__stdcall')
    |   gccAttributeSpecifier
    |   '__declspec' WS* '(' WS* Identifier WS* ')'
    |   entryPointSpecifier
    ;

alignmentSpecifier
    :   '_Alignas' WS* '(' WS* (typeName | constantExpression) WS* ')'
    ;

declarator
    :   pointer? WS* directDeclarator WS* gccDeclaratorExtension*
    ;

directDeclarator
    :   Identifier
    |   '(' WS* declarator WS* ')'
    |   directDeclarator WS* '[' WS* typeQualifierList? WS* assignmentExpression? WS* ']'
    |   directDeclarator WS* '[' WS* 'static' WS* typeQualifierList? WS* assignmentExpression WS* ']'
    |   directDeclarator WS* '[' WS* typeQualifierList WS* 'static' assignmentExpression WS* ']'
    |   directDeclarator WS* '[' WS* typeQualifierList? WS* '*' WS* ']'
    |   directDeclarator WS* '(' WS* parameterTypeList WS* ')'
    |   directDeclarator WS* '(' WS* identifierList? WS* ')'
    |   Identifier WS* ':' WS* DigitSequence  // bit field
    |   '(' WS* typeSpecifier? WS* pointer WS* directDeclarator WS* ')' // function pointer like: (__cdecl *f)
    ;

gccDeclaratorExtension
    :   '__asm' WS* '(' WS* StringLiteral+ WS* ')'
    |   gccAttributeSpecifier
    ;

gccAttributeSpecifier
    :   '__attribute__' WS* '(' WS* '(' WS* gccAttributeList WS* ')' WS* ')'
    ;

gccAttributeList
    :   gccAttribute? WS* (',' WS* gccAttribute? WS*)*
    ;

gccAttribute
    :   ~(',' | '(' | ')') // relaxed def for "identifier or reserved word"
        ('(' WS* argumentExpressionList? WS* ')' WS*)?
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
    |   pointer? WS* directAbstractDeclarator WS* gccDeclaratorExtension*
    ;

directAbstractDeclarator
    :   '(' WS* abstractDeclarator WS* ')' WS* gccDeclaratorExtension*
    |   '[' WS* typeQualifierList? WS* assignmentExpression? WS* ']'
    |   '[' WS* 'static' WS* typeQualifierList? WS* assignmentExpression WS* ']'
    |   '[' WS* typeQualifierList WS* 'static' WS* assignmentExpression WS* ']'
    |   '[' WS* '*' WS* ']'
    |   '(' WS* parameterTypeList? WS* ')' WS* gccDeclaratorExtension*
    |   directAbstractDeclarator WS* '[' WS* typeQualifierList? WS* assignmentExpression? WS* ']'
    |   directAbstractDeclarator WS* '[' WS* 'static' WS* typeQualifierList? WS* assignmentExpression WS* ']'
    |   directAbstractDeclarator WS* '[' WS* typeQualifierList WS* 'static' WS* assignmentExpression WS* ']'
    |   directAbstractDeclarator WS* '[' WS* '*' WS* ']'
    |   directAbstractDeclarator WS* '(' WS* parameterTypeList? WS* ')' WS* gccDeclaratorExtension*
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
    :   '_Static_assert' WS* '(' WS* constantExpression WS* ',' WS* StringLiteral+ WS* ')' endOfItem
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
            ('__asm' | '__asm__') WS*  ('volatile' | '__volatile__') WS*
            '(' WS* (logicalOrExpression WS* (',' WS* logicalOrExpression WS*)*)? WS*
            (':' WS* (logicalOrExpression WS* (',' WS* logicalOrExpression)*)?)* WS*
            ')' endOfItem
        )
    ;

labeledStatement
    :   Identifier WS* ':' WS* statement
    |   'case' WS* constantExpression WS* ':' WS* statement
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
    :   ('goto' WS* Identifier
    |   ('continue' | 'break')
    |   'return' WS* expression?
    |   'goto' WS* unaryExpression // GCC extension
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

As : 'as';
Auto : 'auto';
Break : 'break';
Case : 'case';
Char : 'char';
Const : 'const';
Continue : 'continue';
Default : 'default';
Do : 'do';
Double : 'double';
Else : 'else';
ExtensionTask : 'exttask';
Entry : 'entry';
Enum : 'enum';
Extern : 'extern';
Float : 'float';
For : 'for';
Goto : 'goto';
If : 'if';
Inline : 'inline';
Int : 'int';
Lambda : 'lambda';
Long : 'long';
Register : 'register';
Restrict : 'restrict';
Return : 'return';
Short : 'short';
Signed : 'signed';
Sizeof : 'sizeof';
Spawn : 'spawn';
Static : 'static';
Status : 'status';
Struct : 'struct';
Switch : 'switch';
Typeof : 'typeof';
Typedef : 'typedef';
Union : 'union';
Unsigned : 'unsigned';
Void : 'void';
Volatile : 'volatile';
While : 'while';

Alignas : '_Alignas';
Alignof : '_Alignof';
Atomic : '_Atomic';
Bool : '_Bool';
Complex : '_Complex';
Generic : '_Generic';
Imaginary : '_Imaginary';
Noreturn : '_Noreturn';
StaticAssert : '_Static_assert';
ThreadLocal : '_Thread_local';

LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';

Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';
LeftShift : '<<';
RightShift : '>>';

Plus : '+';
PlusPlus : '++';
Minus : '-';
MinusMinus : '--';
Star : '*';
Div : '/';
Mod : '%';

And : '&';
Or : '|';
AndAnd : '&&';
OrOr : '||';
Caret : '^';
Not : '!';
Tilde : '~';

DecoratorSign : '@';
LambdaStartBlock : '=>';
Question : '?';
Colon : ':';
Semi : ';';
Comma : ',';

Assign : '=';
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

Equal : '==';
NotEqual : '!=';

Arrow : '->';
Dot : '.';
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
