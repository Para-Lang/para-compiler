/*
 * The Antlr4 Grammar file for the Kipper Programming Language
 */

grammar Para;

// Entry Point for an entire file
compilationUnit
    :   translationUnit? EOF
    ;

translationUnit
    :   (externalItem | endOfItem)+
    ;

externalItem
    :   dynamicImport #externalDynamicImport
    |   functionDeclaration # externalFunctionDeclaration
    |   classDeclaration # externalClassDeclaration
    |   structDeclaration #externalStructDeclaration
    |   blockItem # externalBlockItem
    ;

dynamicImport
    :   'import' ('{' identifier* '}' | '*') 'from' string
    ;

lambdaFunction
    :   '(' parameterList? ')' lambdaBody
    ;

lambdaBody
    :    '=>' (expressionLambda | statementLambda)
    ;

expressionLambda
    :   expression
    ;

statementLambda
    :   compoundStatement
    ;

functionDeclaration
    :   functionAttributes? functionTypeSpecifier declarator '(' parameterTypeList? ')' (compoundStatement | endOfItem)
    ;

functionAttributes
    :   'entry'
    ;

functionTypeSpecifier
    :   typeSpecifier
    |   'noret'
    ;

structDeclaration
    :   'struct' declarator ('{' structItems '}' | endOfItem)
    ;

structItems
    :   declaration*
    ;

classDeclaration
    :   'class' declarator ('{' classItems '}' | endOfItem)
    ;

classItems
    :   (declaration | functionDeclaration | initClassFunction)*
    ;

/* Initialisation Function/Constructor of a class */
initClassFunction
    :   'init' '(' parameterTypeList? ')' (compoundStatement | endOfItem)
    ;

endOfItem
    :   ';'
    ;

primaryExpression
    :   '(' expression ')' # groupedPrimaryExpression
    |   identifier # identifierPrimaryExpression
    |   identifier ('.' identifier)+ #memberAccessPrimaryExpression
    |   (string)+ # stringPrimaryExpression
    |   (FStringLiteral)+ # fStringPrimaryExpression
    |   (IntegerConstant | FloatingConstant) #numberPrimaryExpression
    |   CharacterConstant #characterPrimaryExpression
    |   listConstant #listPrimaryExpression
    ;

identifier
    :   Identifier
    ;

string
    :   StringLiteral
    ;

listConstant
    :   '[' constantExpression (',' constantExpression)* ']'
    ;

postfixExpression
    :   primaryExpression #passOnPostfixExpression
    |   primaryExpression arraySpecifier+ #computedMemberAccessPostfixExpression
    |   primaryExpression incrementOrDecrementOperator # incrementOrDecrementPostfixExpression
    |   'new' primaryExpression '(' argumentExpressionList? ')' #objectInitialisationPostfixExpression
    |   primaryExpression '(' argumentExpressionList? ')' #structInitialisationPostfixExpression
    |   primaryExpression '(' argumentExpressionList? ')' # functionCallPostfixExpression
    ;

arraySpecifier
    :   '[' expression ']'
    ;

argumentExpressionList
    :   assignmentExpression (',' assignmentExpression)*
    ;

unaryExpression
    :   postfixExpression # passOnUnaryExpression
    |   'typeof' #typeofUnaryExpression
    |   'delete' postfixExpression #deleteUnaryExpression
    |   incrementOrDecrementOperator postfixExpression # incrementOrDecrementUnaryExpression
    |   unaryOperator postfixExpression # operatorModifiedUnaryExpression
    ;

incrementOrDecrementOperator
    :   ('++' |  '--')
    ;

unaryOperator
    :   '+' | '-' | '!'
    ;

castOrConvertExpression
    :   unaryExpression # passOnCastOrConvertExpression
    |   unaryExpression 'as' typeSpecifier # actualCastOrConvertExpression // conversion function
    ;

multiplicativeExpression
    :   castOrConvertExpression # passOnMultiplicativeExpression
    |   castOrConvertExpression (('*'|'/'|'%'|'**') castOrConvertExpression)* # actualMultiplicativeExpression
    ;

additiveExpression
    :   multiplicativeExpression # passOnAdditiveExpression
    |   multiplicativeExpression (('+'|'-') multiplicativeExpression)* # actualAdditiveExpression
    ;

relationalExpression
    :   additiveExpression # passOnRelationalExpression
    |   additiveExpression (('<'|'>'|'<='|'>=') additiveExpression)* # actualRelationalExpression
    ;

equalityExpression
    :   relationalExpression # passOnEqualityExpression
    |   relationalExpression (('=='| '!=') relationalExpression)* # actualEqualityExpression
    ;

