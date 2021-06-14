![para-c](https://socialify.git.ci/Luna-Klatzer/Para-C/image?description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLuna-Klatzer%2FPara-C%2Fmain%2Fparac.ico&owner=1&pulls=1&stargazers=1&theme=Light)

<br>
<br>
<br>

*Para-C is not intended to be a widely „optimised“ or „production-ready“ programming language. It is solely a free-time
project designed for learning and testing purposes, which we do not intend for anything other than that.*

## Introduction

Para-C (From Greek Origin: Beside C  ) is a programming language designed to integrate C, 
compile to C and serve as an extension to C with additional functionality, 
simplification and helper tools. Including adding more features, like new 
built-in Macros, simplified or new functions, OOP-structures (Under consideration),
list and malloc-handling, expanded data types and additional project-management features.

The compiler will take the Para-C code to compile it down to simple C with the integrated functionality. 
That means that programming in Para-C will be similar but simpler and well looking due to the 
simplifications, new structures, keywords and helper functions. Syntax-wise Para-C will still 
lay onto C to avoid causing issues with more compiler code that would be required for a new 
syntax that can’t be easily integrated into the C-syntax. So newer structures won’t look so new,
and possibly similar to C# or C++, like data-types, one-liners, overloads and getters etc. 

Furthermore, formatting and non-fetal syntax warnings will also be reported, as a help/motivator
to avoid causing inconsistent writing and style. Including possibly harder conventions, that will
try to improve on the loose C-conventions, which are more open to writing code. That means Para-C 
will introduce more conventions regarding naming, type declarations, formatting, commenting and 
will likely also adopt a few Python conventions  and integrate some ideas of the Zen of Python
(Since the Compiler is also written in Cython).  

## Development

![Deploy and test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)
![Coverage](https://raw.githubusercontent.com/Luna-Klatzer/Para-C/main/coverage.svg)

### Building

The building process is relatively simple since it uses simple PyInstaller and Inno-setup to automate the building
process. The compiler is shipped as a one-file executable file and can be run 

#### Build the Parser and Lexer with Antlr4

##### Downloading

To download Antlr4 go to [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar)

Quickstart Installation Guide: [here](https://www.antlr.org/)

##### Using Antlr4

Generating the Parser and Lexer is made up of two parts:

- Using Antlr4 to compile the .g4 file to actual source code
- Implementing the Runtime (The user code that is shipped with the binaries)

*Note: Generating the Parser and Lexer means that the implementation
will be gone. There will be a code base, but regenerating the lexer will
require new a new implementation into the compiler. How long this
will take is uncertain, since the amount of work depend on what changes 
are made in the grammar (.g4 file)*

To generate use:

- Python:
    ```bash
    core -o ./paraccompiler/core/antlr4/python/ -Dlanguage=Python3 ./paraccompiler/core/g4/ParaC.g4
    ```
- Java:
    ```bash
    core -o ./paraccompiler/core/antlr4/java/ -Dlanguage=Java ./paraccompiler/core/g4/ParaC.g4
    ```

Afterwards correctly move the folder using:
```bash
mv ./paraccompiler/core/antlr4/python/paraccompiler/core/g4/* ./paraccompiler/core/antlr4/python/
```

and delete the remaining folder:
```bash
rm -rf ./paraccompiler/core/antlr4/python/paraccompiler/
```

Everything together:
```bash
core -o ./paraccompiler/core/antlr4/python/ -Dlanguage=Python3 ./paraccompiler/core/g4/ParaC.g4 && core -o ./paraccompiler/core/antlr4/java/ -Dlanguage=Java ./paraccompiler/core/g4/ParaC.g4 && mv ./paraccompiler/core/antlr4/python/paraccompiler/core/g4/* ./paraccompiler/core/antlr4/python/ && rm -rf ./paraccompiler/core/antlr4/python/paraccompiler/
```

*Make sure the alias for `antlr4` / `antlr` exists! Else the command will not work*

#### Build the Executable and binaries

This specified script will automatically build the project and create a dist and build folder containing all the binaries 
as well as the executable file. The build folder will contain the raw data and logs, meaning it
is not intended for distribution. The dist folder will contain the distribution-ready data

```bash
python ./build-exe.py
```

##### Installing Antlr

#### Build inno-setup installer for Windows 

Download inno-setup [here](https://jrsoftware.org/download.php/is.exe)

Build inside this folder and use the inno-setup.iss file. The generated installer will be placed inside `./Output`

### Installation
 
To install Para-C, you can either use the pre-built installer for the specified version or build the compiler yourself. 

### Setup

#### For Windows

For Windows the configured inno-setup installer should be used. The installer
will automatically do the installation based on your input.

#### For unix-based systems

Initialise the compiler using:
```bash
parac init
```

Add the compiler to the PATH:

1. Open the .bashrc file in your home directory (for example, /home/your-user-name/.bashrc) in a text editor.
2. Add export `PATH="<your-dir>/bin:$PATH"` to the last line of the file, where your-dir is the directory you want to add.
3. Save the .bashrc file.
4. Restart your terminal.
