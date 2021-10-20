#include <stdio.h>
#include "io.h"


/// Prints the content of the passed string
void __pbl_print_base(__pbl_string_t* out, const char end)
{
    for (int i = 0; i < out->len; i++)
    {
        printf("%c", (char) out->str[i]);
    }
    printf("%c", end);
};

void __pbl_print_args_in(__pbl_print_args_t in)
{
    __pbl_string_t* out = in.out;
    const char end = in.end ? in.end : '\n';
    return __pbl_print_base(out, end);
}