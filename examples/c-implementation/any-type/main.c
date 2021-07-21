/// Main file
#include "__parac__.h"
#include <stdio.h>
#include <string.h>
#include <malloc.h>

ph_AnyType FunctionWithoutPointer(ph_AnyType arg_var) {
    // Checking the type by its name
    if (strcmp(arg_var.type_name, VAR_NAME_SIGNED_INT) == 0)
    {
        printf(
            "Item passed - Type: %s, Value: %i, Addr: %p\n",
            arg_var.type_name,
            *(int *)arg_var.var_pointer,
            arg_var.var_pointer
            );
    }

    *(int *)arg_var.var_pointer = 2;
    return arg_var;
}

ph_AnyType FunctionWithPointer(ph_AnyType *arg_var) {
    // Checking the type by its name
    if (strcmp(arg_var->type_name, VAR_NAME_SIGNED_INT) == 0)
    {
        printf(
            "Item passed - Type: %s, Value: %i, Addr: %p\n",
            arg_var->type_name,
            *(int *)arg_var->var_pointer,
            arg_var->var_pointer
            );
    }

    // Assigning a new value
    *(int *)arg_var->var_pointer = 4;
    return *arg_var;
}

ph_Status Entry_Main() {
    printf(" > Non-pointer Any-type value (int)\n");

    ph_AnyType var1 = {
        .var_pointer = malloc(sizeof(int)),
        .byte_size = sizeof(int),
        .built_in_type = true,
        .type_name = VAR_NAME_SIGNED_INT
    };
    *(int *)var1.var_pointer = 1;

    printf(
        "Item created - Type: %s, Value: %i, Addr: %p\n", var1.type_name, *(int *)var1.var_pointer, var1.var_pointer
        );

    // Using another variable to store the value
    ph_AnyType var2 = FunctionWithoutPointer(var1);

    printf(
        "Item returned - Type: %s, Value: %i, Addr: %p\n", var2.type_name, *(int *)var2.var_pointer, var2.var_pointer
        );

    printf(" > Pointer Any-type value (int)\n");
    ph_AnyType var3 = {

        .var_pointer = malloc(sizeof(int)),
        .byte_size = sizeof(int),
        .built_in_type = true,
        .type_name = VAR_NAME_SIGNED_INT
    };
    *(int *)var3.var_pointer = *(int *) var1.var_pointer;

    printf(
        "Item created - Type: %s, Value: %i, Addr: %p\n", var3.type_name, *(int *)var3.var_pointer, var3.var_pointer
        );

    *(int *)var3.var_pointer = 3;

    printf(
        "Item overwritten - Type: %s, Value: %i, Addr: %p\n", var3.type_name, *(int *)var3.var_pointer, var3.var_pointer
    );

    // Variable storing the return -> is a pointer
    ph_AnyType var4 = FunctionWithPointer(&var3);
    printf(
        "Item returned - Type: %s, Value: %i, Addr: %p\n", var4.type_name, *(int *)var4.var_pointer, var4.var_pointer
        );

    printf(" > Non-pointer Any-type value (char)\n");
    var4 = *ChangeTypeAny(&var4, VAR_NAME_CHAR, sizeof(char), true);
    *(char *) var4.var_pointer = 'a';

    printf(
        "Item overwritten - Type: %s, Value: %c, Addr: %p\n", var4.type_name, *(char *) var4.var_pointer, var4.var_pointer
    );

    int _var5_len = 3;
    ph_AnyType var5[] = {
        {
            .var_pointer = malloc(sizeof(int)),
            .byte_size = sizeof(int),
            .built_in_type = true,
            .type_name = VAR_NAME_SIGNED_INT
        },
        {
            .var_pointer = malloc(sizeof(int)),
            .byte_size = sizeof(int),
            .built_in_type = true,
            .type_name = VAR_NAME_SIGNED_INT
        },
        {
            .var_pointer = malloc(sizeof(int)),
            .byte_size = sizeof(int),
            .built_in_type = true,
            .type_name = VAR_NAME_SIGNED_INT
        }
    };

    printf(" > Non Pointer Any-type value (int[])\n");
    for (int i = 0; i < 3; i++) {
        *(int *) var5[i].var_pointer = i;
        printf(
            "Item created - Type: %s, Index: %i, Value: %i, Addr: %p\n",
            var5[i].type_name,
            i,
            *(int *) var5[i].var_pointer,
            var5[i].var_pointer
        );
    }

    ph_Status _s = { .status_code = 0 };

    // Freeing memory
    DeallocateAny(&var1);
    DeallocateAny(&var2);
    DeallocateAny(&var3);
    DeallocateAny(&var4);
    for (int i = 0; i < _var5_len; i++) DeallocateAny(&var5[i]);

    return _s;
}

int main()
{
    ph_Status r = Entry_Main();
    if (r.is_exception)
    {
        // handle exceptions and log traceback
        printf("Here would be the traceback and error message\n");
    }
    else
    {
        exit(r.status_code);
    }
}