/// ==========================================================
/// Compiler-Generated Header file for Base Content Management
/// ==========================================================

#include <stdio.h>
#include <malloc.h>
#include "__parac__.h"

// =========================================
// User Project Configuration
// =========================================
const char* ph_name = "decorator_example";
const char* ph_description = "Example for showing the functionality of decorators";
const char* ph_author = "Luna Klatzer";
const char* ph_version = "0.1";
const char* ph_license = "GPL-3.0";

// =========================================
// Compiler Configuration
// C-Compiler Paths are included, so that
// using 'parac finish' the compilation can
// be automatically finished
// =========================================

const char* ph_para_compiler_path = "";
const char* ph_c_compiler_path = "";
const char* ph_pcl_path = "";

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
// Additional Function declarations
// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

ph_AnyType* ChangeTypeAny(ph_AnyType *lvalue, char *type_name, size_t byte_size, bool built_in_type) {
    lvalue->var_pointer = realloc(lvalue->var_pointer, byte_size);
    lvalue->type_name = type_name;
    lvalue->byte_size = byte_size;
    lvalue->built_in_type = built_in_type;
    return lvalue;
}

void DeallocateAny(ph_AnyType *lvalue) {
    free(lvalue->var_pointer);
    lvalue->var_pointer = NULL;
    lvalue->type_name = VAR_NAME_DEALLOCATED;
    lvalue->byte_size = sizeof(NULL);
    lvalue->built_in_type = true;
}