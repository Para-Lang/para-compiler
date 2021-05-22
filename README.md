![para-c](https://socialify.git.ci/Luna-Klatzer/para-c/image?description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLuna-Klatzer%2FPara-C%2Fmain%2FPara-C.ico&owner=1&pattern=Charlie%20Brown&pulls=1&stargazers=1&theme=Light)

<br>
<br>
<br>

*Para-C is not intended to be a widely „optimised“ or „production-ready“ programming language. It is solely a free-time
project designed for learning and testing purposes, which we do not intend for anything other than that.*

## Introduction

Para-C (From Greek Origin: Beside C) is a programming language designed to integrate C, compile to C and serve as an
extension to C with additional functionality, simplification and helper tools. Including adding more features, like new
built-in Macros, simplified or new functions, OOP-structures (Under consideration), more straightforward array, list and
malloc-handling, expanded data types and additional project-management features.

The compiler will take the Para-C code to compile it down to simple C with the integrated functionality. That means that
programming in Para-C will be similar but simpler and well looking due to the simplifications, new structures, keywords
and helper functions. Syntax-wise Para-C will still lay onto C to avoid causing issues with more compiler code that
would be required for a new syntax that can’t be easily integrated into the C-syntax. So newer structures won’t look so
new, and possibly similar to C# or C++, like data-types, one-liners, overloads and getters etc.

Furthermore, formatting and non-fetal syntax warnings will also be reported, as a help/motivator to avoid causing
inconsistent writing and style. Including possibly harder conventions, that will try to improve on the loose
C-conventions, which are more open to writing code. That means Para-C will introduce more conventions regarding naming,
type declarations, formatting, commenting and will likely also adopt a few Python conventions and integrate some ideas
of the of Python (Since the Compiler is also written in Cython).

## Development

![Deploy and test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)
![Coverage](./coverage.svg)

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
