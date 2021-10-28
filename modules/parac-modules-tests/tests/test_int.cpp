///
/// Testing for the header pbl-int.h
///
/// @author Luna-Klatzer

#include <pbl.h>
#include "gtest/gtest.h"

TEST(BaseTypesTest, PblInt8) {
  PblInt8_T v = PblGetInt8T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblInt8_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int8_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt8) {
  PblUInt8_T v = PblGetUInt8T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblUInt8_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int8_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblInt8Defaults) {
  PblInt8_T v_1 = PblInt8_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblInt8_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int8_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblInt8_T v_2 = PblInt8_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblInt8_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int8_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt8Defaults) {
  PblUInt8_T v_1 = PblUInt8_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUInt8_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int8_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUInt8_T v_2 = PblUInt8_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUInt8_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int8_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblInt16) {
  PblInt16_T v = PblGetInt16T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblInt16_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int16_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt16) {
  PblUInt16_T v = PblGetUInt16T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblUInt16_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int16_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblInt16Defaults) {
  PblInt16_T v_1 = PblInt16_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblInt16_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int16_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblInt16_T v_2 = PblInt16_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblInt16_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int16_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt16Defaults) {
  PblUInt16_T v_1 = PblUInt16_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUInt16_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int16_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUInt16_T v_2 = PblUInt16_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUInt16_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int16_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblInt32) {
  PblInt32_T v = PblGetInt32T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblInt32_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int32_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt32) {
  PblUInt32_T v = PblGetUInt32T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblUInt32_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int32_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblInt32Defaults) {
  PblInt32_T v_1 = PblInt32_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblInt32_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int32_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblInt32_T v_2 = PblInt32_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblInt32_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int32_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt32Defaults) {
  PblUInt32_T v_1 = PblUInt32_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUInt32_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int32_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUInt32_T v_2 = PblUInt32_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUInt32_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int32_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblInt64) {
  PblInt64_T v = PblGetInt64T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblInt64_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int64_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt64) {
  PblUInt64_T v = PblGetUInt64T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblUInt64_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int64_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblInt64Defaults) {
  PblInt64_T v_1 = PblInt64_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblInt64_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int64_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblInt64_T v_2 = PblInt64_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblInt64_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int64_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUInt64Defaults) {
  PblUInt64_T v_1 = PblUInt64_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUInt64_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int64_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUInt64_T v_2 = PblUInt64_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUInt64_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int64_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblLeastInt8) {
  PblLeastInt8_T v = PblGetLeastInt8T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblLeastInt8_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_least8_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblULeastInt8) {
  PblULeastInt8_T v = PblGetULeastInt8T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblULeastInt8_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_least8_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblLeastInt8Defaults) {
  PblLeastInt8_T v_1 = PblLeastInt8_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblLeastInt8_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_least8_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblLeastInt8_T v_2 = PblLeastInt8_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblLeastInt8_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_least8_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblULeastInt8Defaults) {
  PblULeastInt8_T v_1 = PblULeastInt8_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblULeastInt8_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_least8_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblULeastInt8_T v_2 = PblULeastInt8_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblULeastInt8_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_least8_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblLeastInt16) {
  PblLeastInt16_T v = PblGetLeastInt16T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblLeastInt16_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_least16_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblULeastInt16) {
  PblULeastInt16_T v = PblGetULeastInt16T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblULeastInt16_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_least16_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblLeastInt16Defaults) {
  PblLeastInt16_T v_1 = PblLeastInt16_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblLeastInt16_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_least16_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblLeastInt16_T v_2 = PblLeastInt16_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblLeastInt16_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_least16_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblULeastInt16Defaults) {
  PblULeastInt16_T v_1 = PblULeastInt16_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblULeastInt16_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_least16_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblULeastInt16_T v_2 = PblULeastInt16_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblULeastInt16_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_least16_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblLeastInt32) {
  PblLeastInt32_T v = PblGetLeastInt32T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblLeastInt32_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_least32_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblULeastInt32) {
  PblULeastInt32_T v = PblGetULeastInt32T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblULeastInt32_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_least32_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblLeastInt32Defaults) {
  PblLeastInt32_T v_1 = PblLeastInt32_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblLeastInt32_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_least32_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblLeastInt32_T v_2 = PblLeastInt32_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblLeastInt32_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_least32_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblULeastInt32Defaults) {
  PblULeastInt32_T v_1 = PblULeastInt32_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblULeastInt32_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_least32_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblULeastInt32_T v_2 = PblULeastInt32_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblULeastInt32_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_least32_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblLeastInt64) {
  PblLeastInt64_T v = PblGetLeastInt64T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblLeastInt64_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_least64_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblULeastInt64) {
  PblULeastInt64_T v = PblGetULeastInt64T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblULeastInt64_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_least64_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblLeastInt64Defaults) {
  PblLeastInt64_T v_1 = PblLeastInt64_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblLeastInt64_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_least64_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblLeastInt64_T v_2 = PblLeastInt64_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblLeastInt64_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_least64_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblULeastInt64Defaults) {
  PblULeastInt64_T v_1 = PblULeastInt64_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblULeastInt64_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_least64_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblULeastInt64_T v_2 = PblULeastInt64_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblULeastInt64_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_least64_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblFastInt8) {
  PblFastInt8_T v = PblGetFastInt8T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblFastInt8_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_fast8_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUFastInt8) {
  PblUFastInt8_T v = PblGetUFastInt8T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblUFastInt8_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_fast8_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblFastInt8Defaults) {
  PblFastInt8_T v_1 = PblFastInt8_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblFastInt8_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_fast8_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblFastInt8_T v_2 = PblFastInt8_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblFastInt8_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_fast8_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUFastInt8Defaults) {
  PblUFastInt8_T v_1 = PblUFastInt8_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUFastInt8_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_fast8_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUFastInt8_T v_2 = PblUFastInt8_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUFastInt8_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_fast8_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblFastInt16) {
  PblFastInt16_T v = PblGetFastInt16T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblFastInt16_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_fast16_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUFastInt16) {
  PblUFastInt16_T v = PblGetUFastInt16T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblUFastInt16_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_fast16_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblFastInt16Defaults) {
  PblFastInt16_T v_1 = PblFastInt16_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblFastInt16_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_fast16_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblFastInt16_T v_2 = PblFastInt16_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblFastInt16_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_fast16_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUFastInt16Defaults) {
  PblUFastInt16_T v_1 = PblUFastInt16_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUFastInt16_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_fast16_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUFastInt16_T v_2 = PblUFastInt16_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUFastInt16_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_fast16_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblFastInt32) {
  PblFastInt32_T v = PblGetFastInt32T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblFastInt32_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_fast32_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUFastInt32) {
  PblUFastInt32_T v = PblGetUFastInt32T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblUFastInt32_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_fast32_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblFastInt32Defaults) {
  PblFastInt32_T v_1 = PblFastInt32_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblFastInt32_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_fast32_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblFastInt32_T v_2 = PblFastInt32_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblFastInt32_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_fast32_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUFastInt32Defaults) {
  PblUFastInt32_T v_1 = PblUFastInt32_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUFastInt32_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_fast32_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUFastInt32_T v_2 = PblUFastInt32_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUFastInt32_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_fast32_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblFastInt64) {
  PblFastInt64_T v = PblGetFastInt64T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblFastInt64_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_fast64_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblUFastInt64) {
  PblUFastInt64_T v = PblGetUFastInt64T(0);
  EXPECT_EQ(v.actual, 0);
  EXPECT_EQ(v.meta.byte_size, PblUFastInt64_T_Size);
  EXPECT_EQ(v.meta.byte_size, sizeof(int_fast64_t));
  EXPECT_EQ(v.meta.defined, true);
}

TEST(BaseTypesTest, PblFastInt64Defaults) {
  PblFastInt64_T v_1 = PblFastInt64_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblFastInt64_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_fast64_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblFastInt64_T v_2 = PblFastInt64_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblFastInt64_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_fast64_t));
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(BaseTypesTest, PblUFastInt64Defaults) {
  PblUFastInt64_T v_1 = PblUFastInt64_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblUFastInt64_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, sizeof(int_fast64_t));
  EXPECT_EQ(v_1.meta.defined, false);

  PblUFastInt64_T v_2 = PblUFastInt64_T_DefDefault;

  EXPECT_EQ(v_2.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblUFastInt64_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, sizeof(int_fast64_t));
  EXPECT_EQ(v_2.meta.defined, true);
}