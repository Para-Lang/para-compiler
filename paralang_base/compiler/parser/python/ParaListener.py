# Generated from ./Para.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ParaParser import ParaParser
else:
    from ParaParser import ParaParser

# This class defines a complete listener for a parse tree produced by ParaParser.
class ParaListener(ParseTreeListener):

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


    # Enter a parse tree produced by ParaParser#externalDynamicImport.
    def enterExternalDynamicImport(self, ctx:ParaParser.ExternalDynamicImportContext):
        pass

    # Exit a parse tree produced by ParaParser#externalDynamicImport.
    def exitExternalDynamicImport(self, ctx:ParaParser.ExternalDynamicImportContext):
        pass


    # Enter a parse tree produced by ParaParser#externalFunctionDeclaration.
    def enterExternalFunctionDeclaration(self, ctx:ParaParser.ExternalFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#externalFunctionDeclaration.
    def exitExternalFunctionDeclaration(self, ctx:ParaParser.ExternalFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#externalClassDeclaration.
    def enterExternalClassDeclaration(self, ctx:ParaParser.ExternalClassDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#externalClassDeclaration.
    def exitExternalClassDeclaration(self, ctx:ParaParser.ExternalClassDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#externalStructDeclaration.
    def enterExternalStructDeclaration(self, ctx:ParaParser.ExternalStructDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#externalStructDeclaration.
    def exitExternalStructDeclaration(self, ctx:ParaParser.ExternalStructDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#externalBlockItem.
    def enterExternalBlockItem(self, ctx:ParaParser.ExternalBlockItemContext):
        pass

    # Exit a parse tree produced by ParaParser#externalBlockItem.
    def exitExternalBlockItem(self, ctx:ParaParser.ExternalBlockItemContext):
        pass


    # Enter a parse tree produced by ParaParser#dynamicImport.
    def enterDynamicImport(self, ctx:ParaParser.DynamicImportContext):
        pass

    # Exit a parse tree produced by ParaParser#dynamicImport.
    def exitDynamicImport(self, ctx:ParaParser.DynamicImportContext):
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


    # Enter a parse tree produced by ParaParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:ParaParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:ParaParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#functionAttributes.
    def enterFunctionAttributes(self, ctx:ParaParser.FunctionAttributesContext):
        pass

    # Exit a parse tree produced by ParaParser#functionAttributes.
    def exitFunctionAttributes(self, ctx:ParaParser.FunctionAttributesContext):
        pass


    # Enter a parse tree produced by ParaParser#functionTypeSpecifier.
    def enterFunctionTypeSpecifier(self, ctx:ParaParser.FunctionTypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#functionTypeSpecifier.
    def exitFunctionTypeSpecifier(self, ctx:ParaParser.FunctionTypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#structDeclaration.
    def enterStructDeclaration(self, ctx:ParaParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#structDeclaration.
    def exitStructDeclaration(self, ctx:ParaParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#structItems.
    def enterStructItems(self, ctx:ParaParser.StructItemsContext):
        pass

    # Exit a parse tree produced by ParaParser#structItems.
    def exitStructItems(self, ctx:ParaParser.StructItemsContext):
        pass


    # Enter a parse tree produced by ParaParser#classDeclaration.
    def enterClassDeclaration(self, ctx:ParaParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#classDeclaration.
    def exitClassDeclaration(self, ctx:ParaParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#classItems.
    def enterClassItems(self, ctx:ParaParser.ClassItemsContext):
        pass

    # Exit a parse tree produced by ParaParser#classItems.
    def exitClassItems(self, ctx:ParaParser.ClassItemsContext):
        pass


    # Enter a parse tree produced by ParaParser#initClassFunction.
    def enterInitClassFunction(self, ctx:ParaParser.InitClassFunctionContext):
        pass

    # Exit a parse tree produced by ParaParser#initClassFunction.
    def exitInitClassFunction(self, ctx:ParaParser.InitClassFunctionContext):
        pass


    # Enter a parse tree produced by ParaParser#endOfItem.
    def enterEndOfItem(self, ctx:ParaParser.EndOfItemContext):
        pass

    # Exit a parse tree produced by ParaParser#endOfItem.
    def exitEndOfItem(self, ctx:ParaParser.EndOfItemContext):
        pass


    # Enter a parse tree produced by ParaParser#groupedPrimaryExpression.
    def enterGroupedPrimaryExpression(self, ctx:ParaParser.GroupedPrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#groupedPrimaryExpression.
    def exitGroupedPrimaryExpression(self, ctx:ParaParser.GroupedPrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#identifierPrimaryExpression.
    def enterIdentifierPrimaryExpression(self, ctx:ParaParser.IdentifierPrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#identifierPrimaryExpression.
    def exitIdentifierPrimaryExpression(self, ctx:ParaParser.IdentifierPrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#memberAccessPrimaryExpression.
    def enterMemberAccessPrimaryExpression(self, ctx:ParaParser.MemberAccessPrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#memberAccessPrimaryExpression.
    def exitMemberAccessPrimaryExpression(self, ctx:ParaParser.MemberAccessPrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#stringPrimaryExpression.
    def enterStringPrimaryExpression(self, ctx:ParaParser.StringPrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#stringPrimaryExpression.
    def exitStringPrimaryExpression(self, ctx:ParaParser.StringPrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#fStringPrimaryExpression.
    def enterFStringPrimaryExpression(self, ctx:ParaParser.FStringPrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#fStringPrimaryExpression.
    def exitFStringPrimaryExpression(self, ctx:ParaParser.FStringPrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#numberPrimaryExpression.
    def enterNumberPrimaryExpression(self, ctx:ParaParser.NumberPrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#numberPrimaryExpression.
    def exitNumberPrimaryExpression(self, ctx:ParaParser.NumberPrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#characterPrimaryExpression.
    def enterCharacterPrimaryExpression(self, ctx:ParaParser.CharacterPrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#characterPrimaryExpression.
    def exitCharacterPrimaryExpression(self, ctx:ParaParser.CharacterPrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#listPrimaryExpression.
    def enterListPrimaryExpression(self, ctx:ParaParser.ListPrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#listPrimaryExpression.
    def exitListPrimaryExpression(self, ctx:ParaParser.ListPrimaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#identifier.
    def enterIdentifier(self, ctx:ParaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by ParaParser#identifier.
    def exitIdentifier(self, ctx:ParaParser.IdentifierContext):
        pass


    # Enter a parse tree produced by ParaParser#string.
    def enterString(self, ctx:ParaParser.StringContext):
        pass

    # Exit a parse tree produced by ParaParser#string.
    def exitString(self, ctx:ParaParser.StringContext):
        pass


    # Enter a parse tree produced by ParaParser#listConstant.
    def enterListConstant(self, ctx:ParaParser.ListConstantContext):
        pass

    # Exit a parse tree produced by ParaParser#listConstant.
    def exitListConstant(self, ctx:ParaParser.ListConstantContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnPostfixExpression.
    def enterPassOnPostfixExpression(self, ctx:ParaParser.PassOnPostfixExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnPostfixExpression.
    def exitPassOnPostfixExpression(self, ctx:ParaParser.PassOnPostfixExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#computedMemberAccessPostfixExpression.
    def enterComputedMemberAccessPostfixExpression(self, ctx:ParaParser.ComputedMemberAccessPostfixExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#computedMemberAccessPostfixExpression.
    def exitComputedMemberAccessPostfixExpression(self, ctx:ParaParser.ComputedMemberAccessPostfixExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#incrementOrDecrementPostfixExpression.
    def enterIncrementOrDecrementPostfixExpression(self, ctx:ParaParser.IncrementOrDecrementPostfixExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#incrementOrDecrementPostfixExpression.
    def exitIncrementOrDecrementPostfixExpression(self, ctx:ParaParser.IncrementOrDecrementPostfixExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#objectInitialisationPostfixExpression.
    def enterObjectInitialisationPostfixExpression(self, ctx:ParaParser.ObjectInitialisationPostfixExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#objectInitialisationPostfixExpression.
    def exitObjectInitialisationPostfixExpression(self, ctx:ParaParser.ObjectInitialisationPostfixExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#structInitialisationPostfixExpression.
    def enterStructInitialisationPostfixExpression(self, ctx:ParaParser.StructInitialisationPostfixExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#structInitialisationPostfixExpression.
    def exitStructInitialisationPostfixExpression(self, ctx:ParaParser.StructInitialisationPostfixExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#functionCallPostfixExpression.
    def enterFunctionCallPostfixExpression(self, ctx:ParaParser.FunctionCallPostfixExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#functionCallPostfixExpression.
    def exitFunctionCallPostfixExpression(self, ctx:ParaParser.FunctionCallPostfixExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#arraySpecifier.
    def enterArraySpecifier(self, ctx:ParaParser.ArraySpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#arraySpecifier.
    def exitArraySpecifier(self, ctx:ParaParser.ArraySpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:ParaParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by ParaParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:ParaParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnUnaryExpression.
    def enterPassOnUnaryExpression(self, ctx:ParaParser.PassOnUnaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnUnaryExpression.
    def exitPassOnUnaryExpression(self, ctx:ParaParser.PassOnUnaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#typeofUnaryExpression.
    def enterTypeofUnaryExpression(self, ctx:ParaParser.TypeofUnaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#typeofUnaryExpression.
    def exitTypeofUnaryExpression(self, ctx:ParaParser.TypeofUnaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#deleteUnaryExpression.
    def enterDeleteUnaryExpression(self, ctx:ParaParser.DeleteUnaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#deleteUnaryExpression.
    def exitDeleteUnaryExpression(self, ctx:ParaParser.DeleteUnaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#incrementOrDecrementUnaryExpression.
    def enterIncrementOrDecrementUnaryExpression(self, ctx:ParaParser.IncrementOrDecrementUnaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#incrementOrDecrementUnaryExpression.
    def exitIncrementOrDecrementUnaryExpression(self, ctx:ParaParser.IncrementOrDecrementUnaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#operatorModifiedUnaryExpression.
    def enterOperatorModifiedUnaryExpression(self, ctx:ParaParser.OperatorModifiedUnaryExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#operatorModifiedUnaryExpression.
    def exitOperatorModifiedUnaryExpression(self, ctx:ParaParser.OperatorModifiedUnaryExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#incrementOrDecrementOperator.
    def enterIncrementOrDecrementOperator(self, ctx:ParaParser.IncrementOrDecrementOperatorContext):
        pass

    # Exit a parse tree produced by ParaParser#incrementOrDecrementOperator.
    def exitIncrementOrDecrementOperator(self, ctx:ParaParser.IncrementOrDecrementOperatorContext):
        pass


    # Enter a parse tree produced by ParaParser#unaryOperator.
    def enterUnaryOperator(self, ctx:ParaParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by ParaParser#unaryOperator.
    def exitUnaryOperator(self, ctx:ParaParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnCastOrConvertExpression.
    def enterPassOnCastOrConvertExpression(self, ctx:ParaParser.PassOnCastOrConvertExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnCastOrConvertExpression.
    def exitPassOnCastOrConvertExpression(self, ctx:ParaParser.PassOnCastOrConvertExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualCastOrConvertExpression.
    def enterActualCastOrConvertExpression(self, ctx:ParaParser.ActualCastOrConvertExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualCastOrConvertExpression.
    def exitActualCastOrConvertExpression(self, ctx:ParaParser.ActualCastOrConvertExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnMultiplicativeExpression.
    def enterPassOnMultiplicativeExpression(self, ctx:ParaParser.PassOnMultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnMultiplicativeExpression.
    def exitPassOnMultiplicativeExpression(self, ctx:ParaParser.PassOnMultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualMultiplicativeExpression.
    def enterActualMultiplicativeExpression(self, ctx:ParaParser.ActualMultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualMultiplicativeExpression.
    def exitActualMultiplicativeExpression(self, ctx:ParaParser.ActualMultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnAdditiveExpression.
    def enterPassOnAdditiveExpression(self, ctx:ParaParser.PassOnAdditiveExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnAdditiveExpression.
    def exitPassOnAdditiveExpression(self, ctx:ParaParser.PassOnAdditiveExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualAdditiveExpression.
    def enterActualAdditiveExpression(self, ctx:ParaParser.ActualAdditiveExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualAdditiveExpression.
    def exitActualAdditiveExpression(self, ctx:ParaParser.ActualAdditiveExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnRelationalExpression.
    def enterPassOnRelationalExpression(self, ctx:ParaParser.PassOnRelationalExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnRelationalExpression.
    def exitPassOnRelationalExpression(self, ctx:ParaParser.PassOnRelationalExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualRelationalExpression.
    def enterActualRelationalExpression(self, ctx:ParaParser.ActualRelationalExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualRelationalExpression.
    def exitActualRelationalExpression(self, ctx:ParaParser.ActualRelationalExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnEqualityExpression.
    def enterPassOnEqualityExpression(self, ctx:ParaParser.PassOnEqualityExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnEqualityExpression.
    def exitPassOnEqualityExpression(self, ctx:ParaParser.PassOnEqualityExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualEqualityExpression.
    def enterActualEqualityExpression(self, ctx:ParaParser.ActualEqualityExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualEqualityExpression.
    def exitActualEqualityExpression(self, ctx:ParaParser.ActualEqualityExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnLogicalAndExpression.
    def enterPassOnLogicalAndExpression(self, ctx:ParaParser.PassOnLogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnLogicalAndExpression.
    def exitPassOnLogicalAndExpression(self, ctx:ParaParser.PassOnLogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualLogicalAndExpression.
    def enterActualLogicalAndExpression(self, ctx:ParaParser.ActualLogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualLogicalAndExpression.
    def exitActualLogicalAndExpression(self, ctx:ParaParser.ActualLogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnLogicalOrExpression.
    def enterPassOnLogicalOrExpression(self, ctx:ParaParser.PassOnLogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnLogicalOrExpression.
    def exitPassOnLogicalOrExpression(self, ctx:ParaParser.PassOnLogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualLogicalOrExpression.
    def enterActualLogicalOrExpression(self, ctx:ParaParser.ActualLogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualLogicalOrExpression.
    def exitActualLogicalOrExpression(self, ctx:ParaParser.ActualLogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnConditionalExpression.
    def enterPassOnConditionalExpression(self, ctx:ParaParser.PassOnConditionalExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnConditionalExpression.
    def exitPassOnConditionalExpression(self, ctx:ParaParser.PassOnConditionalExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualConditionalExpression.
    def enterActualConditionalExpression(self, ctx:ParaParser.ActualConditionalExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualConditionalExpression.
    def exitActualConditionalExpression(self, ctx:ParaParser.ActualConditionalExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#passOnAssignmentExpression.
    def enterPassOnAssignmentExpression(self, ctx:ParaParser.PassOnAssignmentExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#passOnAssignmentExpression.
    def exitPassOnAssignmentExpression(self, ctx:ParaParser.PassOnAssignmentExpressionContext):
        pass


    # Enter a parse tree produced by ParaParser#actualAssignmentExpression.
    def enterActualAssignmentExpression(self, ctx:ParaParser.ActualAssignmentExpressionContext):
        pass

    # Exit a parse tree produced by ParaParser#actualAssignmentExpression.
    def exitActualAssignmentExpression(self, ctx:ParaParser.ActualAssignmentExpressionContext):
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


    # Enter a parse tree produced by ParaParser#storageTypeSpecifier.
    def enterStorageTypeSpecifier(self, ctx:ParaParser.StorageTypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#storageTypeSpecifier.
    def exitStorageTypeSpecifier(self, ctx:ParaParser.StorageTypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#initDeclarator.
    def enterInitDeclarator(self, ctx:ParaParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by ParaParser#initDeclarator.
    def exitInitDeclarator(self, ctx:ParaParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by ParaParser#singleItemTypeSpecifier.
    def enterSingleItemTypeSpecifier(self, ctx:ParaParser.SingleItemTypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#singleItemTypeSpecifier.
    def exitSingleItemTypeSpecifier(self, ctx:ParaParser.SingleItemTypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#multiItemTypeSpecifier.
    def enterMultiItemTypeSpecifier(self, ctx:ParaParser.MultiItemTypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#multiItemTypeSpecifier.
    def exitMultiItemTypeSpecifier(self, ctx:ParaParser.MultiItemTypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#typeofTypeSpecifier.
    def enterTypeofTypeSpecifier(self, ctx:ParaParser.TypeofTypeSpecifierContext):
        pass

    # Exit a parse tree produced by ParaParser#typeofTypeSpecifier.
    def exitTypeofTypeSpecifier(self, ctx:ParaParser.TypeofTypeSpecifierContext):
        pass


    # Enter a parse tree produced by ParaParser#explicitTypeHint.
    def enterExplicitTypeHint(self, ctx:ParaParser.ExplicitTypeHintContext):
        pass

    # Exit a parse tree produced by ParaParser#explicitTypeHint.
    def exitExplicitTypeHint(self, ctx:ParaParser.ExplicitTypeHintContext):
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


    # Enter a parse tree produced by ParaParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:ParaParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by ParaParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:ParaParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by ParaParser#initializer.
    def enterInitializer(self, ctx:ParaParser.InitializerContext):
        pass

    # Exit a parse tree produced by ParaParser#initializer.
    def exitInitializer(self, ctx:ParaParser.InitializerContext):
        pass


    # Enter a parse tree produced by ParaParser#statement.
    def enterStatement(self, ctx:ParaParser.StatementContext):
        pass

    # Exit a parse tree produced by ParaParser#statement.
    def exitStatement(self, ctx:ParaParser.StatementContext):
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


    # Enter a parse tree produced by ParaParser#ifStatement.
    def enterIfStatement(self, ctx:ParaParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#ifStatement.
    def exitIfStatement(self, ctx:ParaParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#switchStatement.
    def enterSwitchStatement(self, ctx:ParaParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#switchStatement.
    def exitSwitchStatement(self, ctx:ParaParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by ParaParser#switchLabeledStatement.
    def enterSwitchLabeledStatement(self, ctx:ParaParser.SwitchLabeledStatementContext):
        pass

    # Exit a parse tree produced by ParaParser#switchLabeledStatement.
    def exitSwitchLabeledStatement(self, ctx:ParaParser.SwitchLabeledStatementContext):
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



del ParaParser