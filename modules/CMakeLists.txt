cmake_minimum_required(VERSION 3.17)
project(parac-modules)

add_definitions(-fprofile-arcs -ftest-coverage)

set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fprofile-arcs -ftest-coverage -O0")

include_directories(parac-modules)

add_subdirectory(parac-modules)
add_subdirectory(parac-modules-tests)
target_link_libraries(parac-modules)

if (CMAKE_BUILD_TYPE MATCHES Debug)
    add_definitions(-DDEBUG)
endif()