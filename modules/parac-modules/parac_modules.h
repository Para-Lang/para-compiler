///
/// Main header for the Para-C Base Library (Static C library)
/// Styling and naming are applied based on the Google C++ style guide
/// @see https://google.github.io/styleguide/cppguide.html
///
/// Headers of the library:
/// - io.h
/// - types.h
///
/// @date 08-10-2021
/// @author Luna-Klatzer

// lib-headers includes
#include "io.h"
#include "types.h"


#ifndef PARAC_MODULES_LIBRARY_H
#define PARAC_MODULES_LIBRARY_H

#ifdef __cplusplus
extern "C" {
#endif

/// The current release identifier
#define PARAC_LIB_VERSION "0.1.dev5"
/// Indicates the current library version being a development version
#define PARAC_DEVELOPMENT_RELEASE true
/// Indicates the current library version being a stable version
#define PARAC_STABLE_RELEASE false
/// Indicates the usage of Para-C -> Always true
#define PARAC_LANG true

#ifdef __cplusplus
}
#endif

#endif //PARAC_MODULES_LIBRARY_H
