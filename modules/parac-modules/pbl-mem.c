///
/// Para-C memory management and handling implementation
///
/// @author Luna-Klatzer

#include "./pbl-mem.h"

void* PblValPtr(void* ptr) {
  // Crash on invalid input - Don't bother raising exceptions on this low-level area
  if (ptr == NULL) {
    PblAbortWithCriticalError(1, "PARA-C: Attempted to access invalid memory address (NULL)");
  }
  return ptr;
}

void PblFree(void *ptr) {
  // Crash on invalid input - Don't bother raising exceptions on this low-level area
  if (ptr == NULL) {
    PblAbortWithCriticalError(1,"PARA-C: Attempted to free invalid memory address (NULL)");
  }
  free(ptr);
  // old pointer is invalid
  ptr = NULL;
}

void* PblMalloc(size_t size) {
  // Crash on invalid input - Don't bother raising exceptions on this low-level area
  if (size <= 0) {
    PblAbortWithCriticalError(1,"PARA-C: Attempted to allocate invalid amounts of memory (0)");
  }
  // allocating the memory
  void* ptr = malloc(size);
  if (ptr == NULL) {
    PblAbortWithCriticalError(1,"PARA-C: Failed to allocate memory (Received NULL)");
  }
  return ptr;
}

void* PblRealloc(void* ptr, size_t size) {
  // Crash on invalid input - Don't bother raising exceptions on this low-level area
  if (ptr == NULL) {
    PblAbortWithCriticalError(1,"PARA-C: Attempted to re-allocate invalid memory address (NULL)");
  }
  if (size <= 0) {
    PblAbortWithCriticalError(1,"PARA-C: Attempted to re-allocate invalid amounts of memory (0)");
  }

  // re-allocating the memory
  void* new_ptr = realloc(ptr, size);
  if (new_ptr == NULL) {
    PblAbortWithCriticalError(1,"PARA-C: Failed to re-allocate memory (Received NULL)");
  }
  // old pointer is invalid
  if (new_ptr != ptr) ptr = NULL;
  return new_ptr;
}