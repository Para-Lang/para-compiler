# Generated from ./grammar/ParaC.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParaCParser import ParaCParser
else:
    from ParaCParser import ParaCParser

# This class defines a complete listener for a parse tree produced by ParaCParser.
class ParaCListener(ParseTreeListener):

    # Enter a parse tree produced by ParaCParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:ParaCParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:ParaCParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#lambdaFunction.
    def enterLambdaFunction(self, ctx:ParaCParser.LambdaFunctionContext):
        pass

    # Exit a parse tree produced by ParaCParser#lambdaFunction.
    def exitLambdaFunction(self, ctx:ParaCParser.LambdaFunctionContext):
        pass


    # Enter a parse tree produced by ParaCParser#lambdaBody.
    def enterLambdaBody(self, ctx:ParaCParser.LambdaBodyContext):
        pass

    # Exit a parse tree produced by ParaCParser#lambdaBody.
    def exitLambdaBody(self, ctx:ParaCParser.LambdaBodyContext):
        pass


    # Enter a parse tree produced by ParaCParser#expressionLambda.
    def enterExpressionLambda(self, ctx:ParaCParser.ExpressionLambdaContext):
        pass

    # Exit a parse tree produced by ParaCParser#expressionLambda.
    def exitExpressionLambda(self, ctx:ParaCParser.ExpressionLambdaContext):
        pass


    # Enter a parse tree produced by ParaCParser#statementLambda.
    def enterStatementLambda(self, ctx:ParaCParser.StatementLambdaContext):
        pass

    # Exit a parse tree produced by ParaCParser#statementLambda.
    def exitStatementLambda(self, ctx:ParaCParser.StatementLambdaContext):
        pass


    # Enter a parse tree produced by ParaCParser#postfixExpression.
    def enterPostfixExpression(self, ctx:ParaCParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#postfixExpression.
    def exitPostfixExpression(self, ctx:ParaCParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:ParaCParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by ParaCParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:ParaCParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by ParaCParser#unaryExpression.
    def enterUnaryExpression(self, ctx:ParaCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#unaryExpression.
    def exitUnaryExpression(self, ctx:ParaCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#unaryOperator.
    def enterUnaryOperator(self, ctx:ParaCParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by ParaCParser#unaryOperator.
    def exitUnaryOperator(self, ctx:ParaCParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by ParaCParser#castOrConvertExpression.
    def enterCastOrConvertExpression(self, ctx:ParaCParser.CastOrConvertExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#castOrConvertExpression.
    def exitCastOrConvertExpression(self, ctx:ParaCParser.CastOrConvertExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:ParaCParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:ParaCParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:ParaCParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:ParaCParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#shiftExpression.
    def enterShiftExpression(self, ctx:ParaCParser.ShiftExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#shiftExpression.
    def exitShiftExpression(self, ctx:ParaCParser.ShiftExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#relationalExpression.
    def enterRelationalExpression(self, ctx:ParaCParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#relationalExpression.
    def exitRelationalExpression(self, ctx:ParaCParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#equalityExpression.
    def enterEqualityExpression(self, ctx:ParaCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#equalityExpression.
    def exitEqualityExpression(self, ctx:ParaCParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#andExpression.
    def enterAndExpression(self, ctx:ParaCParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#andExpression.
    def exitAndExpression(self, ctx:ParaCParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:ParaCParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:ParaCParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:ParaCParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:ParaCParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:ParaCParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:ParaCParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:ParaCParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:ParaCParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:ParaCParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:ParaCParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:ParaCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:ParaCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:ParaCParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by ParaCParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:ParaCParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by ParaCParser#expression.
    def enterExpression(self, ctx:ParaCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#expression.
    def exitExpression(self, ctx:ParaCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#constantExpression.
    def enterConstantExpression(self, ctx:ParaCParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#constantExpression.
    def exitConstantExpression(self, ctx:ParaCParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#declaration.
    def enterDeclaration(self, ctx:ParaCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ParaCParser#declaration.
    def exitDeclaration(self, ctx:ParaCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ParaCParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:ParaCParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by ParaCParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:ParaCParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by ParaCParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:ParaCParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:ParaCParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:ParaCParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by ParaCParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:ParaCParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by ParaCParser#initDeclarator.
    def enterInitDeclarator(self, ctx:ParaCParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaCParser#initDeclarator.
    def exitInitDeclarator(self, ctx:ParaCParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaCParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:ParaCParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:ParaCParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#arraySpecifier.
    def enterArraySpecifier(self, ctx:ParaCParser.ArraySpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#arraySpecifier.
    def exitArraySpecifier(self, ctx:ParaCParser.ArraySpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:ParaCParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:ParaCParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#structOrUnionSpecifier.
    def enterStructOrUnionSpecifier(self, ctx:ParaCParser.StructOrUnionSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#structOrUnionSpecifier.
    def exitStructOrUnionSpecifier(self, ctx:ParaCParser.StructOrUnionSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#structOrUnion.
    def enterStructOrUnion(self, ctx:ParaCParser.StructOrUnionContext):
        pass

    # Exit a parse tree produced by ParaCParser#structOrUnion.
    def exitStructOrUnion(self, ctx:ParaCParser.StructOrUnionContext):
        pass


    # Enter a parse tree produced by ParaCParser#structDeclarationList.
    def enterStructDeclarationList(self, ctx:ParaCParser.StructDeclarationListContext):
        pass

    # Exit a parse tree produced by ParaCParser#structDeclarationList.
    def exitStructDeclarationList(self, ctx:ParaCParser.StructDeclarationListContext):
        pass


    # Enter a parse tree produced by ParaCParser#structDeclaration.
    def enterStructDeclaration(self, ctx:ParaCParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by ParaCParser#structDeclaration.
    def exitStructDeclaration(self, ctx:ParaCParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by ParaCParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:ParaCParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by ParaCParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:ParaCParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by ParaCParser#structDeclaratorList.
    def enterStructDeclaratorList(self, ctx:ParaCParser.StructDeclaratorListContext):
        pass

    # Exit a parse tree produced by ParaCParser#structDeclaratorList.
    def exitStructDeclaratorList(self, ctx:ParaCParser.StructDeclaratorListContext):
        pass


    # Enter a parse tree produced by ParaCParser#structDeclarator.
    def enterStructDeclarator(self, ctx:ParaCParser.StructDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaCParser#structDeclarator.
    def exitStructDeclarator(self, ctx:ParaCParser.StructDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaCParser#enumSpecifier.
    def enterEnumSpecifier(self, ctx:ParaCParser.EnumSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#enumSpecifier.
    def exitEnumSpecifier(self, ctx:ParaCParser.EnumSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#enumeratorList.
    def enterEnumeratorList(self, ctx:ParaCParser.EnumeratorListContext):
        pass

    # Exit a parse tree produced by ParaCParser#enumeratorList.
    def exitEnumeratorList(self, ctx:ParaCParser.EnumeratorListContext):
        pass


    # Enter a parse tree produced by ParaCParser#enumerator.
    def enterEnumerator(self, ctx:ParaCParser.EnumeratorContext):
        pass

    # Exit a parse tree produced by ParaCParser#enumerator.
    def exitEnumerator(self, ctx:ParaCParser.EnumeratorContext):
        pass


    # Enter a parse tree produced by ParaCParser#enumerationConstant.
    def enterEnumerationConstant(self, ctx:ParaCParser.EnumerationConstantContext):
        pass

    # Exit a parse tree produced by ParaCParser#enumerationConstant.
    def exitEnumerationConstant(self, ctx:ParaCParser.EnumerationConstantContext):
        pass


    # Enter a parse tree produced by ParaCParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:ParaCParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:ParaCParser.AtomicTypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#typeQualifier.
    def enterTypeQualifier(self, ctx:ParaCParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#typeQualifier.
    def exitTypeQualifier(self, ctx:ParaCParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#functionSpecifier.
    def enterFunctionSpecifier(self, ctx:ParaCParser.FunctionSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#functionSpecifier.
    def exitFunctionSpecifier(self, ctx:ParaCParser.FunctionSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#alignmentSpecifier.
    def enterAlignmentSpecifier(self, ctx:ParaCParser.AlignmentSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#alignmentSpecifier.
    def exitAlignmentSpecifier(self, ctx:ParaCParser.AlignmentSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#declarator.
    def enterDeclarator(self, ctx:ParaCParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by ParaCParser#declarator.
    def exitDeclarator(self, ctx:ParaCParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by ParaCParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:ParaCParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaCParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:ParaCParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaCParser#nestedParenthesesBlock.
    def enterNestedParenthesesBlock(self, ctx:ParaCParser.NestedParenthesesBlockContext):
        pass

    # Exit a parse tree produced by ParaCParser#nestedParenthesesBlock.
    def exitNestedParenthesesBlock(self, ctx:ParaCParser.NestedParenthesesBlockContext):
        pass


    # Enter a parse tree produced by ParaCParser#pointer.
    def enterPointer(self, ctx:ParaCParser.PointerContext):
        pass

    # Exit a parse tree produced by ParaCParser#pointer.
    def exitPointer(self, ctx:ParaCParser.PointerContext):
        pass


    # Enter a parse tree produced by ParaCParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:ParaCParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by ParaCParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:ParaCParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by ParaCParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:ParaCParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by ParaCParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:ParaCParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by ParaCParser#parameterList.
    def enterParameterList(self, ctx:ParaCParser.ParameterListContext):
        pass

    # Exit a parse tree produced by ParaCParser#parameterList.
    def exitParameterList(self, ctx:ParaCParser.ParameterListContext):
        pass


    # Enter a parse tree produced by ParaCParser#regularParameterDeclaration.
    def enterRegularParameterDeclaration(self, ctx:ParaCParser.RegularParameterDeclarationContext):
        pass

    # Exit a parse tree produced by ParaCParser#regularParameterDeclaration.
    def exitRegularParameterDeclaration(self, ctx:ParaCParser.RegularParameterDeclarationContext):
        pass


    # Enter a parse tree produced by ParaCParser#abstractParameterDeclaration.
    def enterAbstractParameterDeclaration(self, ctx:ParaCParser.AbstractParameterDeclarationContext):
        pass

    # Exit a parse tree produced by ParaCParser#abstractParameterDeclaration.
    def exitAbstractParameterDeclaration(self, ctx:ParaCParser.AbstractParameterDeclarationContext):
        pass


    # Enter a parse tree produced by ParaCParser#identifierList.
    def enterIdentifierList(self, ctx:ParaCParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by ParaCParser#identifierList.
    def exitIdentifierList(self, ctx:ParaCParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by ParaCParser#typeName.
    def enterTypeName(self, ctx:ParaCParser.TypeNameContext):
        pass

    # Exit a parse tree produced by ParaCParser#typeName.
    def exitTypeName(self, ctx:ParaCParser.TypeNameContext):
        pass


    # Enter a parse tree produced by ParaCParser#abstractDeclarator.
    def enterAbstractDeclarator(self, ctx:ParaCParser.AbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaCParser#abstractDeclarator.
    def exitAbstractDeclarator(self, ctx:ParaCParser.AbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaCParser#directAbstractDeclarator.
    def enterDirectAbstractDeclarator(self, ctx:ParaCParser.DirectAbstractDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaCParser#directAbstractDeclarator.
    def exitDirectAbstractDeclarator(self, ctx:ParaCParser.DirectAbstractDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaCParser#typedefName.
    def enterTypedefName(self, ctx:ParaCParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by ParaCParser#typedefName.
    def exitTypedefName(self, ctx:ParaCParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by ParaCParser#initializer.
    def enterInitializer(self, ctx:ParaCParser.InitializerContext):
        pass

    # Exit a parse tree produced by ParaCParser#initializer.
    def exitInitializer(self, ctx:ParaCParser.InitializerContext):
        pass


    # Enter a parse tree produced by ParaCParser#initializerList.
    def enterInitializerList(self, ctx:ParaCParser.InitializerListContext):
        pass

    # Exit a parse tree produced by ParaCParser#initializerList.
    def exitInitializerList(self, ctx:ParaCParser.InitializerListContext):
        pass


    # Enter a parse tree produced by ParaCParser#designation.
    def enterDesignation(self, ctx:ParaCParser.DesignationContext):
        pass

    # Exit a parse tree produced by ParaCParser#designation.
    def exitDesignation(self, ctx:ParaCParser.DesignationContext):
        pass


    # Enter a parse tree produced by ParaCParser#designatorList.
    def enterDesignatorList(self, ctx:ParaCParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by ParaCParser#designatorList.
    def exitDesignatorList(self, ctx:ParaCParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by ParaCParser#designator.
    def enterDesignator(self, ctx:ParaCParser.DesignatorContext):
        pass

    # Exit a parse tree produced by ParaCParser#designator.
    def exitDesignator(self, ctx:ParaCParser.DesignatorContext):
        pass


    # Enter a parse tree produced by ParaCParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:ParaCParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by ParaCParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:ParaCParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by ParaCParser#statement.
    def enterStatement(self, ctx:ParaCParser.StatementContext):
        pass

    # Exit a parse tree produced by ParaCParser#statement.
    def exitStatement(self, ctx:ParaCParser.StatementContext):
        pass


    # Enter a parse tree produced by ParaCParser#labeledStatement.
    def enterLabeledStatement(self, ctx:ParaCParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by ParaCParser#labeledStatement.
    def exitLabeledStatement(self, ctx:ParaCParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by ParaCParser#compoundStatement.
    def enterCompoundStatement(self, ctx:ParaCParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by ParaCParser#compoundStatement.
    def exitCompoundStatement(self, ctx:ParaCParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by ParaCParser#blockItemList.
    def enterBlockItemList(self, ctx:ParaCParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by ParaCParser#blockItemList.
    def exitBlockItemList(self, ctx:ParaCParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by ParaCParser#blockItem.
    def enterBlockItem(self, ctx:ParaCParser.BlockItemContext):
        pass

    # Exit a parse tree produced by ParaCParser#blockItem.
    def exitBlockItem(self, ctx:ParaCParser.BlockItemContext):
        pass


    # Enter a parse tree produced by ParaCParser#expressionStatement.
    def enterExpressionStatement(self, ctx:ParaCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by ParaCParser#expressionStatement.
    def exitExpressionStatement(self, ctx:ParaCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by ParaCParser#tryExceptStatement.
    def enterTryExceptStatement(self, ctx:ParaCParser.TryExceptStatementContext):
        pass

    # Exit a parse tree produced by ParaCParser#tryExceptStatement.
    def exitTryExceptStatement(self, ctx:ParaCParser.TryExceptStatementContext):
        pass


    # Enter a parse tree produced by ParaCParser#exceptBlock.
    def enterExceptBlock(self, ctx:ParaCParser.ExceptBlockContext):
        pass

    # Exit a parse tree produced by ParaCParser#exceptBlock.
    def exitExceptBlock(self, ctx:ParaCParser.ExceptBlockContext):
        pass


    # Enter a parse tree produced by ParaCParser#finallyBlock.
    def enterFinallyBlock(self, ctx:ParaCParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by ParaCParser#finallyBlock.
    def exitFinallyBlock(self, ctx:ParaCParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by ParaCParser#elseBlock.
    def enterElseBlock(self, ctx:ParaCParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by ParaCParser#elseBlock.
    def exitElseBlock(self, ctx:ParaCParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by ParaCParser#selectionStatement.
    def enterSelectionStatement(self, ctx:ParaCParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by ParaCParser#selectionStatement.
    def exitSelectionStatement(self, ctx:ParaCParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by ParaCParser#iterationStatement.
    def enterIterationStatement(self, ctx:ParaCParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by ParaCParser#iterationStatement.
    def exitIterationStatement(self, ctx:ParaCParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by ParaCParser#forCondition.
    def enterForCondition(self, ctx:ParaCParser.ForConditionContext):
        pass

    # Exit a parse tree produced by ParaCParser#forCondition.
    def exitForCondition(self, ctx:ParaCParser.ForConditionContext):
        pass


    # Enter a parse tree produced by ParaCParser#forDeclaration.
    def enterForDeclaration(self, ctx:ParaCParser.ForDeclarationContext):
        pass

    # Exit a parse tree produced by ParaCParser#forDeclaration.
    def exitForDeclaration(self, ctx:ParaCParser.ForDeclarationContext):
        pass


    # Enter a parse tree produced by ParaCParser#forExpression.
    def enterForExpression(self, ctx:ParaCParser.ForExpressionContext):
        pass

    # Exit a parse tree produced by ParaCParser#forExpression.
    def exitForExpression(self, ctx:ParaCParser.ForExpressionContext):
        pass


    # Enter a parse tree produced by ParaCParser#jumpStatement.
    def enterJumpStatement(self, ctx:ParaCParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by ParaCParser#jumpStatement.
    def exitJumpStatement(self, ctx:ParaCParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by ParaCParser#compilationUnit.
    def enterCompilationUnit(self, ctx:ParaCParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by ParaCParser#compilationUnit.
    def exitCompilationUnit(self, ctx:ParaCParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by ParaCParser#translationUnit.
    def enterTranslationUnit(self, ctx:ParaCParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by ParaCParser#translationUnit.
    def exitTranslationUnit(self, ctx:ParaCParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by ParaCParser#externalFunctionDefinition.
    def enterExternalFunctionDefinition(self, ctx:ParaCParser.ExternalFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by ParaCParser#externalFunctionDefinition.
    def exitExternalFunctionDefinition(self, ctx:ParaCParser.ExternalFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by ParaCParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:ParaCParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by ParaCParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:ParaCParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by ParaCParser#externalExtTaskDefinition.
    def enterExternalExtTaskDefinition(self, ctx:ParaCParser.ExternalExtTaskDefinitionContext):
        pass

    # Exit a parse tree produced by ParaCParser#externalExtTaskDefinition.
    def exitExternalExtTaskDefinition(self, ctx:ParaCParser.ExternalExtTaskDefinitionContext):
        pass


    # Enter a parse tree produced by ParaCParser#standardFunctionDefinition.
    def enterStandardFunctionDefinition(self, ctx:ParaCParser.StandardFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by ParaCParser#standardFunctionDefinition.
    def exitStandardFunctionDefinition(self, ctx:ParaCParser.StandardFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by ParaCParser#simpleFunctionDefinition.
    def enterSimpleFunctionDefinition(self, ctx:ParaCParser.SimpleFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by ParaCParser#simpleFunctionDefinition.
    def exitSimpleFunctionDefinition(self, ctx:ParaCParser.SimpleFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by ParaCParser#functionDeclarationSpecifiers.
    def enterFunctionDeclarationSpecifiers(self, ctx:ParaCParser.FunctionDeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by ParaCParser#functionDeclarationSpecifiers.
    def exitFunctionDeclarationSpecifiers(self, ctx:ParaCParser.FunctionDeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by ParaCParser#decoratorSpecifier.
    def enterDecoratorSpecifier(self, ctx:ParaCParser.DecoratorSpecifierContext):
        pass

    # Exit a parse tree produced by ParaCParser#decoratorSpecifier.
    def exitDecoratorSpecifier(self, ctx:ParaCParser.DecoratorSpecifierContext):
        pass


    # Enter a parse tree produced by ParaCParser#extensionTaskDefinition.
    def enterExtensionTaskDefinition(self, ctx:ParaCParser.ExtensionTaskDefinitionContext):
        pass

    # Exit a parse tree produced by ParaCParser#extensionTaskDefinition.
    def exitExtensionTaskDefinition(self, ctx:ParaCParser.ExtensionTaskDefinitionContext):
        pass


    # Enter a parse tree produced by ParaCParser#extensionTaskParameterList.
    def enterExtensionTaskParameterList(self, ctx:ParaCParser.ExtensionTaskParameterListContext):
        pass

    # Exit a parse tree produced by ParaCParser#extensionTaskParameterList.
    def exitExtensionTaskParameterList(self, ctx:ParaCParser.ExtensionTaskParameterListContext):
        pass


    # Enter a parse tree produced by ParaCParser#extensionTaskParameter.
    def enterExtensionTaskParameter(self, ctx:ParaCParser.ExtensionTaskParameterContext):
        pass

    # Exit a parse tree produced by ParaCParser#extensionTaskParameter.
    def exitExtensionTaskParameter(self, ctx:ParaCParser.ExtensionTaskParameterContext):
        pass


    # Enter a parse tree produced by ParaCParser#declarationList.
    def enterDeclarationList(self, ctx:ParaCParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by ParaCParser#declarationList.
    def exitDeclarationList(self, ctx:ParaCParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by ParaCParser#endOfItem.
    def enterEndOfItem(self, ctx:ParaCParser.EndOfItemContext):
        pass

    # Exit a parse tree produced by ParaCParser#endOfItem.
    def exitEndOfItem(self, ctx:ParaCParser.EndOfItemContext):
        pass



del ParaCParser