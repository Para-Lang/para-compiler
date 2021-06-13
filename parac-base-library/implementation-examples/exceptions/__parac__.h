/// ==========================================================
/// Compiler-Generated Header file for Base Content Management
/// ==========================================================
#pragma once

/// Imports
#include <stdbool.h>

#ifndef __PARAC___H_
#define __PARAC___H_

/* If the code is included in an CPP environment which Para-C supports, it will be treated as regular C-code */
#if __cplusplus
extern "C" {
#endif

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// User Project Configuration
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
const char* ph_name;
const char* ph_description;
const char* ph_author;
const char* ph_version;
const char* ph_license;

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Compiler Configuration
/// C-Compiler Paths are included, so that using 'parac finish' the compilation can be automatically finished
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#define __PARAC_VERSION__ "Compiler-Inserted"

const char* ph_para_compiler_path;
const char* ph_c_compiler_path;
const char* ph_pcl_path;

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Types definition - Compiler-Generated
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

/// Exit Status structure storing the basic values for a closing return aka. entry-point function return
typedef struct {
    bool is_exception;
    const char* exception;
    const char* traceback;
    int status_code;
} ph_Status;

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Function Return Types
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

/// Undefined Base Return which serves as the base for all Return-Types
typedef struct {
    bool is_exception;
    const char* exception;
    const char* traceback;
    const char* call_stack;
    bool is_null;
} ph_UndefBaseReturn;

/// Para-C Return of Type int. Compiler-Generated
typedef struct {
    ph_UndefBaseReturn base;
    int actual_value;
} ph_ReturnTypeInt;

/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
/// Additional Function declarations
/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#if __cplusplus
}
#endif

#endif