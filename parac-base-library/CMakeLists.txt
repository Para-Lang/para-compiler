cmake_minimum_required(VERSION 3.17)
project(parac-base-library C)

set(CMAKE_C_STANDARD 11)

include_directories(SYSTEM ./src)

set(
    SOURCE_FILES
        ./src/parac.c
        ./src/parac.h
)

add_executable(
        parac-base-library ${SOURCE_FILES}
)
