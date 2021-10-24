///
/// Int Implementation based on stdint.h
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "pbl-types.h"
#include <stdint.h>

#ifndef PARAC_MODULES_INT_H
#define PARAC_MODULES_INT_H

// ---- Exact Int -----------------------------------------------------------------------------------------------------

// ---- Int8 ----------------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Int8 type
#define PblInt8_T_Size sizeof(int8_t)
/// Returns the declaration default for the type `PblInt8_T`
#define PblInt8_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblInt8_T)
/// Returns the definition default for the type `PblInt8_T`
#define PblInt8_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblInt8_T, 0)

/// PBL Int8 implementation
struct PblInt8 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int8_t actual;
};
/// PBL Signed Int8 implementation
typedef struct PblInt8 PblInt8_T;

// ---- UInt8 ---------------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblUInt8_T_Size sizeof(uint8_t)
/// Returns the declaration default for the type `PblUInt8_T`
#define PblUInt8_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUInt8_T)
/// Returns the definition default for the type `PblUInt8_T`
#define PblUInt8_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUInt8_T, 0)
/// PBL Unsigned Int8 implementation
struct PblUInt8 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint8_t actual;
};
/// PBL Signed Long implementation
typedef struct PblUInt8 PblUInt8_T;

// ---- Int16 ---------------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Int16 type
#define PblInt16_T_Size sizeof(int16_t)
/// Returns the declaration default for the type `PblInt16_T`
#define PblInt16_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblInt16_T)
/// Returns the definition default for the type `PblInt16_T`
#define PblInt16_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblInt16_T, 0)

/// PBL Int16 implementation
struct PblInt16 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int16_t actual;
};
/// PBL Signed Int16 implementation
typedef struct PblInt16 PblInt16_T;

// ---- UInt16 --------------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblUInt16_T_Size sizeof(uint16_t)
/// Returns the declaration default for the type `PblUInt16_T`
#define PblUInt16_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUInt16_T)
/// Returns the definition default for the type `PblUInt16_T`
#define PblUInt16_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUInt16_T, 0)

/// PBL UInt16 implementation
struct PblUInt16 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint16_t actual;
};
/// PBL Signed Long implementation
typedef struct PblUInt16 PblUInt16_T;

// ---- Int32 ---------------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Int32 type
#define PblInt32_T_Size sizeof(int32_t)
/// Returns the declaration default for the type `PblInt32_T`
#define PblInt32_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblInt32_T)
/// Returns the definition default for the type `PblInt32_T`
#define PblInt32_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblInt32_T, 0)

/// PBL Int32 implementation
struct PblInt32 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int32_t actual;
};
/// PBL Signed Int32 implementation
typedef struct PblInt32 PblInt32_T;

// ---- UInt32 --------------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblUInt32_T_Size sizeof(uint32_t)
/// Returns the declaration default for the type `PblUInt32_T`
#define PblUInt32_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUInt32_T)
/// Returns the definition default for the type `PblUInt32_T`
#define PblUInt32_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUInt32_T, 0)

/// PBL UInt32 implementation
struct PblUInt32 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint32_t actual;
};
/// PBL Signed Long implementation
typedef struct PblUInt32 PblUInt32_T;

// ---- Int64 ---------------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Int64 type
#define PblInt64_T_Size sizeof(int64_t)
/// Returns the declaration default for the type `PblInt64_T`
#define PblInt64_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblInt64_T)
/// Returns the definition default for the type `PblInt64_T`
#define PblInt64_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblInt64_T, 0)

/// PBL Int64 implementation
struct PblInt64 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int64_t actual;
};
/// PBL Signed Int64 implementation
typedef struct PblInt64 PblInt64_T;

// ---- UInt64 --------------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblUInt64_T_Size sizeof(uint64_t)
/// Returns the declaration default for the type `PblUInt64_T`
#define PblUInt64_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUInt64_T)
/// Returns the definition default for the type `PblUInt64_T`
#define PblUInt64_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUInt64_T, 0)

/// PBL UInt64 implementation
struct PblUInt64 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint64_t actual;
};
/// PBL Signed Long implementation
typedef struct PblUInt64 PblUInt64_T;

// ---- Least Int -----------------------------------------------------------------------------------------------------

// ---- LeastInt8 -----------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed LeastInt8 type
#define PblLeastInt8_T_Size sizeof(int_least8_t)
/// Returns the declaration default for the type `PblLeastInt8_T`
#define PblLeastInt8_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblLeastInt8_T)
/// Returns the definition default for the type `PblLeastInt8_T`
#define PblLeastInt8_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblLeastInt8_T, 0)

/// PBL LeastInt8 implementation
struct PblLeastInt8 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int_least8_t actual;
};
/// PBL Signed LeastInt8 implementation
typedef struct PblLeastInt8 PblLeastInt8_T;

