cmake_minimum_required(VERSION 3.17)
project(ParaC C)

set(CMAKE_C_STANDARD 11)

file(GLOB ParaC CONFIGURE_DEPENDS "*.h" "*.c")

set (CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -static-libstdc++ -static-libgcc")
add_executable(ParaC src/main.c src/compiler/compile.c src/compiler/compile.h src/compiler/basic.c src/compiler/basic.h src/compiler/compile_errors.c src/compiler/compile_errors.h src/main.h)