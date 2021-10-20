//
// Created by Nicol on 09/10/2021.
//

#include <malloc.h>
#include "types.h"

// String implementation

/// Gets the required byte_size for an allocation based on the passed length of the string.
/// The algorithm will always be a multiple of 50 + 1 (for null char '\0').
/// The calculated size is the next biggest multiple of 50 + 1, which is still bigger than the passed length.
size_t __pbl_get_alloc_size_string_t(unsigned int len)
{
    unsigned int alloc_len = 0;
    // The size of the allocated memory should always be bigger than the actual content
    // The length DOES NOT include the end byte, but only the actual content
    if (len < 50) {
        alloc_len = 50;
    }
    else if (len >= 50) {
        while (alloc_len <= len) alloc_len += 50;
    }
    return (alloc_len + 1) * sizeof(char);
}

/// Resizes the string by reallocating the memory - The required size will be calculated from the passed length.
/// The function used for the calculation is '__pbl_get_alloc_size_string_t'
/// @param str The string that should be reallocated
/// @param len The length of the string content that is used to calculate the required size
void __pbl_resize_string_t(__pbl_string_t* str, unsigned int len)
{
    size_t byte_size = __pbl_get_alloc_size_string_t(len);

    // reallocating the memory with the new length - includes space for '\0' byte
    str->str = realloc(str->str, byte_size);
    str->allocated_len = byte_size / sizeof(char);
    str->byte_size = byte_size;
    str->len = len;
}

/// Writes onto a allocated memory the string content
/// @param len Length of the string (should not include null char)
/// @param content The content of the string that should be written to the allocated memory
void __pbl_write_to_string_t(__pbl_string_t* str, unsigned int len_to_write, const char* content)
{
    // bigger or equal means that the required space is bigger than the actual space available,
    // equal is also included since even if it's equal the null-byte needs to be added as well (+1 size)s
    if (__pbl_get_alloc_size_string_t(len_to_write) >= str->byte_size)
    {
        __pbl_resize_string_t(str, len_to_write);
    }

    int i = 0;
    for (; i < len_to_write; i++)
    {
        str->str[i] = (char) content[i];
    }
    str->str[i] = '\0'; // adding end item
}

/// Allocates new memory for a new string
/// Default size is 50 - will be resized with additional space required
/// @param len Length of the string - will be used to calculate allocated memory space (should not include null char)
/// @param content The content of the string that should be written to the allocated memory
__pbl_string_t __pbl_allocate_string_t(unsigned int len, const char* content)
{
    // allocated memory - length = len * size char + 1 (null character (\0))
    size_t byte_size = __pbl_get_alloc_size_string_t(len);

    char* alloc_begin = malloc(byte_size);
    __pbl_string_t str = {
        .byte_size = byte_size,
        .allocated_len = byte_size / sizeof(char),
        .len = len,
        .str = alloc_begin
    };
    __pbl_write_to_string_t(&str, len, content);
    return str;
}

/// Deallocates the entire memory for the string and resets it's struct properties
void __pbl_deallocate_string_t(__pbl_string_t *lvalue)
{
    free(lvalue->str);
    lvalue->str = NULL;
    lvalue->allocated_len = 0;
    lvalue->byte_size = sizeof(NULL);
    lvalue->len = 0;
}