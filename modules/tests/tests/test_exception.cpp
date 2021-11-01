///
/// Testing for the header pbl-exception.h
///
/// @author Luna-Klatzer
#include <pbl.h>

#include "gtest/gtest.h"

TEST(FunctionMetaTest, PblMetaFunctionCallCtxDefaults) {
  PblMetaFunctionCallCtx_T v_1 = PblMetaFunctionCallCtx_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblMetaFunctionCallCtx_T_Size);
  EXPECT_EQ(
    v_1.meta.byte_size,
    sizeof(bool) + sizeof(unsigned int) + sizeof(bool) + 2 * sizeof(PblMetaFunctionCallCtx_T*) + sizeof(NULL)
    );
  EXPECT_EQ(v_1.meta.defined, false);

  PblMetaFunctionCallCtx_T v_2 = PblMetaFunctionCallCtx_T_DefDefault;

  EXPECT_TRUE(v_2.actual.call_origin_ctx == NULL);
  EXPECT_TRUE(v_2.actual.exception == NULL);
  EXPECT_TRUE(v_2.actual.failure_origin_ctx == NULL);
  EXPECT_FALSE(v_2.actual.is_failure.actual);
  EXPECT_EQ(v_2.actual.arg_amount.actual, 0);
  EXPECT_STREQ(v_2.actual.function_identifier.actual.str, "");
  EXPECT_EQ(v_2.meta.byte_size, PblMetaFunctionCallCtx_T_Size);
  EXPECT_EQ(
    v_2.meta.byte_size,
    sizeof(bool) + sizeof(unsigned int) + sizeof(bool) + 2 * sizeof(PblMetaFunctionCallCtx_T*) + sizeof(NULL)
    );
  EXPECT_EQ(v_2.meta.defined, true);
}

TEST(ExceptionTest, PblExceptionDefaults) {
  PblException_T v_1 = PblException_T_DeclDefault;

  EXPECT_EQ(v_1.meta.byte_size, PblException_T_Size);
  EXPECT_EQ(v_1.meta.byte_size, 4 * PblString_T_Size + sizeof(unsigned int) + 2 * sizeof(void*));
  EXPECT_EQ(v_1.meta.defined, false);

  PblException_T v_2 = PblException_T_DefDefault;

  EXPECT_TRUE(v_2.actual.child_exc == NULL);
  EXPECT_TRUE(v_2.actual.parent_exc == NULL);
  EXPECT_STREQ(v_2.actual.name.actual.str, "");
  EXPECT_STREQ(v_2.actual.msg.actual.str, "");
  EXPECT_STREQ(v_2.actual.filename.actual.str, "");
  EXPECT_STREQ(v_2.actual.line_content.actual.str, "");
  EXPECT_EQ(v_2.actual.line.actual, 0);
  EXPECT_EQ(v_2.meta.byte_size, PblException_T_Size);
  EXPECT_EQ(v_2.meta.byte_size, 4 * PblString_T_Size + PblUInt_T_Size + 2 * sizeof(void*));
  EXPECT_EQ(v_2.meta.defined, true);
}

PblInt_T NestedTestFunction(PblMetaFunctionCallCtx_T *this_call_meta, PblUInt_T i)
{
  PblUInt_T line = PblGetUIntT(__LINE__);
  PblException_T *exception = PblGetExceptionT(
    PblGetStringT("test"),
    PblGetStringT("TestException"),
    PblGetStringT(__FILE__),
    line,
    PblGetStringT("raise exception"),
    NULL,
    NULL
    );
  RAISE_EXCEPTION(exception, PblInt_T);
}

PblInt_T TestFunction(PblMetaFunctionCallCtx_T *this_call_meta)
{
  PblInt_T r_1 = PblInt_T_DeclDefault;
  EXCEPTION_CATCH_FUNC_CONSTRUCTOR(NestedTestFunction, r_1, PblInt_T, X1, PblGetUIntT(1))
  return r_1;
}

