![para-c](img/parac-banner.png)

# [Content](#content)

- [The Para-C programming language](#the-para-c-programming-language)
  - [Key-Features](#key-features)
  - [Introduction](#introduction)
  - [CLI](#cli)
    - [Commands](#commands)
  - [Python Module](#python-module)
  - [Installation](#installation)
    - [Install the Python module](#install-the-python-module)
    - [Build the Compiler](#build-the-compiler)
    - [Setting up the Compiler](#setting-up-the-compiler)
      - [For Windows](#for-windows)
      - [For unix-based systems (Including MacOS)](#for-unix-based-systems-including-macos)
         - [Adding the compiler alias on Linux](#adding-the-compiler-alias-on-linux)
      - [Initialising the C Compiler](#initialising-the-c-compiler)
  - [Development](#development)
    - [Parsing and Processing Procedure](#parsing-and-processing-procedure)
    - [Build inno-setup installer for Windows](#build-inno-setup-installer-for-windows)
    - [Building](#building)
      - [Generating the Parser and Lexer](#generating-the-parser-and-lexer)
        - [Downloading Antlr4](#downloading-antlr4)
        - [Generating the Python files](#generating-the-python-files)
        - [Build the executable and binaries](#build-the-executable-and-binaries)
  - [Disclaimer](#disclaimer)
  - [Copyright and License](#copyright-and-license)


[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPara-C%2FPara-C.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FPara-C%2FPara-C?ref=badge_large)

# The Para-C programming language
*This is version 0.1.dev4*

## Key-Features
*Planned/Intended features (Development is still ongoing)*
- Ability to streamline calling processes and handling return
- More advanced and specialised functionality for managing embedded code
- Program-State Saving for continuing execution at a later point
- Multi-Threaded processing with embedded languages in multiple threads
- Ability to integrate processes quickly
- Simplification of the base C language with simplified syntax and additional helper functions
- Ability to manage exceptions and issues with programs (Including Fallback Options)
- Any-Type and integrated conversion functions for type
- Decorator and Overload Functions
- Language Library with additional helper functions
- Simplified syntax and handling of C components for easier coding

## Introduction

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
 
## CLI
The Para-C CLI is the standard CLI for interacting with the standard compiler
implementation. When [installing](#installation) with a generated installer
or `build-exe.py`, this will be the interface used when running the compiler.

### Commands
*Commands displayed are mostly only partly implemented*
- `parac compile` - Compile a Para-C program to C or executable
- `parac run` - Compiles a Para-C program and runs it (Creates build and dist as well)
- `parac c-init` - Console Line Interface for the configuration of the C-compiler
- `parac syntax-check` - Validates the syntax of a Para-C program and logs errors if needed
- `parac analyse` - Analyses a program by running the Pre-Processor and validating the syntax 
  (Not added yet. See [#16](/../../issues/16))

## Python Module

[![PyPI version](https://badge.fury.io/py/parac.svg)](https://badge.fury.io/py/parac)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPara-C%2FPara-C.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FPara-C%2FPara-C?ref=badge_shield)

The `parac` module serves the purpose of combining the entire compiler with
lib into a simple module, which can be imported and used in ways that are not
implemented in the standard CLI. This means both the `preprocessor` and 
`compiler` are available for customisable usage.

For more info see [Module README](./src/README.md).

## Installation
 
To install Para-C, you can either use the pre-built installer for the windows,
by going through the [releases](https://github.com/Para-C/Para-C/releases)
or [build](#build-the-executable-and-binaries) and install the compiler yourself. 
(The last is simpler than it might seem)

### Install the Python module

When wanting to use the compiler as a python module it is recommended to 
install the distributed version on [pypi.org](https://pypi.org/project/parac/),
which will always have the latest releases uploaded. 

To install simply use:
```bash
python3 -m pip install -U parac
```

Or for a specific version:
```bash
python3 -m pip install -U parac==version
```


### Build the Compiler

Building the compiler will generate a `build` and `dist` folder, where the
`dist` folder will contain the actual compiler directory. In this case, the 
`build` folder can be ignored and deleted after building.

For the info about building the compiler see 
[Build the executable and binaries](#build-the-executable-and-binaries)

### Setting up the Compiler

#### For Windows

For Windows, the configured inno-setup installer should be used. The installer
will automatically do the installation based on your input.

#### For unix-based systems (Including MacOS)

On UNIX-based systems the installation is open to the user, including the folder
where the compiler will be placed (It is recommended though to use `/opt`, 
`/usr`, `/usr/local` or similar)

##### Adding the compiler alias on Linux

Steps to add the alias `parac` to your terminal:
1. Open the .bashrc file in your home directory (for example, /home/your-user-name/.bashrc) in a text editor.
2. Add export `PATH="<your-dir>/bin:$PATH"` to the last line of the file, where your-dir is the directory you want to add.
3. Save the .bashrc file.
4. Restart your terminal.

#### Initialising the C Compiler

To start the initialisation setup for the C-Compiler use:

```bash
parac c-init
```

This will add the C-Compiler path to the Para-C compiler and make commands
related to running a Para-C program available. It is not required though and
without it the compiler will simply generate C source files.


## Development

![Deploy and test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)
![Coverage](./coverage.svg)
![License](https://img.shields.io/github/license/Luna-Klatzer/Para-C?color=cyan)
![Lines of Code](https://img.shields.io/tokei/lines/github/Luna-Klatzer/Para-C)

### Parsing and Processing Procedure

Due to the two components, which are the Pre-Processor, and the core Compiler
the entire module is split into two modules: `preprocessor` and `paraccompiler`,
which both implement their handling for the source-code. This means that 
when compiling a file, the file will be sent through the Pre-Processor first,
modified and then sent to the Para-C Compiler. This also means errors reported
will be from the modified file, so that the modified code is visible to the 
user, instead of the file without correct Pre-Processor processing.

### Build inno-setup installer for Windows

Download inno-setup [here](https://jrsoftware.org/download.php/is.exe)

Build inside this folder and use the inno-setup.iss file. The generated installer will be placed inside `./Output`

### Building

#### Generating the Parser and Lexer

*Required for Lexer and Parser Development which include changes on the .g4 grammar files*

##### Downloading Antlr4

To download Antlr4 go [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar)

Quickstart Installation Guide on the Main Website: [here](https://www.antlr.org/)

##### Generating the Python files

Generating the Parser and Lexer is made up of two parts:

- Using Antlr4 to compile the .g4 file to actual source code
- Implementing the Runtime (The user code that is shipped with the binaries)

*Note: Generating the Parser and Lexer means that depending on the changes
the implementation code needs to be changed.*

To generate in the command-line use:
- For the Pre-Processor:
  - Python (Required for the Compiler):
      ```bash
      antlr4 -o ./src/parac/preprocessor/python -Dlanguage=Python3 ./grammar/ParaCPreProcessor.g4
      ```
  - Java:
      ```bash
      antlr4 -o ./src/parac/preprocessor/python -Dlanguage=Java ./grammar/ParaCPreProcessor.g4
      ```

- For the Core Language:
  - Python (Required for the Compiler):
      ```bash
      antlr4 -o ./src/parac/compiler/core/parser/python -Dlanguage=Python3 ./grammar/ParaC.g4
      ```
  - Java:
      ```bash
      antlr4 -o ./src/parac/compiler/core/parser/python -Dlanguage=Java ./grammar/ParaC.g4
      ```
  
Afterwards *if needed* correctly move the folder using:
```bash
mv ./path/to/generated/output/* ./src/compiler/core/<insert-destination>/
```

and delete the remaining folder:
```bash
rm -rf ./path/to/generated/output
```

**Notes:**
- *Make sure the alias for `antlr4` / `antlr` exists! Else the command will not work*
- *Comments are only partly ignored in ParaC.g4, due the intended removal in the Pre-Processor. Errors can occur!*

#### Build the executable and binaries

For generating the binaries, PyInstaller with a wrapper script will be used.
This script will automatically run the generation of source files and copying of data.

To run the script simply use (Python3):
```bash
python ./build-exe.py
```

The script will create a `./build/` and `./dist/` folder.
The `./build/` folder will contain the raw data and logs, while the `./dist/`
folder will contain the distribution-ready binaries and data.

## Disclaimer
Para-C is not intended as a language for production code or professional usage
as of now. It is for now solely a free-time/college project.

This also means that issues or bugs while running can likely occur, and it's 
not a stable or production-ready language as of the point of writing.
(*2021-07-23*).

## Copyright and License

Copyright (c) 2001-2021 Nicolas Klatzer[*](#legal-name-which-does-not-match-the-preferred-and-commonly-used-name-luna-klatzer). All rights reserved.

See the [LICENSE](./LICENSE) for information on terms & conditions for usage

###### *Legal name, which does not match the preferred and commonly used name Luna Klatzer