#include "types.h"

#ifndef PARAC_MODULES_IO_H
#define PARAC_MODULES_IO_H

#ifdef __cplusplus
extern "C" {
#endif

/// File Descriptor used to perform I/O actions on a file
struct pblFileDescriptor {
    // the unique integer identifier associated with the file Descriptor
    int fb;
    /// describes whether the file descriptor is currently in use
    bool open;
};
typedef pblFileDescriptor pblFileDescriptor;

/// Std-Stream for stdin, stdout and stderr
typedef struct {
    /// file descriptor to the file
    int fb;
} pblStdStream;
typedef pblStdStream pblStdStream;

/// Arguments struct for pbl_print (pbl_print_args_in)
struct pbl_print_args_t {
    pblString_T* out;
    const char end;
};
typedef pbl_print_args_t pbl_print_args_t;

void pbl_print_args_in(pbl_print_args_t in);

/// @brief Prints the content of the passed string
/// @param out The string_t that should be printed
/// @param end The end character that should be printed at the end of the print
#define pbl_print(...) pbl_print_args_in((pbl_print_args_t){__VA_ARGS__});

#ifdef __cplusplus
}
#endif

#endif //PARAC_MODULES_IO_H
