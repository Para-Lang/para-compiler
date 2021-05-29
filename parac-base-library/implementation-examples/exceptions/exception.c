/*
 * A simple example file for showing the rough functionality of an exception return and how it is handled.
 * Program-Plan:
 * Entry Function -> Trigger Regular Function -> Trigger Exception Function -> Convert and return correct exit status
 */

#include "__parac__.h"
#include <stdio.h>

/// A generic function serving the purpose of just returning
ph_ReturnTypeInt GenericFunction(bool error)
{
    int local_x = 4;  // local_ prefix is for the local scope

    ph_ReturnTypeInt r = {
        .base.is_exception = error,
        .base.is_null = false,
        .actual_value = local_x
    };
    return r;
}

/// Example Handler which will be used in the PCL (Para-C Core Library)
ph_ExitStatus HandleUncatchedException(const char* exception, const char* traceback)
{
    // do traceback stuff

    printf("An exception was raised\n");

    ph_ExitStatus r = {
        .is_exception = true,
        .exception = exception,
        .traceback = traceback,
        .status_code = 1, // Input Para-C Status code
    };
    return r;
}

/// Converts the exit status to an Entry Type Return
ph_EntryPoint ExitStatusToEntryReturn(ph_ExitStatus s)
{
    ph_EntryPoint r = {
      .exit_r = s
  };
  return r;
}

/// Handles a direct exception return which does not contain any try-except statements
ph_EntryPoint HandleExceptionReturn(ph_UndefBaseReturn r)
{
    ph_ExitStatus status = HandleUncatchedException(r.exception, r.traceback);
    return ExitStatusToEntryReturn(status);
}


/// User defined main with mangling
ph_EntryPoint Entry_Main()
{
    ph_ReturnTypeInt r_int;

    // Compiler will automatically notice if there is a try-except and add the handling appropriately
    r_int = GenericFunction(false);
    if (r_int.base.is_exception)
        return HandleExceptionReturn(r_int.base);
    int local_actual_r = r_int.actual_value;  // actual name: actual_r - local_ prefix is for the local scope

    printf("Return of function that did not error: %i\n", local_actual_r);

    r_int = GenericFunction(true);
    if (r_int.base.is_exception)
        return HandleExceptionReturn(r_int.base);

    ph_ExitStatus exit_r = { .status_code = 0 };
    return ExitStatusToEntryReturn(exit_r);
}

/// Actual main method that will be the entry-point of the program.
/// Will be defined in the PCL (Para-C Core Library) with proper implementation and functionality.
/// This only serves as an example for how the exception system might work
int main()
{
    ph_EntryPoint r = Entry_Main();
    if (r.exit_r.is_exception)
    {
        // handle exceptions and log traceback
        printf("Here would be the traceback and error message\n");
    }
    else
    {
        return r.exit_r.status_code;
    }
}