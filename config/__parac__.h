// Example __parac__.h file that won't be used, but will serve as an example for a finished build
#pragma once

#ifndef __PARAC___H_
#define __PARAC___H_

// If the code is included in an CPP environment which Para-C supports, it will be treated as regular C-code
#if __cplusplus
extern "C" {
#endif

// User Project Configuration
const char* __name__ = "";
const char* __description__ = "";
const char* __author__ = "";
const char* __version__ = "";
const char* __license__ = "";

/*
 Compiler Configuration -
 C-Compiler Paths are included so that using 'parac finish' the compilation will be automatically finished
*/
#define __PARAC_VERSION__ "Compiler-Inserted"

const char* __pcompiler_path__ = "";
const char* __ccompiler_path__ = "";

#if __cplusplus
}
#endif

#endif