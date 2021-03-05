//
// Created by Nicolas Klatzer on 04/03/2021.
//

#include <stdio.h>
#include <string.h>
#include "main.h"
#include "compiler/compile.h"
#include "compiler/compile_errors.h"


/// Runs the compilation process on the passed files / path
void run_compile(char* path, int argc, char *argv[])
{

}

/// Starting point for the para-c compiler
int main(int argc, char* argv[]) {

    printf("Para-C Compiler - %s\n", VERSION);
    if(argc>=2) {
        if (argc==2 && argv[1][0] == '-') {
            if (argv[1][1] == 'c') {
                printf("\nCollecting files . . .");
                if (argv[2] != NULL) {
                    printf("not yet implemented");
                } else {
                    printf(ANSI_COLOR_RED "\nNo file or directory passed for compilation!");
                }
                return 0;
            }
        }
        printf(ANSI_COLOR_RED "Unknown Command-Line Option!");
        return 0;
    }
    printf("\nOptions:");
    printf("\n  -c {file/directory}    Compiles the specified file or directory and generates"
           "a new directory containing the compiled c-code\n");
    return 0;
}
