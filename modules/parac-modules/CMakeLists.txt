project(parac-modules)

set(HEADER_FILES
        io.h
        library.h
        types.h
        )

set(SOURCE_FILES
        io.c
        library.c
        types.c
        )

add_library(parac-modules STATIC ${SOURCE_FILES} ${HEADER_FILES})