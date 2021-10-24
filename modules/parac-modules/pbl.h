///
/// Main header for the Para-C Base Library (Static C library)
/// Styling and naming are similar to the Google C++ style guide
/// @see https://google.github.io/styleguide/cppguide.html
///
/// Headers of the library:
/// - pbl-io.h
/// - pbl-types.h
/// - pbl-string.h
///
/// @date 08-10-2021
/// @author Luna-Klatzer
/// @note The styling guide for the PBL is as following:
/// - Structs/Enums: PascalCase with leading `Pbl`
/// - Struct Properties: snake_case
/// - Constants and Enum Properties: PascalCase with leading `k` (copied from the Google C++ Styling Guide)
/// - Typedef: PascalCase with leading `Pbl` and trailing `_T`
/// - Local Variables: snake_case
/// - Parameters: snake_case
/// - Macros: SCREAMING_SNAKE_CASE (exceptions are function definition macros, where PascalCase is applied)
/// - Functions: PascalCase
/// - Indention is set to 2 spaces
/// @note When declaring a built-in type that should be used inside Para-C, these are following items that must be
/// declared as well (template):
/// // The size of the type `ITEM_T` in bytes - excluding meta-data
/// #define ITEM_T_Size <insert-calculation>
/// // Returns the declaration default for the type `ITEM_T`
/// #define ITEM_T_DeclarationDefault (ITEM_T) {.meta = {.defined=false, .byte_size=ITEM_T_Size}}
/// // Returns the definition default for the type `ITEM_T`
/// #define ITEM_T_DefinitionDefault (ITEM_T) { \
///  .meta = {.defined=false, .byte_size=ITEM_T_Size} \
///  .actual = ...                                            \
/// }
///
/// // Base Struct of ITEM - avoid using this type
/// struct ITEMBase { ... };
///
/// // File Descriptor used to perform I/O actions on a file
/// struct ITEM {
///   /// PBL meta type - keeps track of initialisation
///   PblVarMeta_T meta;
///   /// Actual value
///   struct ITEMBase actual;
/// };
/// typedef struct ITEM ITEM_T;

// lib-headers includes
#include "./pbl-io.h"
#include "./pbl-string.h"
#include "./pbl-types.h"

#ifndef PARAC_MODULES_LIBRARY_H
#define PARAC_MODULES_LIBRARY_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Macros --------------------------------------------------------------------------------------------------------

/// The current release identifier
#define PARAC_LIB_VERSION "0.1.dev5"
/// Indicates the current library version being a development version
#define PARAC_DEVELOPMENT_RELEASE true
/// Indicates the current library version being a stable version
#define PARAC_STABLE_RELEASE false
/// Indicates the usage of Para-C -> Always true
#define PARAC_LANG true

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_LIBRARY_H
