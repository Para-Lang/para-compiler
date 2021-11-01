![para-c](img/parac-banner.png)

# The Para-C programming language

![Py Versions](https://img.shields.io/pypi/pyversions/parac.svg)
[![PyPI version](https://badge.fury.io/py/parac.svg)](https://badge.fury.io/py/parac)
![Coverage](./coverage.svg)
[![codecov](https://codecov.io/gh/Para-C/Para-C/branch/main/graph/badge.svg?token=8I9XL1E7QR)](https://codecov.io/gh/Para-C/Para-C)
![License](https://img.shields.io/github/license/Para-C/Para-C?color=cyan)
[![Documentation Status](https://readthedocs.org/projects/para-c/badge/?version=latest)](https://para-c.readthedocs.io/en/latest/?badge=latest)

[![Build](https://github.com/Luna-Klatzer/Para-C/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/codeql-analysis.yml)
[![Codecov](https://github.com/Luna-Klatzer/Para-C/actions/workflows/codecov.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/codecov.yml)
[![PyTest Linux](https://github.com/Para-C/Para-C/actions/workflows/pytest-linux-coverage.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/pytest-linux-coverage.yml)
[![PyTest MacOs](https://github.com/Para-C/Para-C/actions/workflows/pytest-macos.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/pytest-macos.yml)
[![PyTest Win](https://github.com/Para-C/Para-C/actions/workflows/pytest-win.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/pytest-win.yml)

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
embedded programs / code-bases inside a program, where the language will serve 
as a base for writing overhead and "connector" programs, which can manage 
instances, listen for events, stop and start processes and manage in- and out-data. 

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

## Disclaimer
Para-C is not intended as a language for production code or professional usage
as of now. It is for now solely a free-time/college project.

This also means that issues or bugs while running can likely occur, and it's 
not a stable or production-ready language as of the point of writing.
(*2021-07-23*).

## Copyright and License

![License](https://img.shields.io/github/license/Para-C/Para-C?color=cyan)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPara-C%2FPara-C.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FPara-C%2FPara-C?ref=badge_shield)

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
