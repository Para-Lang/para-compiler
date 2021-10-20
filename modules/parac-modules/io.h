#include "types.h"

#ifndef IO_H
#define IO_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    __pbl_string_t* out;
    const char end;
} __pbl_print_args_t;

void __pbl_print_args_in(__pbl_print_args_t in);

// __pbl_print(__pbl_string_t*, const char)
#define __pbl_print(...) __pbl_print_args_in((__pbl_print_args_t){__VA_ARGS__});

#ifdef __cplusplus
}
#endif

#endif //IO_H
