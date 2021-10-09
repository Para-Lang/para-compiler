# Changelog

All notable changes to the Compiler will be documented in this file.
Note that these changes in this file are specifically for the Compiler.
The full summary will be in the CHANGELOG.md file the main folder 

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

*Note that Documentation changes should not appear here!*

## [Unreleased]

### Added
- `initialise_default_paths` in `parac.const` to initialise the set the const
   variables DEFAULT_LOG_PATH, DEFAULT_BUILD_PATH and DEFAULT_DIST_PATH. This
   allows for more customisation for the defaults paths in Para-C and avoids
   the default paths being wrong after changing the working directory while running.
- Property `errors` in `BaseErrorListener` for storing received errors during
  the parsing process (Both for the Pre-Processor and Compiler).
- New Exception `ParaCSyntaxError` with proper implementation of error logs.
- New Exception `ParaCSyntaxErrorCollection` for storing multiple SyntaxErrors
  and report them at once when initialised.
- New Util functions: `get_input_stream_from_ctx`, `get_original_text` and
  `get_original_text_from_token`.
- Implemented SyntaxError handling using the Antlr4 Error Handler - New Error Strategy is to collect all syntax errors and then at the end collect all warnings and 
  errors and display them.
- Support for Whitespaces in the Antlr4 Grammar file to allow for better error messages and separation.  
- Function in `util/pathtools.py` `ensure_pathlib_path`, which will convert
  the passed value to a pathlib.Path, if it's not already one. It will also 
  resolve all sys-links.
- Property `logic_stream` to `Listener` and updated methods to allow for proper
  future implementation of the logic stream.
- New method `append_antlr_ctx` to the ABC Class `LogicStream` and its 
  implementation.
- Added addition of `program_ctx` to all `FileRunContext` implementation
  classes.

### Changed
- Style of the init banner in the CLI and added docs link.
- Merged dynamic lists and arrays into the standard iterable type associated with `type identifier[]`,
  which can utilise list functionality, but also practically stay normal arrays at the same time if not resized. For 
  more info see the lang document.
- Fixed workdir issue in pytest causing usage outside `./src/pytest` to raise errors.
- Fixed work-directory issue in `build-exe.py` and rewrote structure to allow runtime in the root directory.
- The modules will now commonly use `pathlib.Path` and convert to it if is
  a different type (str, bytes).
- Renamed `validate_file_ending` to `has_valid_file_ending` and fixed a minor bug replacing the
  `all` call (all file endings must be true) to `any`, meaning now only one needs to be true, which
  is the correct and intended way of handling this.
- Renamed `compiler-version` tag in `parac-config.json` to `parac-version`
- Renamed the following keywords in ParaC.g4:
  - `_Alignas` to `alignas`
  - `_Alignof` to `alignof`
  - `_Atomic` to `atomic`
  - `_Bool` to `bool`
  - `_Complex` to `complex`
  - `_Imaginary` to `imaginary`
  - `_Noreturn` to `noreturn`
  - `_Static_assert` to `static_assert`
  - `__Thread_local` to `thread_local`
- Deprecated `const.SEPARATOR` and updated `get_relative_file_name` to properly
  apply to the change
- Updated Error message of `RuntimeError`(Mismatching file_names) in 
  `get_relative_file_name`
- Changed behaviour of `ParacCompiler.validate_syntax()` and removed the 
  additional usage of a listener to walk through the files, even though
  a simple parse was enough for validating the syntax.
- Updated logging messages and added more of them, where they are needed.  
- Renamed `parac_cli` to `parac_ext_cli` and published it to pypi

### Removed
- `list<t>` type from the Grammar file.
- `WORK_DIR` in `parac.const` and implemented dynamic fetching to allow for 
   workdir changes while running.
- Full Support for extensionTaskLambda (deprecated).
- Deprecated `cleanup_path_str()` and `check_valid_path_name()` from `util/pathtools.py`.
- Independent rule `entryPointSpecifier` in ParaC.g4
- Unsupported C keywords and statements from the grammar file (ParaC.g4):
  - `__extension__`
  - `__builtin_va_arg`
  - `__builtin_offsetof`
  - `_Generic` (Might be added later again with new syntax)
  - `__inline__`
  - `__stdcall`
  - `__declspec`
  - `__attribute__`
  - `__asm`
- Removed `__typeof__` version of `typeof` from the grammar file (ParaC.g4)

## [v0.1.dev4] - 2021-07-23

### Added
- Installation section in the README.md
- `.parah` and `.ph` as valid file extensions 
 
### Changed
- Wrong license classifier in setup.py

## [v0.1.dev3] - 2021-07-23

### Changed
- Tags in setup.py, since commas were missing causing faulty identifiers

### Removed
- Banner in README.md to avoid the image processing issue on pypi.org

## [v0.1.dev2] - 2021-07-23

