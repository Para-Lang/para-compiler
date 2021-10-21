//
// Created by Nicol on 09/10/2021.
//

#include <malloc.h>
#include "types.h"

// String implementation

/// @brief Gets the required byte_size for an allocation based on the passed length of the string.
/// @note The algorithm will always be a multiple of 50 + 1 (for null char '\0').
/// The calculated size is the next biggest multiple of 50 + 1, which is still bigger than the passed length.
/// @param len The length of the actual string content, which will be used to calculate the allocation length.
/// @returns The size as size_t (int)
size_t pbl_get_alloc_size_string_t(unsigned int len)
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

/// @brief Resizes the string by reallocating the memory.
/// @note Automatically calculates the size of the new allocated memory based on the length. The function used for the
/// length calculation is 'pbl_get_alloc_size_string_t'
/// @param str The string that should be reallocated
/// @param len The length of the string content that is used to calculate the required size
void pbl_resize_string_t(pbl_string_t* str, unsigned int len)
{
    size_t byte_size = pbl_get_alloc_size_string_t(len);

    // reallocating the memory with the new length - includes space for '\0' byte
    str->str = realloc(str->str, byte_size);
    str->allocated_len = byte_size / sizeof(char);
    str->byte_size = byte_size;
    str->len = len;
}

/// @brief Writes onto the allocated memory the passed string content
/// @param len Length of the string (should not include null char)
/// @param content The content of the string that should be written to the allocated memory
void pbl_write_to_string_t(pbl_string_t* str, unsigned int len_to_write, const char* content)
{
    // bigger or equal means that the required space is bigger than the actual space available,
    // equal is also included since even if it's equal the null-byte needs to be added as well (+1 size)s
    if (pbl_get_alloc_size_string_t(len_to_write) >= str->byte_size)
    {
        pbl_resize_string_t(str, len_to_write);
    }

    int i = 0;
    for (; i < len_to_write; i++)
    {
        str->str[i] = (char) content[i];
    }
    str->str[i] = '\0'; // adding end item
}

/// @brief Allocates new memory for a new string
/// @note Default size/len is 50 - will be resized with additional space required using 'pbl_get_alloc_size_string_t'
/// @param len Length of the string - will be used to calculate allocated memory space (should not include null char)
/// @param content The content of the string that should be written to the allocated memory
/// @returns The new string type that was allocated
pbl_string_t pbl_allocate_string_t(unsigned int len, const char* content)
{
    // allocated memory - length = len * size char + 1 (null character (\0))
    size_t byte_size = pbl_get_alloc_size_string_t(len);

    char* alloc_begin = malloc(byte_size);
    pbl_string_t str = {
        .byte_size = byte_size,
        .allocated_len = byte_size / sizeof(char),
        .len = len,
        .str = alloc_begin
    };
    pbl_write_to_string_t(&str, len, content);
    return str;
}

/// @brief Deallocates the entire memory for the string and resets it's struct properties
/// @note Writes to the string with '\0' before freeing the memory
/// @param lvalue The value that should be de-allocated
void pbl_deallocate_string_t(pbl_string_t *lvalue)
{
    // writing \0 onto the entire space of memory
    char nullify[lvalue->len];
    for (int i = 0; i < lvalue->len; i++) nullify[i] = '\0';
    pbl_write_to_string_t(lvalue, lvalue->len, nullify);

    free(lvalue->str);
    lvalue->str = NULL;
    lvalue->allocated_len = 0;
    lvalue->byte_size = sizeof(NULL);
    lvalue->len = 0;
}