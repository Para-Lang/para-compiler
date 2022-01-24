******************
Compiler Structure
******************

Overview
========

The Para Compiler is the Compiler responsible for the `Para Core Language <./index.html>`_
and the `Para Language Extensions <./tasks/index.html>`_. It parses, analyses
and links the files together to generate a C-source code output or using the
GCC C Compiler (GNU Compiler Collection C Compiler) an executable.

.. note::

    If language extensions are used, the compiler generates executables for
    each language extension (Even if multiple files and components are used,
    the compiler will merge them into a single program, which will, depending
    on the program, call different modules and code), meaning that the output
    will contain multiple executables. There are tools though that merge these
    into a single executable, to make shipping the code easier.

The Structure of the Compiler is made up of multiple components and modules,
which have specified jobs assigned e.g. components will not interact with each
other and the compiler will use the components to put all pieces together,
which in the end make up the finished program.

**The different modules are:**

- `The Pre-Processor, which will alter the code based on the pre-processor directives <./preprocessor.html>`_
- :ref:`The Lexer and Parser, which generate the tokens and the logic trees of the program. (Includes the Conversion to Logical Tokens, which simplifies the tokens to make the job easier for the Semantic Analysis.)<Lexer and Parser>`
- :ref:`The Single-File Semantic Analyser<Semantic Analyser>`
- :ref:`The File Linker<File Linker>`
- :ref:`The Code Optimiser<Code Optimiser>`
- :ref:`The Code Generator<Code Generator>`

Lexer and Parser
================

Overview
--------

The Para Core Language uses for parsing Antlr4, which automatically
generates python files for the parser, listeners and lexer based
on the `Para.g4` file. This file defines the grammar of the language.

The generated code will be wrapped inside a new python module, which will implement 
the code and make it usable in the compiler source code. Using that new Parser module,
the compiler will convert on runtime the inserted file/s into an abstract logic
tree, which contains all items and meta-data of the user-inserted file. These logic trees
are then returned and used to compile the program.

The Parser will start by first parsing the main file and then
afterwards all included files (Data of the included files will be passed by
the Pre-Processor). These will then be wrapped and passed to the Semantic
Analyser.

Antlr4 Structure (Parsing Tree Components)
------------------------------------------

The basic structure of the Parsing Tree is based on the compilationUnit, which
describes the entire file and the EOF (End of File Character). The main
component, one layer under that, is the translationUnit, which describes the
actual code that will be processed in the compiler. The translationUnit
contains a list of externalItems, which can be either a stray Semicolons(;)
or a declaration/definition of a variable or function.

Pre-Processor Grammar
---------------------

