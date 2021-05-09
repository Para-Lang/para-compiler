cmake_minimum_required(VERSION 3.17)
project(para-lib C)

set(CMAKE_C_STANDARD 11)

include_directories(.)

add_executable(lib
        para.c
        para.h)
