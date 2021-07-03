/// Main file
#include "__parac__.h"
#include <stdio.h>
#include <string.h>

ph_AnyType FunctionWithoutPointer(ph_AnyType arg_var)
{
    arg_var.var_name = "arg_var";
    // Checking the type by its name
    if (strcmp(arg_var.type_name, VAR_NAME_SIGNED_INT) == 0)
    {
        printf("Item passed - Name: %s Type: %s, Value: %i\n", arg_var.var_name, arg_var.type_name, *(int *)arg_var.var_pointer);
    }

    *(int *)arg_var.var_pointer = 2;
    return arg_var;
}

ph_AnyType FunctionWithPointer(ph_AnyType *arg_var)
{
    // Since the value is a pointer the name will not be reset, but stays the old value
    // arg_var->var_name = "arg_var";

    // Checking the type by its name
    if (strcmp(arg_var->type_name, VAR_NAME_SIGNED_INT) == 0)
    {
        printf("Item passed - Name: %s Type: %s, Value: %i\n", arg_var->var_name, arg_var->type_name, *(int *)arg_var->var_pointer);
    }

    // Assigning a new value
    *(int *)arg_var->var_pointer = 4;
    return *arg_var;
}

ph_Status Entry_Main()
{
    printf(" > Non-pointer Any-type value\n");
    int _var1 = 1; // Actual value
    ph_AnyType var1 = (ph_AnyType) {
        .var_pointer = &_var1,
        .var_name = "var1",
        .type_name = VAR_NAME_SIGNED_INT
    };

    printf(
        "Item created - Name: %s Type: %s, Value: %i\n",
        var1.var_name,
        var1.type_name,
        *(int *)var1.var_pointer
        );

    // Using another variable to store the value
    ph_AnyType additional_var = FunctionWithoutPointer(var1);
    additional_var.var_name = "additional_var"; // Setting the name after receiving the returned value

    printf(
        "Item returned - Name: %s Type: %s, Value: %i\n",
        additional_var.var_name,
        additional_var.type_name,
        *(int *)additional_var.var_pointer
        );

    printf(" > Pointer Any-type value\n");
    int _var2 = *( int*)var1.var_pointer; // Actual value
    ph_AnyType var2 = (ph_AnyType) {
        .var_pointer = &_var2,
        .var_name = "var2",
        .type_name = VAR_NAME_SIGNED_INT
    };

    printf(
        "Item created - Name: %s Type: %s, Value: %i\n",
        var2.var_name,
        var2.type_name,
        *(int *)var2.var_pointer
        );

    // Using another variable to store the value
    additional_var = FunctionWithPointer(&var2);
    additional_var.var_name = "additional_var"; // Setting the name after receiving the returned value

    printf(
        "Item returned - Name: %s Type: %s, Value: %i\n",
        additional_var.var_name,
        additional_var.type_name,
        *(int *)additional_var.var_pointer
        );

    return (ph_Status) { .status_code = 0 };
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
        return r.status_code;
    }
}