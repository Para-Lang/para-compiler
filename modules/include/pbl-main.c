///
/// Main Functions, types and macros used inside the Para-C. This file includes no other Para-C headers, and serves as
/// the base for the entire base-lib implementation.
///
/// @author Luna-Klatzer

#include "pbl-main.h"


void PblAbortWithCriticalError(int error_code, const char* string) {
  fprintf(stderr, "%s", string);
  exit(error_code);
}
