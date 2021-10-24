///
/// IO Implementation based on stdio.h
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "./pbl-string.h"
#include "./pbl-types.h"
#include <stdbool.h>
#include <stdio.h>

#ifndef PARAC_MODULES_IO_H
#define PARAC_MODULES_IO_H

#ifdef __cplusplus
extern "C" {
#endif

// ---- Declarations --------------------------------------------------------------------------------------------------

// ---- File ----------------------------------------------------------------------------------------------------------

/// Size of the type `PblFile_T` in bytes
#define PblFile_T_Size sizeof(FILE *)
/// Returns the declaration default for the type `PblFile_T`
#define PblFile_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblFile_T)
/// Returns the definition default for the type `PblFile_T`
#define PblFile_T_DefDefault PBL_DEFINITION_SINGLE_CONSTRUCTOR(PblFile_T, NULL)

/// File Descriptor used to perform I/O actions on a file
struct PblFile {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// Actual value
  FILE *actual;
};
/// Stream type, which is a unique alias for PBLFileDescriptor_T
typedef struct PblFile PblFile_T;

// ---- Stream --------------------------------------------------------------------------------------------------------

/// Size of the type `PblStream_T` in bytes
#define PblStream_T_Size PblUInt_T_Size + PblFile_T_Size + PblBool_T_Size + PblString_T_Size
/// Returns the declaration default for the type `PblStream_T`
#define PblStream_T_DeclDefault PBL_DECLARATION_CONSTRUCTOR(PblStream_T)
/// Returns the definition default for the type `PblStream_T`
#define PblStream_T_DefDefault                                                                                         \
  PBL_DEFINITION_STRUCT_CONSTRUCTOR(PblStream_T, .fd = PblUInt_T_DefDefault, .file = PblFile_T_DefDefault,             \
                                    .open = PblBool_T_DefDefault, .mode = PblString_T_DefDefault)

/// Base Struct of PblString - avoid using this type
struct PblStreamBase {
  /// The unique integer identifier associated with the file Descriptor
  PblUInt_T fd;
  /// The FILE pointer, which points to the stream/file - defined if the stream was opened
  PblFile_T file;
  /// Describes whether the file descriptor is currently in use
  PblBool_T open;
  /// The mode the FILE* was opened
  PblString_T mode;
};

/// File Descriptor used to perform I/O actions on a file
struct PblStream {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// Actual value
  struct PblStreamBase actual;
};
/// Stream type, which is a unique alias for PBLFileDescriptor_T
typedef struct PblStream PblStream_T;

// ---- Streams -------------------------------------------------------------------------------------------------------

/// Standard stream for getting input on the default program console
#define PBL_STREAM_STDIN                                                                                               \
  PBL_DEFINITION_STRUCT_CONSTRUCTOR(PblStream_T, .fd = PblGetUIntT(0), .file = PblGetFileT(stdin),                     \
                                    .open = PblGetBoolT(true), .mode = PblGetStringT("a"))

/// Standard stream for outputting to the default program console
#define PBL_STREAM_STDOUT                                                                                              \
  PBL_DEFINITION_STRUCT_CONSTRUCTOR(PblStream_T, .fd = PblGetUIntT(1), .file = PblGetFileT(stdout),                    \
                                    .open = PblGetBoolT(true), .mode = PblGetStringT("a"))

/// Standard stream for outputting error messages to the default program console
#define PBL_STREAM_STDERR                                                                                              \
  PBL_DEFINITION_STRUCT_CONSTRUCTOR(PblStream_T, .fd = PblGetUIntT(2), .file = PblGetFileT(stderr),                    \
                                    .open = PblGetBoolT(true), .mode = PblGetStringT("a"))

// ---- Handler functions ---------------------------------------------------------------------------------------------

/**
 * @brief Converts the low level C-Type to a PBL File type
 * @param val The FILE pointer C-type
 * @return The newly created PBL File type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblFile_T PblGetFileT(FILE *val);

/**
 * @brief Converts the low level C-Type to a PBL Stream type. Creates the FILE* pointer as well
 * @param fd The file descriptor that will be converted
 * @param mode The mode that should be used to open the FILE*
 * @return The newly created PBL Stream type
 * @note This is a C to Para-C type conversion function - args are therefore in C
 */
PblStream_T PblGetStreamT(int fd, const char *mode);

/// Arguments struct for PblPrint (PblPrintOverhead)
struct PblPrintArgs {
  PblString_T *out;
  PblStream_T stream;
  PblChar_T end;
};

/**
 * @brief Prints the content of the passed string
 * @param out The string that should be printed out
 * @param stream The stream it should be printed onto
 * @param end The end character that should be printed after `out`
 * @note This is the base function that is wrapped using `PblPrintOverhead`
 */
void PblPrintBase(PblString_T *out, const PblStream_T stream, const PblChar_T end);

/**
 * @brief Printing overhead for `PblPrintBase` - this it the function called by the macro `PblPrint`
 * @param in The parameter struct
 */
void PblPrintOverhead(struct PblPrintArgs in);

/**
 * @brief Prints the content of the passed string
 * @param out The string that should be printed out
 * @param stream The stream it should be printed onto
 * @param end The end character that should be printed after `out`
 */
#define PblPrint(...) PblPrintOverhead((struct PblPrintArgs){__VA_ARGS__});

#ifdef __cplusplus
}
#endif

#endif//PARAC_MODULES_IO_H
