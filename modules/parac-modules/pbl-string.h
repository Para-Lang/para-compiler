///
/// String Implementation based on dynamic memory allocation
///
/// @author Luna-Klatzer

#include "./pbl-types.h"

#ifndef PARAC_MODULES_STRING_H
#define PARAC_MODULES_STRING_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Declaration ---------------------------------------------------------------------------------------------------

/// Size of the type `PblString_T` in bytes
#define PblString_T_Size PblSize_T_Size + PblUInt_T_Size + PblUInt_T_Size + sizeof(char *)
/// Returns the declaration default for the type `PblString_T`
#define PblString_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblString_T)
/// Returns the definition default for the type `PblString_T`
#define PblString_T_DefDefault PblGetStringT("")

/// Base Struct of PblString - avoid using this type
struct PblStringBase {
  /// Returns only the allocated bytes for the string itself (char *)
  PblSize_T str_alloc_size;
  /// Amount of the chars that can be written to - includes null char (\0)
  PblUInt_T allocated_len;
  /// The length of the string
  PblUInt_T len;
  /// The char* pointer to the allocated memory - using low level C type
  char *str;
};

/// PBL String implementation - uses dynamic memory allocation -> located in heap
struct PblString PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(struct PblStringBase)
typedef struct PblString PblString_T;

// ---- Handler functions ---------------------------------------------------------------------------------------------

/**
 * @brief Gets the Length of a C string (const char*)
 * @param content The char array (pointer)
 * @return The length as Para-C Int
 */
PblUInt_T PblGetLengthOfCString(const char *content);

/**
 * @brief This directly converts a char* to a Para-C string type
 * @param content The char array (pointer)
 * @return The new Para-C string type, which was created using `PblAllocateStringContentT`
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblString_T PblGetStringT(const char *content);

/**
 * @brief Gets the required byte_size for an allocation based on the passed length of the string.
 * @note The algorithm will always be a multiple of 50 + 1 (for null char '\0').
 * The calculated size is the next biggest multiple of 50 + 1, which is still bigger than the passed length.
 * @param len The length of the actual string content, which will be used to calculate the allocation length.
 * @returns The size as size_t (int)
 */
PblSize_T PblGetAllocSizeStringT(PblUInt_T len);

/**
 * @brief Resizes the string by reallocating the memory.
 * @note Automatically calculates the size of the new allocated memory based on the length. The function used for the
 * length calculation is `PblGetAllocSizeStringT`
 * @param str The string that should be reallocated
 * @param len The length of the string content that is used to calculate the required size
 */
PblVoid_T PblResizeStringT(PblString_T *str, PblUInt_T len);

/**
 * @brief Writes onto the allocated memory the passed string content
 * @param len Length of the string (should not include null char)
 * @param content The content of the string that should be written to the allocated memory - C type as this should be
 * used in the back of the program
 */
PblVoid_T PblWriteToStringT(PblString_T *str, const char *content, PblUInt_T len_to_write);

/**
 * @brief Allocates new memory for a new string
 * @note Default size/len is 50 - will be resized with additional space required using 'PblGetAllocSizeStringT'
 * @param len Length of the string - will be used to calculate allocated memory space (should not include null char)
 * @param content The content of the string that should be written to the allocated memory - C type as this should be
 * used for converting char * and char[] to PblString_T
 * @returns The new string type that was allocated
 */
PblString_T PblCreateStringT(const char *content, PblUInt_T len);

/**
 * @brief Allocates new memory for a new string
 * @param byte_size The byte_size that should be allocated
 * @returns The char* pointer to the memory
 */
char *PblAllocateStringContentT(PblSize_T byte_size);

/**
 * @brief Deallocates the entire memory for the string and resets it's struct properties
 * @note Writes to the string with '\0' before freeing the memory
 * @param lvalue The value that should be de-allocated
 */
PblVoid_T PblSafeDeallocateStringT(PblString_T *lvalue);

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_STRING_H
