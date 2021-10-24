project(parac-modules)

set(HEADER_FILES
        pbl-io.h
        pbl.h
        pbl-types.h
        )

set(SOURCE_FILES
        pbl-io.c
        pbl-types.c
        pbl-string.c pbl-string.h pbl-int.c pbl-int.h)

add_library(parac-modules STATIC ${SOURCE_FILES} ${HEADER_FILES})