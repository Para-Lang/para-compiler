///
/// Para-C memory management and handling implementation
///
/// @author Luna-Klatzer

#include <malloc.h>

#include "./pbl-main.h"

#ifndef PARAC_MODULES_MEM_H
#define PARAC_MODULES_MEM_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Helper functions ----------------------------------------------------------------------------------------------

/**
 * @brief Validates the pointer given as parameter and checks whether it's save to access, if it's not safe it will
 * crash the program!
 * @param ptr The pointer to check
 * @return The pointer if the check was successful]
 * @note Only use this function to validate whether the pointer is valid for accessing! This function will count NULL
 * as invalid, meaning this should not be used for pointers that will be defined later!
 */
void* PblValPtr(void* ptr);

/**
 * @brief Frees the passed value and applies checks to avoid faulty freeing of memory.
 * @param ptr The actual pointer to the memory that should be freed
 * @note This will crash the program if the pointer is invalid!
 */
void PblFree(void *ptr);

/**
 * @brief Allocates the passed value and applies checks to avoid faulty allocations of memory.
 * @param size The size of the memory to allocate
 * @return The pointer returned by the C malloc call
 * @note This will crash the program if the size of the value is invalid!
 */
void* PblMalloc(size_t size);

/**
 * @brief Re-allocates the memory to the size given.
 * @param ptr The actual pointer to the memory
 * @param size The size of the memory to allocate
 * @return The pointer returned by the C realloc call - this should usually be the same pointer, but you should not
 * count on that
 * @note Unlike the low-level C realloc(), this may not be used to malloc or free memory and it will raise a critical
 * exception if attempted to secure the memory management process
 */
void* PblRealloc(void* ptr, size_t size);

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_MEM_H
