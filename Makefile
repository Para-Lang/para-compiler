#! /bin/sh
# Para-C Compiler Build Makefile, which builds the compiler for the specified
# target.
#

VERSION = 0.1.dev5
DEFAULT_CLI_SRC_URL = https://github.com/Para-C/Para-C-CLI/archive/refs/tags/${VERSION}.zip
CLI_SRC_URL ?= DEFAULT_CLI_SRC_URL

ifndef TARGET
$(error Required arg 'TARGET' is not set)
endif

# building the source files and generating the binaries
build:
	@echo $(CLI_SRC_URL)

# installing the build to a specified path
install:
	@echo $(CLI_SRC_URL)


