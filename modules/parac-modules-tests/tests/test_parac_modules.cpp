///
/// Testing for the macros in the header parac_modules.h
///
/// @author Luna-Klatzer

#include "gtest/gtest.h"
#include "parac_modules.h"

TEST(MacroTest, SimpleCheckForExistances) {
    EXPECT_TRUE(PARAC_LANG);
    EXPECT_TRUE(strcmp(PARAC_LIB_VERSION, ""));
}