![para-c](https://socialify.git.ci/Luna-Klatzer/para-c/image?description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLuna-Klatzer%2FPara-C%2Fmain%2FPara-C.ico&owner=1&pattern=Charlie%20Brown&pulls=1&stargazers=1&theme=Light)

<br>
<br>
<br>

*Para-C is not intended to be a widely „optimised“ or „production-ready“ programming language. It is solely a free-time
project designed for learning and testing purposes, which we do not intend for anything other than that.*

## Abstract

Para-C (From Greek Origin: Beside C  ) is a programming language designed to integrate C, compile to C and serve as a
helper and simplifier to write better code in C, but with additional functionality. Including adding more features, like
new built-in Macros and functions, OOP-structures, more straightforward array and malloc-handling, expanded data types
and simplified functions. The compiler will take the code with C-base syntax and additional Para-C syntax and keywords
and compile it down to simple C. That means that programming in Para-C will be similar but simpler and well looking due
to the simplifications, new structures, keywords and helper functions. The Compiler will additionally provide simple
checking, through the fact of using the classic compiler structure:

1. The lexical analyser (Tokenizer)
2. Syntax analyser
3. The semantic analyser (Logical analyser)
4. Code Generator and optimiser

which means syntax issues, logic errors and general errors will be detected and logged. The C-code compiler will do the
rest of the job, which will be preferably GCC.

Syntax-wise Para-C will still lay onto C to avoid causing issues with more compiler code that would be required for a
new syntax that can’t be easily integrated into the C-syntax. So newer structures won’t look so new, and possibly
similar to C# or C++, like data-types, one-liners and getters etc.

Furthermore, formatting and non-fetal syntax warnings will also be reported, as a help/motivator to avoid causing
inconsistent writing and style. Including possibly harder conventions, that will try to improve on the loose
C-conventions, which are more open to writing code. That means Para-C will introduce more conventions regarding naming,
type declarations, formatting, commenting and will likely also adopt a few Python conventions and integrate the ideas in
the Zen of Python (Since the Compiler is also written in Cython).

## Development

![Deploy and test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)

### Building

The building process is relatively simple since it uses simple PyInstaller and Inno-setup to automate the building
process. The compiler is shipped as a one-file executable file and can be run 

#### Build for specified OS

This specified script will automatically build the project and create a dist and build folder containing all the 
required data as well as the .exe file, which will be the compiler itself. The build folder will contain the raw data
and should not be used. The dist folder will contain the distribution-ready file

```bash
python ./build-exe.py
```

After that, the installer can be created with the passed .exe for the compiler

#### Build inno-setup installer for Windows 

Download inno-setup [here](https://jrsoftware.org/download.php/is.exe)

Build inside this folder and use the inno-setup.iss file. The generated installer will be placed inside /Output

### Installation
 
To install Para-C, you can either use the pre-built installer for the specified version or build the compiler yourself. 
(Only building the compiler will not be enough for Windows systems, since the configuration of the installer needs
to be run so that the path is correctly modified)