// ---- ULeastInt8 ----------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblULeastInt8_T_Size sizeof(uint_least8_t)
/// Returns the declaration default for the type `PblULeastInt8_T`
#define PblULeastInt8_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblULeastInt8_T)
/// Returns the definition default for the type `PblULeastInt8_T`
#define PblULeastInt8_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblULeastInt8_T, 0)

/// PBL ULeastInt8 implementation
struct PblULeastInt8 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint_least8_t actual;
};
/// PBL Signed Long implementation
typedef struct PblULeastInt8 PblULeastInt8_T;

// ---- LeastInt16 ----------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed LeastInt16 type
#define PblLeastInt16_T_Size sizeof(int_least16_t)
/// Returns the declaration default for the type `PblLeastInt16_T`
#define PblLeastInt16_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblLeastInt16_T)
/// Returns the definition default for the type `PblLeastInt16_T`
#define PblLeastInt16_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblLeastInt16_T, 0)

/// PBL LeastInt16 implementation
struct PblLeastInt16 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int_least16_t actual;
};
/// PBL Signed LeastInt16 implementation
typedef struct PblLeastInt16 PblLeastInt16_T;

// ---- ULeastInt16 ---------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblULeastInt16_T_Size sizeof(uint_least16_t)
/// Returns the declaration default for the type `PblULeastInt16_T`
#define PblULeastInt16_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblULeastInt16_T)
/// Returns the definition default for the type `PblULeastInt16_T`
#define PblULeastInt16_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblULeastInt16_T, 0)

/// PBL ULeastInt16 implementation
struct PblULeastInt16 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint_least16_t actual;
};
/// PBL Signed Long implementation
typedef struct PblULeastInt16 PblULeastInt16_T;

// ---- LeastInt32 ----------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed LeastInt32 type
#define PblLeastInt32_T_Size sizeof(int_least32_t)
/// Returns the declaration default for the type `PblLeastInt32_T`
#define PblLeastInt32_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblLeastInt32_T)
/// Returns the definition default for the type `PblLeastInt32_T`
#define PblLeastInt32_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblLeastInt32_T, 0)

/// PBL LeastInt32 implementation
struct PblLeastInt32 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int_least32_t actual;
};
/// PBL Signed LeastInt32 implementation
typedef struct PblLeastInt32 PblLeastInt32_T;

// ---- ULeastInt32 ---------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblULeastInt32_T_Size sizeof(uint_least32_t)
/// Returns the declaration default for the type `PblULeastInt32_T`
#define PblULeastInt32_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblULeastInt32_T)
/// Returns the definition default for the type `PblULeastInt32_T`
#define PblULeastInt32_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblULeastInt32_T, 0)

/// PBL ULeastInt32 implementation
struct PblULeastInt32 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint_least32_t actual;
};
/// PBL Signed Long implementation
typedef struct PblULeastInt32 PblULeastInt32_T;

// ---- LeastInt64 ----------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed LeastInt64 type
#define PblLeastInt64_T_Size sizeof(int_least64_t)
/// Returns the declaration default for the type `PblLeastInt64_T`
#define PblLeastInt64_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblLeastInt64_T)
/// Returns the definition default for the type `PblLeastInt64_T`
#define PblLeastInt64_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblLeastInt64_T, 0)

/// PBL LeastInt64 implementation
struct PblLeastInt64 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int_least64_t actual;
};
/// PBL Signed LeastInt64 implementation
typedef struct PblLeastInt64 PblLeastInt64_T;

// ---- ULeastInt64 ---------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblULeastInt64_T_Size sizeof(uint_least64_t)
/// Returns the declaration default for the type `PblULeastInt64_T`
#define PblULeastInt64_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblULeastInt64_T)
/// Returns the definition default for the type `PblULeastInt64_T`
#define PblULeastInt64_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblULeastInt64_T, 0)

/// PBL ULeastInt64 implementation
struct PblULeastInt64 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint_least64_t actual;
};
/// PBL Signed Long implementation
typedef struct PblULeastInt64 PblULeastInt64_T;

// ---- Fast Int ------------------------------------------------------------------------------------------------------

// ---- FastestInt8 ---------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed FastestInt8 type
#define PblFastestInt8_T_Size sizeof(int_fast8_t)
/// Returns the declaration default for the type `PblFastestInt8_T`
#define PblFastestInt8_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblFastestInt8_T)
/// Returns the definition default for the type `PblFastestInt8_T`
#define PblFastestInt8_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblFastestInt8_T, 0)

/// PBL FastestInt8 implementation
struct PblFastestInt8 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int_fast8_t actual;
};
/// PBL Signed FastestInt8 implementation
typedef struct PblFastestInt8 PblFastestInt8_T;

