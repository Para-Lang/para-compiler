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
     * If the user attempted to call the decorator again it would result
     * in an error due to it calling itself to wrap itself. This is why
     * the compiler will automatically logs a recursion error in the function!
     */
    // INVALID
    // DecorateFunc_Wrapped deco_func2 = DecorateFunc(DecorateFunc);
    // deco_func2.wrapper(deco_func2._func, 7);

    // DecorateFunc_Wrapped deco_func3 = DecorateFunc(deco_func1.wrapper);
    // deco_func2.wrapper(deco_func3._func, 10);

    // DecorateFunc2_DecoRetType deco_func4 = DecorateFunc2(main_func);
    // deco_func4.wrapper(deco_func4._func, 10);

    /*
     * Currently it is also planned to have decorators wrap decorators, but a major issue arising with that is the
     * management of function return.
     *
     * Example:
     *  A decorator wraps a function and gets wrapped by another function, meaning when it is called the first parameter
     *  is going to be the decorated function (wrapper function) instead of the function pointer for the decorator itself
     *  meaning it will then not be able to call the function since also with other parameters these will be passed
     *  into a function expecting a function pointer resulting in a recursion and segmentation error.
     *
     * Possible solution:
     *  A possible solution to that issue is to pass all functions in the parameters and check their types. Possibly
     *  with a Para-C Core Library Type Struct unionising these types and using another type signalising the type making
     *  it possible to compare the types and then pass everything accordingly. This could be complex though, since
     *  it would mean a lot of checking and type comparisons would need to be done. A user attempting to work with that
     *  will likely not want to remember all types since it would restrict modularity. Therefore a possible function
     *  type should be used where a new struct is created storing the function. This would still need the passing of the
     *  parameter but it would work inside a structure where currently the only function important is the one to call
     *  next.
     *
     * Note: Currently being worked on
     */

    return 0;
}