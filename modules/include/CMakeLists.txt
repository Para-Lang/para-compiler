project(parac-modules)

include(FetchContent)
FetchContent_Declare(
        gc-8.0.6
        URL https://github.com/ivmai/bdwgc/releases/download/v8.0.6/gc-8.0.6.tar.gz
)
FetchContent_MakeAvailable(gc-8.0.6)

set(HEADER_FILES
        pbl-io.h
        pbl.h
        pbl-types.h
        pbl-string.h
        pbl-int.h
        pbl-function.h
        pbl-main.h
        pbl-mem.h
        )

set(SOURCE_FILES
        pbl-io.c
        pbl-types.c
        pbl-string.c
        pbl-int.c
        pbl.c
        pbl-function.c
        pbl-main.c
        pbl-mem.c
        )

set(INCLUDED_EXTENSIONS
        additional/va-opt.h)

add_library(parac-modules STATIC ${SOURCE_FILES} ${HEADER_FILES} ${INCLUDED_EXTENSIONS})