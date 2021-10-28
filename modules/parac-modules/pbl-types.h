///
/// Base Para-C Types Implementation, which implement default declaration and default definition types. This also
/// includes meta-data tracking based on the `PblVarMeta` type.
///
/// @date 08-10-2021
/// @author Luna-Klatzer
/// @note The TYPE_T_Size macros define the actual size of the C-elements, without the meta struct - This is only used
/// to know the actual size that can be used from the user.

#include <stdbool.h>
#include <stddef.h>
#include <malloc.h>

#ifndef PARAC_MODULES_TYPES_H
#define PARAC_MODULES_TYPES_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Macro Functions -----------------------------------------------------------------------------------------------

/// Returns the effective size of a Para-C type that can be actually used. Must be a Para-C type
#define PBL_SIZEOF(type) (type##_Size)
/// Returns the effective C size of a type. This also includes meta data
#define PBL_C_SIZEOF(type) (sizeof(type))

// ---- All Base types implemented in the Para-C style ----------------------------------------------------------------

/// Base Meta Type contained in ALL variables - has no DeclDefault or DefDefault
struct PblMetaVarCtx {
  /// Returns whether the variable is defined. This defaults to false (unless a declaration is use, where accessing the
  /// variable is undefined behaviour. This means it should IN NO CASE BE accessed when it's only declared)
  /// This variable is used to also validate whether a variable can be accessed without raising an error!
  bool defined;
  /// Size of the allocated memory in bytes - this should not include the property PblVarMeta
  /// @note To properly implement this, for a struct implementation there should be both the base (without `meta`)
  /// struct and the actual usage struct (with `meta`). `sizeof` can then be applied onto the base to correctly get
  /// the size
  size_t byte_size;
};

/// Base Meta Type contained in ALL variables
typedef struct PblMetaVarCtx PblMetaVarCtx_T;

// ---- Constructor Macros --------------------------------------------------------------------------------------------

/// Declaration constructor which initialised the meta data for the passed type
#define PBL_DECLARATION_CONSTRUCTOR(type) (type) {                                                                     \
    .meta = {.defined = false, .byte_size = type##_Size}                                                               \
  }

/// Definition constructor which initialises the meta data for the passed type and passes to `.actual` the args as struct
#define PBL_DEFINITION_STRUCT_CONSTRUCTOR(type, ...) (type) {                                                          \
    .meta = {.defined = true, .byte_size = type##_Size}, .actual = { __VA_ARGS__ }                                     \
  }

/// Definition constructor which initialised the meta data for the passed type and passes to `.actual` the single arg
#define PBL_DEFINITION_SINGLE_CONSTRUCTOR(type, var_actual) (type) {                                                   \
    .meta = {.defined = true, .byte_size = type##_Size}, .actual = var_actual                                          \
  }

/// Creates the body for a Para-C type definition wrapper - the base_type is the actual value/struct
#define PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(base_type) { \
    PblMetaVarCtx_T meta; \
    base_type actual; \
   };

// ---- Void Type -----------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL PblVoid_T type
#define PblVoid_T_Size sizeof(void)
/// Returns the declaration default for the type `PblVoid_T`
#define PblVoid_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblVoid_T)

/// PBL Void implementation
struct PblVoid {
  PblMetaVarCtx_T meta;
};
/// PBL Void implementation
typedef struct PblVoid PblVoid_T;

// ---- Numeric Values ------------------------------------------------------------------------------------------------
// All types that are not unsigned are signed by default to ensure consistency
// Note that in those definitions the size is calculated using the C-type (as only one "real" property is there)

// ---- Bool ----------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Bool type
#define PblBool_T_Size sizeof(bool)
/// Returns the declaration default for the type `PblBool_T`
#define PblBool_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblBool_T)
/// Returns the definition default for the type `PblBool_T`
#define PblBool_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblBool_T, false)

/// PBL Bool implementation
struct PblBool PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(bool)
/// PBL Bool implementation
typedef struct PblBool PblBool_T;

// ---- Byte Size -----------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Size type
#define PblSize_T_Size sizeof(size_t)
/// Returns the declaration default for the type `PblSize_T`
#define PblSize_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblSize_T)
/// Returns the definition default for the type `PblSize_T`
#define PblSize_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblSize_T, 0)

/// PBL Byte Size implementation
struct PblSize PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(size_t)
/// PBL Byte Size implementation
typedef struct PblSize PblSize_T;

