#include <stdio.h>
#include "io.h"


/// Prints the content of the passed string
void __pbl_print_base(__pbl_type_string* out, const char end)
{
    for (int i = 0; i < out->len; i++)
    {
        printf("%c", (char) out->str[i]);
    }
    printf("%c", end);
};

void __var_print(__pbl_print_args in)
{
    __pbl_type_string* out = in.out;
    const char end = in.end ? in.end : '\n';
    return __pbl_print_base(out, end);
}