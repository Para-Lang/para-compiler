//
// Created by Nicolas Klatzer on 04/03/2021.
//
#pragma once

#include <stdio.h>

#ifndef PARA_C_COMPILE_H
#define PARA_C_COMPILE_H

FILE *fptr;

// Compiles a directory and compiles every file
// @param path Path of the directory
#define compile_dir(...) compile_dir_wrapper((compile_dir_args){__VA_ARGS__});

int get_size_of_file(FILE *fptr);
char* compile_file(char* path);

#endif //PARA_C_COMPILE_H
