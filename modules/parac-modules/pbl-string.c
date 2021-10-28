///
/// String Implementation based on dynamic memory allocation
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include <malloc.h>
#include <stdbool.h>
#include <string.h>

#include "./pbl-string.h"
#include "./pbl-types.h"

PblUInt_T PblGetLengthOfCString(const char *content) {
  return PblGetUIntT(strlen(content));
}

PblString_T PblGetStringT(const char *content) {
  return PblCreateStringT(content, PblGetLengthOfCString(content));
}

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

PblVoid_T PblResizeStringT(PblString_T *str, PblUInt_T len) {
  PblSize_T byte_size = PblGetAllocSizeStringT(len);

  // reallocating the memory with the new length - includes space for '\0' byte
  str->actual.str = realloc(str->actual.str, byte_size.actual);
  str->actual.allocated_len = PblGetUIntT(byte_size.actual / sizeof(char));
  str->actual.str_alloc_size = byte_size;
  str->actual.len = len;
  return PblVoid_T_DeclDefault;
}

PblVoid_T PblWriteToStringT(PblString_T *str, const char *content, PblUInt_T len_to_write) {
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
  return PblVoid_T_DeclDefault;
}

PblString_T PblCreateStringT(const char *content, PblUInt_T len) {
  // allocated memory - length = len * size char + 1 (null character (\0))
  PblSize_T byte_size = PblGetAllocSizeStringT(len);
  char *alloc_begin = PblAllocateStringContentT(byte_size);

  // Using the DeclDefault to avoid recursion when `DefDefault` is `PblGetStringT("")` aka. an empty string
  PblString_T str = PblString_T_DeclDefault;
  str.actual.str_alloc_size = byte_size;
  str.actual.allocated_len = PblGetUIntT(byte_size.actual / sizeof(char));
  str.actual.len = len;
  str.actual.str = alloc_begin;

  PblWriteToStringT(&str, content, len);
  return str;
}

char *PblAllocateStringContentT(PblSize_T byte_size) {
  return malloc(byte_size.actual);
}

PblVoid_T PblDeallocateStringT(PblString_T *lvalue) {
  // writing \0 onto the entire space of memory
  char nullify[lvalue->actual.len.actual];
  for (int i = 0; i < lvalue->actual.len.actual; i++) nullify[i] = '\0';
  PblWriteToStringT(lvalue, nullify, lvalue->actual.len);

  free(lvalue->actual.str);
  *lvalue = PblString_T_DeclDefault;
  return PblVoid_T_DeclDefault;
}