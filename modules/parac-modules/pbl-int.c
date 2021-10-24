///
/// Int Implementation based on stdint.h
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "pbl-int.h"

/**
 * @brief Converts the low level C-Type to a PBL Int8 type
 * @param val The C-type to be converted
 * @return The newly created PBL Int8 type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblInt8_T PblGetInt8T(int8_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblInt8_T, int8_t)}

/**
* @brief Converts the low level C-Type to a PBL UInt8 type
* @param val The C-type to be converted
* @return The newly created PBL UInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt8_T PblGetUInt8T(uint8_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUInt8_T, uint8_t)}

/**
* @brief Converts the low level C-Type to a PBL Int16 type
* @param val The C-type to be converted
* @return The newly created PBL Int16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblInt16_T PblGetInt16T(int16_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblInt16_T, int16_t)}

/**
* @brief Converts the low level C-Type to a PBL UInt16 type
* @param val The C-type to be converted
* @return The newly created PBL UInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt16_T PblGetUInt16T(uint16_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUInt16_T, uint16_t)}

/**
* @brief Converts the low level C-Type to a PBL Int32 type
* @param val The C-type to be converted
* @return The newly created PBL Int32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblInt32_T PblGetInt32T(int32_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblInt32_T, int32_t)}

/**
* @brief Converts the low level C-Type to a PBL UInt32 type
* @param val The C-type to be converted
* @return The newly created PBL UInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt32_T PblGetUInt32T(uint32_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUInt32_T, uint32_t)}

/**
* @brief Converts the low level C-Type to a PBL Int64 type
* @param val The C-type to be converted
* @return The newly created PBL Int64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblInt64_T PblGetInt64T(int64_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblInt64_T, int64_t)}

/**
* @brief Converts the low level C-Type to a PBL UInt64 type
* @param val The C-type to be converted
* @return The newly created PBL UInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt64_T PblGetUInt64T(uint64_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUInt64_T, uint64_t)}

/**
* @brief Converts the low level C-Type to a PBL LeastInt8 type
* @param val The C-type to be converted
* @return The newly created PBL LeastInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLeastInt8_T PblGetLeastInt8T(int_least8_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLeastInt8_T, int_least8_t)}

/**
* @brief Converts the low level C-Type to a PBL ULeastInt8 type
* @param val The C-type to be converted
* @return The newly created PBL ULeastInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULeastInt8_T
  PblGetULeastInt8T(uint_least8_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblULeastInt8_T, uint_least8_t)}

/**
* @brief Converts the low level C-Type to a PBL LeastInt16 type
* @param val The C-type to be converted
* @return The newly created PBL LeastInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLeastInt16_T
  PblGetLeastInt16T(int_least16_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLeastInt16_T, int_least16_t)}

/**
* @brief Converts the low level C-Type to a PBL ULeastInt16 type
* @param val The C-type to be converted
* @return The newly created PBL ULeastInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULeastInt16_T
  PblGetULeastInt16T(uint_least16_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblULeastInt16_T, uint_least16_t)}

/**
* @brief Converts the low level C-Type to a PBL LeastInt32 type
* @param val The C-type to be converted
* @return The newly created PBL LeastInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLeastInt32_T
  PblGetLeastInt32T(int_least32_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLeastInt32_T, int_least32_t)}

/**
* @brief Converts the low level C-Type to a PBL ULeastInt32 type
* @param val The C-type to be converted
* @return The newly created PBL ULeastInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULeastInt32_T
  PblGetULeastInt32T(uint_least32_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblULeastInt32_T, uint_least32_t)}

/**
* @brief Converts the low level C-Type to a PBL LeastInt64 type
* @param val The C-type to be converted
* @return The newly created PBL LeastInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLeastInt64_T
  PblGetLeastInt64T(int_least64_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLeastInt64_T, int_least64_t)}

/**
* @brief Converts the low level C-Type to a PBL ULeastInt64 type
* @param val The C-type to be converted
* @return The newly created PBL ULeastInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULeastInt64_T
  PblGetULeastInt64T(uint_least64_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblULeastInt64_T, uint_least64_t)}

/**
* @brief Converts the low level C-Type to a PBL FastestInt8 type
* @param val The C-type to be converted
* @return The newly created PBL FastestInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFastestInt8_T
  PblGetFastestInt8T(int_fast8_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblFastestInt8_T, int_fast8_t)}

/**
* @brief Converts the low level C-Type to a PBL UFastestInt8 type
* @param val The C-type to be converted
* @return The newly created PBL UFastestInt8 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUFastestInt8_T
  PblGetUFastestInt8T(uint_fast8_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUFastestInt8_T, uint_fast8_t)}

/**
* @brief Converts the low level C-Type to a PBL FastestInt16 type
* @param val The C-type to be converted
* @return The newly created PBL FastestInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFastestInt16_T
  PblGetFastestInt16T(int_fast16_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblFastestInt16_T, int_fast16_t)}

/**
* @brief Converts the low level C-Type to a PBL UFastestInt16 type
* @param val The C-type to be converted
* @return The newly created PBL UFastestInt16 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUFastestInt16_T
  PblGetUFastestInt16T(uint_fast16_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUFastestInt16_T, uint_fast16_t)}

/**
* @brief Converts the low level C-Type to a PBL FastestInt32 type
* @param val The C-type to be converted
* @return The newly created PBL FastestInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFastestInt32_T
  PblGetFastestInt32T(int_fast32_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblFastestInt32_T, int_fast32_t)}

/**
* @brief Converts the low level C-Type to a PBL UFastestInt32 type
* @param val The C-type to be converted
* @return The newly created PBL UFastestInt32 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUFastestInt32_T
  PblGetUFastestInt32T(uint_fast32_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUFastestInt32_T, uint_fast32_t)}

/**
* @brief Converts the low level C-Type to a PBL FastestInt64 type
* @param val The C-type to be converted
* @return The newly created PBL FastestInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFastestInt64_T
  PblGetFastestInt64T(int_fast64_t val){PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblFastestInt64_T, int_fast64_t)}

/**
* @brief Converts the low level C-Type to a PBL UFastestInt64 type
* @param val The C-type to be converted
* @return The newly created PBL UFastestInt64 type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUFastestInt64_T PblGetUFastestInt64T(uint_fast64_t val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUFastestInt64_T, uint_fast64_t)
}