Since the Pre-Processor is syntax-wise
different than the standard language, mainly noticeable due to the line endings
(pre-processor statements with hard-line endings (``\n`` or ``\r\n``, while the normal
lines use declared line breaks in form of a Semicolons(``;``)), it uses its own
independent grammar file, and as such lexer and parser. Those will parse
everything and pass onto the Pre-Processor itself to generate the altered
files.

Semantic Analyser
=================

Overview
--------

The Semantic Analyser is the first step after the parsing process, which will 
introduce logical checking on the file and validate whether statements are 
valid or not.

This step will mainly work on converting the code into the specific internal
tokens that then can be used to properly process and link all files together. 
This task as a whole is then split into these two separate items:

- Processing the core file, where all inclusions were placed and so all declarations must be available for the logical checking step aka. type-checking and logical cohesion.
- Processing all files that were mentioned by the header aka. all source files where the definitions should be placed. Those files will be all independently processed and their inclusions will also be placed inside the files. Here it's important to note though, that due to this logic, there may never be definitions in headers, as such they would cause errors later in the linker, as it can not predict which value is to be used.

Algorithmic structure
---------------------

The Semantic Analysis will go through each externalDeclaration (Can be either a declaration or functionDefinition) and go through each block individually and check for logical correctness. This means that it will treat each function block as a single token to handle and validate each in their own context.

File Linker
===========

File linking in Para is similar to C, with the key-difference being
though, that the result of the generation is a C project (files and headers
for all items), not byte code.

This means that the linker has the main task to fetch all definitions and link
them together creating in the end the resulting C project and files (This will
be though managed by the code generator).

All definitions will be placed in the C-file, as well as the declarations in
the C-Header. This to preserve the declaration logic, and avoid reference
errors in the C code.

Code Optimiser
==============

The Code Optimiser will be the last step when processing everything, and attempt to check for duplicate declarations, unnecessary variable calls and in general things that just are not that necessary to be in source-code. Here it will still utilise the Para logic tokens, and pass them to the Code generator, which will compile the Para logic tokens into C logic tokens.

Code Generator
==============

As the name states, the code generator will convert the compiled C logic tokens into stable code, by adding all required references and creating the required structure for the functionality to work.

Compiler Warnings
=================

The Compiler while running will check for basic information and will report on possibly problematic issues such as logical issues, possible loss of data or problematic usages of certain types. While running these will be counted and at the end of the run logged as a summary of the process.
To that, syntax warnings for non-fatal formatting and inconsistency issues can be reported, as a help to avoid causing inconsistent writing and style. This also includes the partly stricter conventions, that try to improve on the loose C-conventions, which are more open to writing code.

Compiler Exceptions
===================
Exceptions inside Para are categorised into two categories:

- Non-Fatal Exceptions, which do not interfere with continuing to check the file and
- Fatal Exceptions, which can not be ignored and cause the compiler to interrupt the process and exit.

If only Non-Fatal Exceptions get noticed by the compiler, the compilation will
finish with a summary containing a counter for all errors and warnings while
running the compilation.

If a Fatal-Issue is received and causes a hard interrupt while running, the
return code will be an error code that is specified here. This helps for better
categorisation for certain errors. An error message will also appear with the
error code at the end of the file, including a trace-back if the issue is a bug
inside the compiler. (Note that the actual return code used with exit() is 1
for errors. This is due to the structure of many os-systems that require that
return codes should not exceed the 256 (8-Bits) range

Error-Codes
-----------

All Exceptions inherit from the base code (99) and their respective parent code e.g. for 204 -> 200.

99 Base Error
^^^^^^^^^^^^^

- `99` – BaseError/ParaCompilerError: Base Error every other exception inherits of.

1** Internal Errors
^^^^^^^^^^^^^^^^^^^

- `100` – InternalError: An Exception in the Internal parts of the compiler that are not related to the compilation.
- `101` – InterruptError: The compiler received an interrupt while running. (Derives from the Python Base Exception KeyboardInterrupt)
- `102` – FailedToProcessError: A specific error that is raised inside a compilation process or pre-processor process, which represents a failure in processing the wanted input. This class replaces the actual error that would be logged and all error logs will be printed onto the console.

2** User Input Errors
^^^^^^^^^^^^^^^^^^^^^

- `200` – UserInputError: General Exception due to faulty input of the user
- `201` – FileAccessError: General Exception due to failed interaction with a file
- `202` – FilePermissionError: Failed to access (read, write) to existing file due to missing permissions
- `203` – FileNotFoundError: The File was not found and does not exist! If the file can't be seen it will be treated as well as FileNotFound.
- `204` – IsDirectoryError: File is a directory
- `205` – InvalidArgumentsError: The passed flags or arguments are invalid and can't be processed.
- `206` – ConfigNotFoundError: The configuration file for the project was not found.
- `207` – CCompilerNotFoundError: Failed to locate the configured C Compiler. Path does not exist. (If the file can't be executed, FilePermissionError will be raised)

3** Lexical Errors
^^^^^^^^^^^^^^^^^^

- `300` – LexerError: An issue occurred in the Tokenizer / Lexical Analyser step of compiling. (Derive from the Antlr4 lexer errors)

4** Parser Errors
^^^^^^^^^^^^^^^^^

- `400` – ParserError: An issue occurred in the Parser (Logic Tree generator), which tries to convert the generated Antlr4 tokens into proper Logical Para tokens
- `401` – SyntaxError: A syntax issue occurred while processing that is a direct result of the user failing to input valid code.

5** Logical Errors
^^^^^^^^^^^^^^^^^^

- `500` – LogicalError: An issue occurred while walking through the program, which was caused due to logical irregularity and incompatible statements.

6** Linker Errors
^^^^^^^^^^^^^^^^^

- `600` – LinkerError: An issue occurred while linking the files together and checking dependencies and mergeability. (Logical issues like double declarations or importing a name that was already defined will be treated as linker error since they directly result from the linking process)

9** Other Errors
^^^^^^^^^^^^^^^^

- `900` – UnassociatedError: Exception of type other that is assignable to any other type of exception
- `901` – Unknown Error: Received an unknown exception while running.
