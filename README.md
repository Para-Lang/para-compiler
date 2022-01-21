![para-c](img/parac-banner.png)

# The Para-C programming language

![Latest Release](https://img.shields.io/github/v/release/Para-C/Para-C?include_prereleases)
[![PyPI version](https://badge.fury.io/py/parac.svg)](https://badge.fury.io/py/parac)
![Py Versions](https://img.shields.io/pypi/pyversions/parac.svg)
![Coverage](./coverage.svg)
[![codecov](https://codecov.io/gh/Para-C/Para-C/branch/main/graph/badge.svg?token=8I9XL1E7QR)](https://codecov.io/gh/Para-C/Para-C)
![License](https://img.shields.io/github/license/Para-C/Para-C?color=cyan)
[![Required GCC version](https://img.shields.io/badge/GCC-%3E%3D8.0-blue)](https://github.com/Para-C/Para-C/discussions/76)
![Required CMake version](https://img.shields.io/badge/CMake-%3E%3D3.17-blue)

[![Build](https://github.com/Luna-Klatzer/Para-C/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/codeql-analysis.yml)
[![Codecov](https://github.com/Luna-Klatzer/Para-C/actions/workflows/codecov.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/codecov.yml)
[![PyTest Linux](https://github.com/Para-C/Para-C/actions/workflows/pytest-linux-coverage.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/pytest-linux-coverage.yml)
[![PyTest MacOs](https://github.com/Para-C/Para-C/actions/workflows/pytest-macos.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/pytest-macos.yml)
[![PyTest Win](https://github.com/Para-C/Para-C/actions/workflows/pytest-win.yml/badge.svg)](https://github.com/Para-C/Para-C/actions/workflows/pytest-win.yml)
[![Documentation Status](https://readthedocs.org/projects/para-c/badge/?version=latest)](https://para-c.readthedocs.io/en/latest/?badge=latest)

## Key-Features

*Planned/Intended features (Development is still ongoing)*

- Ability to streamline calling processes and handling arguments and return
  data.
- Multi-Threaded processing, which allows extensions / other programs to be run
  inside each thread.
- Ability to manage exceptions and also define fallbacks. This is also
  supported for extensions that fail.
- Extended Base-Library (Para-C Base Library) with additional types and
  functions.
- Decorator and Overload Functions.
- Simplified syntax and handling of C components for easier coding.
- Provide more Security by forbidding variable shadowing and removing undefined
  behaviour.

## Introduction

Para-C (From Greek "para": Beside/Alongside C) is a programming language that
is designed to integrate other languages and allow for advanced management of
embedded programs / code-bases inside a program, where the language will serve
as a base for writing overhead and "connector" programs, which can manage
instances, listen for events, stop and start processes and manage in- and
out-data.

### Commands

*Commands displayed are mostly only partly implemented*

| Name                   | Description                                                                                      |
|------------------------|--------------------------------------------------------------------------------------------------|
| ``parac compile``      | Compiles a Para-C program to C or an executable.                                                 |
| ``parac run``          | Compiles a Para-C program and runs it.                                                           |
| ``parac c-init``       | Starts the CLI for the configuration of the C-compiler, which is required for running a program. |
| ``parac syntax-check`` | Validates the syntax of a Para-C program and logs errors if needed. (Pre-Processor ignored)      |
| ``parac analyse``      | Analyses a program and validates the syntax (Pre-Processor included - macros required)           |

## Docs

Our documentation can be found [here](https://para-c.readthedocs.io/en/latest/).

## Python Module

[![PyPI version](https://badge.fury.io/py/parac.svg)](https://badge.fury.io/py/parac)

Besides, the option to compile the python code into a binary executable using
pyinstaller, you may also directly utilise the `parac` source module, which
provides an API that can be run in your own python scripts.

For reference on the pypi module please go to the documentation page
[here](https://para-c.readthedocs.io/en/latest/pyapi_ref/index.html)

## Installation

For reference on the installation please go the documentation page 
[here](https://para-c.readthedocs.io/en/latest/installation.html).

## Development

To develop on the Para-C Project, you may contribute to this repo or one of the
following side-repos of Para-C Language:

- [Para-C Base Library](https://github.com/Para-C/Para-C-Base-Library) - C
  Static Library for providing the types, functions and macros used to actually
  run the compiled C-code.
- [Para-C Extension Library](https://github.com/Para-C/Para-C-Extension-Library) - 
  Library for utilising other languages/extensions in a Para-C program. This
  repository is at the moment inactive

For more info on development for the core Python API and compiler, you may go
[here](https://github.com/Para-C/Para-C/blob/main/DEVELOPMENT.md).

## Disclaimer

Para-C is not intended as a language for production code or professional usage
as of now. It is for now solely a free-time/college project.

This also means that issues or bugs while running can likely occur, and it's
not a stable or production-ready language as of the point of writing.
(*2021-12-19*).

## Copyright and License

![License](https://img.shields.io/github/license/Para-C/Para-C?color=cyan)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPara-C%2FPara-C.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FPara-C%2FPara-C?ref=badge_shield)

Copyright (C) 2021 Luna Klatzer

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.

See the [LICENSE](./LICENSE) for information on terms & conditions for usage.

### FOSSA License Report

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPara-C%2FPara-C.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FPara-C%2FPara-C?ref=badge_large)
