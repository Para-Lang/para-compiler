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
PblBool_T PblGetBoolT(bool val) {
  return (PblBool_T){
    .meta={.byte_size = PblBool_T_Size, .defined = true},
    .actual=val,
  };
}

/**
 * @brief Converts the low level C-Type to a PBL Byte Size type
 * @param val The C-type to be converted
 * @return The newly created PBL Byte Size type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblSize_T PblGetSizeT(size_t val) {
  PblSize_T conv = PblSize_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Char type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblChar_T PblGetCharT(signed char val) {
  PblChar_T conv = PblChar_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Unsigned Char type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblUChar_T PblGetUCharT(unsigned char val) {
  PblUChar_T conv = PblUChar_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Short type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblShort_T PblGetShortT(signed short val) {
  PblShort_T conv = PblShort_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Unsigned Short type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblUShort_T PblGetUShortT(unsigned short val) {
  PblUShort_T conv = PblUShort_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Int type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblInt_T PblGetIntT(signed int val) {
  PblInt_T conv = PblInt_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Unsigned Int type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblUInt_T PblGetUIntT(unsigned int val) {
  PblUInt_T conv = PblUInt_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Long type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblLong_T PblGetLongT(signed long val) {
  PblLong_T conv = PblLong_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Unsigned Long type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblULong_T PblGetULongT(unsigned long val) {
  PblULong_T conv = PblULong_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Long Long type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblLongLong_T PblGetLongLongT(signed long long val) {
  PblLongLong_T conv = PblLongLong_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Unsigned Long Long type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblULongLong_T PblGetULongLongT(unsigned long long val) {
  PblULongLong_T conv = PblULongLong_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Float type
 * @param val The C-type to be converted
 * @return The newly created PBL Char type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblFloat_T PblGetFloatT(float val) {
  PblFloat_T conv = PblFloat_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Double type
 * @param val The C-type to be converted
 * @return The newly created PBL Double type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblDouble_T PblGetDoubleT(double val) {
  PblDouble_T conv = PblDouble_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Long Double type
 * @param val The C-type to be converted
 * @return The newly created PBL Long Double type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblLongDouble_T PblGetLongDoubleT(long double val) {
  PblLongDouble_T conv = PblLongDouble_T_DefDefault;
  conv.actual = val;
  return conv;
}
