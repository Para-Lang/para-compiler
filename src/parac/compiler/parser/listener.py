# coding=utf-8
""" Listener Class """
from __future__ import annotations
import logging
from os import PathLike
from typing import TYPE_CHECKING, Union

import antlr4

from .python import ParaCListener
from .python import ParaCParser
from ..ctx import FileCompilationContext, ProgramCompilationContext
from ..logic_stream import ParacLogicStream

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    # Assigning the variables to hold the imported classes for easier type
    # hinting and avoiding exceeding the line length
    ExpressionContext = ParaCParser.ExpressionContext
    FunctionDefinitionContext = ParaCParser.FunctionDefinitionContext
    AssignmentExpressionContext = ParaCParser.AssignmentExpressionContext
    CompilationUnitContext = ParaCParser.CompilationUnitContext

__all__ = [
    'Listener'
]


class Listener(ParaCListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaCListener and then define the wanted
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
        self._log_errors_and_warnings: bool = False

    @property
    def logic_stream(self) -> ParacLogicStream:
        """ Stream which stores the logical tokens for the passed file. """
        return self._file_ctx.logic_stream

    @property
    def file_ctx(self) -> FileCompilationContext:
        """ Fetches the file context for this class """
        return self._file_ctx

    async def walk(self, log_errors_and_warnings: bool) -> None:
        """
        Walks through the parsed CompilationUnitContext and listens to the
        events / goes through the tokens.

        This is a non-compile version of walk_and_generate_logic_stream, which
        is only used stand-alone for syntax-checking. This method does not
        exist on the Pre-Processor counterpart, as it is not necessary.

        :param log_errors_and_warnings: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """
        logger.debug(
            "Walking through logic tree and generating the logic stream"
        )
        self._log_errors_and_warnings = log_errors_and_warnings

        walker = antlr4.ParseTreeWalker()
        walker.walk(self, self.antlr4_file_ctx)

    async def walk_and_generate_logic_stream(
            self, log_errors_and_warnings: bool
    ) -> None:
        """
        Walks through the parsed CompilationUnitContext and listens to the
        events / goes through the tokens and generates the logic stream
        for the FileCompilationContext (self.file_ctx)

        The FileCompilationContext can then be used inside the
        CompilationContext to be linked with other files and to finish
        the compilation for the program

        :param log_errors_and_warnings: If set to True errors, warnings and
         info will be logged onto the console using the local logger instance.
         If an exception is raised or error is encountered, it will be reraised
         with the FailedToProcessError.
        """

        # Variable set to signalise that the items should be added to the
        # logic stream
        self._compiling = True
        await self.walk(log_errors_and_warnings)

    # =========================================
    # Beginning of the file
    # =========================================
    def enterCompilationUnit(
            self,
            ctx: ParaCParser.CompilationUnitContext
    ):
        """
        Enter a parse tree produced by ParaCParser#compilationUnit.

        Is the base from where the tree is going to start (starts at the first
        token of the file and ends at the last token)
        """
        logger.debug("Starting file parsing")

    # =========================================
    # End of the file
    # =========================================
    def exitCompilationUnit(
            self,
            ctx: ParaCParser.CompilationUnitContext
    ):
        """
        Exit a parse tree produced by ParaCParser#compilationUnit.

        Is the point where the token stream will end. (EOF excluded)
        """
        logger.debug("Finished file parsing")

    def enterLambdaFunction(
            self,
            ctx: ParaCParser.LambdaFunctionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#lambdaFunction.
        """
        ...

    def exitLambdaFunction(
            self,
            ctx: ParaCParser.LambdaFunctionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#lambdaFunction.
        """
        ...

    def enterLambdaBody(
            self,
            ctx: ParaCParser.LambdaBodyContext
    ):
        """
        Enter a parse tree produced by ParaCParser#lambdaBody.
        """
        ...

    def exitLambdaBody(
            self,
            ctx: ParaCParser.LambdaBodyContext
    ):
        """
        Exit a parse tree produced by ParaCParser#lambdaBody.
        """
        ...

    def enterExpressionLambda(
            self,
            ctx: ParaCParser.ExpressionLambdaContext
    ):
        """
        Enter a parse tree produced by ParaCParser#expressionLambda.
        """
        ...

    def exitExpressionLambda(
            self,
            ctx: ParaCParser.ExpressionLambdaContext
    ):
        """
        Exit a parse tree produced by ParaCParser#expressionLambda.
        """
        ...

    def enterStatementLambda(
            self,
            ctx: ParaCParser.StatementLambdaContext
    ):
        """
        Enter a parse tree produced by ParaCParser#statementLambda.
        """
        ...

    def exitStatementLambda(
            self,
            ctx: ParaCParser.StatementLambdaContext
    ):
        """
        Exit a parse tree produced by ParaCParser#statementLambda.
        """
        ...

    def enterCastOrConvertExpression(
            self,
            ctx: ParaCParser.CastOrConvertExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#castOrConvertExpression.
        """
        ...

    def exitCastOrConvertExpression(
            self,
            ctx: ParaCParser.CastOrConvertExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#castOrConvertExpression.
        """
        ...

    def enterRegularParameterDeclaration(
            self,
            ctx: ParaCParser.RegularParameterDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#regularDeclaration.
        """
        ...

    def exitRegularParameterDeclaration(
            self,
            ctx: ParaCParser.RegularParameterDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#regularDeclaration.
        """
        ...

    def enterAbstractParameterDeclaration(
            self,
            ctx: ParaCParser.AbstractParameterDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#abstractDeclaration.
        """
        ...

    def exitAbstractParameterDeclaration(
            self,
            ctx: ParaCParser.AbstractParameterDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#abstractDeclaration.
        """
        ...

    def enterExternalFunctionDefinition(
            self,
            ctx: ParaCParser.ExternalFunctionDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#externalFunctionDefinition.
        """
        ...

    def exitExternalFunctionDefinition(
            self,
            ctx: ParaCParser.ExternalFunctionDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#externalFunctionDefinition.
        """
        ...

    def enterExternalDeclaration(
            self,
            ctx: ParaCParser.ExternalDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#externalDeclaration.
        """
        ...

    def exitExternalDeclaration(
            self,
            ctx: ParaCParser.ExternalDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#externalDeclaration.
        """
        ...

    def enterExternalExtTaskDefinition(
            self,
            ctx: ParaCParser.ExternalExtTaskDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#externalExtTaskDefinition.
        """
        ...

    def exitExternalExtTaskDefinition(
            self,
            ctx: ParaCParser.ExternalExtTaskDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#externalExtTaskDefinition.
        """
        ...

    def enterStandardFunctionDefinition(
            self,
            ctx: ParaCParser.StandardFunctionDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#standardFunctionDefinition.
        """
        ...

    def exitStandardFunctionDefinition(
            self,
            ctx: ParaCParser.StandardFunctionDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#standardFunctionDefinition.
        """
        ...

    def enterSimpleFunctionDefinition(
            self,
            ctx: ParaCParser.SimpleFunctionDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#simpleFunctionDefinition.
        """
        ...

    def exitSimpleFunctionDefinition(
            self,
            ctx: ParaCParser.SimpleFunctionDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#simpleFunctionDefinition.
        """
        ...

    def enterFunctionDeclarationSpecifiers(
            self,
            ctx: ParaCParser.FunctionDeclarationSpecifiersContext
    ):
        """
        Enter a parse tree produced by
        ParaCParser#functionDeclarationSpecifiers.
        """
        ...

    def exitFunctionDeclarationSpecifiers(
            self,
            ctx: ParaCParser.FunctionDeclarationSpecifiersContext
    ):
        """
        Exit a parse tree produced by
        ParaCParser#functionDeclarationSpecifiers.
        """
        ...

    def enterDecoratorSpecifier(
            self,
            ctx: ParaCParser.DecoratorSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#decoratorSpecifier.
        """
        ...

    def exitDecoratorSpecifier(
            self,
            ctx: ParaCParser.DecoratorSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#decoratorSpecifier.
        """
        ...

    def enterExtensionTaskDefinition(
            self,
            ctx: ParaCParser.ExtensionTaskDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#extensionTaskDefinition.
        """
        ...

    def exitExtensionTaskDefinition(
            self,
            ctx: ParaCParser.ExtensionTaskDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#extensionTaskDefinition.
        """
        ...

    def enterExtensionTaskParameterList(
            self,
            ctx: ParaCParser.ExtensionTaskParameterListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#extensionTaskParameterList.
        """
        ...

    def exitExtensionTaskParameterList(
            self,
            ctx: ParaCParser.ExtensionTaskParameterListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#extensionTaskParameterList.
        """
        ...

    def enterExtensionTaskParameter(
            self,
            ctx: ParaCParser.ExtensionTaskParameterContext
    ):
        """
        Enter a parse tree produced by ParaCParser#extensionTaskParameter.
        """
        ...

    def exitExtensionTaskParameter(
            self,
            ctx: ParaCParser.ExtensionTaskParameterContext
    ):
        """
        Exit a parse tree produced by ParaCParser#extensionTaskParameter.
        """
        ...

    def enterTryExceptStatement(
            self,
            ctx: ParaCParser.TryExceptStatementContext
    ):
        """
        Enter a parse tree produced by ParaCParser#tryExceptStatement.
        """
        ...

    def exitTryExceptStatement(
            self,
            ctx: ParaCParser.TryExceptStatementContext
    ):
        """
        Exit a parse tree produced by ParaCParser#tryExceptStatement.
        """
        ...

    def enterExceptBlock(
            self,
            ctx: ParaCParser.ExceptBlockContext
    ):
        """
        Enter a parse tree produced by ParaCParser#exceptBlock.
        """
        ...

    def exitExceptBlock(
            self,
            ctx: ParaCParser.ExceptBlockContext
    ):
        """
        Exit a parse tree produced by ParaCParser#exceptBlock.
        """
        ...

    def enterFinallyBlock(
            self,
            ctx: ParaCParser.FinallyBlockContext
    ):
        """
        Enter a parse tree produced by ParaCParser#finallyBlock.
        """
        ...

    def exitFinallyBlock(
            self,
            ctx: ParaCParser.FinallyBlockContext
    ):
        """
        Exit a parse tree produced by ParaCParser#finallyBlock.
        """
        ...

    def enterElseBlock(
            self,
            ctx: ParaCParser.ElseBlockContext
    ):
        """
        Enter a parse tree produced by ParaCParser#elseBlock.
        """
        ...

    def exitElseBlock(
            self,
            ctx: ParaCParser.ElseBlockContext
    ):
        """
        Exit a parse tree produced by ParaCParser#elseBlock.
        """
        ...

    def enterPrimaryExpression(
            self,
            ctx: ParaCParser.PrimaryExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#primaryExpression.
        """
        ...

    def exitPrimaryExpression(
            self,
            ctx: ParaCParser.PrimaryExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#primaryExpression.
        """
        ...

    def enterPostfixExpression(
            self,
            ctx: ParaCParser.PostfixExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#postfixExpression.
        """
        ...

    def exitPostfixExpression(
            self,
            ctx: ParaCParser.PostfixExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#postfixExpression.
        """
        ...

    def enterArgumentExpressionList(
            self,
            ctx: ParaCParser.ArgumentExpressionListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#argumentExpressionList.
        """
        ...

    def exitArgumentExpressionList(
            self,
            ctx: ParaCParser.ArgumentExpressionListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#argumentExpressionList.
        """
        ...

    def enterUnaryExpression(
            self,
            ctx: ParaCParser.UnaryExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#unaryExpression.
        """
        ...

    def exitUnaryExpression(
            self,
            ctx: ParaCParser.UnaryExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#unaryExpression.
        """
        ...

    def enterUnaryOperator(
            self,
            ctx: ParaCParser.UnaryOperatorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#unaryOperator.
        """
        ...

    def exitUnaryOperator(
            self,
            ctx: ParaCParser.UnaryOperatorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#unaryOperator.
        """
        ...

    def enterMultiplicativeExpression(
            self,
            ctx: ParaCParser.MultiplicativeExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#multiplicativeExpression.
        """
        ...

    def exitMultiplicativeExpression(
            self,
            ctx: ParaCParser.MultiplicativeExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#multiplicativeExpression.
        """
        ...

    def enterAdditiveExpression(
            self,
            ctx: ParaCParser.AdditiveExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#additiveExpression.
        """
        ...

    def exitAdditiveExpression(
            self,
            ctx: ParaCParser.AdditiveExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#additiveExpression.
        """
        ...

    def enterShiftExpression(
            self,
            ctx: ParaCParser.ShiftExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#shiftExpression.
        """
        ...

    def exitShiftExpression(
            self,
            ctx: ParaCParser.ShiftExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#shiftExpression.
        """
        ...

    def enterRelationalExpression(
            self,
            ctx: ParaCParser.RelationalExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#relationalExpression.
        """
        ...

    def exitRelationalExpression(
            self,
            ctx: ParaCParser.RelationalExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#relationalExpression.
        """
        ...

    def enterEqualityExpression(
            self,
            ctx: ParaCParser.EqualityExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#equalityExpression.
        """
        ...

    def exitEqualityExpression(
            self,
            ctx: ParaCParser.EqualityExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#equalityExpression.
        """
        ...

    def enterAndExpression(
            self,
            ctx: ParaCParser.AndExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#andExpression.
        """
        ...

    def exitAndExpression(
            self,
            ctx: ParaCParser.AndExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#andExpression.
        """
        ...

    def enterExclusiveOrExpression(
            self,
            ctx: ParaCParser.ExclusiveOrExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#exclusiveOrExpression.
        """
        ...

    def exitExclusiveOrExpression(
            self,
            ctx: ParaCParser.ExclusiveOrExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#exclusiveOrExpression.
        """
        ...

    def enterInclusiveOrExpression(
            self,
            ctx: ParaCParser.InclusiveOrExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#inclusiveOrExpression.
        """
        ...

    def exitInclusiveOrExpression(
            self,
            ctx: ParaCParser.InclusiveOrExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#inclusiveOrExpression.
        """
        ...

    def enterLogicalAndExpression(
            self,
            ctx: ParaCParser.LogicalAndExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#logicalAndExpression.
        """
        ...

    def exitLogicalAndExpression(
            self,
            ctx: ParaCParser.LogicalAndExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#logicalAndExpression.
        """
        ...

    def enterLogicalOrExpression(
            self,
            ctx: ParaCParser.LogicalOrExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#logicalOrExpression.
        """
        ...

    def exitLogicalOrExpression(
            self,
            ctx: ParaCParser.LogicalOrExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#logicalOrExpression.
        """
        ...

    def enterConditionalExpression(
            self,
            ctx: ParaCParser.ConditionalExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#conditionalExpression.
        """
        ...

    def exitConditionalExpression(
            self,
            ctx: ParaCParser.ConditionalExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#conditionalExpression.
        """
        ...

    def enterAssignmentExpression(
            self,
            ctx: ParaCParser.AssignmentExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#assignmentExpression.
        """
        ...

    def exitAssignmentExpression(
            self,
            ctx: ParaCParser.AssignmentExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#assignmentExpression.
        """
        ...

    def enterAssignmentOperator(
            self,
            ctx: ParaCParser.AssignmentOperatorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#assignmentOperator.
        """
        ...

    def exitAssignmentOperator(
            self,
            ctx: ParaCParser.AssignmentOperatorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#assignmentOperator.
        """
        ...

    def enterExpression(
            self,
            ctx: ParaCParser.ExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#expression.
        """
        ...

    def exitExpression(
            self,
            ctx: ParaCParser.ExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#expression.
        """
        ...

    def enterConstantExpression(
            self,
            ctx: ParaCParser.ConstantExpressionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#constantExpression.
        """
        ...

    def exitConstantExpression(
            self,
            ctx: ParaCParser.ConstantExpressionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#constantExpression.
        """
        ...

    def enterDeclaration(
            self,
            ctx: ParaCParser.DeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#declaration.
        """
        ...

    def exitDeclaration(
            self,
            ctx: ParaCParser.DeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#declaration.
        """
        ...

    def enterDeclarationSpecifiers(
            self,
            ctx: ParaCParser.DeclarationSpecifiersContext
    ):
        """
        Enter a parse tree produced by ParaCParser#declarationSpecifiers.
        """
        ...

    def exitDeclarationSpecifiers(
            self,
            ctx: ParaCParser.DeclarationSpecifiersContext
    ):
        """
        Exit a parse tree produced by ParaCParser#declarationSpecifiers.
        """
        ...

    def enterDeclarationSpecifier(
            self,
            ctx: ParaCParser.DeclarationSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#declarationSpecifier.
        """
        ...

    def exitDeclarationSpecifier(
            self,
            ctx: ParaCParser.DeclarationSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#declarationSpecifier.
        """
        ...

    def enterInitDeclaratorList(
            self,
            ctx: ParaCParser.InitDeclaratorListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#initDeclaratorList.
        """
        ...

    def exitInitDeclaratorList(
            self,
            ctx: ParaCParser.InitDeclaratorListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#initDeclaratorList.
        """
        ...

    def enterInitDeclarator(
            self,
            ctx: ParaCParser.InitDeclaratorContext
    ):
        """
        Enter a parse tree produced by ParaCParser#initDeclarator.
        """
        ...

    def exitInitDeclarator(
            self,
            ctx: ParaCParser.InitDeclaratorContext
    ):
        """
        Exit a parse tree produced by ParaCParser#initDeclarator.
        """
        ...

    def enterStorageClassSpecifier(
            self,
            ctx: ParaCParser.StorageClassSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#storageClassSpecifier.
        """
        ...

    def exitStorageClassSpecifier(
            self,
            ctx: ParaCParser.StorageClassSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#storageClassSpecifier.
        """
        ...

    def enterTypeSpecifier(
            self,
            ctx: ParaCParser.TypeSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#typeSpecifier.
        """
        ...

    def exitTypeSpecifier(
            self,
            ctx: ParaCParser.TypeSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#typeSpecifier.
        """
        ...

    def enterStructOrUnionSpecifier(
            self,
            ctx: ParaCParser.StructOrUnionSpecifierContext
    ):
        """
        Enter a parse tree produced by ParaCParser#structOrUnionSpecifier.
        """
        ...

    def exitStructOrUnionSpecifier(
            self,
            ctx: ParaCParser.StructOrUnionSpecifierContext
    ):
        """
        Exit a parse tree produced by ParaCParser#structOrUnionSpecifier.
        """
        ...

    def enterStructOrUnion(
            self,
            ctx: ParaCParser.StructOrUnionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#structOrUnion.
        """
        ...

    def exitStructOrUnion(
            self,
            ctx: ParaCParser.StructOrUnionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#structOrUnion.
        """
        ...

    def enterStructDeclarationList(
            self,
            ctx: ParaCParser.StructDeclarationListContext
    ):
        """
        Enter a parse tree produced by ParaCParser#structDeclarationList.
        """
        ...

    def exitStructDeclarationList(
            self,
            ctx: ParaCParser.StructDeclarationListContext
    ):
        """
        Exit a parse tree produced by ParaCParser#structDeclarationList.
        """
        ...

    def enterStructDeclaration(
            self,
            ctx: ParaCParser.StructDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#structDeclaration.
        """
        ...

    def exitStructDeclaration(
            self,
            ctx: ParaCParser.StructDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#structDeclaration.
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
