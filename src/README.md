![para-c](../img/parac-banner.png)

# `parac` - The Python Module for the Para-C Compiler

[![Python Version](https://img.shields.io/badge/python->=3.8-blue?logo=python)](https://python.org)
![Deploy and test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)
![Coverage](../coverage.svg)
![License](https://img.shields.io/github/license/Luna-Klatzer/Para-C?color=cyan)
![Lines of Code](https://img.shields.io/tokei/lines/github/Para-C/Para-C)


##  Introduction to `parac` (as Python Module)

The `parac` module serves the purpose of combining the entire compiler with
lib into a simple module, which can be imported and used in ways that are not
implemented in the standard CLI. This means both the `preprocessor` and 
`compiler` are available for customisable usage. 

### Structure

#### Tree

```
parac - Main module that can be imported
|-- abc/
|  `-- *
|-- compiler/
|  `-- *
|-- preprocessor/
|  `-- *
|-- util/
|  `-- *
|-- const.py
|-- exceptions.py
`-- logging.py
```

#### Info
- `abc`: ABC classes that are the base for many classes in `preprocessor` and `compiler`
- `compiler`: Main Compiler module, which includes lexer, parser, semantic
   analyser, optimiser and code-generation (not completely implemented yet, 
   due to active development still ongoing)
- `preprocessor`: Pre-Processor module, which implements its own lexer and parser
   for processing files.
- `util`: Module Utility functions, decorators and classes
- `const.py`: Constant values, which are evaluated on `__init__`
- `exceptions.py`: Module exceptions with error-codes ErrorCodes(IntEnum)
- `logging.py`: Logging Implementation for the Module and CLI


## Introduction to Para-C (as Language)

Para-C (From Greek Origin: Beside C ) is a programming language that is 
designed to integrate other languages and allow for advanced management 
of programs / code-bases inside a program, where the language will serve
as a base overhead language with extended C-functionality and simplifications 
to write simpler code. Including adding more features, like new built-in 
functions, libraries, data structures, decorators, function-handling, OOP 
structures (Under consideration), and additional project-management features.

To achieve the multiple language “support” / integration-functionality, the 
compiler will take the Para-C code and compile the source code down to simple 
C and generate the code required to integrate the wanted language, using their
required compiler/interpreter for the language. That means that programming in 
Para-C will be similar to C and partly C#, due to the new features, keywords
and helper functions, but add the simple option to integrate and manage simple
code or even programs that should be directly embedded into the program. Using
this, you can for example embed async functionality from Python directly into
the program, which is not natively supported, and then pass generated data to 
a C++ program, which then uses that to run something else.

## Documentation
Due to active and early development not available. (Can be expected with later
versions, such as v0.2 or 0.3)

## Contributing and Development
Due to active and early development not available. (Can be expected with later
versions, such as v0.1 or v0.2) - Reason for that is the there is not a lot
that can be contributed to, since changes are made while the theory is made
as well. This means contributions are going to be limited until the basic
structure is finished.

### CLI
...

#### Naming convention
All functions associated with the cli and implement special logging (take input,
or create graphic output) must be prefixed with `cli_` for vars and functions, 
and `CLI` for classes. 

This does not apply to items in the `cli.py` file

### Compiler
...

### Pre-Processor
...
