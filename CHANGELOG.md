# Changelog

All notable changes to the Compiler will be documented in this file. Note that
these changes in this file are specifically for the Compiler. The full summary
will be in the CHANGELOG.md file the main folder

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
, and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

*Note that Documentation changes should not appear here!*

## Unreleased

### Added

### Changed
- Behaviour of `DIST_COMPILED_VERSION`, which will try to detect the compiled
  binary state using `sys.argv` and the call identifier.
- Installation behaviour of `para-build.py`, which will from now use
  `/scripts/scripts.spec` to configure and build using pyinstaller. For each
  script in `/scripts/` an executable will be also generated to allow for 
  extensions like `paraproj` to be used in the console.

### Removed
- Unneeded `bin-config.json` and `BIN_CONFIG_PATH` constant
  variable in `const.py`.
- Unneeded `C_COM_EXISTENCE_OVERWRITE`, which is useless
  with the new configuration style.
- Unneeded `MODULE_VERSION` constant variable in `const.py`.

## [v0.1.dev7] - 2022-01-27

### Added
- `Linker` and `LinkerMetaData` classes for the linking step and dependency
  analysis that is between the logical analysis and code
  generation/optimisation.
- CLI for `parac-build.py` to simplify the building process by allowing for 
  more configuration. This also includes web-download and automatic global
  installation. 
- `requirements` folder with requirements for each use-case like `dev`, `prod`
  or `common` (base requirements for both `dev` and `prod`).
- New function `ProgramCompilationContext.parse_all_files()`, which will parse
  all files.
- Parameter `project_root` for `BasicProcess`, `ProgramCompilationContext` and
  `ProgramCompilationContext`, which defines the root of the project structure.
  This will also be used for relative naming and paths!
- New Wrapper class `ParacProjectConfig` for handling json-config files. This
  is still in work and not going to be properly finished until the compiler 
  core has been done.
- Ability to use `logging` without having to stick to CLI formatted logging.

### Updated
- Renamed `build.py` to `parac-build.py` to not interfere with the `build`
  module.
- Removed the `optimiser` module and replaced it with `optimiser.py`.
- Renamed class `ParacParseStream` to ParacQualifiedParseStream.
- Renamed function `CompileProcess._compile()` to `ci_compile`.
- Renamed function  `CompileProcess._gen_preprocessor_temp_files()`
  to `gen_preprocessor_temp_files()`.
- Renamed function `CompileProcess._run_preprocessor()` to
  `preprocess_files()`.
- Renamed parameter `log_errors_and_warnings` to `prefer_logging`.
- Updated handling of `ParacCompiler.validate_syntax()` to be an entry-point
  function, which will take as arguments the wanted file path and encoding. 
  This means no longer a `BasicProcess` or `CompileProcess` is 
  needed!
- Handling of files to use an overall files list defined in
  `parac-config.json`, instead of dynamically fetching using entry files. 
  This means it will be similar to GCC compiler using a pre-defined list of 
  files, and then link all of them together in the end making them ready for
  execution.
- Renamed `Para-C` to `Para` to suit better to its intended feature-set.
- Renamed `parac-build.py` to `para-build.py`.
- Renamed all Python classes prefixes `Parac` to `Para`.
- Moved `logging.py` CLI functions to `para_ext_cli`.
- Made `ParaCompiler.validate_syntax()` an instance method instead of class .
  method as it needs the `ParaCompiler` runtime property `logger`.
- Renamed the class `process.FinishedProcess` to `process.CompileResult`.
- Renamed the class `process.ProgramCompilationProcess` to 
  `process.CompileProcess`.
- Renamed all items named `LogicToken` and `LogicStream` to `ParseToken` and
  `ParseStream`.
- Restructured listeners, context classes and parse stream functions to have
  a more straightforward module structure, while generating a parse stream.

### Removed
- Property `mode` in `bin-config.json`.
- Deprecated `SEPARATOR` and `WIN` from const.py.
- Constant Compiler instance `RUNTIME_COMPILER`.
- Functions related to `c-init`, as the C Compiler configuration will from now
  on be done using `para-config.json`.
- `dist_path` and `build_path` folders, as the code-file generation is now
  handled using `process.CompileResult` and `CompileResult.write_results()`.
