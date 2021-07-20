/*
 * A simple example file for showing the rough functionality of a decorator
 * Program-Plan:
 * Entry Function -> Call decorator -> Create struct for wrapper and function ->
 * Return new point to function -> Call function pointer
 */

#include "decorator.h"

/* C Imports */
#include <stdio.h>

/* -- Start of declaration : Decorator DecorateFunc -- */

// ----> Compiler generated ---->

/// Defined wrapper for the function
/// @param call_ctx Call Context for the wrapper
/// @param x Example for how a user argument could look like
ph_ReturnTypeInt main_DecorateFunc_Wrapper(main_DecorateFunc_WrapContext *call_ctx, int x)
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
main_DecorateFunc_WrapContext DecorateFunc(main_DecorateFunc_WrapContext *ctx)
{
    printf("Called decorator\n");

    // ----> Compiler generated ---->

    main_DecorateFunc_WrapContext new_ctx;
    // Child Context is null -> Reached lowest level of wrapping / The function does not have any more wrapping
    if (!ctx->child_ctx && !ctx->has_child_ctx && !ctx->wrapper_func)
    {
        new_ctx = (main_DecorateFunc_WrapContext) {
            .has_child_ctx = false,
            .wrapper_func = main_DecorateFunc_Wrapper,
            .wrapped_func = ctx->wrapped_func,
            .child_ctx = NULL
        };
    }
    else
    {
        // Creating a new context and passing the context as a child
        new_ctx = (main_DecorateFunc_WrapContext) {
            .has_child_ctx = true,
            .wrapper_func = main_DecorateFunc_Wrapper,
            .child_ctx = ctx,
        };
    }
    // <---- Compiler generated <----

    return new_ctx;
}

/* -- End of Declaration : Decorator DecorateFunc -- */
