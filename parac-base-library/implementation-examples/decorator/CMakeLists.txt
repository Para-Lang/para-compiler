cmake_minimum_required(VERSION 3.17)
project(implementation-examples-exceptions C)

set(CMAKE_C_STANDARD 11)

include_directories(SYSTEM .)

set(
    SOURCE_FILES
        decorator.c
        __parac__.h
)

add_executable(
        implementation-examples-exceptions ${SOURCE_FILES}
)
