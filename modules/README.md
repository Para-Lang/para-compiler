# Overview - Para-C Modules

This is the folder containing the c-implementation library (Para-C Core Library, and partly Para-C Built-In Library),
which is used for the built-in functions, keywords and items, which are required for the base language.

For the Para-C Extension Library, go [to the lib folder](https://github.com/Para-C/Para-C/tree/dev/lib)

# Testing

For testing purposes, [GTest (Google Test)](https://github.com/google/googletest/releases/tag/release-1.11.0)
is used in an C++ environment, which will simply include the C-files and run them.

In actual code usage, the Para-C Compiler will use the code as regular C, and only for testing C++ will/must be used.