- Unneeded `paralang_base.logging` module, which has now been completely replaced
  by the default `logging` handling, and `paralang_base_cli.logging`.

## [v0.1.dev6] - 2021-11-10

### Added

- Updated build-system and added `build.py`, which allows proper building with
  the PBL
- `dummy-entry.py`

### Changed

- Changed behaviour to detect binary mode, by providing the new
  file `bin-config.json`
- Replaced based on the recent implementation changed, `compiler-config.json`
  with `bin-config.json`, which specifically is configured for the Para-C
  Compiler, and the OS it was built on.

### Removed

- Removed unneeded constants: `INVALID_WIN_FILE_NAME_CHARS`
  , `INVALID_UNIX_FILE_NAME_CHARS` and `DEFAULT_CONFIG`

## [v0.1.dev5] - 2021-11-09

### Added

- `initialise_default_paths` in `parac.const` to initialise the set the const
  variables DEFAULT_LOG_PATH, DEFAULT_BUILD_PATH and DEFAULT_DIST_PATH. This
  allows for more customisation for the defaults paths in Para-C and avoids the
  default paths being wrong after changing the working directory while running.
- Property `errors` in `BaseErrorListener` for storing received errors during
  the parsing process (Both for the Pre-Processor and Compiler).
- New Exception `ParaCSyntaxError` with proper implementation of error logs.
- New Exception `ParaCSyntaxErrorCollection` for storing multiple SyntaxErrors
  and report them at once when initialised.
- New Util functions: `get_input_stream_from_ctx`, `get_original_text` and
  `get_original_text_from_token`.
- Implemented SyntaxError handling using the Antlr4 Error Handler - New Error
  Strategy is to collect all syntax errors and then at the end collect all
  warnings and errors and display them.
- Support for Whitespaces in the Antlr4 Grammar file to allow for better error
  messages and separation.
- Function in `util/pathtools.py` `ensure_pathlib_path`, which will convert the
  passed value to a pathlib.Path, if it's not already one. It will also resolve
  all sys-links.
- Property `parse_stream` to `Listener` and updated methods to allow for proper
  future implementation of the logic stream.
- New method `append_antlr_ctx` to the ABC Class `ParseStream` and its
  implementation.
- Addition of `program_ctx` to all `FileRunContext` implementation classes.

### Changed

- Style of the init banner in the CLI and added docs link.
- Merged dynamic lists and arrays into the standard iterable type associated
  with `type identifier[]`, which can utilise list functionality, but also
  practically stay normal arrays at the same time if not resized. For more info
  see the lang document.
- Fixed workdir issue in pytest causing usage outside `./src/pytest` to raise
  errors.
- Fixed work-directory issue in `build-exe.py` and rewrote structure to allow
  runtime in the root directory.
- The modules will now commonly use `pathlib.Path` and convert to it if is a
  different type (str, bytes).
- Renamed `validate_file_ending` to `has_valid_file_ending` and fixed a minor
  bug replacing the
  `all` call (all file endings must be true) to `any`, meaning now only one
  needs to be true, which is the correct and intended way of handling this.
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
  additional usage of a listener to walk through the files, even though a
  simple parse was enough for validating the syntax.
