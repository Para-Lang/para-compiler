#! /bin/sh
# Para-C Compiler Build Makefile, which builds the compiler for the specified
# target.
#

VERSION = 0.1.dev5

build:
	ifndef TARGET
	$(error Required arg 'TARGET' is not set)
	endif

# installing the build to a specified path
install:
	ifndef TARGET
	$(error Required arg 'TARGET' is not set)
	endif