// ---- UFastestInt8 --------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblUFastestInt8_T_Size sizeof(uint_fast8_t)
/// Returns the declaration default for the type `PblUFastestInt8_T`
#define PblUFastestInt8_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUFastestInt8_T)
/// Returns the definition default for the type `PblUFastestInt8_T`
#define PblUFastestInt8_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUFastestInt8_T, 0)

/// PBL UFastestInt8 implementation
struct PblUFastestInt8 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint_fast8_t actual;
};
/// PBL Signed Long implementation
typedef struct PblUFastestInt8 PblUFastestInt8_T;

// ---- FastestInt16 --------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed FastestInt16 type
#define PblFastestInt16_T_Size sizeof(int_fast16_t)
/// Returns the declaration default for the type `PblFastestInt16_T`
#define PblFastestInt16_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblFastestInt16_T)
/// Returns the definition default for the type `PblFastestInt16_T`
#define PblFastestInt16_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblFastestInt16_T, 0)

/// PBL FastestInt16 implementation
struct PblFastestInt16 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int_fast16_t actual;
};
/// PBL Signed FastestInt16 implementation
typedef struct PblFastestInt16 PblFastestInt16_T;

// ---- UFastestInt16 -------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblUFastestInt16_T_Size sizeof(uint_fast16_t)
/// Returns the declaration default for the type `PblUFastestInt16_T`
#define PblUFastestInt16_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUFastestInt16_T)
/// Returns the definition default for the type `PblUFastestInt16_T`
#define PblUFastestInt16_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUFastestInt16_T, 0)

/// PBL UFastestInt16 implementation
struct PblUFastestInt16 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint_fast16_t actual;
};
/// PBL Signed Long implementation
typedef struct PblUFastestInt16 PblUFastestInt16_T;

// ---- FastestInt32 --------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed FastestInt32 type
#define PblFastestInt32_T_Size sizeof(int_fast32_t)
/// Returns the declaration default for the type `PblFastestInt32_T`
#define PblFastestInt32_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblFastestInt32_T)
/// Returns the definition default for the type `PblFastestInt32_T`
#define PblFastestInt32_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblFastestInt32_T, 0)

/// PBL FastestInt32 implementation
struct PblFastestInt32 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int_fast32_t actual;
};
/// PBL Signed FastestInt32 implementation
typedef struct PblFastestInt32 PblFastestInt32_T;

// ---- UFastestInt32 -------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblUFastestInt32_T_Size sizeof(uint_fast32_t)
/// Returns the declaration default for the type `PblUFastestInt32_T`
#define PblUFastestInt32_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUFastestInt32_T)
/// Returns the definition default for the type `PblUFastestInt32_T`
#define PblUFastestInt32_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUFastestInt32_T, 1)

/// PBL UFastestInt32 implementation
struct PblUFastestInt32 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint_fast32_t actual;
};
/// PBL Signed Long implementation
typedef struct PblUFastestInt32 PblUFastestInt32_T;

// ---- FastestInt64 --------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed FastestInt64 type
#define PblFastestInt64_T_Size sizeof(int_fast64_t)
/// Returns the declaration default for the type `PblFastestInt64_T`
#define PblFastestInt64_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblFastestInt64_T)
/// Returns the definition default for the type `PblFastestInt64_T`
#define PblFastestInt64_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblFastestInt64_T, 1)

/// PBL FastestInt64 implementation
struct PblFastestInt64 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  int_fast64_t actual;
};
/// PBL Signed FastestInt64 implementation
typedef struct PblFastestInt64 PblFastestInt64_T;

// ---- UFastestInt64 -------------------------------------------------------------------------------------------------

/// Returns the size in bytes of the PBL Signed Long type
#define PblUFastestInt64_T_Size sizeof(uint_fast64_t)
/// Returns the declaration default for the type `PblUFastestInt64_T`
#define PblUFastestInt64_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUFastestInt64_T)
/// Returns the definition default for the type `PblUFastestInt64_T`
#define PblUFastestInt64_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUFastestInt64_T, 1)

/// PBL UFastestInt64 implementation
struct PblUFastestInt64 {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// actual value - C type
  uint_fast64_t actual;
};
/// PBL Signed Long implementation
typedef struct PblUFastestInt64 PblUFastestInt64_T;

// ---- Helper Functions ----------------------------------------------------------------------------------------------

