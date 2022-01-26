![](https://raw.githubusercontent.com/Para-Lang/Para/v0.1.dev7/img/para-banner.png)

# `paralang_base` - The Python Module for the Para Compiler

![License](https://img.shields.io/github/license/Para-Lang/Para?color=cyan)
![Lines of Code](https://img.shields.io/tokei/lines/github/Para-Lang/Para)
![Py Versions](https://img.shields.io/pypi/pyversions/para.svg)
[![Documentation Status](https://readthedocs.org/projects/para/badge/?version=latest)](https://para.readthedocs.io/en/latest/?badge=latest)

## Introduction to `paralang_base` (as Python Module)

The `para` module serves the purpose of combining the entire compiler with lib
into a simple module, which can be imported and used in ways that are not
implemented in the standard CLI. This means both the `preprocessor` and
`compiler` are available for customisable usage.

### Installation

```bash
python3 -m pip install -U paralang_base
```

*With specific version*:

```bash
python3 -m pip install -U paralang_base==version
```

## Para Language

Para (From Greek "para": Beside/Alongside) is a programming language that
is designed to integrate other languages and allow for advanced management of
embedded programs / code-bases inside a program, where the language will serve
as a base for writing overhead and "connector" programs, which can manage
instances, listen for events, stop and start processes and manage in- and
out-data.

### Runtime Info

There are two different usage (run) options where the compiler can be used:

- Python module, which is either the source code execution or usage of the
  imported module
- Compiled distribution, which is the compiled version of Para, which
  included the CLI. Due to the difference in implementation, only this version
  can be configured, since the python module is intended for customised
  behaviour, meaning the pre-configured runtime options are not available.

To differentiate between the two runtime modes, there are constant variables
that are set during initialisation:

- `DIST_COMPILED_VERSION: bool` - If `True` it's the distribution version, aka.
  called using the compiled binaries
- `MODULE_VERSION: bool` - If `True` it's the module version

### Para CLI - `paralang_cli`

The CLI itself is an extension to the base module, as it provides extended
graphical logging and configuration options from the console. It includes the
base Para compiler module, and extends its functionality and provides
scripts that are added automatically to the path on installation.

This means after installation of `paralang_cli`, you can use the Para compiler
directly with a CLI (command line interface). 

To show the current Para installation version, you can use the following:
```bash
para --version
```

The PyPi release of the CLI can be found
[here](https://pypi.org/project/paralang_cli/).

## Contributing and Development

Due to active and early development not available. (Can be expected with later
versions, such as v0.1 or v0.2)

Reason for that is the there is not yet a lot that can be contributed to, since
the project is in early build up. This means contributions are going to be 
limited until the basic structure is finished.

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
