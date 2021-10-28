///
/// Exception Implementation
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "pbl-exception.h"

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

PblVoid_T RaiseNewException(PblMetaFunctionCallCtx_T* this_call_meta, PblException_T *exception) {
  this_call_meta->actual.is_failure = PblGetBoolT(true);
  this_call_meta->actual.failure_origin_ctx = this_call_meta;
  this_call_meta->actual.exception = exception;
  return PblVoid_T_DeclDefault;
}

PblVoid_T DeallocateExceptionT(PblException_T *exc) {
  PblDeallocateStringT(&exc->actual.msg);
  PblDeallocateStringT(&exc->actual.name);
  PblDeallocateStringT(&exc->actual.filename);
  PblDeallocateStringT(&exc->actual.line_content);

  *exc = PblException_T_DeclDefault;
  free(exc);
  return PblVoid_T_DeclDefault;
}