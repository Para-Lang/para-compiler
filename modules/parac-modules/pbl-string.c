///
/// String Implementation based on dynamic memory allocation
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "./pbl-string.h"
#include "./pbl-types.h"
#include <malloc.h>
#include <stdbool.h>
#include <string.h>

/**
 * @brief Gets the Length of a C string (const char*)
 * @param content The char array (pointer)
 * @return The length as Para-C Int
 */
PblUInt_T PblGetLengthOfCString(const char *content)
{
  return PblGetUIntT(strlen(content));
}

/**
 * @brief This directly converts a char* to a Para-C string type
 * @param content The char array (pointer)
 * @return The new Para-C string type, which was created using `PblAllocateStringT`
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblString_T PblGetStringT(const char *content)
{
  return PblCreateStringT(content, PblGetLengthOfCString(content));
}

/**
 * @brief Gets the required byte_size for an allocation based on the passed length of the string.
 * @note The algorithm will always be a multiple of 50 + 1 (for null char '\0').
 * The calculated size is the next biggest multiple of 50 + 1, which is still bigger than the passed length.
 * @param len The length of the actual string content, which will be used to calculate the allocation length.
 * @returns The size as size_t (int)
 */
PblSize_T PblGetAllocSizeStringT(PblUInt_T len) {
  unsigned int alloc_len = 0;
  // The size of the allocated memory should always be bigger than the actual content
  // The length DOES NOT include the end byte, but only the actual content
  if (len.actual < 50) {
    alloc_len = 50;
  } else if (len.actual >= 50) {
    while (alloc_len <= len.actual) alloc_len += 50;
  }
  return PblGetSizeT((alloc_len + 1) * sizeof(char));
}

/**
 * @brief Resizes the string by reallocating the memory.
 * @note Automatically calculates the size of the new allocated memory based on the length. The function used for the
 * length calculation is `PblGetAllocSizeStringT`
 * @param str The string that should be reallocated
 * @param len The length of the string content that is used to calculate the required size
 */
void PblResizeStringT(PblString_T *str, PblUInt_T len) {
  PblSize_T byte_size = PblGetAllocSizeStringT(len);

  // reallocating the memory with the new length - includes space for '\0' byte
  str->actual.str = realloc(str->actual.str, byte_size.actual);
  str->actual.allocated_len = PblGetUIntT(byte_size.actual / sizeof(char));
  str->actual.str_alloc_size = byte_size;
  str->actual.len = len;
}

/**
 * @brief Writes onto the allocated memory the passed string content
 * @param len Length of the string (should not include null char)
 * @param content The content of the string that should be written to the allocated memory - C type as this should be
 * used in the back of the program
 */
void PblWriteToStringT(PblString_T *str, const char *content, PblUInt_T len_to_write) {
  // bigger or equal means that the required space is bigger than the actual space available,
  // equal is also included since even if it's equal the null-byte needs to be added as well (+1 byte)
  if (PblGetAllocSizeStringT(len_to_write).actual >= str->actual.str_alloc_size.actual) {
    PblResizeStringT(str, len_to_write);
  }

  int i = 0;
  for (; i < len_to_write.actual; i++) { str->actual.str[i] = (char) content[i]; }
  // adding end item
  str->actual.str[i] = '\0';

  // updating meta data
  str->meta.defined = true;
}

/**
 * @brief Allocates new memory for a new string
 * @note Default size/len is 50 - will be resized with additional space required using 'PblGetAllocSizeStringT'
 * @param len Length of the string - will be used to calculate allocated memory space (should not include null char)
 * @param content The content of the string that should be written to the allocated memory - C type as this should be
 * used for converting char * and char[] to PblString_T
 * @returns The new string type that was allocated
 */
PblString_T PblCreateStringT(const char *content, PblUInt_T len)
{
  // allocated memory - length = len * size char + 1 (null character (\0))
  PblSize_T byte_size = PblGetAllocSizeStringT(len);
  char *alloc_begin = PblAllocateStringT(byte_size);

  // Using the DeclDefault to avoid recursion when `DefDefault` is `PblGetStringT("")` aka. an empty string
  PblString_T str = PblString_T_DeclDefault;
  str.actual.str_alloc_size = byte_size;
  str.actual.allocated_len = PblGetUIntT(byte_size.actual / sizeof(char));
  str.actual.len = len;
  str.actual.str = alloc_begin;

  PblWriteToStringT(&str, content, len);
  return str;
}

/**
 * @brief Allocates new memory for a new string
 * @param byte_size The byte_size that should be allocated
 * @returns The char* pointer to the memory
 */
char* PblAllocateStringT(PblSize_T byte_size) {
  return malloc(byte_size.actual);
}

/**
 * @brief Deallocates the entire memory for the string and resets it's struct properties
 * @note Writes to the string with '\0' before freeing the memory
 * @param lvalue The value that should be de-allocated
 */
void PblDeallocateStringT(PblString_T *lvalue) {
  // writing \0 onto the entire space of memory
  char nullify[lvalue->actual.len.actual];
  for (int i = 0; i < lvalue->actual.len.actual; i++) nullify[i] = '\0';
  PblWriteToStringT(lvalue, nullify, lvalue->actual.len);

  free(lvalue->actual.str);
  lvalue->actual.str = NULL;
  lvalue->actual.allocated_len = PblGetUIntT(0);
  lvalue->actual.str_alloc_size = PblGetSizeT(sizeof(NULL));
  lvalue->actual.len = PblGetUIntT(0);
  lvalue->meta.defined = false;
}