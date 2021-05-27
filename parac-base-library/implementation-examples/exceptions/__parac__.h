/* Compiler-Generated Header file for Base Content Managment */
#pragma once

#include <stdbool.h>

#ifndef __PARAC___H_
#define __PARAC___H_

/* If the code is included in an CPP environment which Para-C supports, it will be treated as regular C-code */
#if __cplusplus
extern "C" {
#endif

/* User Project Configuration */
const char* ph_name_ = "exceptions_example";
const char* ph_description_ = "Example for showing how the exceptions 'should' work";
const char* ph_author_ = "Luna Klatzer";
const char* ph_version_ = "0.1";
const char* ph_license_ = "GPL-3.0";

/*
 * Compiler Configuration -
 * C-Compiler Paths are included so that using 'parac finish' the compilation will be automatically finished
 */
#define __PARAC_VERSION__ "Compiler-Inserted"

const char* ph_pcompiler_path_ = "";
const char* ph_ccompiler_path_ = "";

/*
 * Types definition - Compiler-Generated
 */

/* EntryPoint definition. Only here to not break the system since the macros do not exist yet in the PCL */

/* Exit Status structure storing the basic values for a closing return aka. entry-point function return */
typedef struct {
    bool is_exception;
    const char* exception;
    const char* traceback;
    int status_code;
} ph_ExitStatus;

/* Type defining the EntryPoint of a Program */
typedef union {
    ph_ExitStatus exit_r;
} ph_EntryPoint;

/*
 * Return Types - Compiler-Generated
 */

/* Undefined Base Return which serves as the base for all ReturnTypes */
typedef struct {
    bool is_exception;
    const char* exception;
    const char* traceback;
    bool is_null;
} ph_UndefBaseReturn;

/* Para-C Return of Type int. Compiler-Generated */
typedef struct {
    ph_UndefBaseReturn base;
    int actual_value;
} ph_ReturnTypeInt;

#if __cplusplus
}
#endif

#endif