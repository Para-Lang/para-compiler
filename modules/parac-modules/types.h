//
// Created by Luna-K on 09/10/2021.
//

#ifndef PARAC_MODULES_TYPES_H
#define PARAC_MODULES_TYPES_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

// String implementation - uses memory allocation -> located in heap
typedef struct __pbl_string_t {
    // Size of the allocated memory in bytes
    size_t byte_size;
    // Amount of the chars that can be written to - includes null char (\0)
    unsigned int allocated_len;
    // The length of the string
    unsigned int len;
    // The void* pointer to the allocated memory
    char* str;
} __pbl_string_t;

size_t __pbl_get_alloc_size_string_t(unsigned int len);
void __pbl_resize_string_t(__pbl_string_t* str, unsigned int len);
void __pbl_write_to_string_t(__pbl_string_t* str, unsigned int len_to_write, const char* content);
__pbl_string_t __pbl_allocate_string_t(unsigned int len, const char* content);
void __pbl_deallocate_string_t(__pbl_string_t *lvalue);

#ifdef __cplusplus
}
#endif

#endif //PARAC_MODULES_TYPES_H
