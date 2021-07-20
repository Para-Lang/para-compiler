/// ==========================================================
/// Compiler-Generated Header file for Base Content Management
/// ==========================================================
#pragma once

/// Imports
#include <stdbool.h>
#include <stdarg.h>
#include <stdlib.h>

#ifndef __PARAC___H_
#define __PARAC___H_

#if __cplusplus
extern "C" {
#endif

// =========================================
// User Project Configuration
// =========================================

const char* ph_name;
const char* ph_description;
const char* ph_author;
const char* ph_version;
const char* ph_license;

// =========================================
// Compiler Configuration
// C-Compiler Paths are included, so that
// using 'parac finish' the compilation can
// be automatically finished
// =========================================

#define __PARAC_VERSION__ "Compiler-Inserted"

const char* ph_para_compiler_path;
const char* ph_c_compiler_path;
const char* ph_pcl_path;

// =========================================
// Types definition
// =========================================

// Basic name declarations

#define VAR_NAME_SIGNED_CHAR "BUILT_IN_SIGNED_CHAR"
#define VAR_NAME_UNSIGNED_CHAR "BUILT_IN_UNSIGNED_CHAR"
#define VAR_NAME_CHAR "BUILT_IN_CHAR"
#define VAR_NAME_SIGNED_INT "BUILT_IN_SIGNED_INT"
#define VAR_NAME_UNSIGNED_INT "BUILT_IN_UNSIGNED_INT"
#define VAR_NAME_SIGNED_LONG "BUILT_IN_SIGNED_LONG"
#define VAR_NAME_UNSIGNED_LONG "BUILT_IN_UNSIGNED_LONG"
#define VAR_NAME_SIGNED_SHORT "BUILT_IN_SIGNED_SHORT"
#define VAR_NAME_UNSIGNED_SHORT "BUILT_IN_UNSIGNED_SHORT"
#define VAR_NAME_SIGNED_LONG_LONG "BUILT_IN_SIGNED_LONG_LONG"
#define VAR_NAME_UNSIGNED_LONG_LONG "BUILT_IN_UNSIGNED_LONG_LONG"
#define VAR_NAME_DEALLOCATED "DEALLOCATED_NULL"

/// Exit Status structure storing the basic values for a closing return aka. entry-point function return */
typedef struct ph_ExitStatus {
    bool is_exception;
    const char* exception;
    const char* traceback;
    int status_code;
} ph_Status;

/// Any type which contains a pointer to the specific variable
typedef struct ph_AnyType {
    void* var_pointer;
    char* type_name;
    bool built_in_type;
    size_t byte_size;
} ph_AnyType;

// =========================================
// Function Return Types
// =========================================

/// Undefined Base Return which serves as the base for all ReturnTypes.  Compiler-Generated
typedef struct ph_UndefBaseReturn {
    bool is_exception;
    const char* exception;
    const char* traceback;
    bool is_null;
} ph_UndefBaseReturn;

/// Para-C Return of Type int. Compiler-Generated
typedef struct ph_ReturnTypeInt {
    ph_UndefBaseReturn base;
    int actual_value;
} ph_ReturnTypeInt;

// =========================================
// Decorator Return Types - Function Pointer Types
// =========================================

typedef ph_ReturnTypeInt (*ph_DecoType_Int_Int)(int);

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
/// Decorator 'main_DecorateFunc' from the file <insert-file-name>
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
typedef struct main_DecorateFunc_WrapContext main_DecorateFunc_WrapContext;

/// Signature of the wrapper - Returns int and contains as parameters a int return function and an int
/// This type will be automatically generated for any wrapper, but only used in the decorator for correctly creating
/// the struct which will store the wrapper and wrapped function.
typedef ph_ReturnTypeInt (*main_DecorateFunc_Wrapper_Type)(main_DecorateFunc_WrapContext*, int); // R: int - P: struct, int

/// Context for the DecorateFunc Decorator. Contains a child_ctx element to point to a child if it exists. Contains
/// a wrapper function and wrapped function. The wrapped function should be NULL if child_ctx is populated.
typedef struct main_DecorateFunc_WrapContext {
    bool has_child_ctx;
    ph_DecoType_Int_Int wrapped_func;
    main_DecorateFunc_Wrapper_Type wrapper_func;
    main_DecorateFunc_WrapContext *child_ctx;
} main_DecorateFunc_WrapContext;

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Additional Function declarations
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

/// Deallocates the memory of the any_type and defuses the dangling pointer
void DeallocateAny(ph_AnyType*);
/// Changes the type of the AnyType, reallocated the memory to fit the specified memory and overwrites the properties
/// correctly
ph_AnyType* ChangeTypeAny(ph_AnyType *, char *, size_t, bool);

#if __cplusplus
}
#endif

#endif