logicalAndExpression
    :   equalityExpression # passOnLogicalAndExpression
    |   equalityExpression ('&&' equalityExpression)* # actualLogicalAndExpression
    ;

logicalOrExpression
    :   logicalAndExpression # passOnLogicalOrExpression
    |   logicalAndExpression ( '||' logicalAndExpression)* # actualLogicalOrExpression
    ;

conditionalExpression
    :   logicalOrExpression # passOnConditionalExpression
    |   logicalOrExpression '?' expression ':' conditionalExpression # actualConditionalExpression
    ;

assignmentExpression
    :   conditionalExpression # passOnAssignmentExpression
    |   unaryExpression assignmentOperator assignmentExpression # actualAssignmentExpression
    ;

assignmentOperator
    :   '=' | '*=' | '/=' | '%=' | '+=' | '-='
    ;

expression
    :   assignmentExpression (',' assignmentExpression)*
    ;

constantExpression
    :   conditionalExpression
    ;

declaration
    :   storageTypeSpecifier? initDeclarator endOfItem
    ;

storageTypeSpecifier
    :   'const'
    ;

initDeclarator
    :   typeSpecifier declarator ('=' initializer)?
    ;

typeSpecifier
    :   Identifier # singleItemTypeSpecifier // for single items, like 'num'
    |   Identifier explicitTypeHint # multiItemTypeSpecifier // for lists
    |   'typeof' '(' Identifier ')' # typeofTypeSpecifier // typeof another variable
    ;

explicitTypeHint
    :   '<' (Identifier)* '>'
    ;

declarator
    :   directDeclarator
    ;

directDeclarator
    :   Identifier
    ;

nestedParenthesesBlock
    :   (   ~('(' | ')')
        |   '(' nestedParenthesesBlock ')'
        )*
    ;

parameterTypeList
    :   parameterList (',' '...')?
    ;

parameterList
    :   parameterDeclaration (',' parameterDeclaration)*
    ;

parameterDeclaration
    :   typeSpecifier declarator
    ;

initializer
    :   assignmentExpression
    ;

statement
    :   compoundStatement
    |   expressionStatement
    |   selectionStatement
    |   iterationStatement
    |   jumpStatement
    ;

compoundStatement
    :   '{' blockItemList?'}'
    ;

blockItemList
    :   blockItem+
    ;

blockItem
    :   (statement | declaration)
    ;

expressionStatement
    :   expression? endOfItem
    ;

selectionStatement
    :   'if' '(' expression ')' statement ('else' statement)? #ifStatement
    |   'switch' '(' expression ')' '{' (switchLabeledStatement)* '}' #switchStatement
    ;

switchLabeledStatement
    :   'case' constantExpression ':' statement
    |   'default' ':' statement
    ;

iterationStatement
    :   For '(' forCondition ')' statement
    |   While '(' expression ')' statement
    |   Do statement While '(' expression ')' endOfItem
    ;

forCondition
	  :   (forDeclaration | expression?) endOfItem forExpression? endOfItem forExpression?
	  ;

forDeclaration
    :   storageTypeSpecifier? initDeclarator
    ;

forExpression
    :   assignmentExpression (',' assignmentExpression )*
    ;

jumpStatement
    :   (('continue' | 'break')
    |   'return' expression?
    )
    endOfItem
    ;

// Lexer Rules (tokens / token rules)

// import
Import : 'import';
From : 'from';

// const / var
Const : 'const';

// conversion
As : 'as';

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

// function-related
Return : 'return';
NoRet : 'noret';
Entry : 'entry';

// object-related
New : 'new';
Struct : 'struct';
Class : 'class';

// typeof operator
Typeof : 'typeof';

// delete variable
Delete : 'delete';

// Punctuators
LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';

// Mathematical operators
Plus : '+';
PlusPlus : '++';
Minus : '-';
MinusMinus : '--';
Star : '*';
Div : '/';
Mod : '%';
PowerTo : '**';

// Boolish Logical Operations
AndAnd : '&&';
OrOr : '||';
Not : '!';

// General comma
Comma : ',';

// Value assign
Assign : '=';

// '*=' | '/=' | '%=' | '+=' | '-=' |
StarAssign : '*=';
DivAssign : '/=';
ModAssign : '%=';
PlusAssign : '+=';
MinusAssign : '-=';

// Value Comparison
Equal : '==';
NotEqual : '!=';
Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';

// property accessing
Dot : '.';

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

CharacterConstant
    :   '\'' CCharSequence '\''
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

FStringLiteral
    :   'f' '"' SCharSequence? '"'
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

Whitespace
    :   [ \t]+
        -> skip
    ;

BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

Newline
    :   (  '\r' '\n'? | '\n')
        -> skip
    ;
