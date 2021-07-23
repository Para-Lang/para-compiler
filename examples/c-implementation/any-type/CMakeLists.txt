cmake_minimum_required(VERSION 3.17)
project(any_type C)

set(CMAKE_C_STANDARD 11)

include_directories(SYSTEM .)

set(
        SOURCE_FILES
        main.c
        __parac__.c
        __parac__.h
)

add_executable(
        any_type ${SOURCE_FILES}
)
