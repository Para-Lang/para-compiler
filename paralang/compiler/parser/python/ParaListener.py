# Generated from ./Para.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParaParser import ParaParser
else:
    from ParaParser import ParaParser

# This class defines a complete listener for a parse tree produced by ParaParser.
class ParaListener(ParseTreeListener):

    # Enter a parse tree produced by ParaParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:ParaParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:ParaParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#lambdaFunction.
    def enterLambdaFunction(self, ctx:ParaParser.LambdaFunctionContext):
        pass

    # Exit a parse tree produced by ParaParser#lambdaFunction.
    def exitLambdaFunction(self, ctx:ParaParser.LambdaFunctionContext):
        pass


    # Enter a parse tree produced by ParaParser#lambdaBody.
    def enterLambdaBody(self, ctx:ParaParser.LambdaBodyContext):
        pass

    # Exit a parse tree produced by ParaParser#lambdaBody.
    def exitLambdaBody(self, ctx:ParaParser.LambdaBodyContext):
        pass


    # Enter a parse tree produced by ParaParser#expressionLambda.
    def enterExpressionLambda(self, ctx:ParaParser.ExpressionLambdaContext):
        pass

    # Exit a parse tree produced by ParaParser#expressionLambda.
    def exitExpressionLambda(self, ctx:ParaParser.ExpressionLambdaContext):
        pass


    # Enter a parse tree produced by ParaParser#statementLambda.
    def enterStatementLambda(self, ctx:ParaParser.StatementLambdaContext):
        pass

    # Exit a parse tree produced by ParaParser#statementLambda.
    def exitStatementLambda(self, ctx:ParaParser.StatementLambdaContext):
        pass


    # Enter a parse tree produced by ParaParser#postfixExpression.
    def enterPostfixExpression(self, ctx:ParaParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#postfixExpression.
    def exitPostfixExpression(self, ctx:ParaParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:ParaParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by ParaParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:ParaParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by ParaParser#unaryExpression.
    def enterUnaryExpression(self, ctx:ParaParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#unaryExpression.
    def exitUnaryExpression(self, ctx:ParaParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#unaryOperator.
    def enterUnaryOperator(self, ctx:ParaParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by ParaParser#unaryOperator.
    def exitUnaryOperator(self, ctx:ParaParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by ParaParser#castOrConvertExpression.
    def enterCastOrConvertExpression(self, ctx:ParaParser.CastOrConvertExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#castOrConvertExpression.
    def exitCastOrConvertExpression(self, ctx:ParaParser.CastOrConvertExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:ParaParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:ParaParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:ParaParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:ParaParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#shiftExpression.
    def enterShiftExpression(self, ctx:ParaParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#shiftExpression.
    def exitShiftExpression(self, ctx:ParaParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#relationalExpression.
    def enterRelationalExpression(self, ctx:ParaParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#relationalExpression.
    def exitRelationalExpression(self, ctx:ParaParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#equalityExpression.
    def enterEqualityExpression(self, ctx:ParaParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#equalityExpression.
    def exitEqualityExpression(self, ctx:ParaParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#andExpression.
    def enterAndExpression(self, ctx:ParaParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#andExpression.
    def exitAndExpression(self, ctx:ParaParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:ParaParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:ParaParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:ParaParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:ParaParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:ParaParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:ParaParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:ParaParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:ParaParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:ParaParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:ParaParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:ParaParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:ParaParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:ParaParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by ParaParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:ParaParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by ParaParser#expression.
    def enterExpression(self, ctx:ParaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#expression.
    def exitExpression(self, ctx:ParaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#constantExpression.
    def enterConstantExpression(self, ctx:ParaParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#constantExpression.
    def exitConstantExpression(self, ctx:ParaParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#declaration.
    def enterDeclaration(self, ctx:ParaParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#declaration.
    def exitDeclaration(self, ctx:ParaParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:ParaParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by ParaParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:ParaParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by ParaParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:ParaParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:ParaParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:ParaParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by ParaParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:ParaParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by ParaParser#initDeclarator.
    def enterInitDeclarator(self, ctx:ParaParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaParser#initDeclarator.
    def exitInitDeclarator(self, ctx:ParaParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:ParaParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:ParaParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#arraySpecifier.
    def enterArraySpecifier(self, ctx:ParaParser.ArraySpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#arraySpecifier.
    def exitArraySpecifier(self, ctx:ParaParser.ArraySpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:ParaParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:ParaParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:ParaParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:ParaParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#structOrUnion.
    def enterStructOrUnion(self, ctx:ParaParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by ParaParser#structOrUnion.
    def exitStructOrUnion(self, ctx:ParaParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by ParaParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:ParaParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by ParaParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:ParaParser.StructDeclarationListContext):
        pass


    # Enter a parse tree produced by ParaParser#structDeclaration.
    def enterStructDeclaration(self, ctx:ParaParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#structDeclaration.
    def exitStructDeclaration(self, ctx:ParaParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:ParaParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by ParaParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:ParaParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by ParaParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:ParaParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by ParaParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:ParaParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by ParaParser#structDeclarator.
    def enterStructDeclarator(self, ctx:ParaParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaParser#structDeclarator.
    def exitStructDeclarator(self, ctx:ParaParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:ParaParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:ParaParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#enumeratorList.
    def enterEnumeratorList(self, ctx:ParaParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by ParaParser#enumeratorList.
    def exitEnumeratorList(self, ctx:ParaParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by ParaParser#enumerator.
    def enterEnumerator(self, ctx:ParaParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by ParaParser#enumerator.
    def exitEnumerator(self, ctx:ParaParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by ParaParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:ParaParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by ParaParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:ParaParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by ParaParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:ParaParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:ParaParser.AtomicTypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#typeQualifier.
    def enterTypeQualifier(self, ctx:ParaParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by ParaParser#typeQualifier.
    def exitTypeQualifier(self, ctx:ParaParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by ParaParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:ParaParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:ParaParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#alignmentSpecifier.
    def enterAlignmentSpecifier(self, ctx:ParaParser.AlignmentSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#alignmentSpecifier.
    def exitAlignmentSpecifier(self, ctx:ParaParser.AlignmentSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#declarator.
    def enterDeclarator(self, ctx:ParaParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by ParaParser#declarator.
    def exitDeclarator(self, ctx:ParaParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by ParaParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:ParaParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:ParaParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:ParaParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by ParaParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:ParaParser.NestedParenthesesBlockContext):
        pass


    # Enter a parse tree produced by ParaParser#pointer.
    def enterPointer(self, ctx:ParaParser.PointerContext):
        pass

    # Exit a parse tree produced by ParaParser#pointer.
    def exitPointer(self, ctx:ParaParser.PointerContext):
        pass


    # Enter a parse tree produced by ParaParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:ParaParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by ParaParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:ParaParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by ParaParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:ParaParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by ParaParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:ParaParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by ParaParser#parameterList.
    def enterParameterList(self, ctx:ParaParser.ParameterListContext):
        pass

    # Exit a parse tree produced by ParaParser#parameterList.
    def exitParameterList(self, ctx:ParaParser.ParameterListContext):
        pass


    # Enter a parse tree produced by ParaParser#regularParameterDeclaration.
    def enterRegularParameterDeclaration(self, ctx:ParaParser.RegularParameterDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#regularParameterDeclaration.
    def exitRegularParameterDeclaration(self, ctx:ParaParser.RegularParameterDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#abstractParameterDeclaration.
    def enterAbstractParameterDeclaration(self, ctx:ParaParser.AbstractParameterDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#abstractParameterDeclaration.
    def exitAbstractParameterDeclaration(self, ctx:ParaParser.AbstractParameterDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#identifierList.
    def enterIdentifierList(self, ctx:ParaParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by ParaParser#identifierList.
    def exitIdentifierList(self, ctx:ParaParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by ParaParser#typeName.
    def enterTypeName(self, ctx:ParaParser.TypeNameContext):
        pass

    # Exit a parse tree produced by ParaParser#typeName.
    def exitTypeName(self, ctx:ParaParser.TypeNameContext):
        pass


    # Enter a parse tree produced by ParaParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:ParaParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:ParaParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:ParaParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:ParaParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaParser#typedefName.
    def enterTypedefName(self, ctx:ParaParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by ParaParser#typedefName.
    def exitTypedefName(self, ctx:ParaParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by ParaParser#initializer.
    def enterInitializer(self, ctx:ParaParser.InitializerContext):
        pass

    # Exit a parse tree produced by ParaParser#initializer.
    def exitInitializer(self, ctx:ParaParser.InitializerContext):
        pass


    # Enter a parse tree produced by ParaParser#initializerList.
    def enterInitializerList(self, ctx:ParaParser.InitializerListContext):
        pass

    # Exit a parse tree produced by ParaParser#initializerList.
    def exitInitializerList(self, ctx:ParaParser.InitializerListContext):
        pass


    # Enter a parse tree produced by ParaParser#designation.
    def enterDesignation(self, ctx:ParaParser.DesignationContext):
        pass

    # Exit a parse tree produced by ParaParser#designation.
    def exitDesignation(self, ctx:ParaParser.DesignationContext):
        pass


    # Enter a parse tree produced by ParaParser#designatorList.
    def enterDesignatorList(self, ctx:ParaParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by ParaParser#designatorList.
    def exitDesignatorList(self, ctx:ParaParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by ParaParser#designator.
    def enterDesignator(self, ctx:ParaParser.DesignatorContext):
        pass

    # Exit a parse tree produced by ParaParser#designator.
    def exitDesignator(self, ctx:ParaParser.DesignatorContext):
        pass


    # Enter a parse tree produced by ParaParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:ParaParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:ParaParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#statement.
    def enterStatement(self, ctx:ParaParser.StatementContext):
        pass

    # Exit a parse tree produced by ParaParser#statement.
    def exitStatement(self, ctx:ParaParser.StatementContext):
        pass


    # Enter a parse tree produced by ParaParser#labeledStatement.
    def enterLabeledStatement(self, ctx:ParaParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#labeledStatement.
    def exitLabeledStatement(self, ctx:ParaParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#compoundStatement.
    def enterCompoundStatement(self, ctx:ParaParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#compoundStatement.
    def exitCompoundStatement(self, ctx:ParaParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#blockItemList.
    def enterBlockItemList(self, ctx:ParaParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by ParaParser#blockItemList.
    def exitBlockItemList(self, ctx:ParaParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by ParaParser#blockItem.
    def enterBlockItem(self, ctx:ParaParser.BlockItemContext):
        pass

    # Exit a parse tree produced by ParaParser#blockItem.
    def exitBlockItem(self, ctx:ParaParser.BlockItemContext):
        pass


    # Enter a parse tree produced by ParaParser#expressionStatement.
    def enterExpressionStatement(self, ctx:ParaParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#expressionStatement.
    def exitExpressionStatement(self, ctx:ParaParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#tryExceptStatement.
    def enterTryExceptStatement(self, ctx:ParaParser.TryExceptStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#tryExceptStatement.
    def exitTryExceptStatement(self, ctx:ParaParser.TryExceptStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#exceptBlock.
    def enterExceptBlock(self, ctx:ParaParser.ExceptBlockContext):
        pass

    # Exit a parse tree produced by ParaParser#exceptBlock.
    def exitExceptBlock(self, ctx:ParaParser.ExceptBlockContext):
        pass


    # Enter a parse tree produced by ParaParser#finallyBlock.
    def enterFinallyBlock(self, ctx:ParaParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by ParaParser#finallyBlock.
    def exitFinallyBlock(self, ctx:ParaParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by ParaParser#elseBlock.
    def enterElseBlock(self, ctx:ParaParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by ParaParser#elseBlock.
    def exitElseBlock(self, ctx:ParaParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by ParaParser#selectionStatement.
    def enterSelectionStatement(self, ctx:ParaParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#selectionStatement.
    def exitSelectionStatement(self, ctx:ParaParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#iterationStatement.
    def enterIterationStatement(self, ctx:ParaParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#iterationStatement.
    def exitIterationStatement(self, ctx:ParaParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#forCondition.
    def enterForCondition(self, ctx:ParaParser.ForConditionContext):
        pass

    # Exit a parse tree produced by ParaParser#forCondition.
    def exitForCondition(self, ctx:ParaParser.ForConditionContext):
        pass


    # Enter a parse tree produced by ParaParser#forDeclaration.
    def enterForDeclaration(self, ctx:ParaParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#forDeclaration.
    def exitForDeclaration(self, ctx:ParaParser.ForDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#forExpression.
    def enterForExpression(self, ctx:ParaParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#forExpression.
    def exitForExpression(self, ctx:ParaParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#jumpStatement.
    def enterJumpStatement(self, ctx:ParaParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#jumpStatement.
    def exitJumpStatement(self, ctx:ParaParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#compilationUnit.
    def enterCompilationUnit(self, ctx:ParaParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by ParaParser#compilationUnit.
    def exitCompilationUnit(self, ctx:ParaParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by ParaParser#translationUnit.
    def enterTranslationUnit(self, ctx:ParaParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by ParaParser#translationUnit.
    def exitTranslationUnit(self, ctx:ParaParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by ParaParser#externalFunctionDefinition.
    def enterExternalFunctionDefinition(self, ctx:ParaParser.ExternalFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by ParaParser#externalFunctionDefinition.
    def exitExternalFunctionDefinition(self, ctx:ParaParser.ExternalFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by ParaParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:ParaParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:ParaParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#externalExtTaskDefinition.
    def enterExternalExtTaskDefinition(self, ctx:ParaParser.ExternalExtTaskDefinitionContext):
        pass

    # Exit a parse tree produced by ParaParser#externalExtTaskDefinition.
    def exitExternalExtTaskDefinition(self, ctx:ParaParser.ExternalExtTaskDefinitionContext):
        pass


    # Enter a parse tree produced by ParaParser#standardFunctionDefinition.
    def enterStandardFunctionDefinition(self, ctx:ParaParser.StandardFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by ParaParser#standardFunctionDefinition.
    def exitStandardFunctionDefinition(self, ctx:ParaParser.StandardFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by ParaParser#simpleFunctionDefinition.
    def enterSimpleFunctionDefinition(self, ctx:ParaParser.SimpleFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by ParaParser#simpleFunctionDefinition.
    def exitSimpleFunctionDefinition(self, ctx:ParaParser.SimpleFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by ParaParser#functionDeclarationSpecifiers.
    def enterFunctionDeclarationSpecifiers(self, ctx:ParaParser.FunctionDeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by ParaParser#functionDeclarationSpecifiers.
    def exitFunctionDeclarationSpecifiers(self, ctx:ParaParser.FunctionDeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by ParaParser#decoratorSpecifier.
    def enterDecoratorSpecifier(self, ctx:ParaParser.DecoratorSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#decoratorSpecifier.
    def exitDecoratorSpecifier(self, ctx:ParaParser.DecoratorSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#extensionTaskDefinition.
    def enterExtensionTaskDefinition(self, ctx:ParaParser.ExtensionTaskDefinitionContext):
        pass

    # Exit a parse tree produced by ParaParser#extensionTaskDefinition.
    def exitExtensionTaskDefinition(self, ctx:ParaParser.ExtensionTaskDefinitionContext):
        pass


    # Enter a parse tree produced by ParaParser#extensionTaskParameterList.
    def enterExtensionTaskParameterList(self, ctx:ParaParser.ExtensionTaskParameterListContext):
        pass

    # Exit a parse tree produced by ParaParser#extensionTaskParameterList.
    def exitExtensionTaskParameterList(self, ctx:ParaParser.ExtensionTaskParameterListContext):
        pass


    # Enter a parse tree produced by ParaParser#extensionTaskParameter.
    def enterExtensionTaskParameter(self, ctx:ParaParser.ExtensionTaskParameterContext):
        pass

    # Exit a parse tree produced by ParaParser#extensionTaskParameter.
    def exitExtensionTaskParameter(self, ctx:ParaParser.ExtensionTaskParameterContext):
        pass


    # Enter a parse tree produced by ParaParser#declarationList.
    def enterDeclarationList(self, ctx:ParaParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by ParaParser#declarationList.
    def exitDeclarationList(self, ctx:ParaParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by ParaParser#endOfItem.
    def enterEndOfItem(self, ctx:ParaParser.EndOfItemContext):
        pass

    # Exit a parse tree produced by ParaParser#endOfItem.
    def exitEndOfItem(self, ctx:ParaParser.EndOfItemContext):
        pass



del ParaParser