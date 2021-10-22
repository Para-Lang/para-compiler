#include <stdio.h>
#include "io.h"

void pbl_print_base(pblString_T* out, const char end)
{
    for (int i = 0; i < out->len; i++)
    {
        printf("%c", (char) out->str[i]);
    }
    printf("%c", end);
}

void pbl_print_args_in(pbl_print_args_t in)
{
    pblString_T* out = in.out;
    const char end = in.end ? in.end : '\n';
    return pbl_print_base(out, end);
}
