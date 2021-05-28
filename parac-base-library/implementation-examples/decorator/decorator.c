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

/*
 * Signature of the wrapper - Returns in this case int and contains as parameters a int return function and an int
 * This type will be automatically generated for any wrapper, but only used in the decorator for correctly creating
 * the struct which will store the wrapper and function.
 */
typedef ph_ReturnTypeInt (*DecorateFunc_WrapperType)(ph_ReturnTypeInt (*)(int), int); // R: int - P: (*)(int), int
/* Defined wrapper for the function */
ph_ReturnTypeInt DecorateFunc_Wrapper(ph_ReturnTypeInt (*local_f)(int), int x)
{
    printf("Called wrapper\n");
    int local_r = local_f(x).actual_value; // Ignoring exception checking in this example
    printf("Finished function call\n");

    ph_ReturnTypeInt r = {
        .base.is_exception = false,
        .base.is_null = false,
        .actual_value = local_r
    };
    return r;
}

typedef struct { ph_DecoType_Int_Int _func; DecorateFunc_WrapperType wrapper; } DecorateFuncDecoType;
/* Simple decorator */
DecorateFuncDecoType DecorateFunc(ph_ReturnTypeInt (*f)(int))
{
    printf("Called decorator\n");

    DecorateFuncDecoType r = { ._func = f, .wrapper = DecorateFunc_Wrapper, };
    return r;
}

/*
 * Signature of the wrapper - Returns in this case int and contains as parameters a int return function and an int
 * This type will be automatically generated for any wrapper, but only used in the decorator for correctly creating
 * the struct which will store the wrapper and function.
 */
typedef ph_ReturnTypeInt (*DecorateFunc2_WrapperType)(ph_ReturnTypeInt (*)(int), int); // R: int - P: (*)(int), int
/* Defined wrapper for the function */
ph_ReturnTypeInt DecorateFunc2_Wrapper(ph_ReturnTypeInt (*local_f)(int), int x)
{
    printf("Called wrapper\n");
    int local_r = local_f(x).actual_value; // Ignoring exception checking in this example
    printf("Finished function call\n");

    ph_ReturnTypeInt r = {
        .base.is_exception = false,
        .base.is_null = false,
        .actual_value = local_r
    };
    return r;
}

typedef struct { ph_DecoType_Int_Int _func; DecorateFunc2_WrapperType wrapper; } DecorateFunc2DecoType;
/* Simple decorator */
DecorateFunc2DecoType DecorateFunc2(ph_ReturnTypeInt (*f)(int))
{
    printf("Called decorator\n");

    DecorateFunc2DecoType r = { ._func = f, .wrapper = DecorateFunc2_Wrapper, };
    return r;
}

int main()
{
    /*
     * Decorating the main_func function
     */
    DecorateFuncDecoType deco_func1 = DecorateFunc(main_func);
    deco_func1.wrapper(deco_func1._func, 5);  // Calls the function as if it was a normal one

    /*
     * If the user attempted to call the decorator again it would result
     * in an error due to it calling itself to wrap itself. This is why
     * the compiler will automatically logs a recursion error in the function!
     */
    // INVALID
    // DecorateFuncDecoType deco_func2 = DecorateFunc(DecorateFunc);
    // deco_func2.wrapper(deco_func2._func, 7);

    // DecorateFuncDecoType deco_func3 = DecorateFunc(deco_func1.wrapper);
    // deco_func2.wrapper(deco_func3._func, 10);

    DecorateFunc2DecoType deco_func4 = DecorateFunc2(main_func);
    deco_func4.wrapper(deco_func4._func, 10);

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
     */

    return 0;
}