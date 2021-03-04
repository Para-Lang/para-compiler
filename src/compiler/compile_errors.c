//
// Created by Nicol on 04/03/2021.
//

#include "compile_errors.h"
#include <stdlib.h>

CompileError FILE_NOT_FOUND = {
    .name = "FILE_NOT_FOUND",
    .code = 2,
    .msg = "Failed to find the specified file"
} ;

void close_with_error(CompileError error) {
    printf(ANSI_COLOR_RED "Failed to compile selected files due to an exception occurring while running: \n");
    printf("%i - %s: %s", error.code, error.name, error.msg);
    exit(1);
}
