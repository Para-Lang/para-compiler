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
#define PblFile_T_Size sizeof(FILE*)
/// Returns the declaration default for the type `PblFile_T`
#define PblFile_T_DeclDefault (PblFile_T) {.meta={.defined=false, .byte_size=PblFile_T_Size}}
/// Returns the definition default for the type `PblFile_T`
#define PblFile_T_DefDefault (PblFile_T) {                   \
    .meta={.defined=false, .byte_size=PblFile_T_Size},       \
    .actual=NULL                                             \
  }

/// File Descriptor used to perform I/O actions on a file
struct PblFile {
  /// PBL meta type - keeps track of initialisation
  PblVarMeta_T meta;
  /// Actual value
  FILE* actual;
};
/// Stream type, which is a unique alias for PBLFileDescriptor_T
typedef struct PblFile PblFile_T;

// ---- Stream --------------------------------------------------------------------------------------------------------

/// Size of the type `PblStream_T` in bytes
#define PblStream_T_Size PblUInt_T_Size + PblFile_T_Size + PblBool_T_Size
/// Returns the declaration default for the type `PblStream_T`
#define PblStream_T_DeclDefault (PblStream_T) {.meta={.defined=false, .byte_size=PblStream_T_Size}}
/// Returns the definition default for the type `PblStream_T`
#define PblStream_T_DefDefault (PblStream_T) {                                                    \
    .meta={.defined=false, .byte_size=PblStream_T_Size},                                          \
    .actual={.fd=PblUInt_T_DefDefault, .file=PblFile_T_DefDefault, .open=PblBool_T_DefDefault}    \
  }

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
#define PBL_STREAM_STDIN (PblStream_T) {                                              \
    .meta={.defined=true, .byte_size=PblStream_T_Size},                               \
    .actual={                                                                         \
      .fd={.meta={.defined=true, .byte_size=PblUInt_T_Size}, .actual=0},              \
      .file=PblGetFileT(stdin),                                                       \
      .open=PblGetBoolT(true)                                                         \
      .mode                                                                                  \
    }                                                                                 \
  }

/// Standard stream for outputting to the default program console
#define PBL_STREAM_STDOUT (PblStream_T) {                                             \
    .meta={.defined=true, .byte_size=PblStream_T_Size},                               \
    .actual={                                                                         \
      .fd={.meta={.defined=true, .byte_size=PblUInt_T_Size}, .actual=1},              \
      .file=PblGetFileT(stdout),                                                      \
      .open=PblGetBoolT(true)                                                         \
    }                                                                                 \
  }

/// Standard stream for outputting error messages to the default program console
#define PBL_STREAM_STDERR (PblStream_T) {                                             \
    .meta={.defined=true, .byte_size=PblStream_T_Size},                               \
    .actual={                                                                         \
      .fd={.meta={.defined=true, .byte_size=PblUInt_T_Size}, .actual=2},              \
      .file=PblGetFileT(stderr),                                                      \
      .open=PblGetBoolT(true)                                                         \
    }                                                                                 \
  }

// ---- Handler functions ---------------------------------------------------------------------------------------------

PblFile_T PblGetFileT(FILE* val);

PblStream_T PblGetStreamT(int fd, const char* mode);

/// Arguments struct for PblPrint (PblPrintOverhead)
struct PblPrintArgs {
  PblString_T *out;
  PblStream_T stream;
  PblChar_T end;
};

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
