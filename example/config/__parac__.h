/// ==========================================================
///  Example __para__.h file that won't be used, but will serve as an example for a finished build
/// ==========================================================
#pragma once

/// Imports
#include <stdbool.h>

#ifndef __PARAC___H_
#define __PARAC___H_

// If the code is included in an CPP environment which Para supports,
// it will be treated as regular C-code
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
// using 'para finish' the compilation can
// be automatically finished
// =========================================

#define __PARAC_VERSION__ "Compiler-Inserted"

const char* ph_para_compiler_path;
const char* ph_c_compiler_path;
const char* ph_pcl_path;

#if __cplusplus
}
#endif

#endif