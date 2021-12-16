# Development

## Parsing and Processing Procedure

Due to the two components, which are the Pre-Processor, and the core Compiler
the entire module is split into two modules: `preprocessor` and `paraccompiler`,
which both implement their handling for the source-code. This means that 
when compiling a file, the file will be sent through the Pre-Processor first,
modified and then sent to the Para-C Compiler. 

This also means errors reported will be from the modified file, so that the 
modified code is visible to the user, instead of the file without correct 
Pre-Processor processing.

## Build inno-setup installer for Windows

Download inno-setup [here](https://jrsoftware.org/download.php/is.exe)

Build inside this folder and use the inno-setup.iss file. The generated installer will be placed inside `./Output`

## Building

### Generating the Parser and Lexer

*Required for Lexer and Parser Development which include changes on the .g4 grammar files*

#### Downloading Antlr4

To download Antlr4 go [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar)

Quickstart Installation Guide on the Main Website: [here](https://www.antlr.org/)

#### Generating the Python files

Generating the Parser and Lexer is made up of two parts:

- Using Antlr4 to compile the .g4 file to actual source code
- Implementing the Runtime (The user code that is shipped with the binaries)

*Note: Generating the Parser and Lexer means that depending on the changes
the implementation code needs to be changed.*

To generate in the command-line use:
- For the Pre-Processor:
  - Python (Required for the Compiler):
      ```bash
      antlr4 -o ./parac/preprocessor/python -Dlanguage=Python3 ./grammar/ParaCPreProcessor.g4
      ```
  - Java:
      ```bash
      antlr4 -o ./parac/preprocessor/python -Dlanguage=Java ./grammar/ParaCPreProcessor.g4
      ```

- For the Core Language:
  - Python (Required for the Compiler):
      ```bash
      antlr4 -o ./parac/compiler/parser/python -Dlanguage=Python3 ./grammar/ParaC.g4
      ```
  - Java:
      ```bash
      antlr4 -o ./parac/compiler/parser/python -Dlanguage=Java ./grammar/ParaC.g4
      ```
  
Afterwards *if needed* correctly move the folder using:
```bash
mv ./path/to/generated/output/* ./src/compiler/core/<insert-destination>/
```

and delete the remaining folder:
```bash
rm -rf ./path/to/generated/output
```

**Notes:**
- *Make sure the alias for `antlr4` / `antlr` exists! Else the command will not work*
- *Comments are only partly ignored in ParaC.g4, due the intended removal in the Pre-Processor. Errors can occur!*

### Build the executable and binaries

For generating the binaries, PyInstaller with a wrapper script will be used.
This script will automatically run the generation of source files and copying of data.

To run the script simply use (Python3):
```bash
python ./src/parac-build.py
```

The script will create a `./build/` and `./dist/` folder.
The `./build/` folder will contain the raw data and logs, while the `./dist/`
folder will contain the distribution-ready binaries and data.

## Generating the docs

To generate the docs for a one-time usage, use the following:

```bash
./docs/make.bat html
```

or for an active http server, which will automatically reload changes:

```bash
sphinx-autobuild ./docs/source ./docs/build/html
```

