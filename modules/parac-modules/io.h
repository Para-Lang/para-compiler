#include "types.h"

#ifndef IO_H
#define IO_H

#ifdef __cplusplus
extern "C" {
#endif

// Arguments struct for pbl_print (pbl_print_args_in)
typedef struct {
    pbl_string_t* out;
    const char end;
} pbl_print_args_t;

void pbl_print_args_in(pbl_print_args_t in);

/// @brief Prints the content of the passed string
/// @param out The string_t that should be printed
/// @param end The end character that should be printed at the end of the print
#define pbl_print(...) pbl_print_args_in((pbl_print_args_t){__VA_ARGS__});

#ifdef __cplusplus
}
#endif

#endif //IO_H
