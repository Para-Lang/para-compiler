# Overview - Para-C Modules

This is the folder containing the c-implementation library (Para-C Core Library, and partly Para-C Built-In Library),
which is used for the built-in functions, keywords and items, which are required for the base language.

For the Para-C Extension Library, go [to the lib folder](https://github.com/Para-C/Para-C/tree/dev/lib)

# Testing

For testing purposes, [GTest (Google Test)](https://github.com/google/googletest/releases/tag/release-1.11.0)
is used in an C++ environment, which will simply include the C-files and run them.

In actual code usage, the Para-C Compiler will use the code as regular C, and only for testing C++ will/must be used.

# Basic Concepts

## Meta-Data Tracking - `pbl-types.h`

Para-C implements meta-data tracking using `PblMetaVarCtx_T` and pre-defined macros, tracking things like:
- If the variable has been defined yet
- Effective space the user has to utilise. Note that effective space does not include actual space that is allocated! 
This is due to meta-data also taking up a bit of memory space.

## Memory accessing - `pbl-mem.h`

(Currently in work - to be decided)

## Function Meta-Data Tracking - `pbl-function.h`

Inside Para-C, when calling a Para-C function, so-called `PblMetaFunctionCallCtx_T` types are passed
as the first argument to every function, which contain:

- The meta-data of the invocation aka. call context, 
- The data necessary to track [exception meta-data](#exceptions---pbl-functionh)

These meta-data variables will be dynamically created for every invocation and will be allocated in the heap.
Meaning they can be accessed outside of the context, and used to create crash-tracebacks to 
get extensive execution info on the failure of the program.

## Exceptions - `pbl-function.h`

Exceptions in Para-C are very similarly implemented to the exceptions in C#. 

Exceptions can be raised, re-raised with a parent-exception and child-exception, caught using an `except` block
and also used to pre-maturely abort the program. 

Inside Para-C these are though implemented using the `PblMetaFunctionCallCtx_T` types, which will
store the traceback and exception information. All macros for exceptions have been implemented in this header
and should be always used when implementing higher level functions.
