///
/// Testing for the header io.h
///
/// @author Luna-Klatzer

#include "gtest/gtest.h"
#include "io.h"
#include "types.h"

TEST(IOPrintTest, SimplePrint) {
    pbl_string_t string = pbl_allocate_string_t(
        11, "hello world"
    );

    // size is per default 50 + 1 (for null char)
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));

    pbl_print(&string);

    // deallocating the string
    pbl_deallocate_string_t(&string);
}
