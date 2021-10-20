//
// Testing for the header types.h - Created by Luna-K on 09/10/2021.
//

#include "gtest/gtest.h"
#include "types.h"

// IMPORTANT! When actually using __pbl_string_t, do not use a bigger length than of the actual string

TEST(StringTypesTest, SimpleInitialisation1) {
    __pbl_string_t string = __pbl_allocate_string_t(
        15, "hello world"
    );

    // size is per default 50 + 1 (for null char)
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));

    // deallocating the string
    __pbl_deallocate_string_t(&string);
}

TEST(StringTypesTest, SimpleInitialisation2) {
    __pbl_string_t string = __pbl_allocate_string_t(
        60, "hello world"
    );

    // size is per default 50 + 1 (for null char) - will be resized to 100, since len is 60
    EXPECT_EQ(string.byte_size, (100 + 1) * sizeof(char));

    // deallocating the string
    __pbl_deallocate_string_t(&string);
}

TEST(StringTypesTest, SimpleInitialisation3) {
    __pbl_string_t string = __pbl_allocate_string_t(
        600, "hello world"
    );

    // size is per default 50 + 1 (for null char) - will be resized to 100, since len is 60
    EXPECT_EQ(string.byte_size, (650 + 1) * sizeof(char));

    // deallocating the string
    __pbl_deallocate_string_t(&string);
}

TEST(StringTypesTest, ValidateDeallocation) {
    __pbl_string_t string = __pbl_allocate_string_t(
        49, "hello world"
    );

    // size is per default 50 + 1 (for null char) - will be resized to 100, since len is 60
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));

    // deallocating the string
    __pbl_deallocate_string_t(&string);

    EXPECT_EQ(string.byte_size, sizeof(NULL));
    EXPECT_EQ(string.len, 0);
    EXPECT_EQ(string.allocated_len, 0);
}

TEST(StringTypesTest, ValidateAllocation) {
    __pbl_string_t string = __pbl_allocate_string_t(
        49, "hello world"
    );
    // size is per default 50 + 1 (for null char) - will be resized to 100, since len is 60
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));
    EXPECT_EQ(string.len, 49);
    EXPECT_EQ(string.allocated_len, 51);

    // deallocating the string
    __pbl_deallocate_string_t(&string);
}

TEST(StringTypesTest, ValidateOverwrite) {
    __pbl_string_t string = __pbl_allocate_string_t(
        11, "hello world"
    );
    // size is per default 50 + 1 (for null char) - will be resized to 100, since len is 60
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));
    EXPECT_EQ(string.len, 11);
    EXPECT_EQ(string.allocated_len, 51);

    __pbl_write_to_string_t(&string, 15, "Hello World!!!!");
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));
    EXPECT_EQ(string.len, 15);
    EXPECT_EQ(string.allocated_len, 51);

    // deallocating the string
    __pbl_deallocate_string_t(&string);
}

TEST(StringTypesTest, ValidateReallocOverwrite) {
    __pbl_string_t string = __pbl_allocate_string_t(
        11, "hello world"
    );
    // size is per default 50 + 1 (for null char) - will be resized to 100, since len is 60
    EXPECT_EQ(string.byte_size, (50 + 1) * sizeof(char));
    EXPECT_EQ(string.len, 11);
    EXPECT_EQ(string.allocated_len, 51);

    __pbl_write_to_string_t(
        &string,
        50,
        "12345678901234567890123456789012345678901234567890"
    );
    EXPECT_EQ(string.byte_size, (100 + 1) * sizeof(char));
    EXPECT_EQ(string.len, 50);
    EXPECT_EQ(string.allocated_len, 101);

    // deallocating the string
    __pbl_deallocate_string_t(&string);
}
