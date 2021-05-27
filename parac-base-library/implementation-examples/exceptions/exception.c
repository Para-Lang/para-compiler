#include <stdio.h>
#include <stdbool.h>

typedef struct {
    bool is_exception;
    const char* exception;
    const char* traceback;
    bool is_null;
    int actual_value;
} ReturnTypeInt;

typedef struct {
    bool is_exception;
    const char* exception;
    const char* traceback;
    int status_code;
} ExitStatus;

typedef union {
    ExitStatus exit_r;
} EntryPoint;

ReturnTypeInt GenericFunction(bool error)
{
    int local_x = 4;  // local_ prefix is for the local scope
    
    ReturnTypeInt r = {
        .is_exception = error,
        .is_null = false,
        .actual_value = local_x
    };
    return r;
}

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

EntryPoint ExitStatusToEntryReturn(ExitStatus s)
{
  EntryPoint r = {
      .exit_r = s
  };
  return r;
}

// User defined main with mangling
EntryPoint Entry_Main()
{
    ReturnTypeInt r_int;

    // Compiler will automatically notice if there is a try-except and add the handling appropriately
    r_int = GenericFunction(false);
    if (r_int.is_exception)
        return ExitStatusToEntryReturn(HandleUncatchedException(r_int.exception, r_int.traceback));
    int local_actual_r = r_int.actual_value;  // actual name: actual_r - local_ prefix is for the local scope

    printf("Return of function that did not error: %i\n", local_actual_r);

    r_int = GenericFunction(true);
    if (r_int.is_exception)
        return ExitStatusToEntryReturn(HandleUncatchedException(r_int.exception, r_int.traceback));

    ExitStatus exit_r = { .status_code = 0 };
    return ExitStatusToEntryReturn(exit_r);
}

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