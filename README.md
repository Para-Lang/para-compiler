![](https://raw.githubusercontent.com/Para-Lang/Para/v0.1.dev7/img/para-language.png)

# The Para language and Compiler

![Latest Release](https://img.shields.io/github/v/release/Para-Lang/Para?include_prereleases)
[![PyPI version](https://badge.fury.io/py/paralang-base.svg)](https://badge.fury.io/py/paralang-base)
![Py Versions](https://img.shields.io/pypi/pyversions/paralang-base.svg)
![License](https://img.shields.io/github/license/Para-Lang/Para?color=cyan)
[![Documentation Status](https://readthedocs.org/projects/para/badge/?version=latest)](https://para.readthedocs.io/en/latest/?badge=latest)
![Coverage](./coverage.svg)
[![codecov](https://codecov.io/gh/Para-Lang/Para/branch/main/graph/badge.svg?token=8I9XL1E7QR)](https://codecov.io/gh/Para-Lang/Para)
[![paralang-base](https://snyk.io/advisor/python/paralang-base/badge.svg)](https://snyk.io/advisor/python/paralang-base)

[![Build](https://github.com/Para-Lang/Para/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Para-Lang/Para/actions/workflows/codeql-analysis.yml)
[![Codecov](https://github.com/Para-Lang/Para/actions/workflows/codecov.yml/badge.svg)](https://github.com/Para-Lang/Para/actions/workflows/codecov.yml)
[![PyTest Linux](https://github.com/Para-Lang/Para/actions/workflows/pytest-linux-coverage.yml/badge.svg)](https://github.com/Para-Lang/Para/actions/workflows/pytest-linux-coverage.yml)
[![PyTest MacOs](https://github.com/Para-Lang/Para/actions/workflows/pytest-macos.yml/badge.svg)](https://github.com/Para-Lang/Para/actions/workflows/pytest-macos.yml)
[![PyTest Win](https://github.com/Para-Lang/Para/actions/workflows/pytest-win.yml/badge.svg)](https://github.com/Para-Lang/Para/actions/workflows/pytest-win.yml)
[![Documentation Status](https://readthedocs.org/projects/para/badge/?version=latest)](https://para.readthedocs.io/en/latest/?badge=latest)

## Key-Features

*Planned/Intended features (Development is still ongoing)*

- Ability to streamline calling processes and handling arguments and return
  data.
- Multi-Threaded processing, which allows extensions / other programs to be run
  inside each thread.
- Ability to manage exceptions and also define fallbacks. This is also
  supported for extensions that fail.
- Extended Base-Library (Para Base Library) with additional types and
  functions.
- Decorator and Overload Functions.
- Simplified syntax and handling of C components for easier coding.
- Provide more Security by forbidding variable shadowing and removing undefined
  behaviour.

## Introduction

Para (From Greek "para": Beside/Alongside) is a programming language that
is designed to integrate other languages and allow for advanced management of
embedded programs / code-bases inside a program, where the language will serve
as a base for writing overhead and "connector" programs, which can manage
instances, listen for events, stop and start processes and manage in- and
out-data.

### Commands

*Commands displayed are mostly only partly implemented*

| Name                  | Description                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------|
| ``para compile``      | Compiles a Para program to C or an executable.                                                   |
| ``para run``          | Compiles a Para program and runs it.                                                             |
| ``para syntax-check`` | Validates the syntax of a Para program and logs errors if needed. (Pre-Processor ignored)        |
| ``para analyse``      | Analyses a program and validates the syntax (Pre-Processor included - macros required)           |

## Docs

Our documentation can be found [here](https://para.readthedocs.io/en/latest/).

## Python Module

[![PyPI version](https://badge.fury.io/py/paralang-base.svg)](https://badge.fury.io/py/paralang-base)

Besides, the option to compile the python code into a binary executable using
pyinstaller, you may also directly utilise the `parac` source module, which
provides an API that can be run in your own python scripts.

For reference on the pypi module please go to the documentation page
[here](https://para.readthedocs.io/en/latest/pyapi_ref/index.html)

## Installation

For reference on the installation please go the documentation page 
[here](https://para.readthedocs.io/en/latest/installation.html).

## Copyright and License

![License](https://img.shields.io/github/license/Para-Lang/Para?color=cyan)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPara-Lang%2FPara.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2FPara-Lang%2FPara?ref=badge_shield)

Copyright (C) 2021-2022 Luna Klatzer

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.

See the [LICENSE](https://raw.githubusercontent.com/Para-Lang/Para/main/LICENSE)
for information on terms & conditions for usage.

### FOSSA License Report

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FPara-Lang%2FPara.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FPara-Lang%2FPara?ref=badge_large)
