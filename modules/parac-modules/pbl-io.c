///
/// IO Implementation based on stdio.h
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "./pbl-io.h"
#include "./pbl-string.h"
#include <stdio.h>

/**
 * @brief Converts the low level C-Type to a PBL File type
 * @param val The FILE pointer C-type
 * @return The newly created PBL File type
 * @note This is a C to Para-C type conversion function - args are in C therefore
 */
PblFile_T PblGetFileT(FILE* val) {
  PblFile_T conv = PblFile_T_DefDefault;
  conv.actual = val;
  return conv;
}

/**
 * @brief Converts the low level C-Type to a PBL Stream type. Creates the FILE* pointer as well
 * @param fd The file descriptor that will be converted
 * @param fd The mode that should be used to open the FILE*
 * @return The newly created PBL Stream type
 * @note This is a C to Para-C type conversion function - args are therefore in C
 */
PblStream_T PblGetStreamT(int fd, const char* mode) {
  PblStream_T conv = PblStream_T_DefDefault;
  conv.actual.fd = PblGetUIntT(fd);
  conv.actual.file = PblGetFileT(fdopen(fd, mode));
  conv.actual.open = PblGetBoolT(true);
  return conv;
}

/**
 * @brief The base of the PblPrint() (macro) function
 * @param out The string that should be printed out
 * @param stream The stream it should be printed onto
 * @param end The end character that should be printed after `out`
 */
void PblPrintBase(PblString_T *out, const PblStream_T stream, const PblChar_T end) {
  fprintf(stream.actual.file.actual, "%s", out->actual.str);
  fprintf(stream.actual.file.actual, "%c", end.actual);
}

void PblPrintOverhead(struct PblPrintArgs in) {
  PblString_T *out = (PblString_T *) in.out;
  PblStream_T stream = in.stream.meta.defined ? in.stream : PBL_STREAM_STDOUT;
  PblChar_T end =
    in.end.meta.defined ? in.end : (PblChar_T){.actual='\n', .meta={.defined = true, .byte_size = PblChar_T_Size}};
  return PblPrintBase(out, stream, end);
}
