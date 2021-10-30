///
/// IO Implementation based on stdio.h
///
/// @author Luna-Klatzer

#include <stdio.h>

#include "./pbl-io.h"
#include "./pbl-string.h"
#include "./pbl-mem.h"

PblFile_T PblGetFileT(FILE *val) {
  // Validate the pointer for safety measures
  val = PblValPtr(val);

  PblFile_T conv = PblFile_T_DefDefault;
  conv.actual = val;
  return conv;
}

PblStream_T PblGetStreamT(int fd, const char *mode) {
  // Validate the pointer for safety measures
  mode = PblValPtr((void*) mode);

  PblStream_T conv = PblStream_T_DefDefault;
  conv.actual.fd = PblGetUIntT(fd);
  conv.actual.file = PblGetFileT(fdopen(fd, mode));
  conv.actual.mode = PblGetStringT(mode);
  conv.actual.open = PblGetBoolT(true);
  return conv;
}

PblVoid_T PblPrint_Base(PblString_T *out, const PblStream_T stream, const PblChar_T end) {
  // Validate the pointer for safety measures
  out = PblValPtr((void*) out);

  fprintf(stream.actual.file.actual, "%s", out->actual.str);
  fprintf(stream.actual.file.actual, "%c", end.actual);
  return PblVoid_T_DeclDefault;
}

PblVoid_T PblPrint_Overhead(struct PblPrint_Args in) {
  // Validate the pointer for safety measures
  PblString_T *out = PblValPtr((void*) in.out);

  PblStream_T stream = in.stream.meta.defined ? in.stream : PBL_STREAM_STDOUT;
  PblChar_T end = in.end.meta.defined ? in.end : PblGetCharT('\n');
  return PblPrint_Base(out, stream, end);
}
