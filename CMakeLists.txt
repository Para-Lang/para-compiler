cmake_minimum_required(VERSION 3.17)
project(Para_C C)

set(CMAKE_C_STANDARD 99)

file(GLOB Para_C CONFIGURE_DEPENDS "*.h" "*.c")

add_executable(Para_C src/main.c src/compiler/compile.c src/compiler/compile.h src/compiler/basic.c src/compiler/basic.h src/compiler/compile_errors.c src/compiler/compile_errors.h)