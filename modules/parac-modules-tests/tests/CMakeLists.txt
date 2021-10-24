include_directories(${gtest_SOURCE_DIR}/include ${gtest_SOURCE_DIR})

add_executable(runParacModulesTests
        test_io.cpp
        test_types.cpp
        test_parac_modules.cpp test_string.cpp test_int.cpp)

target_link_libraries(runParacModulesTests gtest gtest_main)
target_link_libraries(runParacModulesTests parac-modules)