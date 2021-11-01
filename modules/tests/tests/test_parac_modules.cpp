///
/// Testing for the macros in the header pbl.h
///
/// @author Luna-Klatzer

#include <cstring>
#include <pbl.h>
#include "gtest/gtest.h"

TEST(MacroTest, SimpleCheckForExistances) {
  EXPECT_TRUE(__parac);
  EXPECT_TRUE(strcmp(__parac, "0.1.dev5") == 0);
}