- Updated logging messages and added more of them, where they are needed.
- Renamed `parac_cli` to `parac_ext_cli` and published it to pypi
- Moved Para-C Base Library data to new
  repo [here](https://github.com/Para-Lang/Para-Base-Library)
- Deleted the file `entry_cli.py` here, and moved the function
  to `parac-ext-cli`
  [here](https://github.com/Para-Lang/Para-CLI). This function can now be called
  using `cli_run()`; This means that the main repo and module can only be run
  as module, and the CLI is a fully separate entity.

### Removed

- `list<t>` type from the Grammar file.
- `WORK_DIR` in `parac.const` and implemented dynamic fetching to allow for
  workdir changes while running.
- Full Support for extensionTaskLambda (deprecated).
- Deprecated `cleanup_path_str()` and `check_valid_path_name()`
  from `util/pathtools.py`.
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
- Removed `goto` as it is not supported in the Para-C logic (ParaC.g4)
- Return-value `bool` from `ParacCompiler.validate_syntax()` as it is
  unnecessary with the raised exception when encountering a SyntaxError

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
- pypi Module Structure with new parent `parac`. Releases from now on will be
  uploaded to pypi.org as module
- Distinction between distribution and module version and const Values
  (`const.py`) `DIST_COMPILED_VERSION` and `MODULE_VERSION` for separating
  Distribution and Module/Source-Code Version.
- Pre-Processor module, including its own grammar and handling for files
- Integration of the compiled Antlr4 lexer and parser in both Pre-Processor and
  Compiler
- ABC Base Class Files (in module `parac/abc/`) for both Pre-Processor and
  Para-Compiler
- New Exception Classes (With appropriate Update
  of `class ErrorCodes(IntEnum)`):
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
  finished its processing run. This means the Compiler will receive the
  modified files and raise errors on the *modified* ones and not the original
  ones.
- Process Classes that manage an entire Run of the Compiler: `BasicProcess`
  , `FinishedProcess` and `ProgramCompilationProcess`
- Context Classes that manage the context for a specific file or program (both
  Pre-Processor and Compiler):
  `FileCompilationContext`, `ProgramCompilationContext`
  , `FilePreProcessorContext`,
  `ProgramPreProcessorContext` with respective parent ABC
  classes: `FileRunContext`
  and `ProgramCompilationContext`
- Implementation of Base ABC Class `ParseStream` (inherits `list` as parent)
- `remove_comments_from_str` in `ParacCompiler` with support for all line
  endings
- In `abortable` decorator (`utils.py`);
    - New argument `preserve_exception`: If set to `True` preserves original
      exception and not raise a new one from it
    - New argument `abort_on_internal_errors`: If set to `True` Internal Errors
      are treated like `InterruptErrors` and will abort the compilation
- Class `InternalErrorInfo` for saving information about an exception causing
  an `InternalError`
- Property `origin_exc` to `InterrruptError` for saving the original exception
  instance that was raised.
- New module `parac_cli` for implementing the `parac` module

### Changed

- Module Structure and added new parent module `parac` for both compiler and
  preprocessor.
- Token Classes and refined items
- In `build-exe.py`; Implemented `pathlib.Path` usage and proper handling
  changed based on the new structure
- Antlr4 Grammar file to include Pre-Processor statements and the basic
  entry-file specification syntax
- Updated runtime and added `asyncio` implementation support for running
  processes async and concurrent as optimisation.
- Error codes and exceptions (as stated in the language
  document `doc/ParaC-Luna-Klatzer.docx`)
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
- Renamed `para_exceptions.py` to `exceptions.py` and moved it to base
  folder `parac`

### Removed

- pytest option `--github=<true/false>` (Became unnecessary and deprecated)
- Comment Parsing Support. Comments are now handled over the function
  `parac.compiler.core.compiler.ParacCompiler.remove_comments_from_str`

## [v0.1.dev1] - 2021-07-04

### Added

- Added structure for the core compiler and pre-processor
- Added syntax to the grammar files for the core language and preprocessor
  directives
- Added basic CLI Interface for interacting with the compiler
- Added compiler structure and place-holder functions for later implementation
- Added examples for implementation and user-code
- Set up a testing structure for the compiler using `pytest`
- Created testing files for the parser and lexer

[unreleased]: https://github.com/Para-Lang/Para/compare/v0.1.dev7...dev
[v0.1.dev7]: https://github.com/Para-Lang/Para/compare/v0.1.dev6...v0.1.dev7
[v0.1.dev6]: https://github.com/Para-Lang/Para/compare/v0.1.dev5...v0.1.dev6
[v0.1.dev5]: https://github.com/Para-Lang/Para/compare/v0.1.dev4...v0.1.dev5
[v0.1.dev4]: https://github.com/Para-Lang/Para/compare/v0.1.dev3...v0.1.dev4
[v0.1.dev3]: https://github.com/Para-Lang/Para/compare/v0.1.dev2...v0.1.dev3
[v0.1.dev2]: https://github.com/Para-Lang/Para/compare/v0.1.dev1...v0.1.dev2
[v0.1.dev1]: https://github.com/Para-Lang/Para/releases/tag/v0.1.dev1
