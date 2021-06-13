/// Main file
#include "__parac__.h"
#include "decorator.h"
#include <stdio.h>

/// Actual user function that is defined by the user. main_ is added through the mangling
ph_ReturnTypeInt main_func(int x)
{
    printf("Called decorated function - Passed argument: %i\n", x);

    /* Compiler generated return */
    return (ph_ReturnTypeInt) {
        .base.is_exception = false,
        .base.is_null = false,
        .actual_value = 3
    };
}

/// Actual user function that is defined by the user. main_ is added through the mangling
ph_ReturnTypeInt main_func2(int x)
{
    printf("Called decorated function 2 with the same wrapper - Passed argument: %i\n", x);

    /* Compiler generated return */
    return (ph_ReturnTypeInt) {
        .base.is_exception = false,
        .base.is_null = false,
        .actual_value = 3
    };
}

ph_Status Entry_Main()
{
    /* Decorating the main_func function */
    main_DecorateFunc_WrapContext p;
    p = (main_DecorateFunc_WrapContext) { .wrapped_func = &main_func };

    main_DecorateFunc_WrapContext deco_ctx = DecorateFunc(&p);
    deco_ctx.wrapper_func(&deco_ctx, 5);  // Calls the function as if it was a normal one

    main_DecorateFunc_WrapContext deco_ctx4 = DecorateFunc(&p);
    deco_ctx4.wrapper_func(&deco_ctx4, 10);

    /* Other function */

    p = (main_DecorateFunc_WrapContext) { .wrapped_func = &main_func2 };
    main_DecorateFunc_WrapContext deco_ctx5 = DecorateFunc(&p);
    deco_ctx5.wrapper_func(&deco_ctx5, 15);

    /*
     * If the user attempts to call the decorator again it will result
     * in an error due to the wrapper calling itself to wrap itself. This is why
     * the compiler will automatically log a recursion error!
     *
     *  Revision: This is possible now, through using a context module type and a context pointer in the background.
     *   If the user calls the decorator to wrap the already wrapped context it will be passed as a child and the wrapped
     *   method will be NULL, meaning the context will execute it's code and then call the function, which will execute
     *   itself again. This also means the decorator will be able to handle multiple decorations without any issue.
     *
     *  Note: Working except the pointer which loses its values after being passed
     *
     *  Revision 2: The bug has been fixed. It was a result of the pointer inside DecorateFunc pointing to a copy of
     *  the context that was passed aka. the parameter. Therefore it pointed to an position that then got lost since
     *  the value was not passed as a pointer but as the literal value meaning it was destroyed afterwards aka. the
     *  values were lost to nothingness.
     */

    /* Wrapping the wrapped context */
    main_DecorateFunc_WrapContext deco_ctx6 = DecorateFunc(&deco_ctx5);
    deco_ctx6.wrapper_func(&deco_ctx6, 20);

    /* Wrapping the wrapped context wrapping the wrapped context ... */
    main_DecorateFunc_WrapContext deco_ctx7 = DecorateFunc(&deco_ctx6);
    main_DecorateFunc_WrapContext deco_ctx8 = DecorateFunc(&deco_ctx7);
    main_DecorateFunc_WrapContext deco_ctx9 = DecorateFunc(&deco_ctx8);

    printf("Calling wrapper that was wrapped multiple times\n");
    deco_ctx9.wrapper_func(&deco_ctx9, 25);

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