// ---- Char ----------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Signed Char type
#define PblChar_T_Size sizeof(signed char)
/// Returns the declaration default for the type `PblChar_T`
#define PblChar_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblChar_T)
/// Returns the definition default for the type `PblChar_T`
#define PblChar_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblChar_T, 0)

/// PBL Signed Char implementation
struct PblChar PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(signed char)
/// PBL Signed Char implementation
typedef struct PblChar PblChar_T;

// ---- UChar ---------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Unsigned Char type
#define PblUChar_T_Size sizeof(unsigned char)
/// Returns the declaration default for the type `PblUChar_T_Size`
#define PblUChar_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUChar_T)
/// Returns the definition default for the type `PblUChar_T_Size`
#define PblUChar_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUChar_T, 0)

/// PBL Unsigned Char implementation
struct PblUChar PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(unsigned char)
/// PBL Unsigned Char implementation
typedef struct PblUChar PblUChar_T;

// ---- Short ---------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Signed Short type
#define PblShort_T_Size sizeof(signed short)
/// Returns the declaration default for the type `PblShort_T`
#define PblShort_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblShort_T)
/// Returns the definition default for the type `PblShort_T`
#define PblShort_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblShort_T, 0)

/// PBL Signed Short implementation
struct PblShort PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(signed short)
/// PBL Signed Short implementation
typedef struct PblShort PblShort_T;

// ---- UShort --------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Unsigned Short type
#define PblUShort_T_Size sizeof(unsigned short)
/// Returns the declaration default for the type `PblUShort_T_Size`
#define PblUShort_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUShort_T)
/// Returns the definition default for the type `PblUShort_T_Size`
#define PblUShort_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUShort_T, 0)

/// PBL Unsigned Short implementation
struct PblUShort PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(unsigned short)
/// PBL Unsigned Short implementation
typedef struct PblUShort PblUShort_T;

// ---- Int -----------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Signed Int type
#define PblInt_T_Size sizeof(signed int)
/// Returns the declaration default for the type `PblInt_T`
#define PblInt_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblInt_T)
/// Returns the definition default for the type `PblInt_T`
#define PblInt_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblInt_T, 0)

/// PBL Signed Int implementation
struct PblInt PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(signed int)
/// PBL Signed Int implementation
typedef struct PblInt PblInt_T;

// ---- UInt ----------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Unsigned Int type
#define PblUInt_T_Size sizeof(unsigned int)
/// Returns the declaration default for the type `PblUInt_T`
#define PblUInt_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblUInt_T)
/// Returns the definition default for the type `PblUInt_T`
#define PblUInt_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblUInt_T, 0)

/// PBL Unsigned Int implementation
struct PblUInt PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(unsigned int)
/// PBL Unsigned Int implementation
typedef struct PblUInt PblUInt_T;

// ---- Long ----------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Signed Long type
#define PblLong_T_Size sizeof(signed long)
/// Returns the declaration default for the type `PblLong_T`
#define PblLong_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblLong_T)
/// Returns the definition default for the type `PblLong_T`
#define PblLong_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblLong_T, 0)

/// PBL Signed Long implementation
struct PblLong PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(signed long)
/// PBL Signed Long implementation
typedef struct PblLong PblLong_T;

// ---- ULong ---------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Unsigned Long type
#define PblULong_T_Size sizeof(unsigned long)
/// Returns the declaration default for the type `PblULong_T`
#define PblULong_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblULong_T)
/// Returns the definition default for the type `PblULong_T`
#define PblULong_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblULong_T, 0)

/// PBL Unsigned Long implementation
struct PblULong PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(unsigned long)
/// PBL Unsigned Long implementation
typedef struct PblULong PblULong_T;

// ---- Long Long -----------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Signed Long Long type
#define PblLongLong_T_Size sizeof(signed long long)
/// Returns the declaration default for the type `PblLongLong_T`
#define PblLongLong_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblLongLong_T)
/// Returns the definition default for the type `PblLongLong_T`
#define PblLongLong_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblLongLong_T, 0)

/// PBL Signed Long Long implementation
struct PblLongLong PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(signed long long)
/// PBL Signed Long Long implementation
typedef struct PblLongLong PblLongLong_T;

// ---- ULong Long ----------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Unsigned Long Long type
#define PblULongLong_T_Size sizeof(unsigned long long)
/// Returns the declaration default for the type `PblULongLong_T`
#define PblULongLong_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblULongLong_T)
/// Returns the definition default for the type `PblULongLong_T`
#define PblULongLong_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblULongLong_T, 0)

/// PBL Unsigned Long Long implementation
struct PblULongLong PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(unsigned long long)
/// PBL Unsigned Long Long implementation
typedef struct PblULongLong PblULongLong_T;

