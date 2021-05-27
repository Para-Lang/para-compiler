cmake_minimum_required(VERSION 3.17)
project(implementation-examples-exceptions C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(
        implementation-examples-exceptions exception.c
)
