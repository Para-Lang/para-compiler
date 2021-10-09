//
// Created by Nicol on 09/10/2021.
//

#include <malloc.h>
#include "types.h"

// String implementation

/// Gets the required byte_size
size_t __pbl_get_alloc_size_type_string(unsigned int len)
{
    unsigned int alloc_len = 0;
    // The size of the allocated memory should always be bigger than the actual content
    // The length DOES NOT include the end byte, but only the actual content
    if (len < 50) {
        alloc_len = 50;
    }
    else if (len >= 50) {
        while (alloc_len < len) alloc_len += 50;
    }
    return (alloc_len + 1) * sizeof(char);
}

void __pbl_resize_type_string(__pbl_type_string* str, unsigned int len)
{
    size_t byte_size = __pbl_get_alloc_size_type_string(len);

    // reallocating the memory with the new length - includes space for '\0' byte
    str->str = realloc(str->str, byte_size);
    str->allocated_len = byte_size / sizeof(char);
    str->byte_size = byte_size;
    str->len = len;
}

/// Writes onto a allocated memory the string content
/// @param len Length of the string (should not include null char)
/// @param content The content of the string that should be written to the allocated memory
void __pbl_write_to_string(__pbl_type_string* str, unsigned int len_to_write, const char* content)
{
    // smaller or equal means too little memory is available,
    // since even if it's equal the null-byte needs to be added as well
    if (__pbl_get_alloc_size_type_string(len_to_write) <= str->byte_size)
    {
        __pbl_resize_type_string(str, len_to_write);
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
__pbl_type_string __pbl_allocate_type_string(unsigned int len, const char* content)
{
    // allocated memory - length = len * size char + 1 (null character (\0))
    size_t byte_size = __pbl_get_alloc_size_type_string(len);

    char* alloc_begin = malloc(byte_size);
    __pbl_type_string str = {
        .byte_size = byte_size,
        .allocated_len = byte_size / sizeof(char),
        .len = len,
        .str = alloc_begin
    };
    __pbl_write_to_string(&str, len, content);
    return str;
}

/// Deallocates the entire memory for the string and resets it's values
void __pbl_deallocate_type_string(__pbl_type_string *lvalue)
{
    free(lvalue->str);
    lvalue->str = NULL;
    lvalue->allocated_len = 0;
    lvalue->byte_size = sizeof(NULL);
    lvalue->len = 0;
}