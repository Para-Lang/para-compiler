/* Para-C imports */
#include "__parac__.h"

/* C Imports */
#include <stdio.h>

/*
 * A generic function serving the purpose of just returning 4
 */
ReturnTypeInt GenericFunction(bool error)
{
    int local_x = 4;  // local_ prefix is for the local scope
    
    ReturnTypeInt r = {
        .base.is_exception = error,
        .base.is_null = false,
        .actual_value = local_x
    };
    return r;
}

/* Example Handler which will be used in the PCL (Para-C Core Library) */
ExitStatus HandleUncatchedException(const char* exception, const char* traceback)
{
    // do traceback stuff

    printf("An exception was raised\n");

    ExitStatus r = {
        .is_exception = true,
        .exception = exception,
        .traceback = traceback,
        .status_code = 1, // Input Para-C Status code
    };
    return r;
}

/* Converts the exit status to an Entry Type Return */
EntryPoint ExitStatusToEntryReturn(ExitStatus s)
{
  EntryPoint r = {
      .exit_r = s
  };
  return r;
}

/* User defined main with mangling */
EntryPoint Entry_Main()
{
    ReturnTypeInt r_int;

    // Compiler will automatically notice if there is a try-except and add the handling appropriately
    r_int = GenericFunction(false);
    if (r_int.base.is_exception)
        return ExitStatusToEntryReturn(HandleUncatchedException(r_int.base.exception, r_int.base.traceback));
    int local_actual_r = r_int.actual_value;  // actual name: actual_r - local_ prefix is for the local scope

    printf("Return of function that did not error: %i\n", local_actual_r);

    r_int = GenericFunction(true);
    if (r_int.base.is_exception)
        return ExitStatusToEntryReturn(HandleUncatchedException(r_int.base.exception, r_int.base.traceback));

    ExitStatus exit_r = { .status_code = 0 };
    return ExitStatusToEntryReturn(exit_r);
}

/*
 * Actual main method that will be the entry-point of the program.
 * Will be defined in the PCL (Para-C Core Library) with proper implementation and functionality.
 * This only serves as an example for how the exception system might work
 */
int main()
{
  EntryPoint r = Entry_Main();
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