#include "__parac__.h"

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// User Project Configuration
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
const char* ph_name = "decorator_example";
const char* ph_description = "Example for showing the functionality of decorators";
const char* ph_author = "Luna Klatzer";
const char* ph_version = "0.1";
const char* ph_license = "GPL-3.0";

/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
/// Compiler Configuration
/// C-Compiler Paths are included, so that using 'parac finish' the compilation can be automatically finished
/// = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

const char* ph_para_compiler_path = "";
const char* ph_c_compiler_path = "";

/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
/// Additional Function declarations
/// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

/// Converts the the exit-status to an entry-return type
ph_EntryPoint ExitStatusToEntryReturn(ph_ExitStatus s) { return (ph_EntryPoint) { .exit_r = s }; }
