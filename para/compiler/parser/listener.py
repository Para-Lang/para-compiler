# coding=utf-8
""" Listener Class """
from __future__ import annotations

import logging
from os import PathLike
from typing import TYPE_CHECKING, Union

import antlr4

from .python import ParaListener
from .python import ParaParser
from ..compile_ctx import FileCompilationContext, ProgramCompilationContext
from ..logic_stream import ParaQualifiedLogicStream

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    # Assigning the variables to hold the imported classes for easier type
    # hinting and avoiding exceeding the line length
    ExpressionContext = ParaParser.ExpressionContext
    FunctionDefinitionContext = ParaParser.FunctionDefinitionContext
    AssignmentExpressionContext = ParaParser.AssignmentExpressionContext
    CompilationUnitContext = ParaParser.CompilationUnitContext

__all__ = [
    'Listener'
]


class Listener(ParaListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaListener and then define the wanted
    behaviour inside a compilation.
    """

    def __init__(
            self,
            antlr4_file_ctx: CompilationUnitContext,
            file_stream: antlr4.InputStream,
            relative_file_name: Union[str, PathLike],
            program_ctx: ProgramCompilationContext
    ):
        self._file_ctx = FileCompilationContext(
            relative_file_name, program_ctx
        )
        self.antlr4_file_ctx: CompilationUnitContext = antlr4_file_ctx
        self.file_stream: antlr4.InputStream = file_stream

        self._compiling: bool = False
        self._prefer_logging: bool = False

    @property
    def logic_stream(self) -> ParaQualifiedLogicStream:
        """ Stream which stores the logical tokens for the passed file. """
        return self._file_ctx.logic_stream

    @property
    def file_ctx(self) -> FileCompilationContext:
        """ Fetches the file context for this class """
        return self._file_ctx

    async def walk(self, prefer_logging: bool) -> None:
        """
        Walks through the parsed CompilationUnitContext and listens to the
        events / goes through the tokens.

        This is a non-compile version of walk_and_generate_logic_stream, which
        is only used stand-alone for syntax-checking. This method does not
        exist on the Pre-Processor counterpart, as it is not necessary.

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """
        logger.debug(
            "Walking through logic tree and generating the logic stream"
        )
        self._prefer_logging = prefer_logging

        walker = antlr4.ParseTreeWalker()
        walker.walk(self, self.antlr4_file_ctx)

    async def walk_and_generate_logic_stream(
            self, prefer_logging: bool
    ) -> None:
        """
        Walks through the parsed CompilationUnitContext and listens to the
        events / goes through the tokens and generates the logic stream
        for the FileCompilationContext (self.file_ctx)

        The FileCompilationContext can then be used inside the
        CompilationContext to be linked with other files and to finish
        the compilation for the program

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """

        # Variable set to signalise that the items should be added to the
        # logic stream
        self._compiling = True
        await self.walk(prefer_logging)

    # =========================================
    # Beginning of the file
    # =========================================
    def enterCompilationUnit(
            self,
            ctx: ParaParser.CompilationUnitContext
    ):
        """
        Enter a parse tree produced by ParaParser#compilationUnit.

        Is the base from where the tree is going to start (starts at the first
        token of the file and ends at the last token)
        """
        logger.debug("Starting file parsing")

    # =========================================
    # End of the file
    # =========================================
    def exitCompilationUnit(
            self,
            ctx: ParaParser.CompilationUnitContext
    ):
        """
        Exit a parse tree produced by ParaParser#compilationUnit.

        Is the point where the token stream will end. (EOF excluded)
        """
        logger.debug("Finished file parsing")

    def enterLambdaFunction(
            self,
            ctx: ParaParser.LambdaFunctionContext
    ):
        """
        Enter a parse tree produced by ParaParser#lambdaFunction.
        """
        ...

    def exitLambdaFunction(
            self,
            ctx: ParaParser.LambdaFunctionContext
    ):
        """
        Exit a parse tree produced by ParaParser#lambdaFunction.
        """
        ...

    def enterLambdaBody(
            self,
            ctx: ParaParser.LambdaBodyContext
    ):
        """
        Enter a parse tree produced by ParaParser#lambdaBody.
        """
        ...

    def exitLambdaBody(
            self,
            ctx: ParaParser.LambdaBodyContext
    ):
        """
        Exit a parse tree produced by ParaParser#lambdaBody.
        """
        ...

    def enterExpressionLambda(
            self,
            ctx: ParaParser.ExpressionLambdaContext
    ):
        """
        Enter a parse tree produced by ParaParser#expressionLambda.
        """
        ...

    def exitExpressionLambda(
            self,
            ctx: ParaParser.ExpressionLambdaContext
    ):
        """
        Exit a parse tree produced by ParaParser#expressionLambda.
        """
        ...

    def enterStatementLambda(
            self,
            ctx: ParaParser.StatementLambdaContext
    ):
        """
        Enter a parse tree produced by ParaParser#statementLambda.
        """
        ...

    def exitStatementLambda(
            self,
            ctx: ParaParser.StatementLambdaContext
    ):
        """
        Exit a parse tree produced by ParaParser#statementLambda.
        """
        ...

    def enterCastOrConvertExpression(
            self,
            ctx: ParaParser.CastOrConvertExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#castOrConvertExpression.
        """
        ...

    def exitCastOrConvertExpression(
            self,
            ctx: ParaParser.CastOrConvertExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#castOrConvertExpression.
        """
        ...

    def enterRegularParameterDeclaration(
            self,
            ctx: ParaParser.RegularParameterDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaParser#regularDeclaration.
        """
        ...

    def exitRegularParameterDeclaration(
            self,
            ctx: ParaParser.RegularParameterDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaParser#regularDeclaration.
        """
        ...

    def enterAbstractParameterDeclaration(
            self,
            ctx: ParaParser.AbstractParameterDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaParser#abstractDeclaration.
        """
        ...

    def exitAbstractParameterDeclaration(
            self,
            ctx: ParaParser.AbstractParameterDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaParser#abstractDeclaration.
        """
        ...

    def enterExternalFunctionDefinition(
            self,
            ctx: ParaParser.ExternalFunctionDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaParser#externalFunctionDefinition.
        """
        ...

    def exitExternalFunctionDefinition(
            self,
            ctx: ParaParser.ExternalFunctionDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaParser#externalFunctionDefinition.
        """
        ...

    def enterExternalDeclaration(
            self,
            ctx: ParaParser.ExternalDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaParser#externalDeclaration.
        """
        ...

    def exitExternalDeclaration(
            self,
            ctx: ParaParser.ExternalDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaParser#externalDeclaration.
        """
        ...

    def enterExternalExtTaskDefinition(
            self,
            ctx: ParaParser.ExternalExtTaskDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaParser#externalExtTaskDefinition.
        """
        ...

    def exitExternalExtTaskDefinition(
            self,
            ctx: ParaParser.ExternalExtTaskDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaParser#externalExtTaskDefinition.
        """
        ...

    def enterStandardFunctionDefinition(
            self,
            ctx: ParaParser.StandardFunctionDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaParser#standardFunctionDefinition.
        """
        ...

    def exitStandardFunctionDefinition(
            self,
            ctx: ParaParser.StandardFunctionDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaParser#standardFunctionDefinition.
        """
        ...

    def enterSimpleFunctionDefinition(
            self,
            ctx: ParaParser.SimpleFunctionDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaParser#simpleFunctionDefinition.
        """
        ...

    def exitSimpleFunctionDefinition(
            self,
            ctx: ParaParser.SimpleFunctionDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaParser#simpleFunctionDefinition.
        """
        ...

    def enterFunctionDeclarationSpecifiers(
            self,
            ctx: ParaParser.FunctionDeclarationSpecifiersContext
    ):
        """
        Enter a parse tree produced by
        ParaParser#functionDeclarationSpecifiers.
        """
        ...

    def exitFunctionDeclarationSpecifiers(
            self,
            ctx: ParaParser.FunctionDeclarationSpecifiersContext
    ):
        """
        Exit a parse tree produced by
        ParaParser#functionDeclarationSpecifiers.
        """
        ...

    def enterDecoratorSpecifier(
            self,
            ctx: ParaParser.DecoratorSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaParser#decoratorSpecifier.
        """
        ...

    def exitDecoratorSpecifier(
            self,
            ctx: ParaParser.DecoratorSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaParser#decoratorSpecifier.
        """
        ...

    def enterExtensionTaskDefinition(
            self,
            ctx: ParaParser.ExtensionTaskDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaParser#extensionTaskDefinition.
        """
        ...

    def exitExtensionTaskDefinition(
            self,
            ctx: ParaParser.ExtensionTaskDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaParser#extensionTaskDefinition.
        """
        ...

    def enterExtensionTaskParameterList(
            self,
            ctx: ParaParser.ExtensionTaskParameterListContext
    ):
        """
        Enter a parse tree produced by ParaParser#extensionTaskParameterList.
        """
        ...

    def exitExtensionTaskParameterList(
            self,
            ctx: ParaParser.ExtensionTaskParameterListContext
    ):
        """
        Exit a parse tree produced by ParaParser#extensionTaskParameterList.
        """
        ...

    def enterExtensionTaskParameter(
            self,
            ctx: ParaParser.ExtensionTaskParameterContext
    ):
        """
        Enter a parse tree produced by ParaParser#extensionTaskParameter.
        """
        ...

    def exitExtensionTaskParameter(
            self,
            ctx: ParaParser.ExtensionTaskParameterContext
    ):
        """
        Exit a parse tree produced by ParaParser#extensionTaskParameter.
        """
        ...

    def enterTryExceptStatement(
            self,
            ctx: ParaParser.TryExceptStatementContext
    ):
        """
        Enter a parse tree produced by ParaParser#tryExceptStatement.
        """
        ...

    def exitTryExceptStatement(
            self,
            ctx: ParaParser.TryExceptStatementContext
    ):
        """
        Exit a parse tree produced by ParaParser#tryExceptStatement.
        """
        ...

    def enterExceptBlock(
            self,
            ctx: ParaParser.ExceptBlockContext
    ):
        """
        Enter a parse tree produced by ParaParser#exceptBlock.
        """
        ...

    def exitExceptBlock(
            self,
            ctx: ParaParser.ExceptBlockContext
    ):
        """
        Exit a parse tree produced by ParaParser#exceptBlock.
        """
        ...

    def enterFinallyBlock(
            self,
            ctx: ParaParser.FinallyBlockContext
    ):
        """
        Enter a parse tree produced by ParaParser#finallyBlock.
        """
        ...

    def exitFinallyBlock(
            self,
            ctx: ParaParser.FinallyBlockContext
    ):
        """
        Exit a parse tree produced by ParaParser#finallyBlock.
        """
        ...

    def enterElseBlock(
            self,
            ctx: ParaParser.ElseBlockContext
    ):
        """
        Enter a parse tree produced by ParaParser#elseBlock.
        """
        ...

    def exitElseBlock(
            self,
            ctx: ParaParser.ElseBlockContext
    ):
        """
        Exit a parse tree produced by ParaParser#elseBlock.
        """
        ...

    def enterPrimaryExpression(
            self,
            ctx: ParaParser.PrimaryExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#primaryExpression.
        """
        ...

    def exitPrimaryExpression(
            self,
            ctx: ParaParser.PrimaryExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#primaryExpression.
        """
        ...

    def enterPostfixExpression(
            self,
            ctx: ParaParser.PostfixExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#postfixExpression.
        """
        ...

    def exitPostfixExpression(
            self,
            ctx: ParaParser.PostfixExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#postfixExpression.
        """
        ...

    def enterArgumentExpressionList(
            self,
            ctx: ParaParser.ArgumentExpressionListContext
    ):
        """
        Enter a parse tree produced by ParaParser#argumentExpressionList.
        """
        ...

    def exitArgumentExpressionList(
            self,
            ctx: ParaParser.ArgumentExpressionListContext
    ):
        """
        Exit a parse tree produced by ParaParser#argumentExpressionList.
        """
        ...

    def enterUnaryExpression(
            self,
            ctx: ParaParser.UnaryExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#unaryExpression.
        """
        ...

    def exitUnaryExpression(
            self,
            ctx: ParaParser.UnaryExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#unaryExpression.
        """
        ...

    def enterUnaryOperator(
            self,
            ctx: ParaParser.UnaryOperatorContext
    ):
        """
        Enter a parse tree produced by ParaParser#unaryOperator.
        """
        ...

    def exitUnaryOperator(
            self,
            ctx: ParaParser.UnaryOperatorContext
    ):
        """
        Exit a parse tree produced by ParaParser#unaryOperator.
        """
        ...

    def enterMultiplicativeExpression(
            self,
            ctx: ParaParser.MultiplicativeExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#multiplicativeExpression.
        """
        ...

    def exitMultiplicativeExpression(
            self,
            ctx: ParaParser.MultiplicativeExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#multiplicativeExpression.
        """
        ...

    def enterAdditiveExpression(
            self,
            ctx: ParaParser.AdditiveExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#additiveExpression.
        """
        ...

    def exitAdditiveExpression(
            self,
            ctx: ParaParser.AdditiveExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#additiveExpression.
        """
        ...

    def enterShiftExpression(
            self,
            ctx: ParaParser.ShiftExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#shiftExpression.
        """
        ...

    def exitShiftExpression(
            self,
            ctx: ParaParser.ShiftExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#shiftExpression.
        """
        ...

    def enterRelationalExpression(
            self,
            ctx: ParaParser.RelationalExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#relationalExpression.
        """
        ...

    def exitRelationalExpression(
            self,
            ctx: ParaParser.RelationalExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#relationalExpression.
        """
        ...

    def enterEqualityExpression(
            self,
            ctx: ParaParser.EqualityExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#equalityExpression.
        """
        ...

    def exitEqualityExpression(
            self,
            ctx: ParaParser.EqualityExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#equalityExpression.
        """
        ...

    def enterAndExpression(
            self,
            ctx: ParaParser.AndExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#andExpression.
        """
        ...

    def exitAndExpression(
            self,
            ctx: ParaParser.AndExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#andExpression.
        """
        ...

    def enterExclusiveOrExpression(
            self,
            ctx: ParaParser.ExclusiveOrExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#exclusiveOrExpression.
        """
        ...

    def exitExclusiveOrExpression(
            self,
            ctx: ParaParser.ExclusiveOrExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#exclusiveOrExpression.
        """
        ...

    def enterInclusiveOrExpression(
            self,
            ctx: ParaParser.InclusiveOrExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#inclusiveOrExpression.
        """
        ...

    def exitInclusiveOrExpression(
            self,
            ctx: ParaParser.InclusiveOrExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#inclusiveOrExpression.
        """
        ...

    def enterLogicalAndExpression(
            self,
            ctx: ParaParser.LogicalAndExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#logicalAndExpression.
        """
        ...

    def exitLogicalAndExpression(
            self,
            ctx: ParaParser.LogicalAndExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#logicalAndExpression.
        """
        ...

    def enterLogicalOrExpression(
            self,
            ctx: ParaParser.LogicalOrExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#logicalOrExpression.
        """
        ...

    def exitLogicalOrExpression(
            self,
            ctx: ParaParser.LogicalOrExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#logicalOrExpression.
        """
        ...

    def enterConditionalExpression(
            self,
            ctx: ParaParser.ConditionalExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#conditionalExpression.
        """
        ...

    def exitConditionalExpression(
            self,
            ctx: ParaParser.ConditionalExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#conditionalExpression.
        """
        ...

    def enterAssignmentExpression(
            self,
            ctx: ParaParser.AssignmentExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#assignmentExpression.
        """
        ...

    def exitAssignmentExpression(
            self,
            ctx: ParaParser.AssignmentExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#assignmentExpression.
        """
        ...

    def enterAssignmentOperator(
            self,
            ctx: ParaParser.AssignmentOperatorContext
    ):
        """
        Enter a parse tree produced by ParaParser#assignmentOperator.
        """
        ...

    def exitAssignmentOperator(
            self,
            ctx: ParaParser.AssignmentOperatorContext
    ):
        """
        Exit a parse tree produced by ParaParser#assignmentOperator.
        """
        ...

    def enterExpression(
            self,
            ctx: ParaParser.ExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#expression.
        """
        ...

    def exitExpression(
            self,
            ctx: ParaParser.ExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#expression.
        """
        ...

    def enterConstantExpression(
            self,
            ctx: ParaParser.ConstantExpressionContext
    ):
        """
        Enter a parse tree produced by ParaParser#constantExpression.
        """
        ...

    def exitConstantExpression(
            self,
            ctx: ParaParser.ConstantExpressionContext
    ):
        """
        Exit a parse tree produced by ParaParser#constantExpression.
        """
        ...

    def enterDeclaration(
            self,
            ctx: ParaParser.DeclarationContext
    ):
        """
        Enter a parse tree produced by ParaParser#declaration.
        """
        ...

    def exitDeclaration(
            self,
            ctx: ParaParser.DeclarationContext
    ):
        """
        Exit a parse tree produced by ParaParser#declaration.
        """
        ...

    def enterDeclarationSpecifiers(
            self,
            ctx: ParaParser.DeclarationSpecifiersContext
    ):
        """
        Enter a parse tree produced by ParaParser#declarationSpecifiers.
        """
        ...

    def exitDeclarationSpecifiers(
            self,
            ctx: ParaParser.DeclarationSpecifiersContext
    ):
        """
        Exit a parse tree produced by ParaParser#declarationSpecifiers.
        """
        ...

    def enterDeclarationSpecifier(
            self,
            ctx: ParaParser.DeclarationSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaParser#declarationSpecifier.
        """
        ...

    def exitDeclarationSpecifier(
            self,
            ctx: ParaParser.DeclarationSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaParser#declarationSpecifier.
        """
        ...

    def enterInitDeclaratorList(
            self,
            ctx: ParaParser.InitDeclaratorListContext
    ):
        """
        Enter a parse tree produced by ParaParser#initDeclaratorList.
        """
        ...

    def exitInitDeclaratorList(
            self,
            ctx: ParaParser.InitDeclaratorListContext
    ):
        """
        Exit a parse tree produced by ParaParser#initDeclaratorList.
        """
        ...

    def enterInitDeclarator(
            self,
            ctx: ParaParser.InitDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaParser#initDeclarator.
        """
        ...

    def exitInitDeclarator(
            self,
            ctx: ParaParser.InitDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaParser#initDeclarator.
        """
        ...

    def enterStorageClassSpecifier(
            self,
            ctx: ParaParser.StorageClassSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaParser#storageClassSpecifier.
        """
        ...

    def exitStorageClassSpecifier(
            self,
            ctx: ParaParser.StorageClassSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaParser#storageClassSpecifier.
        """
        ...

    def enterTypeSpecifier(
            self,
            ctx: ParaParser.TypeSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaParser#typeSpecifier.
        """
        ...

    def exitTypeSpecifier(
            self,
            ctx: ParaParser.TypeSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaParser#typeSpecifier.
        """
        ...

    def enterStructOrUnionSpecifier(
            self,
            ctx: ParaParser.StructOrUnionSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaParser#structOrUnionSpecifier.
        """
        ...

    def exitStructOrUnionSpecifier(
            self,
            ctx: ParaParser.StructOrUnionSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaParser#structOrUnionSpecifier.
        """
        ...

    def enterStructOrUnion(
            self,
            ctx: ParaParser.StructOrUnionContext
    ):
        """
        Enter a parse tree produced by ParaParser#structOrUnion.
        """
        ...

    def exitStructOrUnion(
            self,
            ctx: ParaParser.StructOrUnionContext
    ):
        """
        Exit a parse tree produced by ParaParser#structOrUnion.
        """
        ...

    def enterStructDeclarationList(
            self,
            ctx: ParaParser.StructDeclarationListContext
    ):
        """
        Enter a parse tree produced by ParaParser#structDeclarationList.
        """
        ...

    def exitStructDeclarationList(
            self,
            ctx: ParaParser.StructDeclarationListContext
    ):
        """
        Exit a parse tree produced by ParaParser#structDeclarationList.
        """
        ...

    def enterStructDeclaration(
            self,
            ctx: ParaParser.StructDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaParser#structDeclaration.
        """
        ...

    def exitStructDeclaration(
            self,
            ctx: ParaParser.StructDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaParser#structDeclaration.
        """
        ...

    def enterSpecifierQualifierList(
            self,
            ctx: ParaCParser.SpecifierQualifierListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#specifierQualifierList.
        """
        ...

    def exitSpecifierQualifierList(
            self,
            ctx: ParaCParser.SpecifierQualifierListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#specifierQualifierList.
        """
        ...

    def enterStructDeclaratorList(
            self,
            ctx: ParaCParser.StructDeclaratorListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#structDeclaratorList.
        """
        ...

    def exitStructDeclaratorList(
            self,
            ctx: ParaCParser.StructDeclaratorListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#structDeclaratorList.
        """
        ...

    def enterStructDeclarator(
            self,
            ctx: ParaCParser.StructDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#structDeclarator.
        """
        ...

    def exitStructDeclarator(
            self,
            ctx: ParaCParser.StructDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#structDeclarator.
        """
        ...

    def enterEnumSpecifier(
            self,
            ctx: ParaCParser.EnumSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#enumSpecifier.
        """
        ...

    def exitEnumSpecifier(
            self,
            ctx: ParaCParser.EnumSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#enumSpecifier.
        """
        ...

    def enterEnumeratorList(
            self,
            ctx: ParaCParser.EnumeratorListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#enumeratorList.
        """
        ...

    def exitEnumeratorList(
            self,
            ctx: ParaCParser.EnumeratorListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#enumeratorList.
        """
        ...

    def enterEnumerator(
            self,
            ctx: ParaCParser.EnumeratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#enumerator.
        """
        ...

    def exitEnumerator(
            self,
            ctx: ParaCParser.EnumeratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#enumerator.
        """
        ...

    def enterEnumerationConstant(
            self,
            ctx: ParaCParser.EnumerationConstantContext
    ):
        """
        Enter a parse tree produced by ParaCParser#enumerationConstant.
        """
        ...

    def exitEnumerationConstant(
            self,
            ctx: ParaCParser.EnumerationConstantContext
    ):
        """
        Exit a parse tree produced by ParaCParser#enumerationConstant.
        """
        ...

    def enterAtomicTypeSpecifier(
            self,
            ctx: ParaCParser.AtomicTypeSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#atomicTypeSpecifier.
        """
        ...

    def exitAtomicTypeSpecifier(
            self,
            ctx: ParaCParser.AtomicTypeSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#atomicTypeSpecifier.
        """
        ...

    def enterTypeQualifier(
            self,
            ctx: ParaCParser.TypeQualifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typeQualifier.
        """
        ...

    def exitTypeQualifier(
            self,
            ctx: ParaCParser.TypeQualifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typeQualifier.
        """
        ...

    def enterFunctionSpecifier(
            self,
            ctx: ParaCParser.FunctionSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#functionSpecifier.
        """
        ...

    def exitFunctionSpecifier(
            self,
            ctx: ParaCParser.FunctionSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#functionSpecifier.
        """
        ...

    def enterAlignmentSpecifier(
            self,
            ctx: ParaCParser.AlignmentSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#alignmentSpecifier.
        """
        ...

    def exitAlignmentSpecifier(
            self,
            ctx: ParaCParser.AlignmentSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#alignmentSpecifier.
        """
        ...

    def enterDeclarator(
            self,
            ctx: ParaCParser.DeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#declarator.
        """
        ...

    def exitDeclarator(
            self,
            ctx: ParaCParser.DeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#declarator.
        """
        ...

    def enterDirectDeclarator(
            self,
            ctx: ParaCParser.DirectDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#directDeclarator.
        """
        ...

    def exitDirectDeclarator(
            self,
            ctx: ParaCParser.DirectDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#directDeclarator.
        """
        ...

    def enterNestedParenthesesBlock(
            self,
            ctx: ParaCParser.NestedParenthesesBlockContext
    ):
        """
        Enter a parse tree produced by ParaCParser#nestedParenthesesBlock.
        """
        ...

    def exitNestedParenthesesBlock(
            self,
            ctx: ParaCParser.NestedParenthesesBlockContext
    ):
        """
        Exit a parse tree produced by ParaCParser#nestedParenthesesBlock.
        """
        ...

    def enterPointer(
            self,
            ctx: ParaCParser.PointerContext
    ):
        """
        Enter a parse tree produced by ParaCParser#pointer.
        """
        ...

    def exitPointer(
            self,
            ctx: ParaCParser.PointerContext
    ):
        """
        Exit a parse tree produced by ParaCParser#pointer.
        """
        ...

    def enterTypeQualifierList(
            self,
            ctx: ParaCParser.TypeQualifierListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typeQualifierList.
        """
        ...

    def exitTypeQualifierList(
            self,
            ctx: ParaCParser.TypeQualifierListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typeQualifierList.
        """
        ...

    def enterParameterTypeList(
            self,
            ctx: ParaCParser.ParameterTypeListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#parameterTypeList.
        """
        ...

    def exitParameterTypeList(
            self,
            ctx: ParaCParser.ParameterTypeListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#parameterTypeList.
        """
        ...

    def enterParameterList(
            self,
            ctx: ParaCParser.ParameterListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#parameterList.
        """
        ...

    def exitParameterList(
            self,
            ctx: ParaCParser.ParameterListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#parameterList.
        """
        ...

    def enterIdentifierList(
            self,
            ctx: ParaCParser.IdentifierListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#identifierList.
        """
        ...

    def exitIdentifierList(
            self,
            ctx: ParaCParser.IdentifierListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#identifierList.
        """
        ...

    def enterTypeName(
            self,
            ctx: ParaCParser.TypeNameContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typeName.
        """
        ...

    def exitTypeName(
            self,
            ctx: ParaCParser.TypeNameContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typeName.
        """
        ...

    def enterAbstractDeclarator(
            self,
            ctx: ParaCParser.AbstractDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#abstractDeclarator.
        """
        ...

    def exitAbstractDeclarator(
            self,
            ctx: ParaCParser.AbstractDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#abstractDeclarator.
        """
        ...

    def enterDirectAbstractDeclarator(
            self,
            ctx: ParaCParser.DirectAbstractDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#directAbstractDeclarator.
        """
        ...

    def exitDirectAbstractDeclarator(
            self,
            ctx: ParaCParser.DirectAbstractDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#directAbstractDeclarator.
        """
        ...

    def enterTypedefName(
            self,
            ctx: ParaCParser.TypedefNameContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typedefName.
        """
        ...

    def exitTypedefName(
            self,
            ctx: ParaCParser.TypedefNameContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typedefName.
        """
        ...

    def enterInitializer(
            self,
            ctx: ParaCParser.InitializerContext
    ):
        """
        Enter a parse tree produced by ParaCParser#initializer.
        """
        ...

    def exitInitializer(
            self,
            ctx: ParaCParser.InitializerContext
    ):
        """
        Exit a parse tree produced by ParaCParser#initializer.
        """
        ...

    def enterInitializerList(
            self,
            ctx: ParaCParser.InitializerListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#initializerList.
        """
        ...

    def exitInitializerList(
            self,
            ctx: ParaCParser.InitializerListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#initializerList.
        """
        ...

    def enterDesignation(
            self,
            ctx: ParaCParser.DesignationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#designation.
        """
        ...

    def exitDesignation(
            self,
            ctx: ParaCParser.DesignationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#designation.
        """
        ...

    def enterDesignatorList(
            self,
            ctx: ParaCParser.DesignatorListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#designatorList.
        """
        ...

    def exitDesignatorList(
            self,
            ctx: ParaCParser.DesignatorListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#designatorList.
        """
        ...

    def enterDesignator(
            self,
            ctx: ParaCParser.DesignatorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#designator.
        """
        ...

    def exitDesignator(
            self,
            ctx: ParaCParser.DesignatorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#designator.
        """
        ...

    def enterStaticAssertDeclaration(
            self,
            ctx: ParaCParser.StaticAssertDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#staticAssertDeclaration.
        """
        ...

    def exitStaticAssertDeclaration(
            self,
            ctx: ParaCParser.StaticAssertDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#staticAssertDeclaration.
        """
        ...

    def enterStatement(
            self,
            ctx: ParaCParser.StatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#statement.
        """
        ...

    def exitStatement(
            self,
            ctx: ParaCParser.StatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#statement.
        """
        ...

    def enterLabeledStatement(
            self,
            ctx: ParaCParser.LabeledStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#labeledStatement.
        """
        ...

    def exitLabeledStatement(
            self,
            ctx: ParaCParser.LabeledStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#labeledStatement.
        """
        ...

    def enterCompoundStatement(
            self,
            ctx: ParaCParser.CompoundStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#compoundStatement.
        """
        ...

    def exitCompoundStatement(
            self,
            ctx: ParaCParser.CompoundStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#compoundStatement.
        """
        ...

    def enterBlockItemList(
            self,
            ctx: ParaCParser.BlockItemListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#blockItemList.
        """
        ...

    def exitBlockItemList(
            self,
            ctx: ParaCParser.BlockItemListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#blockItemList.
        """
        ...

    def enterBlockItem(
            self,
            ctx: ParaCParser.BlockItemContext
    ):
        """
        Enter a parse tree produced by ParaCParser#blockItem.
        """
        ...

    def exitBlockItem(
            self,
            ctx: ParaCParser.BlockItemContext
    ):
        """
        Exit a parse tree produced by ParaCParser#blockItem.
        """
        ...

    def enterExpressionStatement(
            self,
            ctx: ParaCParser.ExpressionStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#expressionStatement.
        """
        ...

    def exitExpressionStatement(
            self,
            ctx: ParaCParser.ExpressionStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#expressionStatement.
        """
        ...

    def enterSelectionStatement(
            self,
            ctx: ParaCParser.SelectionStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#selectionStatement.
        """
        ...

    def exitSelectionStatement(
            self,
            ctx: ParaCParser.SelectionStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#selectionStatement.
        """
        ...

    def enterIterationStatement(
            self,
            ctx: ParaCParser.IterationStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#iterationStatement.
        """
        ...

    def exitIterationStatement(
            self,
            ctx: ParaCParser.IterationStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#iterationStatement.
        """
        ...

    def enterForCondition(
            self,
            ctx: ParaCParser.ForConditionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#forCondition.
        """
        ...

    def exitForCondition(
            self,
            ctx: ParaCParser.ForConditionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#forCondition.
        """
        ...

    def enterForDeclaration(
            self,
            ctx: ParaCParser.ForDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#forDeclaration.
        """
        ...

    def exitForDeclaration(
            self,
            ctx: ParaCParser.ForDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#forDeclaration.
        """
        ...

    def enterForExpression(
            self,
            ctx: ParaCParser.ForExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#forExpression.
        """
        ...

    def exitForExpression(
            self,
            ctx: ParaCParser.ForExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#forExpression.
        """
        ...

    def enterJumpStatement(
            self,
            ctx: ParaCParser.JumpStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#jumpStatement.
        """
        ...

    def exitJumpStatement(
            self,
            ctx: ParaCParser.JumpStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#jumpStatement.
        """
        ...

    def enterTranslationUnit(
            self,
            ctx: ParaCParser.TranslationUnitContext
    ):
        """
        Enter a parse tree produced by ParaCParser#translationUnit.
        """
        ...

    def exitTranslationUnit(
            self,
            ctx: ParaCParser.TranslationUnitContext
    ):
        """
        Exit a parse tree produced by ParaCParser#translationUnit.
        """
        ...

    def enterDeclarationList(
            self,
            ctx: ParaCParser.DeclarationListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#declarationList.
        """
        ...

    def exitDeclarationList(
            self,
            ctx: ParaCParser.DeclarationListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#declarationList.
        """
        ...
