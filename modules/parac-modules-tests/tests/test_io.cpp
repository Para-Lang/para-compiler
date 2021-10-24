///
/// Testing for the header pbl-io.h
///
/// @author Luna-Klatzer

#include "pbl-io.h"
#include "pbl-types.h"
#include "gtest/gtest.h"

TEST(IOPrintTest, SimplePrint) {
  PblString_T str = PblAllocateStringT("hello world", PblGetUIntT(11));

  // size is per default 50 + 1 (for null char)
  EXPECT_EQ(str.actual.str_alloc_size.actual, (50 + 1) * sizeof(char));

  PblPrint(&str);

  // deallocating the string
  PblDeallocateStringT(&str);
}

TEST(IOPrintTest, SimplePrintWithSetStream) {
  PblString_T str = PblAllocateStringT("hello world", PblGetUIntT(11));

  // size is per default 50 + 1 (for null char)
  EXPECT_EQ(str.actual.str_alloc_size.actual, (50 + 1) * sizeof(char));

  PblPrint(.out = &str, .stream=PBL_STREAM_STDOUT);

  // deallocating the string
  PblDeallocateStringT(&str);
}

