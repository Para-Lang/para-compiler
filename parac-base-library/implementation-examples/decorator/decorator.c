/*
 * A simple example file for showing the rough functionality of a decorator
 * Program-Plan:
 * Entry Function -> Call decorator -> Create struct for wrapper and function ->
 * Return new point to function -> Call function pointer
 */

/* Para-C imports */
#include "__parac__.h"

/* C Imports */
#include <stdio.h>

/* Actual user function that is defined by the user. main_ is added through the mangling */
ph_ReturnTypeInt main_func(int x)
{
    printf("Called decorated function - Passed argument: %i\n", x);

    /* Compiler generated return */
    ph_ReturnTypeInt r = {
        .base.is_exception = false,
        .base.is_null = false,
        .actual_value = 3
    };
    return r;
}

/* Actual user function that is defined by the user. main_ is added through the mangling */
ph_ReturnTypeInt main_func2(int x)
{
    printf("Called decorated function 2 with the same wrapper - Passed argument: %i\n", x);

    /* Compiler generated return */
    ph_ReturnTypeInt r = {
        .base.is_exception = false,
        .base.is_null = false,
        .actual_value = 3
    };
    return r;
}


/* -- Start of declaration : Decorator DecorateFunc -- */

// ----> Compiler generated ---->

typedef struct DecorateFunc_WrapContext DecorateFunc_WrapContext;

/// Signature of the wrapper - Returns int and contains as parameters a int return function and an int
/// This type will be automatically generated for any wrapper, but only used in the decorator for correctly creating
/// the struct which will store the wrapper and wrapped function.
typedef ph_ReturnTypeInt (*DecorateFunc_Wrapper_Type)(DecorateFunc_WrapContext*, int); // R: int - P: struct, int

/// Context for the DecorateFunc Decorator. Contains a child_ctx element to point to a child if it exists. Contains
/// a wrapper function and wrapped function. The wrapped function should be NULL if child_ctx is populated.
typedef struct DecorateFunc_WrapContext {
    bool has_child_ctx;
    ph_DecoType_Int_Int wrapped_func;
    DecorateFunc_Wrapper_Type wrapper_func;
    DecorateFunc_WrapContext *child_ctx;
} DecorateFunc_WrapContext;
// <---- Compiler generated <----

/// Defined wrapper for the function
/// @param call_ctx Call Context for the wrapper
/// @param x Example for how a user argument could look like
ph_ReturnTypeInt DecorateFunc_Wrapper(DecorateFunc_WrapContext *call_ctx, int x)
{
    printf("Called wrapper\n");

    // ----> Compiler generated ---->

    ph_ReturnTypeInt call_r;

    // Child Context is null -> Reached lowest level of wrapping
    if (!call_ctx->child_ctx && !call_ctx->has_child_ctx)
    {
        // Calling the wrapped function
        call_r = call_ctx->wrapped_func(x);
    }
    else
    {
        // Passing the context down one level to the other function
        call_r = call_ctx->child_ctx->wrapper_func(call_ctx->child_ctx, x);
    }

    int local_r = call_r.actual_value;
    // <---- Compiler generated <----

    printf("Finished function call\n");

    // ----> Compiler generated ---->

    ph_ReturnTypeInt func_r = {
        .base.is_exception = false,
        .base.is_null = false,
        .actual_value = local_r
    };

    // <---- Compiler generated <----
    return func_r;
}

/// Decorates a function and returns a struct containing the func and the wrapper specified for this decorator.
/// @param passable Passable struct that can either contain a function or an initialised wrapped struct that should
/// be wrapped again. In both cases the types must match with the target of the decorator to correctly pass
/// the arguments.
DecorateFunc_WrapContext DecorateFunc(DecorateFunc_WrapContext ctx)
{
    printf("Called decorator\n");

    // ----> Compiler generated ---->

    DecorateFunc_WrapContext new_ctx;
    // Child Context is null -> Reached lowest level of wrapping / The function does not have any more wrapping
    if (!ctx.child_ctx && !ctx.has_child_ctx && !ctx.wrapper_func)
    {
        new_ctx = (DecorateFunc_WrapContext) {
            .has_child_ctx = false,
            .wrapper_func = DecorateFunc_Wrapper,
            .wrapped_func = ctx.wrapped_func,
            .child_ctx = NULL
        };
    }
    else
    {
        // Creating a new context and passing the context as a child
        new_ctx = (DecorateFunc_WrapContext) {
            .has_child_ctx = true,
            .wrapper_func = DecorateFunc_Wrapper,
            .child_ctx = &ctx,
        };
    }
    // <---- Compiler generated <----

    return new_ctx;
}

/* -- End of Declaration : Decorator DecorateFunc-- */

int main()
{
    /* Decorating the main_func function */
    DecorateFunc_WrapContext p;
    p = (DecorateFunc_WrapContext) { .wrapped_func = &main_func };

    DecorateFunc_WrapContext deco_ctx = DecorateFunc(p);
    deco_ctx.wrapper_func(&deco_ctx, 5);  // Calls the function as if it was a normal one

    DecorateFunc_WrapContext deco_ctx4 = DecorateFunc(p);
    deco_ctx4.wrapper_func(&deco_ctx4, 10);

    /* Other function */

    p = (DecorateFunc_WrapContext) { .wrapped_func = &main_func2 };
    DecorateFunc_WrapContext deco_ctx5 = DecorateFunc(p);
    deco_ctx5.wrapper_func(&deco_ctx5, 15);

    /*
     * If the user attempts to call the decorator again it will result
     * in an error due to the wrapper calling itself to wrap itself. This is why
     * the compiler will automatically log a recursion error!
     *
     * Revision: This is possible now, through using a context module type and a context pointer in the background.
     * If the user calls the decorator to wrap the already wrapped context it will be passed as a child and the wrapped
     * method will be NULL, meaning the context will execute it's code and then call the function, which will execute
     * itself again. This also means the decorator will be able to handle multiple decorations without any issue.
     *
     * Note: Working except the pointer which loses its values after being passed
     */

    /* Wrapping the wrapped context */
    DecorateFunc_WrapContext deco_ctx6 = DecorateFunc(deco_ctx5);
    deco_ctx6.wrapper_func(&deco_ctx6, 20);

    /* Wrapping the wrapped context wrapping the wrapped context ... */
    DecorateFunc_WrapContext deco_ctx7 = DecorateFunc(deco_ctx6);
    DecorateFunc_WrapContext deco_ctx8 = DecorateFunc(deco_ctx7);
    DecorateFunc_WrapContext deco_ctx9 = DecorateFunc(deco_ctx8);
    deco_ctx9.wrapper_func(&deco_ctx9, 25);

    return 0;
}