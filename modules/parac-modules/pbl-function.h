///
/// Function-related types
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "pbl-string.h"
#include "pbl-types.h"

#ifndef PARAC_MODULES_FUNCTION_H
#define PARAC_MODULES_FUNCTION_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Meta Type -----------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL MetaFunctionCallCtx type
#define PblMetaFunctionCallCtx_T_Size \
  PblBool_T_Size + PblUInt_T_Size + PblBool_T_Size + 2 * sizeof(PblMetaFunctionCallCtx_T*) + sizeof(NULL)
/// Returns the declaration default for the type `PblMetaFunctionCallCtx_T`
#define PblMetaFunctionCallCtx_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblMetaFunctionCallCtx_T)
/// Returns the definition default for the type `PblMetaFunctionCallCtx_T`
#define PblMetaFunctionCallCtx_T_DefDefault                                                                            \
  PBL_DEFINITION_STRUCT_CONSTRUCTOR(PblMetaFunctionCallCtx_T, .function_identifier=PblString_T_DefDefault,             \
                                    .is_failure = PblBool_T_DefDefault,  .arg_amount = PblUInt_T_DefDefault,           \
                                    .is_threaded = PblBool_T_DefDefault, .failure_origin_ctx = NULL,                   \
                                    .call_origin_ctx = NULL, .exception = NULL)

/// Base Meta Type passed to all functions
struct PblMetaFunctionCallCtxBase {
  /// Returns the function name - identifier
  PblString_T function_identifier;
  /// Returns whether the function failed due to an exception occurring
  PblBool_T is_failure;
  /// Returns the amount of arguments passed
  PblUInt_T arg_amount;
  /// Returns whether the function is threaded -> in an thread / threaded context
  PblBool_T is_threaded;
  /// Returns the origin meta variable for the function where the exception occurred
  /// Only available when is_failure is true
  /// (Reserved for PblMetaFunctionCallCtx_T)
  void* failure_origin_ctx;
  /// Returns the call origin ctx, which called the function associated with *this* context
  /// (Reserved for PblMetaFunctionCallCtx_T)
  void* call_origin_ctx;
  /// Returns the exception whether one was raised
  /// Only available when is_failure is true
  /// (Reserved for PblException_T)
  void* exception;
};

struct PblMetaFunctionCallCtx PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(struct PblMetaFunctionCallCtxBase)

/// Base Meta Type passed to all functions
typedef struct PblMetaFunctionCallCtx PblMetaFunctionCallCtx_T;

// ---- Helper Functions ----------------------------------------------------------------------------------------------

/**
 * @brief Allocates a new function call ctx, which will be located in the heap to store the function info publicly
 * as long as necessary, and avoid the destruction after leaving the function stack
 * @return The new allocated ctx (pointer)
 */
PblMetaFunctionCallCtx_T *PblAllocateMetaFunctionCallCtxT();

/**
 * @brief Gets a new function call ctx, which will be located in the heap
 * @return The newly created function call ctx (pointer)
 */
PblMetaFunctionCallCtx_T *PblGetMetaFunctionCallCtxT(PblString_T function_identifier, PblBool_T is_failure,
                                                     PblUInt_T arg_amount, PblBool_T is_threaded,
                                                     PblMetaFunctionCallCtx_T *failure_origin_ctx,
                                                     PblMetaFunctionCallCtx_T *call_origin_ctx,
                                                     PblVoid_T *exception);

/**
 * @brief Deallocates the passed function call ctx and safely resets all values
 * @param exc The function call ctx to deallocate
 */
PblVoid_T PblDeallocateMetaFunctionCallCtxT(PblMetaFunctionCallCtx_T *exc);

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_FUNCTION_H