TEST(ExceptionTest, OneNestCall) {
  PblInt_T r_1 = PblInt_T_DeclDefault;
  PblMetaFunctionCallCtx_T this_call_meta = PblMetaFunctionCallCtx_T_DefDefault;
  C_BASE_EXCEPTION_CATCH_CONSTRUCTOR(TestFunction, r_1, H3, PblGetBoolT(false),&this_call_meta,);

  EXPECT_EQ(r_1.meta.defined, false);
  EXPECT_TRUE(this_call_meta.actual.is_failure.actual);
  EXPECT_TRUE(this_call_meta.actual.failure_origin_ctx != NULL);
  EXPECT_TRUE(this_call_meta.actual.exception != NULL);
  EXPECT_TRUE(this_call_meta.actual.call_origin_ctx == NULL);
  EXPECT_STREQ(((PblException_T*)this_call_meta.actual.exception)->actual.msg.actual.str, "test");
  EXPECT_STREQ(((PblException_T*)this_call_meta.actual.exception)->actual.name.actual.str, "TestException");
  EXPECT_STREQ(((PblException_T*)this_call_meta.actual.exception)->actual.filename.actual.str, __FILE__);
  EXPECT_STREQ(((PblException_T*)this_call_meta.actual.exception)->actual.line_content.actual.str, "raise exception");
}

PblInt_T TestFunction2(PblMetaFunctionCallCtx_T *this_call_meta) {
  EXCEPTION_TRY_EXCEPT_BLOCK(
    {
      PblInt_T r_1 = PblInt_T_DeclDefault;
      EXCEPTION_TRY_BLOCK_CATCH_FUNC_CONSTRUCTOR(NestedTestFunction, r_1, PblInt_T, X1, Y2, PblGetUIntT(1))
      return r_1;
    },
    {
      EXCEPTION_CREATE_EXCEPT_BLOCK(
        "test",
        {
          return PblGetIntT(1);
        },
        Y2
        )
    },
    Y2,
    this_call_meta,
    PblInt_T
    );
  // default return is 0 - aka. the exception was raised
  return PblGetIntT(0);
}

TEST(ExceptionTest, TryExceptCall) {
  PblInt_T r_1 = PblInt_T_DeclDefault;
  PblMetaFunctionCallCtx_T this_call_meta = PblMetaFunctionCallCtx_T_DefDefault;
  C_BASE_EXCEPTION_CATCH_CONSTRUCTOR(TestFunction2, r_1, H3, PblGetBoolT(false), &this_call_meta,);

  // Try-except should never if there is a except statement that was executed, log it's exception and throw the results
  // away right after finishing up
  EXPECT_FALSE(this_call_meta.actual.is_failure.actual);
  EXPECT_TRUE(this_call_meta.actual.failure_origin_ctx == NULL);
  EXPECT_TRUE(this_call_meta.actual.exception == NULL);
  EXPECT_TRUE(this_call_meta.actual.call_origin_ctx == NULL);
  EXPECT_EQ(r_1.meta.defined, true);
  EXPECT_EQ(r_1.actual, 1);
}

PblInt_T TestFunction3(PblMetaFunctionCallCtx_T *this_call_meta) {
  EXCEPTION_TRY_EXCEPT_BLOCK(
    {
      PblInt_T r_1 = PblInt_T_DeclDefault;
      EXCEPTION_TRY_BLOCK_CATCH_FUNC_CONSTRUCTOR(NestedTestFunction, r_1, PblInt_T, X1, Y2, PblGetUIntT(1))
      return r_1;
    },
    {
      EXCEPTION_CREATE_EXCEPT_BLOCK(
        "test",
        {
          return PblGetIntT(1);
        },
        Y2
      )
    },
    Y2,
    this_call_meta,
    PblInt_T
  );
  // default return is 0 - aka. the exception was raised
  return PblGetIntT(0);
}

TEST(ExceptionTest, TryExceptCallWithContinuation) {
  PblInt_T r_1 = PblInt_T_DeclDefault;
  PblMetaFunctionCallCtx_T this_call_meta = PblMetaFunctionCallCtx_T_DefDefault;
  C_BASE_EXCEPTION_CATCH_CONSTRUCTOR(TestFunction3, r_1, H3, PblGetBoolT(false), &this_call_meta,);

  EXPECT_FALSE(this_call_meta.actual.is_failure.actual);
  EXPECT_TRUE(this_call_meta.actual.failure_origin_ctx == NULL);
  EXPECT_TRUE(this_call_meta.actual.exception == NULL);
  EXPECT_TRUE(this_call_meta.actual.call_origin_ctx == NULL);
  EXPECT_EQ(r_1.meta.defined, true);
  EXPECT_EQ(r_1.actual, 1);
}