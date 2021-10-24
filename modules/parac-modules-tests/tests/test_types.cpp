/// Testing for the header pbl-types.h
///
/// @author Luna-Klatzer

#include "pbl-types.h"
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

TEST(BaseTypesTest, PblSize) {
  PblSize_T v = PblGetSizeT(sizeof(int));
  EXPECT_EQ(v.actual, sizeof(int));
  EXPECT_EQ(v.meta.byte_size, PblSize_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(size_t));
  EXPECT_EQ(v.meta.defined, true);
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

TEST(BaseTypesTest, PblFloat) {
  PblFloat_T v = PblGetFloatT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblFloat_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(float));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblDouble) {
  PblDouble_T v = PblGetDoubleT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblDouble_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(double));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblLongDouble) {
  PblLongDouble_T v = PblGetLongDoubleT('x');
  EXPECT_EQ(v.actual, 'x');
  EXPECT_EQ(v.meta.byte_size, PblLongDouble_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(long double));
  EXPECT_EQ(v.meta.defined, true);
}
