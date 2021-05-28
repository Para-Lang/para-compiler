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


/* -- Start of declaration : Decorator DecorateFunc -- */

// --> Compiler generated -->
typedef struct DecorateFunc_WrapContext DecorateFunc_WrapContext;

/// Signature of the wrapper - Returns int and contains as parameters a int return function and an int
/// This type will be automatically generated for any wrapper, but only used in the decorator for correctly creating
/// the struct which will store the wrapper and wrapped functionj.
typedef ph_ReturnTypeInt (*DecorateFunc_Wrapper_Type)(DecorateFunc_WrapContext, int); // R: int - P: (*)(int), int

/// Context for the DecorateFunc Decorator. Contains a child_ctx element to point to a child if it exists. Contains
/// a wrapper function and wrapped function. The wrapped function should be NULL if child_ctx is populated.
typedef struct DecorateFunc_WrapContext {
    ph_DecoType_Int_Int wrapped_func;
    DecorateFunc_Wrapper_Type wrapper_func;
    struct DecorateFunc_WrapContext *child_ctx;
} DecorateFunc_WrapContext;
// <-- Compiler generated <--

/// Defined wrapper for the function
/// @param call_ctx Call Context for the wrapper
/// @param x Example for how a user argument could look like
ph_ReturnTypeInt DecorateFunc_Wrapper(DecorateFunc_WrapContext call_ctx, int x)
{
    printf("Called wrapper\n");

    // --> Compiler generated -->
    ph_ReturnTypeInt call_r;

    // Child Context is null -> Reached lowest level of wrapping
    if (!call_ctx.child_ctx)
    {
        // Calling the wrapped function
        call_r = call_ctx.wrapped_func(x);
    }
    else
    {
        // Passing the context down one level to the other function
        call_r = call_ctx.child_ctx->wrapper_func(*call_ctx.child_ctx, x);
    }

    int local_r = call_r.actual_value;
    // <-- Compiler generated <--

    printf("Finished function call\n");

    // --> Compiler generated -->
    ph_ReturnTypeInt func_r = {
        .base.is_exception = false,
        .base.is_null = false,
        .actual_value = local_r
    };
    // <-- Compiler generated <--
    return func_r;
}

/// Decorates a function and returns a struct containing the func and the wrapper specified for this decorator.
/// @param passable Passable struct that can either contain a function or an initialised wrapped struct that should
/// be wrapped again. In both cases the types must match with the target of the decorator to correctly pass
/// the arguments.
DecorateFunc_WrapContext DecorateFunc(DecorateFunc_WrapContext ctx)
{
    printf("Called decorator\n");

    // --> Compiler generated -->
    DecorateFunc_WrapContext new_ctx;
    // Child Context is null -> Reached lowest level of wrapping / The function does not have any more wrapping
    if (!ctx.child_ctx)
    {
        new_ctx = (DecorateFunc_WrapContext) {
            .wrapper_func = DecorateFunc_Wrapper,
            .wrapped_func = ctx.wrapped_func
        };
    }
    else

    {
        // Creating a new context and passing the context as a child
        new_ctx = (DecorateFunc_WrapContext) {
            .wrapper_func = DecorateFunc_Wrapper,
            .child_ctx = &ctx,
        };
    }
    // <-- Compiler generated <--

    return new_ctx;
}

/* -- End of Declaration : Decorator DecorateFunc-- */

int main()
{
    /*
     * Decorating the main_func function
     */
    DecorateFunc_WrapContext p = { .wrapped_func = main_func };

    DecorateFunc_WrapContext deco_ctx = DecorateFunc(p);
    deco_ctx.wrapper_func(deco_ctx, 5);  // Calls the function as if it was a normal one

    /*
     * If the user attempts to call the decorator again it will result
     * in an error due to the wrapper calling itself to wrap itself. This is why
     * the compiler will automatically log a recursion error!
     */
    // INVALID
    // DecorateFunc_WrapContext deco_ctx2 = DecorateFunc(DecorateFunc);
    // deco_ctx2.wrapper_func(deco_ctx2, 7);

    // DecorateFunc_WrapContext deco_ctx3 = DecorateFunc(deco_ctx1.wrapper_func);
    // deco_ctx2.wrapper_func(deco_ctx3, 10);

    DecorateFunc_WrapContext deco_ctx4 = DecorateFunc(p);
    deco_ctx4.wrapper_func(deco_ctx4, 10);

    return 0;
}