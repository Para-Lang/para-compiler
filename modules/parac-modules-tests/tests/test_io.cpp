//
// Testing for the header io.h - Created by Luna-K on 09/10/2021.
//

#include "gtest/gtest.h"
#include "io.h"
#include "types.h"

TEST(IOPrintTest, SimplePrint) {
    __pbl_type_string string = __pbl_allocate_type_string(
        11, "hello world"
    );

    // size is per default 50 + 1 (for null char)
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));

    __pbl_print(&string);

    // deallocating the string
    __pbl_deallocate_type_string(&string);
}
