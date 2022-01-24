# `para` - The Python Module for the Para Compiler

![License](https://img.shields.io/github/license/Para-Lang/Para?color=cyan)
![Lines of Code](https://img.shields.io/tokei/lines/github/Para-Lang/Para)
![Py Versions](https://img.shields.io/pypi/pyversions/para.svg)
[![Documentation Status](https://readthedocs.org/projects/para-c/badge/?version=latest)](https://para-c.readthedocs.io/en/latest/?badge=latest)

## Introduction to `para` (as Python Module)

The `para` module serves the purpose of combining the entire compiler with lib
into a simple module, which can be imported and used in ways that are not
implemented in the standard CLI. This means both the `preprocessor` and
`compiler` are available for customisable usage.

### Installation

```bash
python3 -m pip install -U para
```

*With specific version*:

```bash
python3 -m pip install -U para==version
```

### Structure

#### Tree

```
para - Main module that can be imported
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

- `abc`: ABC classes that are the base for many classes in `preprocessor`
  and `compiler`
- `compiler`: Main Compiler module, which includes lexer, parser, semantic
  analyser, optimiser and code-generation (not completely implemented yet, due
  to active development still ongoing)
- `preprocessor`: Pre-Processor module, which implements its own lexer and
  parser for processing files.
- `util`: Module Utility functions, decorators and classes
- `const.py`: Constant values, which are evaluated on `__init__`
- `exceptions.py`: Module exceptions with error-codes ErrorCodes(IntEnum)
- `logging.py`: Logging Implementation for the Module and CLI

## Introduction to Para (as Language)

Para (From Greek "para": Beside/Alongside) is a programming language that
is designed to integrate other languages and allow for advanced management of
embedded programs / code-bases inside a program, where the language will serve
as a base for writing overhead and "connector" programs, which can manage
instances, listen for events, stop and start processes and manage in- and
out-data.

## Documentation

[![Documentation Status](https://readthedocs.org/projects/para-c/badge/?version=latest)](https://para-c.readthedocs.io/en/latest/?badge=latest)

Documentations are available on the official readthedocs.org site, though 
*note that the docs are still unfinished and things will be likely changing the
more development progresses. For finalisation, it might take until v0.2 or 
v0.3, so please be patient*

## Contributing and Development

Due to active and early development not available. (Can be expected with later
versions, such as v0.1 or v0.2) - Reason for that is the there is not a lot
that can be contributed to, since changes are made while the theory is made as
well. This means contributions are going to be limited until the basic
structure is finished.

### Running Info

There are two different usage (run) options where the compiler can be used:

- Python module, which is either the source code execution or usage of the
  imported module
- Compiled distribution, which is the compiled version of Para, which
  included the CLI. Due to the difference in implementation, only this version
  can be configured, since the python module is intended for customised
  behaviour, meaning the pre-configured runtime options are not available.

To differentiate between the two, there are constant variables that are set
during initialisation (Only one can be true, if one is true the other is
automatically false):

- `DIST_COMPILED_VERSION: bool` - If `True` it's the distribution version, aka.
  called using the compiled binaries
- `MODULE_VERSION: bool` - If `True` it's the module version

## Extensions

### `para-ext-cli` - CLI

The CLI is its own unique project, as the main compiler is a native python
project, which is used using the normal Python interpreter. Therefore, it also
has its own pypi release site, which can be
found [here](https://pypi.org/project/para-ext-cli/).