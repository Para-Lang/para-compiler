//
// Created by Nicolas Klatzer on 04/03/2021.
//

#include <stdbool.h>
#include "compile.h"
#include "compile_errors.h"

// Runs through a file and gets its size (amount of characters)
// @return The amount of characters in ints
int get_size_of_file(FILE *fptr) {
    char c;
    int count = 0;
    for (c = (char) getc(fptr); c != EOF; c = (char) getc(fptr)) {
        count++;
    }
    return count;
}

// Compiles a .para file and converts it to .c
// @param path Path of the file (relative or absolute path)
// @return The file in a char[] (string) format that can be written to a file
char* compile_file(char* path) {
    fptr = fopen(path, "r");

    CompileError error;
    if (fptr == NULL) {
        char msg[512];
        error = FILE_NOT_FOUND;
        snprintf(msg, sizeof(msg), "Failed to compile file at path: %s", path);
        error.msg = msg;
        return "";
    }

    // Creating a new string containing the entire content of the file
    // The length will be exactly the length of all characters combined
    char file[get_size_of_file(fptr)];
    char* compiled_file = file;

    fclose(fptr);
    return compiled_file;
}

// Compiles a directory and compiles every file
// @param path Path of the directory
void compile_dir_base(char* path, bool ignore_others) {

}

typedef struct {
    char* path;
    bool ignore_others;
} compile_dir_args;

void compile_dir_wrapper(compile_dir_args args) {
    // Defaults to false if it wasn't passed
    bool ignore_others = args.ignore_others ? args.ignore_others : false;
    return compile_dir_base(args.path, ignore_others);
}