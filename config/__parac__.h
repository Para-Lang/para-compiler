/// ==========================================================
///  Example __parac__.h file that won't be used, but will serve as an example for a finished build
/// ==========================================================
#pragma once

/// Imports
#include <stdbool.h>

#ifndef __PARAC___H_
#define __PARAC___H_

/*
 * If the code is included in an CPP environment which Para-C supports,
 * it will be treated as regular C-code
 */
#if __cplusplus
extern "C" {
#endif

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// User Project Configuration
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
const char* ph_name_ = "example_parac_header";
const char* ph_description_ = "Example for the parac base header";
const char* ph_author_ = "Luna Klatzer";
const char* ph_version_ = "0.1";
const char* ph_license_ = "GPL-3.0";

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Compiler Configuration
/// C-Compiler Paths are included, so that using 'parac finish' the compilation can be automatically finished
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
#define __PARAC_VERSION__ "Compiler-Inserted"

const char* ph_pcompiler_path_ = "";
const char* ph_ccompiler_path_ = "";

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Types definition - Compiler-Generated
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

// ...

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Function Return Types
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

// ...

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Decorator Return Types - Function Pointer Types
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

// ...

/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
/// Additional Function declarations
/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#if __cplusplus
}
#endif

#endif