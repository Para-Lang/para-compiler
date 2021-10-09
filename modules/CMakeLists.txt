cmake_minimum_required(VERSION 3.17)
project(parac-modules)

set(CMAKE_C_STANDARD 11)

include_directories(parac-modules)

add_subdirectory(parac-modules)
add_subdirectory(parac-modules-tests)
target_link_libraries(parac-modules)