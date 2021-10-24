///
/// Testing for the header pbl-io.h
///
/// @author Luna-Klatzer

#include "pbl-io.h"
#include "pbl-types.h"
#include "gtest/gtest.h"

TEST(IOPrintTest, SimplePrint) {
  PblString_T string = PblAllocateStringT("hello world", PblGetUIntT(11));

  // size is per default 50 + 1 (for null char)
  EXPECT_EQ(string.actual.str_alloc_size.actual, (50 + 1) * sizeof(char));

  PblPrint(&string);

  // deallocating the string
  PblDeallocateStringT(&string);
}

TEST(IOPrintTest, SimplePrintWithSetStream) {
  PblString_T string = PblAllocateStringT("hello world", PblGetUIntT(11));

  // size is per default 50 + 1 (for null char)
  EXPECT_EQ(string.actual.str_alloc_size.actual, (50 + 1) * sizeof(char));

  PblPrint(.out = &string, .stream=PBL_STREAM_STDOUT);

  // deallocating the string
  PblDeallocateStringT(&string);
}

