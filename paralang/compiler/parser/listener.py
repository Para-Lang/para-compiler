# coding=utf-8
""" Listener Class """
from __future__ import annotations

import logging
import antlr4
from typing import TYPE_CHECKING, Optional

from .python import ParaListener
from .python import ParaParser
from ..parse_stream import ParaQualifiedParseStream

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    # Assigning the variables to hold the imported classes for easier type
    # hinting and avoiding exceeding the line length
    ExpressionContext = ParaParser.ExpressionContext
    FunctionDefinitionContext = ParaParser.FunctionDefinitionContext
    AssignmentExpressionContext = ParaParser.AssignmentExpressionContext
    CompilationUnitContext = ParaParser.CompilationUnitContext
    ExternalItemContext = ParaParser.ExternalItemContext

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
            antlr4_file_ctx: ParaParser.CompilationUnitContext
    ):
        self._antlr4_file_ctx: ParaParser.CompilationUnitContext = \
            antlr4_file_ctx
        self._prefer_logging: bool = False
        self._current_external_item = None
        self._parse_stream: Optional[ParaQualifiedParseStream] = None
        self._running = False

    @property
    def antlr4_file_ctx(self) -> ParaParser.CompilationUnitContext:
        """
        The antlr4 file ctx, which represents the entire file in a logic
        tree made up of tokens
        """
        return self._antlr4_file_ctx

    @property
    def running(self) -> bool:
        """ Returns whether at the moment a stream generation is being run """
        return self._running

    async def walk(
            self, prefer_logging: bool
    ) -> ParaQualifiedParseStream:
        """
        Walks through the parsed CompilationUnitContext and listens to the
        events / goes through the tokens and generates a logic stream.

        The FileCompilationContext can then be used inside the
        CompilationContext to be linked with other files and to finish
        the compilation for the program.

        :param prefer_logging: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """
        if self._running:
            raise RuntimeError("May not run two generations at the same time!")

        self._parse_stream = ParaQualifiedParseStream()
        self._running = True

        logger.debug(
            "Walking through parse tree and generating the logic stream"
        )
        self._prefer_logging: bool = prefer_logging

        walker = antlr4.ParseTreeWalker()
        walker.walk(self, self.antlr4_file_ctx)

        self._running = False
        return self._parse_stream

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
            ctx: ParaParser.SpecifierQualifierListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#specifierQualifierList.
        """
        ...

    def exitSpecifierQualifierList(
            self,
            ctx: ParaParser.SpecifierQualifierListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#specifierQualifierList.
        """
        ...

    def enterStructDeclaratorList(
            self,
            ctx: ParaParser.StructDeclaratorListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#structDeclaratorList.
        """
        ...

    def exitStructDeclaratorList(
            self,
            ctx: ParaParser.StructDeclaratorListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#structDeclaratorList.
        """
        ...

    def enterStructDeclarator(
            self,
            ctx: ParaParser.StructDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#structDeclarator.
        """
        ...

    def exitStructDeclarator(
            self,
            ctx: ParaParser.StructDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#structDeclarator.
        """
        ...

    def enterEnumSpecifier(
            self,
            ctx: ParaParser.EnumSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#enumSpecifier.
        """
        ...

    def exitEnumSpecifier(
            self,
            ctx: ParaParser.EnumSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#enumSpecifier.
        """
        ...

    def enterEnumeratorList(
            self,
            ctx: ParaParser.EnumeratorListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#enumeratorList.
        """
        ...

    def exitEnumeratorList(
            self,
            ctx: ParaParser.EnumeratorListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#enumeratorList.
        """
        ...

    def enterEnumerator(
            self,
            ctx: ParaParser.EnumeratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#enumerator.
        """
        ...

    def exitEnumerator(
            self,
            ctx: ParaParser.EnumeratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#enumerator.
        """
        ...

    def enterEnumerationConstant(
            self,
            ctx: ParaParser.EnumerationConstantContext
    ):
        """
        Enter a parse tree produced by ParaCParser#enumerationConstant.
        """
        ...

    def exitEnumerationConstant(
            self,
            ctx: ParaParser.EnumerationConstantContext
    ):
        """
        Exit a parse tree produced by ParaCParser#enumerationConstant.
        """
        ...

    def enterAtomicTypeSpecifier(
            self,
            ctx: ParaParser.AtomicTypeSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#atomicTypeSpecifier.
        """
        ...

    def exitAtomicTypeSpecifier(
            self,
            ctx: ParaParser.AtomicTypeSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#atomicTypeSpecifier.
        """
        ...

    def enterTypeQualifier(
            self,
            ctx: ParaParser.TypeQualifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typeQualifier.
        """
        ...

    def exitTypeQualifier(
            self,
            ctx: ParaParser.TypeQualifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typeQualifier.
        """
        ...

    def enterFunctionSpecifier(
            self,
            ctx: ParaParser.FunctionSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#functionSpecifier.
        """
        ...

    def exitFunctionSpecifier(
            self,
            ctx: ParaParser.FunctionSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#functionSpecifier.
        """
        ...

    def enterAlignmentSpecifier(
            self,
            ctx: ParaParser.AlignmentSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#alignmentSpecifier.
        """
        ...

    def exitAlignmentSpecifier(
            self,
            ctx: ParaParser.AlignmentSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#alignmentSpecifier.
        """
        ...

    def enterDeclarator(
            self,
            ctx: ParaParser.DeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#declarator.
        """
        ...

    def exitDeclarator(
            self,
            ctx: ParaParser.DeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#declarator.
        """
        ...

    def enterDirectDeclarator(
            self,
            ctx: ParaParser.DirectDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#directDeclarator.
        """
        ...

    def exitDirectDeclarator(
            self,
            ctx: ParaParser.DirectDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#directDeclarator.
        """
        ...

    def enterNestedParenthesesBlock(
            self,
            ctx: ParaParser.NestedParenthesesBlockContext
    ):
        """
        Enter a parse tree produced by ParaCParser#nestedParenthesesBlock.
        """
        ...

    def exitNestedParenthesesBlock(
            self,
            ctx: ParaParser.NestedParenthesesBlockContext
    ):
        """
        Exit a parse tree produced by ParaCParser#nestedParenthesesBlock.
        """
        ...

    def enterPointer(
            self,
            ctx: ParaParser.PointerContext
    ):
        """
        Enter a parse tree produced by ParaCParser#pointer.
        """
        ...

    def exitPointer(
            self,
            ctx: ParaParser.PointerContext
    ):
        """
        Exit a parse tree produced by ParaCParser#pointer.
        """
        ...

    def enterTypeQualifierList(
            self,
            ctx: ParaParser.TypeQualifierListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typeQualifierList.
        """
        ...

    def exitTypeQualifierList(
            self,
            ctx: ParaParser.TypeQualifierListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typeQualifierList.
        """
        ...

    def enterParameterTypeList(
            self,
            ctx: ParaParser.ParameterTypeListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#parameterTypeList.
        """
        ...

    def exitParameterTypeList(
            self,
            ctx: ParaParser.ParameterTypeListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#parameterTypeList.
        """
        ...

    def enterParameterList(
            self,
            ctx: ParaParser.ParameterListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#parameterList.
        """
        ...

    def exitParameterList(
            self,
            ctx: ParaParser.ParameterListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#parameterList.
        """
        ...

    def enterIdentifierList(
            self,
            ctx: ParaParser.IdentifierListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#identifierList.
        """
        ...

    def exitIdentifierList(
            self,
            ctx: ParaParser.IdentifierListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#identifierList.
        """
        ...

    def enterTypeName(
            self,
            ctx: ParaParser.TypeNameContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typeName.
        """
        ...

    def exitTypeName(
            self,
            ctx: ParaParser.TypeNameContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typeName.
        """
        ...

    def enterAbstractDeclarator(
            self,
            ctx: ParaParser.AbstractDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#abstractDeclarator.
        """
        ...

    def exitAbstractDeclarator(
            self,
            ctx: ParaParser.AbstractDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#abstractDeclarator.
        """
        ...

    def enterDirectAbstractDeclarator(
            self,
            ctx: ParaParser.DirectAbstractDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#directAbstractDeclarator.
        """
        ...

    def exitDirectAbstractDeclarator(
            self,
            ctx: ParaParser.DirectAbstractDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#directAbstractDeclarator.
        """
        ...

    def enterTypedefName(
            self,
            ctx: ParaParser.TypedefNameContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typedefName.
        """
        ...

    def exitTypedefName(
            self,
            ctx: ParaParser.TypedefNameContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typedefName.
        """
        ...

    def enterInitializer(
            self,
            ctx: ParaParser.InitializerContext
    ):
        """
        Enter a parse tree produced by ParaCParser#initializer.
        """
        ...

    def exitInitializer(
            self,
            ctx: ParaParser.InitializerContext
    ):
        """
        Exit a parse tree produced by ParaCParser#initializer.
        """
        ...

    def enterInitializerList(
            self,
            ctx: ParaParser.InitializerListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#initializerList.
        """
        ...

    def exitInitializerList(
            self,
            ctx: ParaParser.InitializerListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#initializerList.
        """
        ...

    def enterDesignation(
            self,
            ctx: ParaParser.DesignationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#designation.
        """
        ...

    def exitDesignation(
            self,
            ctx: ParaParser.DesignationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#designation.
        """
        ...

    def enterDesignatorList(
            self,
            ctx: ParaParser.DesignatorListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#designatorList.
        """
        ...

    def exitDesignatorList(
            self,
            ctx: ParaParser.DesignatorListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#designatorList.
        """
        ...

    def enterDesignator(
            self,
            ctx: ParaParser.DesignatorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#designator.
        """
        ...

    def exitDesignator(
            self,
            ctx: ParaParser.DesignatorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#designator.
        """
        ...

    def enterStaticAssertDeclaration(
            self,
            ctx: ParaParser.StaticAssertDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#staticAssertDeclaration.
        """
        ...

    def exitStaticAssertDeclaration(
            self,
            ctx: ParaParser.StaticAssertDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#staticAssertDeclaration.
        """
        ...

    def enterStatement(
            self,
            ctx: ParaParser.StatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#statement.
        """
        ...

    def exitStatement(
            self,
            ctx: ParaParser.StatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#statement.
        """
        ...

    def enterLabeledStatement(
            self,
            ctx: ParaParser.LabeledStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#labeledStatement.
        """
        ...

    def exitLabeledStatement(
            self,
            ctx: ParaParser.LabeledStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#labeledStatement.
        """
        ...

    def enterCompoundStatement(
            self,
            ctx: ParaParser.CompoundStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#compoundStatement.
        """
        ...

    def exitCompoundStatement(
            self,
            ctx: ParaParser.CompoundStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#compoundStatement.
        """
        ...

    def enterBlockItemList(
            self,
            ctx: ParaParser.BlockItemListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#blockItemList.
        """
        ...

    def exitBlockItemList(
            self,
            ctx: ParaParser.BlockItemListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#blockItemList.
        """
        ...

    def enterBlockItem(
            self,
            ctx: ParaParser.BlockItemContext
    ):
        """
        Enter a parse tree produced by ParaCParser#blockItem.
        """
        ...

    def exitBlockItem(
            self,
            ctx: ParaParser.BlockItemContext
    ):
        """
        Exit a parse tree produced by ParaCParser#blockItem.
        """
        ...

    def enterExpressionStatement(
            self,
            ctx: ParaParser.ExpressionStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#expressionStatement.
        """
        ...

    def exitExpressionStatement(
            self,
            ctx: ParaParser.ExpressionStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#expressionStatement.
        """
        ...

    def enterSelectionStatement(
            self,
            ctx: ParaParser.SelectionStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#selectionStatement.
        """
        ...

    def exitSelectionStatement(
            self,
            ctx: ParaParser.SelectionStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#selectionStatement.
        """
        ...

    def enterIterationStatement(
            self,
            ctx: ParaParser.IterationStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#iterationStatement.
        """
        ...

    def exitIterationStatement(
            self,
            ctx: ParaParser.IterationStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#iterationStatement.
        """
        ...

    def enterForCondition(
            self,
            ctx: ParaParser.ForConditionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#forCondition.
        """
        ...

    def exitForCondition(
            self,
            ctx: ParaParser.ForConditionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#forCondition.
        """
        ...

    def enterForDeclaration(
            self,
            ctx: ParaParser.ForDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#forDeclaration.
        """
        ...

    def exitForDeclaration(
            self,
            ctx: ParaParser.ForDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#forDeclaration.
        """
        ...

    def enterForExpression(
            self,
            ctx: ParaParser.ForExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#forExpression.
        """
        ...

    def exitForExpression(
            self,
            ctx: ParaParser.ForExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#forExpression.
        """
        ...

    def enterJumpStatement(
            self,
            ctx: ParaParser.JumpStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#jumpStatement.
        """
        ...

    def exitJumpStatement(
            self,
            ctx: ParaParser.JumpStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#jumpStatement.
        """
        ...

    def enterTranslationUnit(
            self,
            ctx: ParaParser.TranslationUnitContext
    ):
        """
        Enter a parse tree produced by ParaCParser#translationUnit.
        """
        ...

    def exitTranslationUnit(
            self,
            ctx: ParaParser.TranslationUnitContext
    ):
        """
        Exit a parse tree produced by ParaCParser#translationUnit.
        """
        ...

    def enterDeclarationList(
            self,
            ctx: ParaParser.DeclarationListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#declarationList.
        """
        ...

    def exitDeclarationList(
            self,
            ctx: ParaParser.DeclarationListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#declarationList.
        """
        ...
