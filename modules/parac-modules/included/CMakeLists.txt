project(parac-modules)

include(FetchContent)
FetchContent_Declare(
        gc-8.0.6
        URL https://github.com/ivmai/bdwgc/releases/download/v8.0.6/gc-8.0.6.tar.gz
)
FetchContent_MakeAvailable(gc-8.0.6)