// ---- Float ---------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Float type
#define PblFloat_T_Size sizeof(float)
/// Returns the declaration default for the type `PblFloat_T`
#define PblFloat_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblFloat_T)
/// Returns the definition default for the type `PblFloat_T`
#define PblFloat_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblFloat_T, 0)

/// PBL Float implementation
struct PblFloat PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(float)
/// PBL Float implementation
typedef struct PblFloat PblFloat_T;

// ---- Double --------------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Double type
#define PblDouble_T_Size sizeof(double)
/// Returns the declaration default for the type `PblDouble_T`
#define PblDouble_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblDouble_T)
/// Returns the definition default for the type `PblDouble_T`
#define PblDouble_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblDouble_T, 0)

/// PBL Double implementation
struct PblDouble PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(double)
/// PBL Double implementation
typedef struct PblDouble PblDouble_T;

// ---- Long Double ---------------------------------------------------------------------------------------------------

/// (Never use this for malloc - this only indicates the usable memory space)
/// Returns the size in bytes of the PBL Long Double type
#define PblLongDouble_T_Size sizeof(long double)
/// Returns the declaration default for the type `PblLongDouble_T`
#define PblLongDouble_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblLongDouble_T)
/// Returns the definition default for the type `PblLongDouble_T`
#define PblLongDouble_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblLongDouble_T, 0)

/// PBL Long Double implementation
struct PblLongDouble PBL_TYPE_DEFINITION_WRAPPER_CONSTRUCTOR(long double)
/// PBL Long Double implementation
typedef struct PblLongDouble PblLongDouble_T;

// ---- Helper Functions ----------------------------------------------------------------------------------------------

/// This a macro function definition body constructor, which should be used to directly convert C types into their
/// Para-C counterparts. This should be only used for Para-C types that have as actual a single property, as this does
/// not support complex initialisation.
#define PBL_CONVERSION_FUNCTION_DEF_CONSTRUCTOR(parac_type, c_type) {                                                  \
    parac_type conv = parac_type##_DefDefault;                                                                         \
    conv.actual = val;                                                                                                 \
    return conv;                                                                                                       \
  }

/**
 * @brief Converts the low level C-Type to a PBL Bool type
 * @param val The C-type to be converted
 * @return The newly created PBL Bool type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 * @
 */
PblBool_T PblGetBoolT(bool val);

/**
* @brief Converts the low level C-Type to a PBL Byte Size type
* @param val The C-type to be converted
* @return The newly created PBL Byte Size type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblSize_T PblGetSizeT(size_t val);

/**
* @brief Converts the low level C-Type to a PBL Char type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblChar_T PblGetCharT(signed char val);

/**
* @brief Converts the low level C-Type to a PBL Unsigned Char type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUChar_T PblGetUCharT(unsigned char val);

/**
* @brief Converts the low level C-Type to a PBL Short type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblShort_T PblGetShortT(signed short val);

/**
* @brief Converts the low level C-Type to a PBL Unsigned Short type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUShort_T PblGetUShortT(unsigned short val);

/**
* @brief Converts the low level C-Type to a PBL Int type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblInt_T PblGetIntT(signed int val);

/**
* @brief Converts the low level C-Type to a PBL Unsigned Int type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblUInt_T PblGetUIntT(unsigned int val);

/**
* @brief Converts the low level C-Type to a PBL Long type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLong_T PblGetLongT(signed long val);

/**
* @brief Converts the low level C-Type to a PBL Unsigned Long type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULong_T PblGetULongT(unsigned long val);

/**
* @brief Converts the low level C-Type to a PBL Long Long type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLongLong_T PblGetLongLongT(signed long long val);

/**
* @brief Converts the low level C-Type to a PBL Unsigned Long Long type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblULongLong_T PblGetULongLongT(unsigned long long val);

/**
* @brief Converts the low level C-Type to a PBL Float type
* @param val The C-type to be converted
* @return The newly created PBL Char type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblFloat_T PblGetFloatT(float val);

/**
* @brief Converts the low level C-Type to a PBL Double type
* @param val The C-type to be converted
* @return The newly created PBL Double type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblDouble_T PblGetDoubleT(double val);

/**
* @brief Converts the low level C-Type to a PBL Long Double type
* @param val The C-type to be converted
* @return The newly created PBL Long Double type
* @note This is a C to Para-C type conversion function - args are in C therefore
*/
PblLongDouble_T PblGetLongDoubleT(long double val);

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_TYPES_H
