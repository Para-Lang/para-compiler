///
/// Function-related types
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "pbl-function.h"

PblMetaFunctionCallCtx_T *PblAllocateMetaFunctionCallCtxT() {
  PblMetaFunctionCallCtx_T* ptr = malloc(sizeof(PblMetaFunctionCallCtx_T));
  *ptr = PblMetaFunctionCallCtx_T_DefDefault;
  return ptr;
}

PblMetaFunctionCallCtx_T *PblGetMetaFunctionCallCtxT(PblString_T function_identifier, PblBool_T is_failure,
                                                     PblUInt_T arg_amount, PblBool_T is_threaded,
                                                     PblMetaFunctionCallCtx_T *failure_origin_ctx,
                                                     PblMetaFunctionCallCtx_T *call_origin_ctx,
                                                     void *exception) {
  PblMetaFunctionCallCtx_T *ptr = PblAllocateMetaFunctionCallCtxT();
  ptr->actual = (struct PblMetaFunctionCallCtxBase){
    .function_identifier=function_identifier, .is_failure=is_failure, .arg_amount=arg_amount,
    .is_threaded=is_threaded, .failure_origin_ctx=failure_origin_ctx, .call_origin_ctx=call_origin_ctx,
    .exception=exception
  };
  return ptr;
}

PblVoid_T PblDeallocateMetaFunctionCallCtxT(PblMetaFunctionCallCtx_T *exc) {
  *exc = PblMetaFunctionCallCtx_T_DeclDefault;
  free(exc);
  return PblVoid_T_DeclDefault;
}
