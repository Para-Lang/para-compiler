project(parac-modules-tests)

include(FetchContent)
FetchContent_Declare(
        gtest-1.11.0
        URL https://github.com/google/googletest/archive/609281088cfefc76f9d0ce82e1ff6c30cc3591e5.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(gtest-1.11.0)

add_subdirectory(tests)