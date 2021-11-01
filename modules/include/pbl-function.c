///
/// Function-related types and exception implementation
///
/// @author Luna-Klatzer

#include "./pbl-function.h"

PblMetaFunctionCallCtx_T *PblAllocateMetaFunctionCallCtxT() {
  PblMetaFunctionCallCtx_T* ptr = PblMalloc(sizeof(PblMetaFunctionCallCtx_T));
  *ptr = PblMetaFunctionCallCtx_T_DefDefault;
  return ptr;
}

PblMetaFunctionCallCtx_T *PblGetMetaFunctionCallCtxT(PblString_T function_identifier, PblBool_T is_failure,
                                                     PblUInt_T arg_amount, PblBool_T is_threaded,
                                                     PblMetaFunctionCallCtx_T *failure_origin_ctx,
                                                     PblMetaFunctionCallCtx_T *call_origin_ctx,
                                                     PblException_T *exception) {
  PblMetaFunctionCallCtx_T *ptr = PblAllocateMetaFunctionCallCtxT();
  *ptr = PblMetaFunctionCallCtx_T_DefDefault;

  ptr->actual = (struct PblMetaFunctionCallCtxBase) {
    .function_identifier=function_identifier, .is_failure=is_failure, .arg_amount=arg_amount,
    .is_threaded=is_threaded, .failure_origin_ctx=failure_origin_ctx, .call_origin_ctx=call_origin_ctx,
    .exception=exception
  };
  return ptr;
}

PblVoid_T PblSafeDeallocateMetaFunctionCallCtxT(PblMetaFunctionCallCtx_T *ctx) {
  // Validate the pointer for safety measures
  ctx = PblValPtr((void *) ctx);

  if (ctx->meta.defined) {
    if (ctx->actual.exception != NULL) PblSafeDeallocateExceptionT(ctx->actual.exception);
    PblSafeDeallocateStringT(&(ctx->actual.function_identifier));

    // resetting the values
    *ctx = PblMetaFunctionCallCtx_T_DeclDefault;
    PblFree(ctx);
  }
  return PblVoid_T_DeclDefault;
}

PblException_T *PblAllocateExceptionType() {
  PblException_T *ptr = PblMalloc(sizeof(PblException_T));
  *ptr = PblException_T_DeclDefault;
  return ptr;
}

PblException_T *PblGetExceptionT(PblString_T msg, PblString_T name, PblString_T filename, PblUInt_T line,
                                 PblString_T line_content, PblVoid_T *parent_exc, PblVoid_T *child_exc) {
  PblException_T *ptr = PblAllocateExceptionType();

  // Using the Definition Default
  *ptr = PblException_T_DefDefault;
  ptr->actual = (struct PblExceptionBase){
    .msg = msg, .name = name, .filename = filename, .line = line,
    .line_content = line_content, .parent_exc = parent_exc, .child_exc = child_exc
  };

  return ptr;
}

PblVoid_T PblRaiseNewException(PblMetaFunctionCallCtx_T* this_call_meta, PblException_T *exception) {
  // Validate the pointer for safety measures
  this_call_meta = PblValPtr((void *) this_call_meta);
  exception = PblValPtr((void *) exception);

  this_call_meta->actual.is_failure = PblGetBoolT(true);
  this_call_meta->actual.failure_origin_ctx = this_call_meta;
  this_call_meta->actual.exception = exception;
  return PblVoid_T_DeclDefault;
}

// TODO! Add Deallocating function for deallocating exception parents and children

PblVoid_T PblSafeDeallocateExceptionT(PblException_T *exc) {
  // Validate the pointer for safety measures
  exc = PblValPtr((void *) exc);

  // only if the exception is still defined
  if (exc->meta.defined)
  {
    // deallocate if the values are defined -> if not, skip de-allocation
    if (exc->actual.msg.meta.defined) PblSafeDeallocateStringT(&(exc->actual.msg));
    if (exc->actual.msg.meta.defined) PblSafeDeallocateStringT(&(exc->actual.name));
    if (exc->actual.msg.meta.defined) PblSafeDeallocateStringT(&(exc->actual.filename));
    if (exc->actual.msg.meta.defined) PblSafeDeallocateStringT(&(exc->actual.line_content));

    *exc = PblException_T_DeclDefault;
    PblFree(exc);
  }
  return PblVoid_T_DeclDefault;
}

PblVoid_T PblCleanupExceptionContext(PblMetaFunctionCallCtx_T* cleanup_ctx) {
  // Validate the pointer for safety measures
  cleanup_ctx = PblValPtr((void *) cleanup_ctx);

  // if an exception was raised -> cleanup the original context and all it's parents until reaching the cleanup_ctx
  // again
  if (cleanup_ctx->actual.is_failure.actual) {
    PblMetaFunctionCallCtx_T* current_ctx = cleanup_ctx->actual.failure_origin_ctx;
    PblMetaFunctionCallCtx_T* next_ctx;
    while (current_ctx != cleanup_ctx && current_ctx != NULL) {
      next_ctx = current_ctx->actual.call_origin_ctx;
      PblSafeDeallocateMetaFunctionCallCtxT(current_ctx);
      current_ctx = next_ctx;
    }
  }
  PblSafeDeallocateMetaFunctionCallCtxT(cleanup_ctx);
  return PblVoid_T_DeclDefault;
};