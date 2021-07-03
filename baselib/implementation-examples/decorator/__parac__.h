/// ==========================================================
/// Compiler-Generated Header file for Base Content Management
/// ==========================================================
#pragma once

/// Imports
#include <stdbool.h>
#include <stdarg.h>

#ifndef __PARAC___H_
#define __PARAC___H_

/*
 * If the code is included in an CPP environment which Para-C supports,
 * it will be treated as regular C-code
 */
#if __cplusplus
extern "C" {
#endif

/// =========================================
/// User Project Configuration
/// =========================================
const char* ph_name;
const char* ph_description;
const char* ph_author;
const char* ph_version;
const char* ph_license;

/// =========================================
/// Compiler Configuration
/// C-Compiler Paths are included, so that
/// using 'parac finish' the compilation can
/// be automatically finished
/// =========================================
#define __PARAC_VERSION__ "Compiler-Inserted"

const char* ph_para_compiler_path;
const char* ph_c_compiler_path;
const char* ph_pcl_path;

/// =========================================
/// Types definition
/// =========================================

/// Exit Status structure storing the basic values for a closing return aka. entry-point function return */
typedef struct ph_ExitStatus {
    bool is_exception;
    const char* exception;
    const char* traceback;
    int status_code;
} ph_Status;

/// =========================================
/// Function Return Types
/// =========================================

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

/// =========================================
/// Decorator Return Types - Function Pointer Types
/// =========================================

typedef ph_ReturnTypeInt (*ph_DecoType_Int_Int)(int);

/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
/// Decorator 'main_DecorateFunc' from the file <insert-file-name>
/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
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

/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
/// Additional Function declarations
/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#if __cplusplus
}
#endif

#endif