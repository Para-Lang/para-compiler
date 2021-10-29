///
/// Main header for the Para-C Base Library (Static C library)
/// Styling and naming are similar to the Google C++ style guide
/// @see https://google.github.io/styleguide/cppguide.html
///
/// Headers of the library:
/// - pbl-io.h
/// - pbl-types.h
/// - pbl-string.h
/// - pbl-int.h
/// - pbl-function.h
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
/// #define ITEM_T_DefinitionDefault (ITEM_T) {               \
///  .meta = {.defined=false, .byte_size=ITEM_T_Size}         \
///  .actual = ...                                            \
/// }
///
/// // Base Struct of ITEM - avoid using this type
/// struct ITEMBase { ... };
///
/// // File Descriptor used to perform I/O actions on a file
/// struct ITEM PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(struct ITEMBase)
/// typedef struct ITEM ITEM_T;

// lib-headers includes
#include "./pbl-int.h"
#include "./pbl-io.h"
#include "./pbl-string.h"
#include "./pbl-types.h"
#include "./pbl-function.h"

#ifndef PARAC_MODULES_LIBRARY_H
#define PARAC_MODULES_LIBRARY_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Macros --------------------------------------------------------------------------------------------------------

/// The current release identifier
#define __parac "0.1.dev5"
/// Indicates the current library version being a development version
#define __parac_dev true
/// Indicates the current library version being a stable version
#define __parac_stable false

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_LIBRARY_H
