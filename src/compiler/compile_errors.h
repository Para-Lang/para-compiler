//
// Created by Nicol on 04/03/2021.
//
#pragma once

#include <stdio.h>

#ifndef PARA_C_COMPILE_ERRORS_H
#define PARA_C_COMPILE_ERRORS_H

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN    "\x1b[36m"
#define ANSI_COLOR_RESET   "\x1b[0m"

typedef struct {
    char *name;
    int code;
    char *msg;
} CompileError;

extern CompileError FILE_NOT_FOUND;

void close_with_error(CompileError error);

#endif //PARA_C_COMPILE_ERRORS_H
