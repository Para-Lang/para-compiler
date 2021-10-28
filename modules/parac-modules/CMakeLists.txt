project(parac-modules)

set(HEADER_FILES
        pbl-io.h
        pbl.h
        pbl-types.h
        pbl-string.h
        pbl-int.h
        pbl-exception.h
        pbl-function.h)

set(SOURCE_FILES
        pbl-io.c
        pbl-types.c
        pbl-string.c
        pbl-int.c
        pbl-exception.c
        pbl.c
        pbl-function.c)

set(INCLUDED_EXTENSIONS
        included/va-opt.h)

add_library(parac-modules STATIC ${SOURCE_FILES} ${HEADER_FILES} ${INCLUDED_EXTENSIONS})