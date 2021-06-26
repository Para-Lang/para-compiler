# coding=utf-8
""" Listener Class """
from __future__ import annotations
import logging
from typing import TYPE_CHECKING

import antlr4

from .python import ParaCListener
from .python import ParaCParser as parser
from ..compilation_ctx import FileCompilationContext

logger = logging.getLogger(__name__)
ParaCParser = parser.ParaCParser

if TYPE_CHECKING:
    # Assigning the variables to hold the imported classes for easier type
    # hinting and avoiding exceeding the line length
    _p = parser.ParaCParser
    ExpressionContext = _p.ExpressionContext
    FunctionDefinitionContext = _p.FunctionDefinitionContext
    AssignmentExpressionContext = _p.AssignmentExpressionContext
    CompilationUnitContext = _p.CompilationUnitContext


__all__ = [
    'Listener'
]


# TODO! Add missing listener functions when grammar file was finished
class Listener(ParaCListener.ParaCListener):
    """
    Listener that listens for events inside the parsing. It will inherit all
    generated methods from the ParaCListener and then define the wanted
    behaviour inside a compilation.
    """

    def __init__(self, unit_ctx: CompilationUnitContext):
        self.file_ctx = FileCompilationContext()
        self.unit_ctx = unit_ctx
        self.code_str = ""

        self._compiling = False
        self._enable_out = False

    def walk(self, enable_out: bool) -> None:
        """
        Walks through the parsed CompilationUnitContext and listens to the
        events / goes through the tokens

        :param enable_out: If set to True errors, warnings and info will be
                           logged onto the console using the local logger
                           instance. (Errors will then NOT be raised but only
                           logged)
        """
        self._enable_out = enable_out

        walker = antlr4.ParseTreeWalker()
        walker.walk(self, self.unit_ctx)

        ...  # TODO! Add warnings system

    def walk_and_compile(self, enable_out: bool) -> None:
        """
        Walks through the parsed CompilationUnitContext and listens to the
        events / goes through the tokens and fills the FileCompilationContext
        (self.file_ctx) appropriately with the data.

        The FileCompilationContext can then be used inside the
        CompilationContext to be linked with other files and to finish
        the compilation for the program

        :param enable_out: If set to True errors, warnings and info will be
                   logged onto the console using the local logger
                   instance. (Errors will then NOT be raised but only
                   logged)
        """
        self._compiling = True
        self.walk(enable_out)

        # TODO! Add wrap-up and 'compilation'

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

    def enterExtFunctionDefinition(
            self,
            ctx: ParaCParser.ExtFunctionDefinitionContext
    ):
        """
        Enter a parse tree produced by ParaCParser#extFunctionDefition.
        """
        ...

    def exitExtFunctionDefinition(
            self,
            ctx: ParaCParser.ExtFunctionDefinitionContext
    ):
        """
        Exit a parse tree produced by ParaCParser#extFunctionDefition.
        """
        ...

    def enterExtDeclaration(
            self,
            ctx: ParaCParser.ExtDeclarationContext
    ):
        """
        Enter a parse tree produced by ParaCParser#extDeclaration.
        """
        ...

    def exitExtDeclaration(
            self,
            ctx: ParaCParser.ExtDeclarationContext
    ):
        """
        Exit a parse tree produced by ParaCParser#extDeclaration.
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

    def enterGenericSelection(
            self,
            ctx: ParaCParser.GenericSelectionContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#genericSelection.
        """
        ...

    def exitGenericSelection(
            self,
            ctx: ParaCParser.GenericSelectionContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#genericSelection.
        """
        ...

    def enterGenericAssocList(
            self,
            ctx: ParaCParser.GenericAssocListContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#genericAssocList.
        """
        ...

    def exitGenericAssocList(
            self,
            ctx: ParaCParser.GenericAssocListContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#genericAssocList.
        """
        ...

    def enterGenericAssociation(
            self,
            ctx: ParaCParser.GenericAssociationContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#genericAssociation.
        """
        ...

    def exitGenericAssociation(
            self,
            ctx: ParaCParser.GenericAssociationContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#genericAssociation.
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

    def enterCastExpression(
            self,
            ctx: ParaCParser.CastExpressionContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#castExpression.
        """
        ...

    def exitCastExpression(
            self,
            ctx: ParaCParser.CastExpressionContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#castExpression.
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

    def enterDeclarationSpecifiers2(
            self,
            ctx: ParaCParser.DeclarationSpecifiers2Context
    ): 
        """
        Enter a parse tree produced by ParaCParser#declarationSpecifiers2.
        """
        ...

    def exitDeclarationSpecifiers2(
            self,
            ctx: ParaCParser.DeclarationSpecifiers2Context
    ): 
        """
        Exit a parse tree produced by ParaCParser#declarationSpecifiers2.
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

    def enterEntryPointSpecifier(
            self,
            ctx: ParaCParser.EntryPointSpecifierContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#entryPointSpecifider.
        """
        ...

    def exitEntryPointSpecifier(
            self,
            ctx: ParaCParser.EntryPointSpecifierContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#entryPointSpecifider.
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

    def enterGccDeclaratorExtension(
            self,
            ctx: ParaCParser.GccDeclaratorExtensionContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#gccDeclaratorExtension.
        """
        ...

    def exitGccDeclaratorExtension(
            self,
            ctx: ParaCParser.GccDeclaratorExtensionContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#gccDeclaratorExtension.
        """
        ...

    def enterGccAttributeSpecifier(
            self,
            ctx: ParaCParser.GccAttributeSpecifierContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#gccAttributeSpecifier.
        """
        ...

    def exitGccAttributeSpecifier(
            self,
            ctx: ParaCParser.GccAttributeSpecifierContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#gccAttributeSpecifier.
        """
        ...

    def enterGccAttributeList(
            self,
            ctx: ParaCParser.GccAttributeListContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#gccAttributeList.
        """
        ...

    def exitGccAttributeList(
            self,
            ctx: ParaCParser.GccAttributeListContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#gccAttributeList.
        """
        ...

    def enterGccAttribute(
            self,
            ctx: ParaCParser.GccAttributeContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#gccAttribute.
        """
        ...

    def exitGccAttribute(
            self,
            ctx: ParaCParser.GccAttributeContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#gccAttribute.
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

    def enterParameterDeclaration(
            self,
            ctx: ParaCParser.ParameterDeclarationContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#parameterDeclaration.
        """
        ...

    def exitParameterDeclaration(
            self,
            ctx: ParaCParser.ParameterDeclarationContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#parameterDeclaration.
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

    def enterFunctionDefinition(
            self,
            ctx: ParaCParser.FunctionDefinitionContext
    ): 
        """
        Enter a parse tree produced by ParaCParser#functionDefinition.
        """
        ...

    def exitFunctionDefinition(
            self,
            ctx: ParaCParser.FunctionDefinitionContext
    ): 
        """
        Exit a parse tree produced by ParaCParser#functionDefinition.
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
