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
    - [Generating the Docs](#generating-the-docs)
  - [Disclaimer](#disclaimer)
  - [Copyright and License](#copyright-and-license)


# The Para-C programming language
![Build](https://img.shields.io/github/workflow/status/Para-C/Para-C/CodeQL?logo=github)
[![PyPI version](https://badge.fury.io/py/parac.svg)](https://badge.fury.io/py/parac)
[![Documentation Status](https://readthedocs.org/projects/para-c/badge/?version=latest)](https://para-c.readthedocs.io/en/latest/?badge=latest)
![License](https://img.shields.io/github/license/Para-C/Para-C?color=cyan)
![Lines of Code](https://img.shields.io/tokei/lines/github/Para-C/Para-C)
![Py Versions](https://img.shields.io/pypi/pyversions/parac.svg)

## Key-Features
*Planned/Intended features (Development is still ongoing)*
- Ability to streamline calling processes and handling arguments and return data.
- Multi-Threaded processing with embedded languages in multiple threads.
- Ability to manage exceptions and issues with programs (Including Fallback Options).
- Extended Base-Library (Para-C Base Library) with additional types and functions.
- Decorator and Overload Functions.
- Simplified syntax and handling of C components for easier coding.
- Provide more Security by forbidding variable shadowing and removing undefined behaviour.

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
required compiler/interpreter for the language. 

That means that programming in Para-C will be more similar to higher-level languages 
than to C, due to the new features, keywords and helper functions. Including adding 
the simple option to integrate and manage code or programs that should be directly 
embedded into the management program. 

Using this, you can for example embed async functionality 
from Python directly into the program, which is not natively supported, and 
then pass generated data to a C++ program, which then uses that to run 
something else. 

This can also include proper management based on web events and
data or using the Para-C project configuration to compile code on runtime as 
well with specified compilers so that in the end the project can be compiled in
one go and properly merged with the Para-C program. 

## CLI
The Para-C CLI is the standard CLI for interacting with the standard compiler
implementation. When [installing](#installation) with a generated installer
or `build-exe.py`, this will be the interface used when running the compiler.

### Commands
*Commands displayed are mostly only partly implemented*

| Name                   | Description                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------|
| ``parac compile``      | Compiles a Para-C program to C or an executable.                                                 |
| ``parac run``          | Compiles a Para-C program and runs it.                                                           |
| ``parac c-init``       | Starts the CLI for the configuration of the C-compiler, which is required for running a program. |
| ``parac syntax-check`` | Validates the syntax of a Para-C program and logs errors if needed. (Pre-Processor ignored)      |
| ``parac analyse``      | Analyses a program and validates the syntax (Pre-Processor included - macros required)           |

## Python Module

[![PyPI version](https://badge.fury.io/py/parac.svg)](https://badge.fury.io/py/parac)

The `parac` module serves the purpose of combining the entire compiler with
lib into a simple module, which can be imported and used in ways that are not
implemented in the standard CLI. This means both the `preprocessor` and 
`compiler` are available for customisable usage.

For more info see [Module README](src/PYPI_README.md).

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
will automatically do the installation based on your input and create the
correct entries to the system, so that you can utilise the compiler right after
installation.

#### For unix-based systems (Including MacOS)

On UNIX-based systems the installation is open to the user, including the folder
where the compiler will be placed (It is recommended though to use `/opt`, 
`/usr`, `/usr/local` or similar)

##### Adding the compiler alias on Linux

1. Open your `~/.bash_aliases` file using `nano ~/.bash_aliases`
2. Add `alias parac="<your-dir>/bin/parac"` to the last line of the file, where your-dir is the directory you moved parac into.
3. Save the `.bash_aliases` file.
4. Activate for the terminal session using `source ~/.bash_aliases`
5. Permanently add the alias by adding this line to the end of your `~/.bashrc` file:
   
  ```bash
  if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
  fi
  ```

##### Adding the compiler alias on MacOS

The previous instructions for linux also work on MacOS due to it being unix as well

[Additional Info on MacOS Dock Aliases the official website](
https://support.apple.com/en-al/guide/mac-help/mchlp1046/mac>)

#### Initialising the C Compiler

To start the initialisation setup for the C-Compiler use:

```bash
parac c-init
```

This will add the C-Compiler path to the Para-C compiler and make commands
related to running a Para-C program available. It is not required though and
without it the compiler will simply generate C source files.


## Development

![Test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)
![Coverage](./coverage.svg)
![Lines of Code](https://img.shields.io/tokei/lines/github/Luna-Klatzer/Para-C)
[![codecov](https://codecov.io/gh/Para-C/Para-C/branch/main/graph/badge.svg?token=8I9XL1E7QR)](https://codecov.io/gh/Para-C/Para-C)

### Parsing and Processing Procedure

Due to the two components, which are the Pre-Processor, and the core Compiler
the entire module is split into two modules: `preprocessor` and `paraccompiler`,
which both implement their handling for the source-code. This means that 
when compiling a file, the file will be sent through the Pre-Processor first,
modified and then sent to the Para-C Compiler. 

This also means errors reported will be from the modified file, so that the 
modified code is visible to the user, instead of the file without correct 
Pre-Processor processing.

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
      antlr4 -o ./src/parac/compiler/parser/python -Dlanguage=Python3 ./grammar/ParaC.g4
      ```
  - Java:
      ```bash
      antlr4 -o ./src/parac/compiler/parser/python -Dlanguage=Java ./grammar/ParaC.g4
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
python ./src/build-exe.py
```

The script will create a `./build/` and `./dist/` folder.
The `./build/` folder will contain the raw data and logs, while the `./dist/`
folder will contain the distribution-ready binaries and data.

### Generating the docs

To generate one time use:

```bash
./docs/make.bat html
```

or for active http server, which will reload changes:

```bash
sphinx-autobuild ./docs/source ./docs/build/html
```


## Disclaimer
Para-C is not intended as a language for production code or professional usage
as of now. It is for now solely a free-time/college project.

This also means that issues or bugs while running can likely occur, and it's 
not a stable or production-ready language as of the point of writing.
(*2021-07-23*).

## Copyright and License

![License](https://img.shields.io/github/license/Para-C/Para-C?color=cyan)

Copyright (C) 2021 [Nicolas Klatzer*](#legal-name-which-does-not-match-the-preferred-and-commonly-used-name-luna-klatzer).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

See the [LICENSE](./LICENSE) for information on terms & conditions for usage.

###### *Legal name, which does not match the preferred and commonly used name Luna Klatzer

### FOSSA License Report

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPara-C%2FPara-C.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FPara-C%2FPara-C?ref=badge_large)
