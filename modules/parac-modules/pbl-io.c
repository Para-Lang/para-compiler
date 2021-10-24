///
/// IO Implementation based on stdio.h
///
/// @date 08-10-2021
/// @author Luna-Klatzer

#include "./pbl-io.h"
#include "./pbl-string.h"
#include <stdio.h>

PblFile_T PblGetFileT(FILE *val) {
  PblFile_T conv = PblFile_T_DefDefault;
  conv.actual = val;
  return conv;
}

PblStream_T PblGetStreamT(int fd, const char *mode) {
  PblStream_T conv = PblStream_T_DefDefault;
  conv.actual.fd = PblGetUIntT(fd);
  conv.actual.file = PblGetFileT(fdopen(fd, mode));
  conv.actual.mode = PblGetStringT(mode);
  conv.actual.open = PblGetBoolT(true);
  return conv;
}

void PblPrintBase(PblString_T *out, const PblStream_T stream, const PblChar_T end) {
  fprintf(stream.actual.file.actual, "%s", out->actual.str);
  fprintf(stream.actual.file.actual, "%c", end.actual);
}

void PblPrintOverhead(struct PblPrintArgs in) {
  PblString_T *out = (PblString_T *) in.out;
  PblStream_T stream = in.stream.meta.defined ? in.stream : PBL_STREAM_STDOUT;
  PblChar_T end =
    in.end.meta.defined ? in.end : (PblChar_T){.actual = '\n', .meta = {.defined = true, .byte_size = PblChar_T_Size}};
  return PblPrintBase(out, stream, end);
}
