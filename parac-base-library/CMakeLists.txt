cmake_minimum_required(VERSION 3.17)
project(parac-base-library C)

set(CMAKE_C_STANDARD 11)

include_directories(./src)

add_executable(
    parac-base-library src/parac.h src/parac.c
)
