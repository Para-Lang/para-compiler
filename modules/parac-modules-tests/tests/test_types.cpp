/// Testing for the header pbl-types.h
///
/// @author Luna-Klatzer

#include <pbl.h>
#include "gtest/gtest.h"

// TODO! Add tests for the type defaults and size

TEST(MacroTypesTest, PblSizeof) {
  EXPECT_EQ(PblBool_T_Size, PBL_SIZEOF(PblBool_T));
}

TEST(MacroTypesTest, CSizeof) {
  EXPECT_EQ(sizeof(char), PBL_C_SIZEOF(char));
}

TEST(BaseTypesTest, PblBool) {
  PblBool_T v = PblGetBoolT(true);
  EXPECT_EQ(v.actual, true);
  EXPECT_EQ(v.meta.byte_size, PblBool_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(bool));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblBoolDefaults) {
  PblBool_T v_1 = PblBool_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblBool_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(bool));
  EXPECT_EQ(v_1.meta.defined, false);

  PblBool_T v_2 = PblBool_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblBool_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(bool));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblSize) {
  PblSize_T v = PblGetSizeT(sizeof(int));
  EXPECT_EQ(v.actual, sizeof(int));
  EXPECT_EQ(v.meta.byte_size, PblSize_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(size_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblSizeDefaults) {
  PblSize_T v_1 = PblSize_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblSize_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(size_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblSize_T v_2 = PblSize_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblSize_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(size_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblChar) {
  PblChar_T v = PblGetCharT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblChar_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned char));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed char));
  EXPECT_EQ(v.meta.byte_size, sizeof(char));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUChar) {
  PblUChar_T v = PblGetUCharT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblUChar_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned char));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed char));
  EXPECT_EQ(v.meta.byte_size, sizeof(char));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblCharDefaults) {
  PblChar_T v_1 = PblChar_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblChar_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(char));
  EXPECT_EQ(v_1.meta.defined, false);

  PblChar_T v_2 = PblChar_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblChar_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(char));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUCharDefaults) {
  PblUChar_T v_1 = PblUChar_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUChar_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(char));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUChar_T v_2 = PblUChar_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUChar_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(char));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblShort) {
  PblShort_T v = PblGetShortT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblShort_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned short));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed short));
  EXPECT_EQ(v.meta.byte_size, sizeof(short));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUShort) {
  PblUShort_T v = PblGetUShortT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblUShort_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned short));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed short));
  EXPECT_EQ(v.meta.byte_size, sizeof(short));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblShortDefaults) {
  PblShort_T v_1 = PblShort_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblShort_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(short));
  EXPECT_EQ(v_1.meta.defined, false);

  PblShort_T v_2 = PblShort_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblShort_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(short));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUShortDefaults) {
  PblUShort_T v_1 = PblUShort_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUShort_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(short));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUShort_T v_2 = PblUShort_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUShort_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(short));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblInt) {
  PblInt_T v = PblGetIntT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblInt_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned int));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed int));
  EXPECT_EQ(v.meta.byte_size, sizeof(int));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt) {
  PblUInt_T v = PblGetUIntT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblUInt_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned int));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed int));
  EXPECT_EQ(v.meta.byte_size, sizeof(int));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblIntDefaults) {
  PblInt_T v_1 = PblInt_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblInt_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int));
  EXPECT_EQ(v_1.meta.defined, false);

  PblInt_T v_2 = PblInt_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblInt_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUIntDefaults) {
  PblUInt_T v_1 = PblUInt_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUInt_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUInt_T v_2 = PblUInt_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUInt_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblLong) {
  PblLong_T v = PblGetLongT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblLong_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned long));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed long));
  EXPECT_EQ(v.meta.byte_size, sizeof(long));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblULong) {
  PblULong_T v = PblGetULongT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblULong_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned long));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed long));
  EXPECT_EQ(v.meta.byte_size, sizeof(long));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblLongDefaults) {
  PblLong_T v_1 = PblLong_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblLong_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(long));
  EXPECT_EQ(v_1.meta.defined, false);

  PblLong_T v_2 = PblLong_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblLong_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(long));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblULongDefaults) {
  PblULong_T v_1 = PblULong_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblULong_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(long));
  EXPECT_EQ(v_1.meta.defined, false);

  PblULong_T v_2 = PblULong_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblULong_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(long));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblLongLong) {
  PblLongLong_T v = PblGetLongLongT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblLongLong_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned long long));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed long long));
  EXPECT_EQ(v.meta.byte_size, sizeof(long long));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblULongLong) {
  PblULongLong_T v = PblGetULongLongT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblULongLong_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(unsigned long long));
  EXPECT_EQ(v.meta.byte_size, sizeof(signed long long));
  EXPECT_EQ(v.meta.byte_size, sizeof(long long));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblLongLongDefaults) {
  PblLongLong_T v_1 = PblLongLong_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblLongLong_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(long long));
  EXPECT_EQ(v_1.meta.defined, false);

  PblLongLong_T v_2 = PblLongLong_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblLongLong_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(long long));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblULongLongDefaults) {
  PblULongLong_T v_1 = PblULongLong_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblULongLong_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(long long));
  EXPECT_EQ(v_1.meta.defined, false);

  PblULongLong_T v_2 = PblULongLong_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblULongLong_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(long long));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblFloat) {
  PblFloat_T v = PblGetFloatT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblFloat_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(float));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblFloatDefaults) {
  PblFloat_T v_1 = PblFloat_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblFloat_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(float));
  EXPECT_EQ(v_1.meta.defined, false);

  PblFloat_T v_2 = PblFloat_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblFloat_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(float));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblDouble) {
  PblDouble_T v = PblGetDoubleT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblDouble_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(double));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblDoubleDefaults) {
  PblDouble_T v_1 = PblDouble_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblDouble_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(double));
  EXPECT_EQ(v_1.meta.defined, false);

  PblDouble_T v_2 = PblDouble_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblDouble_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(double));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblLongDouble) {
  PblLongDouble_T v = PblGetLongDoubleT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblLongDouble_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(long double));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblLongDoubleDefaults) {
  PblLongDouble_T v_1 = PblLongDouble_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblLongDouble_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(long double));
  EXPECT_EQ(v_1.meta.defined, false);

  PblLongDouble_T v_2 = PblLongDouble_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblLongDouble_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(long double));
  EXPECT_EQ(v_2.meta.defined, true);
}