![para-c](https://socialify.git.ci/Luna-Klatzer/Para-C/image?description=1&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FLuna-Klatzer%2FPara-C%2Fmain%2Fparac.ico&owner=1&pulls=1&stargazers=1&theme=Light)

<br>
<br>
<br>

*Para-C is not intended to be a widely „optimised“ or „production-ready“ programming language. It is solely a free-time
project designed for learning and testing purposes, which we do not intend for anything other than that.*

## Introduction

Para-C (From Greek Origin: Beside C ) is a programming language that is 
designed to integrate other languages and allow for advanced management of
programs / code-bases inside a program, where the language will serve as a 
base overhead language with extended C-functionality and simplifications to
write simpler code. Including adding more features, like new built-in 
functions, libraries, data structures, decorators, function-handling, OOP
structures (Under consideration), and additional project-management features.  

To achieve the multiple language “support” / integration-functionality, the 
compiler will take the Para-C code and compile the source code down to simple
C and generate the code required to integrate the wanted language, using their 
required compiler/interpreter for the language. That means that programming in
Para-C will be similar to C and partly C#, due to the new features, keywords 
and helper functions, but add the simple option to integrate and manage simple 
code or even programs that should be directly embedded into the program. Using
this, you can for example embed async functionality from Python directly into
the program, which is not natively supported, and then pass generated data to
a C++ program, which then uses that to run something else. 
 

## Development

![Deploy and test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)
![Coverage](https://raw.githubusercontent.com/Luna-Klatzer/Para-C/main/coverage.svg)
![License](https://img.shields.io/github/license/Luna-Klatzer/Para-C?color=cyan)
![Lines of Code](https://img.shields.io/tokei/lines/github/Luna-Klatzer/Para-C)

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
    antlr4 -o ./paraccompiler/core/antlr4/python/ -Dlanguage=Python3 ./paraccompiler/core/antlr4/ParaC.g4
    ```
- Java:
    ```bash
    antlr4 -o ./paraccompiler/core/antlr4/java/ -Dlanguage=Java ./paraccompiler/core/antlr4/ParaC.g4
    ```

Afterwards correctly move the folder using:
```bash
mv ./paraccompiler/core/antlr4/python/paraccompiler/core/antlr4/* ./paraccompiler/core/antlr4/python/
```

and delete the remaining folder:
```bash
rm -rf ./paraccompiler/core/antlr4/python/paraccompiler/
```

Everything together:
```bash
antlr4 -o ./paraccompiler/core/antlr4/python/ -Dlanguage=Python3 ./paraccompiler/core/antlr4/ParaC.g4 && antlr4 -o ./paraccompiler/core/antlr4/java/ -Dlanguage=Java ./paraccompiler/core/antlr4/ParaC.g4 && mv ./paraccompiler/core/antlr4/python/paraccompiler/core/antlr4/* ./paraccompiler/core/antlr4/python/ && rm -rf ./paraccompiler/core/antlr4/python/paraccompiler/
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
