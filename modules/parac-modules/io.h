#include "types.h"

#ifndef IO_H
#define IO_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    __pbl_type_string* out;
    const char end;
} __pbl_print_args;

void __var_print(__pbl_print_args);

// __pbl_print(__pbl_type_string*, const char)
#define __pbl_print(...) __var_print((__pbl_print_args){__VA_ARGS__});

#ifdef __cplusplus
}
#endif

#endif //IO_H