/**
 * @brief Converts the low level C-Type to a PBL Int8 type
 * @param val The C-type to be converted
 * @return The newly created PBL Int8 type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblInt8_T PblGetInt8T(int8_t val);

/**
* @brief Converts the low level C-Type to a PBL UInt8 type
* @param val The C-type to be converted
* @return The newly created PBL UInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt8_T PblGetUInt8T(uint8_t val);

/**
* @brief Converts the low level C-Type to a PBL Int16 type
* @param val The C-type to be converted
* @return The newly created PBL Int16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblInt16_T PblGetInt16T(int16_t val);

/**
* @brief Converts the low level C-Type to a PBL UInt16 type
* @param val The C-type to be converted
* @return The newly created PBL UInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt16_T PblGetUInt16T(uint16_t val);

/**
* @brief Converts the low level C-Type to a PBL Int32 type
* @param val The C-type to be converted
* @return The newly created PBL Int32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblInt32_T PblGetInt32T(int32_t val);

/**
* @brief Converts the low level C-Type to a PBL UInt32 type
* @param val The C-type to be converted
* @return The newly created PBL UInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt32_T PblGetUInt32T(uint32_t val);

/**
* @brief Converts the low level C-Type to a PBL Int64 type
* @param val The C-type to be converted
* @return The newly created PBL Int64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblInt64_T PblGetInt64T(int64_t val);

/**
* @brief Converts the low level C-Type to a PBL UInt64 type
* @param val The C-type to be converted
* @return The newly created PBL UInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt64_T PblGetUInt64T(uint64_t val);

/**
* @brief Converts the low level C-Type to a PBL LeastInt8 type
* @param val The C-type to be converted
* @return The newly created PBL LeastInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLeastInt8_T PblGetLeastInt8T(int_least8_t val);

/**
* @brief Converts the low level C-Type to a PBL ULeastInt8 type
* @param val The C-type to be converted
* @return The newly created PBL ULeastInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULeastInt8_T PblGetULeastInt8T(uint_least8_t val);

/**
* @brief Converts the low level C-Type to a PBL LeastInt16 type
* @param val The C-type to be converted
* @return The newly created PBL LeastInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLeastInt16_T PblGetLeastInt16T(int_least16_t val);

/**
* @brief Converts the low level C-Type to a PBL ULeastInt16 type
* @param val The C-type to be converted
* @return The newly created PBL ULeastInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULeastInt16_T PblGetULeastInt16T(uint_least16_t val);

/**
* @brief Converts the low level C-Type to a PBL LeastInt32 type
* @param val The C-type to be converted
* @return The newly created PBL LeastInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLeastInt32_T PblGetLeastInt32T(int_least32_t val);

/**
* @brief Converts the low level C-Type to a PBL ULeastInt32 type
* @param val The C-type to be converted
* @return The newly created PBL ULeastInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULeastInt32_T PblGetULeastInt32T(uint_least32_t val);

/**
* @brief Converts the low level C-Type to a PBL LeastInt64 type
* @param val The C-type to be converted
* @return The newly created PBL LeastInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLeastInt64_T PblGetLeastInt64T(int_least64_t val);

/**
* @brief Converts the low level C-Type to a PBL ULeastInt64 type
* @param val The C-type to be converted
* @return The newly created PBL ULeastInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULeastInt64_T PblGetULeastInt64T(uint_least64_t val);

/**
* @brief Converts the low level C-Type to a PBL FastestInt8 type
* @param val The C-type to be converted
* @return The newly created PBL FastestInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFastestInt8_T PblGetFastestInt8T(int_fast8_t val);

/**
* @brief Converts the low level C-Type to a PBL UFastestInt8 type
* @param val The C-type to be converted
* @return The newly created PBL UFastestInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUFastestInt8_T PblGetUFastestInt8T(uint_fast8_t val);

/**
* @brief Converts the low level C-Type to a PBL FastestInt16 type
* @param val The C-type to be converted
* @return The newly created PBL FastestInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFastestInt16_T PblGetFastestInt16T(int_fast16_t val);

/**
* @brief Converts the low level C-Type to a PBL UFastestInt16 type
* @param val The C-type to be converted
* @return The newly created PBL UFastestInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUFastestInt16_T PblGetUFastestInt16T(uint_fast16_t val);

/**
* @brief Converts the low level C-Type to a PBL FastestInt32 type
* @param val The C-type to be converted
* @return The newly created PBL FastestInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFastestInt32_T PblGetFastestInt32T(int_fast32_t val);

/**
* @brief Converts the low level C-Type to a PBL UFastestInt32 type
* @param val The C-type to be converted
* @return The newly created PBL UFastestInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUFastestInt32_T PblGetUFastestInt32T(uint_fast32_t val);

/**
* @brief Converts the low level C-Type to a PBL FastestInt64 type
* @param val The C-type to be converted
* @return The newly created PBL FastestInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFastestInt64_T PblGetFastestInt64T(int_fast64_t val);

/**
* @brief Converts the low level C-Type to a PBL UFastestInt64 type
* @param val The C-type to be converted
* @return The newly created PBL UFastestInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUFastestInt64_T PblGetUFastestInt64T(uint_fast64_t val);

#endif//PARAC_MODULES_INT_H
