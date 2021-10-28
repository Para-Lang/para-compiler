///
/// Testing for the header pbl-io.h
///
/// @author Luna-Klatzer

#include <pbl.h>
#include "gtest/gtest.h"

TEST(IOFileTest, ConversionCheck) {
  FILE* val = fdopen(2, "w+");
  PblFile_T stream = PblGetFileT(val);

  EXPECT_EQ(stream.actual, val);
  EXPECT_EQ(stream.meta.defined, true);
  EXPECT_EQ(stream.meta.byte_size, PblFile_T_Size);
  EXPECT_EQ(
    stream.meta.byte_size,
    sizeof(FILE*)
  );
}

TEST(IOStreamTest, ConversionCheck) {
  PblStream_T stream = PblGetStreamT(1, "w+");

  EXPECT_EQ(stream.actual.fd.actual, 1);
  EXPECT_TRUE(strcmp(stream.actual.mode.actual.str, "w+") == 0);
  EXPECT_EQ(stream.actual.open.actual, true);
  EXPECT_EQ(stream.meta.defined, true);
  EXPECT_EQ(stream.meta.byte_size, PblStream_T_Size);
  EXPECT_EQ(
    stream.meta.byte_size,
    PblString_T_Size + PblUInt_T_Size + PblFile_T_Size + PblBool_T_Size
    );
}

TEST(IOPrintTest, SimplePrint) {
  PblString_T str = PblCreateStringT("hello world", PblGetUIntT(11));

  // size is per default 50 + 1 (for null char)
  EXPECT_EQ(str.actual.str_alloc_size.actual, (50 + 1) * sizeof(char));

  PblPrint(.out=&str, .end=PblGetCharT(' '));
  PblPrint(&str);

  // deallocating the string
  PblDeallocateStringT(&str);
}

TEST(IOPrintTest, SimplePrintWithSetStream) {
  PblString_T str = PblCreateStringT("hello world", PblGetUIntT(11));

  // size is per default 50 + 1 (for null char)
  EXPECT_EQ(str.actual.str_alloc_size.actual, (50 + 1) * sizeof(char));

  PblPrint(.out = &str, .stream=PBL_STREAM_STDOUT);

  // deallocating the string
  PblDeallocateStringT(&str);
}

