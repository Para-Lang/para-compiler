//
// Created by Luna-K on 09/10/2021.
//

#ifndef PARAC_MODULES_TYPES_H
#define PARAC_MODULES_TYPES_H

#include <stddef.h>

// String implementation - uses memory allocation -> located in heap
typedef struct __pbl_type_string {
    // Size of the allocated memory in bytes
    size_t byte_size;
    // Amount of the chars that can be written to - includes null char (\0)
    unsigned int allocated_len;
    // The length of the string
    unsigned int len;
    // The void* pointer to the allocated memory
    char* str;
} __pbl_type_string;

size_t __pbl_get_alloc_size_type_string(unsigned int len);
void __pbl_resize_type_string(__pbl_type_string* str, unsigned int len);
void __pbl_write_to_string(__pbl_type_string* str, unsigned int len_to_write, const char* content);
__pbl_type_string __pbl_allocate_type_string(unsigned int len, const char* content);
void __pbl_deallocate_type_string(__pbl_type_string *lvalue);

#endif //PARAC_MODULES_TYPES_H
