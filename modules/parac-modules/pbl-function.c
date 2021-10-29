///
/// Function-related types and exception implementation
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

PblVoid_T PblDeallocateMetaFunctionCallCtxT(PblMetaFunctionCallCtx_T *ctx) {
  // only deallocate if the exception exists and is still defined. If not defined freeing would cause a SIGSEGV later on
  if (ctx->actual.exception != NULL && ctx->actual.exception->meta.defined)
  {
    PblDeallocateExceptionT(ctx->actual.exception);
  }

  // resetting the values
  *ctx = PblMetaFunctionCallCtx_T_DeclDefault;
  free(ctx);
  return PblVoid_T_DeclDefault;
}

PblException_T *PblAllocateExceptionType() {
  PblException_T *ptr = malloc(sizeof(PblException_T));
  *ptr = PblException_T_DeclDefault;
  return ptr;
}

PblException_T *PblGetExceptionT(PblString_T msg, PblString_T name, PblString_T filename, PblUInt_T line,
                                 PblString_T line_content, PblVoid_T *parent_exc, PblVoid_T *child_exc) {
  PblException_T *ptr = PblAllocateExceptionType();
  ptr->actual = (struct PblExceptionBase){
    .msg = msg, .name = name, .filename = filename, .line = line,
    .line_content = line_content, .parent_exc = parent_exc, .child_exc = child_exc
  };
  return ptr;
}

PblVoid_T PblRaiseNewException(PblMetaFunctionCallCtx_T* this_call_meta, PblException_T *exception) {
  this_call_meta->actual.is_failure = PblGetBoolT(true);
  this_call_meta->actual.failure_origin_ctx = this_call_meta;
  this_call_meta->actual.exception = exception;
  return PblVoid_T_DeclDefault;
}

PblVoid_T PblDeallocateExceptionT(PblException_T *exc) {
  PblDeallocateStringT(&exc->actual.msg);
  PblDeallocateStringT(&exc->actual.name);
  PblDeallocateStringT(&exc->actual.filename);
  PblDeallocateStringT(&exc->actual.line_content);

  *exc = PblException_T_DeclDefault;
  free(exc);
  return PblVoid_T_DeclDefault;
}

PblVoid_T PblCleanupExceptionContext(PblMetaFunctionCallCtx_T* cleanup_ctx) {
  // if an exception was raised -> cleanup the original context and all it's parents until reaching the cleanup_ctx
  // again
  if (cleanup_ctx->actual.is_failure.actual) {
    PblMetaFunctionCallCtx_T* current_ctx = cleanup_ctx->actual.failure_origin_ctx;
    PblMetaFunctionCallCtx_T* next_ctx;
    while (current_ctx != cleanup_ctx) {
      next_ctx = current_ctx->actual.call_origin_ctx;
      // only deallocate if the ctx exists and is still defined. If not defined, freeing would cause a SIGSEGV later on
      if (current_ctx->meta.defined) PblDeallocateMetaFunctionCallCtxT(current_ctx);
      current_ctx = next_ctx;
    }
  }
  PblDeallocateMetaFunctionCallCtxT(cleanup_ctx);
  return PblVoid_T_DeclDefault;
};