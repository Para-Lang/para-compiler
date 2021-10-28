///
/// Exception Implementation
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "pbl-types.h"
#include "pbl-string.h"
#include "pbl-function.h"
#include "./included/va-opt.h"

#ifndef PARAC_MODULES_EXCEPTION_H
#define PARAC_MODULES_EXCEPTION_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Raise exception Macros ----------------------------------------------------------------------------------------

/// This a "one-liner" constructor, which will allocate a new exception and raise it (return to the caller of the
/// stack)
#define RAISE_EXCEPTION(exception, call_return_type)                                                                   \
  RaiseNewException(this_call_meta, exception);                                                                        \
  return call_return_type##_DeclDefault;

// ---- Invoke with Exception handling (in C or Para-C context) -------------------------------------------------------

#define CALL_FUNC_WITH_META_CTX(func, var_to_pass, unique_id, is_threaded, meta_ctx, args)                             \
  PblMetaFunctionCallCtx_T *unique_id##_##func = PblGetMetaFunctionCallCtxT(                                           \
      PblGetStringT(#func), PblGetBoolT(false), PblGetUIntT(0), is_threaded, NULL, meta_ctx, NULL                      \
 );                                                                                                                    \
  var_to_pass = func(unique_id##_##func IFN(args)(, args));                                                            \

// ---- Invoke and Catch Exception handling ---------------------------------------------------------------------------

#define C_BASE_EXCEPTION_CATCH_CONSTRUCTOR(func, var_to_pass, unique_id, is_threaded, meta_ctx, args)                  \
  CALL_FUNC_WITH_META_CTX(                                                                                             \
    func, var_to_pass, unique_id, is_threaded, &this_call_meta, IFN(args)(args)                                        \
  )                                                                                                                    \
  if (unique_id##_##func->actual.is_failure.actual) {                                                                  \
    this_call_meta.actual.is_failure = PblGetBoolT(true);                                                              \
    this_call_meta.actual.exception = unique_id##_##func->actual.exception;                                            \
    this_call_meta.actual.failure_origin_ctx =                                                                         \
      unique_id##_##func->actual.failure_origin_ctx ?                                                                  \
                                                    unique_id##_##func->actual.failure_origin_ctx                      \
                                                    :                                                                  \
                                                    unique_id##_##func;                                                \
  }

/// This is a "one-liner" constructor for functions that accept arguments and have a return, which will call the passed
/// function with the args (__VA_ARGS__) and return to the caller of the stack, if the called function returns with a
/// raised exception.
/// @param func The function that should be called with the passed variadic arguments
/// @param var_to_pass The variable the return of the function should be passed to
/// @param ctx_rtype The return type of the context (function) where this macro is used. If an exception occurs the
/// default value (_DeclDefault) will be returned.
/// @param unique_id The unique id the call ctx should be declared as. It follows the following scheme: unique##_##func
#define EXCEPTION_CATCH_FUNC_CONSTRUCTOR(func, var_to_pass, ctx_rtype, unique_id, args...)                             \
  CALL_FUNC_WITH_META_CTX(                                                                                             \
    func, var_to_pass, unique_id, this_call_meta->actual.is_threaded, this_call_meta, IFN(args)(args)                  \
  )                                                                                                                    \
  if (unique_id##_##func->actual.is_failure.actual) {                                                                  \
    this_call_meta->actual.is_failure = PblGetBoolT(true);                                                             \
    this_call_meta->actual.exception = unique_id##_##func->actual.exception;                                           \
    this_call_meta->actual.failure_origin_ctx = unique_id##_##func;                                                    \
    return ctx_rtype##_DeclDefault;                                                                                    \
  }

// --- Exception Implementation ---------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Long Double type
#define PblException_T_Size 4 * PblString_T_Size + PblUInt_T_Size + 2 * sizeof(void*)
/// Returns the declaration default for the type `PblException_T`
#define PblException_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblException_T)
/// Returns the definition default for the type `PblException_T`
#define PblException_T_DefDefault                                                                                      \
  PBL_DEFINITION_STRUCT_CONSTRUCTOR(PblException_T, .msg = PblString_T_DefDefault, .name = PblString_T_DefDefault,     \
                                    .filename = PblString_T_DefDefault, .line = PblUInt_T_DefDefault,                  \
                                    .line_content = PblString_T_DefDefault, .parent_exc = NULL, .child_exc = NULL)

struct PblExceptionBase {
  /// Returns the message of the exception
  PblString_T msg;
  /// Returns the name of the exception
  PblString_T name;
  /// Returns the filename where the exception occurred
  PblString_T filename;
  /// Returns the line where the exception occurred
  PblUInt_T line;
  /// Returns the content of the line - macro inserted
  PblString_T line_content;
  /// Returns the parent exception if it exists
  /// (Reserved for PblException_T)
  PblVoid_T *parent_exc;
  /// Returns the child exception if it exists
  /// (Reserved for PblException_T)
  PblVoid_T *child_exc;
};

/// Exception implementation
struct PblException PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(struct PblExceptionBase)
/// Exception implementation
typedef struct PblException PblException_T;

// ---- Helper Functions ----------------------------------------------------------------------------------------------

/**
 * @brief Allocates a new Exception type ctx, which is located in the heap
 * @return The new allocated exception (pointer)
 */
PblException_T *PblAllocateExceptionType();

/**
 * @brief Gets a new Exception Type, which is located in the heap
 * @return The newly created exception (pointer)
 */
PblException_T *PblGetExceptionT(PblString_T msg, PblString_T name, PblString_T filename, PblUInt_T line,
                                 PblString_T line_content, PblVoid_T *parent_exc, PblVoid_T *child_exc);

/**
 * @brief Raises a new exception by updating the local context info
 * @param this_call_meta The current context info that should be updated
 * @param exception The exception that was initialised
 */
PblVoid_T RaiseNewException(PblMetaFunctionCallCtx_T* this_call_meta, PblException_T *exception);

/**
 * @brief Deallocates the passed exception type and safely resets all values
 * @param exc The exception to deallocate
 */
PblVoid_T DeallocateExceptionT(PblException_T *exc);

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_EXCEPTION_H