### Added
- Pure syntax check command (`parac syntax-check`, For info see #9 and #10)
- Added const file `const.py` for containing constant values that are used
  throughout the module
- pypi Module Structure with new parent `parac`. Releases from now on will be uploaded to pypi.org as module
- Distinction between distribution and module version and const Values 
  (`const.py`) `DIST_VERSION` and `MODULE_VERSION` for separating Distribution
  and Module/Source-Code Version.
- Pre-Processor module, including its own grammar and handling for files
- Integration of the compiled Antlr4 lexer and parser in both Pre-Processor and Compiler
- ABC Base Class Files (in module `parac/abc/`) for both Pre-Processor and Para-Compiler
- New Exception Classes (With appropriate Update of `class ErrorCodes(IntEnum)`): 
  - `InternalError`
  - `FailedToProcessError`
  - `UserInputError`
  - `FileAccessError`
  - `InvalidArgumentsError`
  - `ConfigNotFoundError`
  - `CCompilerNotFoundError`
  - `LexerError`
  - `ParserError`
  - `LogicalError`
  - `LinkerError`
  - `UnassociatedError`
  - `UnknownError`
- Temp file handling for creating new temporary files after the Pre-Processor
  finished its processing run. This means the Compiler will receive the modified files
  and raise errors on the *modified* ones and not the original ones.
- Process Classes that manage an entire Run of the Compiler: `BasicProcess`, `FinishedProcess` and
  `ProgramCompilationProcess`
- Context Classes that manage the context for a specific file or program (both Pre-Processor and Compiler):
  `FileCompilationContext`, `ProgramCompilationContext`, `FilePreProcessorContext`,
  `ProgramPreProcessorContext` with respective parent ABC classes: `FileRunContext`
  and `ProgramCompilationContext`
- Implementation of Base ABC Class `LogicStream` (inherits `list` as parent)  
- `remove_comments_from_str` in `ParacCompiler` with support for all line endings
- In `abortable` decorator (`utils.py`);
  - New argument `preserve_exception`: If set to `True` preserves original 
    exception and not raise a new one from it
  - New argument `abort_on_internal_errors`: If set to `True` Internal Errors
    are treated like `InterruptErrors` and will abort the compilation
- Class `InternalErrorInfo` for saving information about an exception causing an `InternalError`
- Property `origin_exc` to `InterrruptError` for saving the original exception instance that was raised.
- New module `parac_cli` for implementing the `parac` module
- `modules/parac-modules` as the base folder for the library items
- `modules/parac-modules/types.h` for the types for Para-C and added basic string implementation
- `modules/parac-modules/io.h` for IO management in Para-C - added basic `print` function

### Changed
- Module Structure and added new parent module `parac` for both compiler and preprocessor.
- Token Classes and refined items  
- In `build-exe.py`; Implemented `pathlib.Path` usage and proper handling changed based on the new structure
- Antlr4 Grammar file to include Pre-Processor statements and 
  the basic entry-file specification syntax
- Updated runtime and added `asyncio` implementation support for running
  processes async and concurrent as optimisation.
- Error codes and exceptions (as stated in the language document `doc/ParaC-Luna-Klatzer.docx`)
- Usage of `antlr4.InputStream` (string stream) instead of `antlr4.FileStream`
- Updated tests appropriately to the changes
- Renamed `AbortError` to `InterruptError`
- Renamed `EntryFilePermissionError` to `FilePermissionError` 
- Renamed `EntryFileAccessError` to `FileAccessError` 
- Renamed `EntryFileNotFoundError` to `FileNotFoundError`
- `ParacErrorListener` and let it inherit base ABC class `BaseErrorListener`
- `README.md` and added appropriate documentation on antlr4, cli and changes
- Renamed cli command `init` to `c-init`
- Renamed `parac-base-library` to `lib` and moved it to `src/lib`
- Moved `logging` to base folder `parac`
- Moved `utils.py` and split items into multiple files in `parac/util`
- Renamed `para_exceptions.py` to `exceptions.py` and moved it to base folder `parac`

### Removed
- pytest option `--github=<true/false>` (Became unnecessary and deprecated)
- Comment Parsing Support. Comments are now handled over the function 
  `parac.compiler.core.compiler.ParacCompiler.remove_comments_from_str`


## [v0.1.dev1] - 2021-07-04

### Added
- Added structure for the core compiler and pre-processor
- Added syntax to the grammar files for the core language and preprocessor directives
- Added basic CLI Interface for interacting with the compiler
- Added compiler structure and place-holder functions for later implementation
- Added examples for implementation and user-code
- Set up a testing structure for the compiler using `pytest`
- Created testing files for the parser and lexer

[unreleased]: https://github.com/Para-C/Para-C/compare/v0.1.dev4...dev
[v0.1.dev4]: https://github.com/Para-C/Para-C/compare/v0.1.dev3...v0.1.dev4
[v0.1.dev3]: https://github.com/Para-C/Para-C/compare/v0.1.dev2...v0.1.dev3
[v0.1.dev2]: https://github.com/Para-C/Para-C/compare/v0.1.dev1...v0.1.dev2
[v0.1.dev1]: https://github.com/Para-C/Para-C/releases/tag/v0.1.dev1
