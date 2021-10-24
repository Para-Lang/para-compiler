///
/// Base Para-C Types Implementation, which implement default declaration and default definition types. This also
/// includes meta-data tracking based on the `PblVarMeta` type.
///
/// @date 08-10-2021
/// @author Luna-Klatzer
/// @note The TYPE_T_Size macros define the actual size of the C-elements, without the meta struct - This is only used
/// to know the actual size that can be used from the user.

#include "pbl-types.h"

/**
 * @brief Converts the low level C-Type to a PBL Bool type
 * @param val The C-type to be converted
 * @return The newly created PBL Bool type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblBool_T PblGetBoolT(bool val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblBool_T, bool)

  /**
* @brief Converts the low level C-Type to a PBL Byte Size type
* @param val The C-type to be converted
* @return The newly created PBL Byte Size type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblSize_T PblGetSizeT(size_t val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblSize_T, size_t)

  /**
* @brief Converts the low level C-Type to a PBL Char type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblChar_T PblGetCharT(signed char val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblChar_T, signed char)

  /**
* @brief Converts the low level C-Type to a PBL Unsigned Char type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblUChar_T PblGetUCharT(unsigned char val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUChar_T, unsigned char)

  /**
* @brief Converts the low level C-Type to a PBL Short type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblShort_T PblGetShortT(signed short val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblShort_T, signed short)

  /**
* @brief Converts the low level C-Type to a PBL Unsigned Short type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblUShort_T PblGetUShortT(unsigned short val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUShort_T, unsigned short)

  /**
* @brief Converts the low level C-Type to a PBL Int type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblInt_T PblGetIntT(signed int val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblInt_T, signed int)

  /**
* @brief Converts the low level C-Type to a PBL Unsigned Int type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblUInt_T PblGetUIntT(unsigned int val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUInt_T, unsigned int)

  /**
* @brief Converts the low level C-Type to a PBL Long type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblLong_T PblGetLongT(signed long val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLong_T, signed long)

  /**
* @brief Converts the low level C-Type to a PBL Unsigned Long type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblULong_T PblGetULongT(unsigned long val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblULong_T, unsigned long)

  /**
* @brief Converts the low level C-Type to a PBL Long Long type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblLongLong_T PblGetLongLongT(signed long long val)
    PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLongLong_T, signed long long)

  /**
* @brief Converts the low level C-Type to a PBL Unsigned Long Long type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblULongLong_T PblGetULongLongT(unsigned long long val)
    PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblULongLong_T, unsigned long long)

  /**
* @brief Converts the low level C-Type to a PBL Float type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblFloat_T PblGetFloatT(float val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblFloat_T, float)

  /**
* @brief Converts the low level C-Type to a PBL Double type
* @param val The C-type to be converted
* @return The newly created PBL Double type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblDouble_T PblGetDoubleT(double val) PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblDouble_T, double)

  /**
* @brief Converts the low level C-Type to a PBL Long Double type
* @param val The C-type to be converted
* @return The newly created PBL Long Double type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
  PblLongDouble_T PblGetLongDoubleT(long double val)
    PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLongDouble_T, long double)
