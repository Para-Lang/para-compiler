///
/// String Implementation based on dynamic memory allocation
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "pbl-types.h"

#ifndef PARAC_MODULES_STRING_H
#define PARAC_MODULES_STRING_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Declaration ---------------------------------------------------------------------------------------------------

/// Size of the type `PblString_T` in bytes
#define PblString_T_Size PblSize_T_Size + PblUInt_T_Size + PblUInt_T_Size + sizeof(char*)
/// Returns the declaration default for the type `PblString_T`
#define PblString_T_DeclDefault (PblString_T) {.meta={.defined=false, .byte_size=PblString_T_Size}}
/// Returns the definition default for the type `PblString_T`
#define PblString_T_DefDefault (PblString_T) {                                        \
    .meta={.defined=true, .byte_size=PblString_T_Size},                               \
    .actual={                                                                         \
      .str_alloc_size=PblSize_T_DefDefault, .allocated_len=PblUInt_T_DefDefault,      \
      .len=PblUInt_T_DefDefault, .str=NULL                                            \
    }                                                                                 \
  }

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
struct PblString {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// Actual value
  struct PblStringBase actual;
};
typedef struct PblString PblString_T;

// ---- Handler functions ---------------------------------------------------------------------------------------------

PblUInt_T PblGetLengthOfCString(const char *content);

PblString_T PblGetStringT(const char *content);

PblSize_T PblGetAllocSizeStringT(PblUInt_T len);

void PblResizeStringT(PblString_T *str, PblUInt_T len);

void PblWriteToStringT(PblString_T *str, const char *content, PblUInt_T len_to_write);

PblString_T PblAllocateStringT(const char *content, PblUInt_T len);

void PblDeallocateStringT(PblString_T *lvalue);

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_STRING_H
