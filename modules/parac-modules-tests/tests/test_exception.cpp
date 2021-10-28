///
/// Testing for the header pbl-exception.h
///
/// @author Luna-Klatzer
#include <pbl.h>

#include "gtest/gtest.h"

PblInt_T NestedTestFunction(PblMetaFunctionCallCtx_T *this_call_meta, PblUInt_T i)
{
  PblUInt_T line = PblGetUIntT(__LINE__);
  PblException_T *exception = PblGetExceptionT(
    PblGetStringT("test"), PblGetStringT("TestException"), PblGetStringT(__FILE__),
    line, PblGetStringT("raise exception"), NULL, NULL
    );
  RAISE_EXCEPTION(exception, PblInt_T);
}

PblInt_T TestFunction(PblMetaFunctionCallCtx_T *this_call_meta)
{
  PblInt_T r_1 = PblInt_T_DeclDefault;
  EXCEPTION_CATCH_FUNC_CONSTRUCTOR(NestedTestFunction, r_1, PblInt_T, X1, PblGetUIntT(1))
  return r_1;
}

TEST(BaseFunctionTest, OneNestCall) {
  PblInt_T r_1 = PblInt_T_DeclDefault;
  PblMetaFunctionCallCtx_T this_call_meta = PblMetaFunctionCallCtx_T_DefDefault;
  C_BASE_EXCEPTION_CATCH_CONSTRUCTOR(TestFunction, r_1, H3, PblGetBoolT(false), &call_ctx,);
  EXPECT_EQ(r_1.meta.defined, false);
}
