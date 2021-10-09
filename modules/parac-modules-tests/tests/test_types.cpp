//
// Testing for the header types.h - Created by Luna-K on 09/10/2021.
//

#include "gtest/gtest.h"
#include "types.h"

TEST(StringTypesTest, SimpleInitialisation) {
    __pbl_type_string string;
    string = __pbl_allocate_type_string(
            10, "hello world"
        );

    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));
}