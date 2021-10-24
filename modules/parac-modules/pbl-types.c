///
/// Base Para-C Types Implementation, which implement default declaration and default definition types. This also
/// includes meta-data tracking based on the `PblVarMeta` type.
///
/// @date 08-10-2021
/// @author Luna-Klatzer
/// @note The TYPE_T_Size macros define the actual size of the C-elements, without the meta struct - This is only used
/// to know the actual size that can be used from the user.

#include "pbl-types.h"

PblBool_T PblGetBoolT(bool val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblBool_T, bool)
}

PblSize_T PblGetSizeT(size_t val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblSize_T, size_t)
}

PblChar_T PblGetCharT(signed char val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblChar_T, signed char)
}

PblUChar_T PblGetUCharT(unsigned char val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUChar_T, unsigned char)
}

PblShort_T PblGetShortT(signed short val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblShort_T, signed short)
}

PblUShort_T PblGetUShortT(unsigned short val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUShort_T, unsigned short)
}

PblInt_T PblGetIntT(signed int val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblInt_T, signed int)
}

PblUInt_T PblGetUIntT(unsigned int val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblUInt_T, unsigned int)
}

PblLong_T PblGetLongT(signed long val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLong_T, signed long)
}

PblULong_T PblGetULongT(unsigned long val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblULong_T, unsigned long)
}

PblLongLong_T PblGetLongLongT(signed long long val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLongLong_T, signed long long)
  }

PblULongLong_T PblGetULongLongT(unsigned long long val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblULongLong_T, unsigned long long)
}

PblFloat_T PblGetFloatT(float val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblFloat_T, float)
}

PblDouble_T PblGetDoubleT(double val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblDouble_T, double)
}

PblLongDouble_T PblGetLongDoubleT(long double val) {
  PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(PblLongDouble_T, long double)
}