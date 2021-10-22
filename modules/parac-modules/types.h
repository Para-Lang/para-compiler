//
// Created by Luna-K on 09/10/2021.
//

#ifndef PARAC_MODULES_TYPES_H
#define PARAC_MODULES_TYPES_H

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

/// parac string implementation - uses memory allocation -> located in heap
struct pblString_T {
    /// Size of the allocated memory in bytes
    size_t byte_size;
    /// Amount of the chars that can be written to - includes null char (\0)
    unsigned int allocated_len;
    /// The length of the string
    unsigned int len;
    /// The char* pointer to the allocated memory
    char* str;
};
typedef pblString_T pblString_T;

// String implementations

size_t pbl_get_alloc_size_string_t(unsigned int len);
void pbl_resize_string_t(pblString_T* str, unsigned int len);
void pbl_write_to_string_t(pblString_T* str, unsigned int len_to_write, const char* content);
pblString_T pbl_allocate_string_t(unsigned int len, const char* content);
void pbl_deallocate_string_t(pblString_T *lvalue);

#ifdef __cplusplus
}
#endif

#endif //PARAC_MODULES_TYPES_H
