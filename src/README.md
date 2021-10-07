# `parac` - The Python Module for the Para-C Compiler

![License](https://img.shields.io/github/license/Luna-Klatzer/Para-C?color=cyan)
![Lines of Code](https://img.shields.io/tokei/lines/github/Para-C/Para-C)
![Py Versions](https://img.shields.io/pypi/pyversions/parac.svg)

##  Introduction to `parac` (as Python Module)

The `parac` module serves the purpose of combining the entire compiler with
lib into a simple module, which can be imported and used in ways that are not
implemented in the standard CLI. This means both the `preprocessor` and 
`compiler` are available for customisable usage. 

### Installation

```bash
python3 -m pip install -U parac
```

*With specific version*:
```bash
python3 -m pip install -U parac==version
```

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

Para-C (From Greek "para": Beside/Alongside C) is a programming language that 
is designed to integrate other languages and allow for advanced management of 
programs / code-bases inside a program, where the language will serve as a base
for writing overhead and connector programs, which manage instances, can listen
for events, stop and start processes and generally manage in- and out-data. 
This also includes adding more features for the C11 standard, like new built-in
functions, libraries, struct-like data structures, decorators,
memory-management, console handling with management for stdin, stdout and
stderr, additional function-handling, lightweight OOP structures, and 
additional project-management features.  

To achieve the multiple language “support” / integration-functionality, the 
compiler will take the Para-C code and compile the source code down to simple 
C and generate the code required to integrate the wanted language, using their
required compiler/interpreter for the language. That means that programming in 
Para-C will be more similar to higher-level languages than to C, due to the new
features, keywords and helper functions. Including adding the simple option to
integrate and manage code or programs that should be directly embedded into the
management program. Using this, you can for example embed async functionality 
from Python directly into the program, which is not natively supported, and 
then pass generated data to a C++ program, which then uses that to run 
something else. This can also include proper management based on web events and
data or using the Para-C project configuration to compile code on runtime as 
well with specified compilers so that in the end the project can be compiled in
one go and properly merged with the Para-C program. 

## Documentation
Due to active and early development not available. (Can be expected with later
versions, such as v0.2 or 0.3)

## Contributing and Development
Due to active and early development not available. (Can be expected with later
versions, such as v0.1 or v0.2) - Reason for that is the there is not a lot
that can be contributed to, since changes are made while the theory is made
as well. This means contributions are going to be limited until the basic
structure is finished.

### Running Info
There are two different usage (run) options where the compiler can be used:
- Python module, which is either the source code execution or usage of the
  imported module
- Compiled distribution, which is the compiled version of Para-C, which included the
  CLI. Due to the difference in implementation, only this version can be 
  configured, since the python module is intended for customised behaviour, 
  meaning the pre-configured runtime options are not available. 
  
To differentiate between the two, there are constant variables that are set
during initialisation (Only one can be true, if one is true the other is 
automatically false):
 - `DIST_VERSION: bool` - If `True` it's the distribution version
 - `MODULE_VERSION: bool` - If `True` it's the module version

**Notes:**
1. The most notable difference between the two options is the location of
   the lib folder, containing the C implementation. The folder is in the module
   version in the root folder of the **module**, aka. where setup.py is/was located
   and in the distribution folder in the main **root** folder. The entry point is
   in this case in the ./bin/ folder
2. Currently, both commands `run` and `compile` will raise after 15% completion 
   `TypeError: cannot unpack non-iterable NoneType object`, which is expected,
   since the code-generation is not completed and therefore the compilation
   can not be finished as wanted.


### CLI
...

#### Naming convention
All functions associated with the cli and implement special logging (take input,
or create graphic output) must be prefixed with `cli_` for vars and functions, 
and `CLI` for classes.

### Compiler
...

### Pre-Processor
...
