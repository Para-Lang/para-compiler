//
// Testing for the header io.h - Created by Luna-K on 09/10/2021.
//

#include "gtest/gtest.h"
#include "io.h"
#include "types.h"

TEST(IOPrintTest, SimplePrint) {
    __pbl_string_t string = __pbl_allocate_string_t(
        11, "hello world"
    );

    // size is per default 50 + 1 (for null char)
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));

    __pbl_print(&string);

    // deallocating the string
    __pbl_deallocate_string_t(&string);
}
