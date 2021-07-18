![para-c](./Para-C-Redesign-Banner.png)

*Note: Para-C is not intended to be a widely „optimised“ or „production-ready“
programming language. It is for now solely a free-time/college project*

## Key-Features
*Planned/Intended features (Development is still ongoing)*
- Ability to stream-line calling processes and handling return
- More advanced and specialised functionality for managing embedded code
- Program-State Saving for continuing execution at a later point
- Multi-Threaded processing with embedded languages in multiple threads
- Ability to integrate processes quickly
- Simplification of the base C language with simplified syntax and additional helper functions
- Ability to manage exceptions and issues with programs (Including Fallback Options)
- Any-Type and integrated conversion functions for type
- Decorator and Overload Functions
- Language Library with additional helper functions
- Simplified syntax and handling of C components for easier coding

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
 
## CLI

### Commands
*Commands displayed are mostly only partly implemented*
- `parac compile` - Compile a Para-C program to C or executable
- `parac run` - Compiles a Para-C program and runs it (Creates build and dist as well)
- `parac c-init` - Console Line Interface for the configuration of the C-compiler
- `parac syntax-check` - Validates the syntax of a Para-C program and logs errors if needed
- `parac analyse` - Analyses a program by running the Pre-Processor and validating the syntax (Not added yet. See [#9](/../../issues/9) and [#10](/../../issues/10))

## Development

![Deploy and test workflow](https://github.com/Luna-Klatzer/Para-C/actions/workflows/python-test.yml/badge.svg)
![Coverage](./coverage.svg)
![License](https://img.shields.io/github/license/Luna-Klatzer/Para-C?color=cyan)
![Lines of Code](https://img.shields.io/tokei/lines/github/Luna-Klatzer/Para-C)

### Parsing and Processing Procedure

Due to the two components, which are the Pre-Processor, and the core Compiler
the entire module is split into two modules: `preprocessor` and `paraccompiler`,
which both implement their own handling for the source-code. This means that 
when compiling a file, the file will be sent through the Pre-Processor first,
modified and then sent to the Para-C Compiler. This also means errors reported
will be from the modified file, so that the modified code is visible to the 
user, instead of the file without correct Pre-Processor processing.

### Building

#### Generating the Parser and Lexer

*Required for Lexer and Parser Development which include changes on the .g4 grammar files*

##### Downloading Antlr4

To download Antlr4 go [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar)

Quickstart Installation Guide on the Main Website: [here](https://www.antlr.org/)

##### Generating the Source files

Generating the Parser and Lexer is made up of two parts:

- Using Antlr4 to compile the .g4 file to actual source code
- Implementing the Runtime (The user code that is shipped with the binaries)

*Note: Generating the Parser and Lexer means that depending on the changes
the implementation code needs to be changed.*

To generate in the command-line use:
- For the Pre-Processor:
  - Python (Required for the Compiler):
      ```bash
      antlr4 -o ./preprocessor/python -Dlanguage=Python3 ./grammar/ParaCPreProcessor.g4
      ```
  - Java:
      ```bash
      antlr4 -o ./preprocessor/python -Dlanguage=Java ./grammar/ParaCPreProcessor.g4
      ```

- For the Core Language:
  - Python (Required for the Compiler):
      ```bash
      antlr4 -o ./paraccompiler/core/parser/python -Dlanguage=Python3 ./grammar/ParaC.g4
      ```
  - Java:
      ```bash
       antlr4 -o ./paraccompiler/core/parser/python -Dlanguage=Java ./grammar/ParaC.g4
      ```
  
Afterwards *if needed* correctly move the folder using:
```bash
mv ./path/to/generated/output/* ./paraccompiler/core/<insert-destination>/
```

and delete the remaining folder:
```bash
rm -rf ./path/to/generated/output
```

**Notes:**
- *Make sure the alias for `antlr4` / `antlr` exists! Else the command will not work*
- *Comments are only partly ignored in ParaC.g4, due the intended removal in the Pre-Processor. Errors can occur!*

#### Build the Executable and binaries

For generating the binaries, PyInstaller with a wrapper script will be used.
This script will automatically run the generation of source files and copying of data.

To run the script simply use (Python3):
```bash
python ./build-exe.py
```

The script will create a `./build/` and `./dist/` folder.
The `./build/` folder will contain the raw data and logs, while the `./dist/`
folder will contain the distribution-ready binaries and data.

### Installation
 
To install Para-C, you can either use the pre-built installer for the specified 
version or [build](#build-the-executable-and-binaries) and install the compiler yourself. 

#### Build inno-setup installer for Windows 

Download inno-setup [here](https://jrsoftware.org/download.php/is.exe)

Build inside this folder and use the inno-setup.iss file. The generated installer will be placed inside `./Output`

### Setup

#### For Windows

For Windows the configured inno-setup installer should be used. The installer
will automatically do the installation based on your input.

#### For unix-based systems

On unix-based systems the installation is open to the user, including the folder
where the compiler will be placed (It is recommended though to use `/opt`, 
`/usr`, `/usr/local` or similar)

Steps to add the alias `parac` to your terminal:
1. Open the .bashrc file in your home directory (for example, /home/your-user-name/.bashrc) in a text editor.
2. Add export `PATH="<your-dir>/bin:$PATH"` to the last line of the file, where your-dir is the directory you want to add.
3. Save the .bashrc file.
4. Restart your terminal.

#### Initialising the C Compiler

To start the initialisation setup for the C-Compiler use:

```bash
parac c-init
```

This will add the C-Compiler path to the Para-C compiler and make commands
related to running a Para-C program available. It is not required though and
without it the compiler will simply generate C source files.
