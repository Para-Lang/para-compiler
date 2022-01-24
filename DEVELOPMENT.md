# Development

## Installing Dependencies

To install the dev-dependencies, simply use `./requirements/dev.txt` with pip,
like the following:

```bash
pip install -r requirements/dev.txt
```

Or for a virtual environment:

```bash
pipenv install -r requirements/dev.txt
```
## Building

### Build inno-setup installer for Windows

Download inno-setup [here](https://jrsoftware.org/download.php/is.exe)

Build inside this folder and use the inno-setup.iss file. The generated
installer will be placed inside `./Output`

### Generating the Parser and Lexer

*Required for Lexer and Parser Development which include changes on the .g4
grammar files*

#### Downloading Antlr4

To download Antlr4
go [here](https://www.antlr.org/download/antlr-4.9.2-complete.jar)

Quickstart Installation Guide on the Main
Website: [here](https://www.antlr.org/)

#### Generating the Python files

Generating the Parser and Lexer is made up of two parts:

- Using Antlr4 to compile the .g4 file to actual source code
- Implementing the Runtime (The user code that is shipped with the binaries)

*Note: Generating the Parser and Lexer means that depending on the changes the
implementation code needs to be changed.*

To generate in the command-line use:

- For the Pre-Processor:
    - Python (Required for the Compiler):
        ```bash
        antlr4 -o ./para/preprocessor/parser -Dlanguage=Python3 ./ParaPreProcessor.g4
        ```
    - Java:
        ```bash
        antlr4 -o ./para/preprocessor/parser -Dlanguage=Java ./ParaPreProcessor.g4
        ```

- For the Core Language:
    - Python (Required for the Compiler):
        ```bash
        antlr4 -o ./para/compiler/parser/python -Dlanguage=Python3 ./Para.g4
        ```
    - Java:
        ```bash
        antlr4 -o ./para/compiler/parser/python -Dlanguage=Java ./Para.g4
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

- *Make sure the alias for `antlr4` / `antlr` exists! Else the command will not
  work*
- *Comments are only partly ignored in Para.g4, due the intended removal in
  the Pre-Processor. Errors can occur!*

## Generating the docs

To generate the docs for a one-time usage, use the following:

```bash
./docs/make.bat html
```

or for an active http server, which will automatically reload changes, use
this:

```bash
sphinx-autobuild ./docs/source ./docs/build/html
```

