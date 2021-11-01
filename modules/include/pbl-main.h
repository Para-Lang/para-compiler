///
/// Main Functions, types and macros used inside the Para-C. This file includes no other Para-C headers, and serves as
/// the base for the entire base-lib implementation.
///
/// @author Luna-Klatzer

#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

#ifndef PARAC_MODULES_MAIN_H
#define PARAC_MODULES_MAIN_H

// ---- Main Functions ------------------------------------------------------------------------------------------------

void PblAbortWithCriticalError(int error_code, const char* string);

#endif//PARAC_MODULES_MAIN_H
