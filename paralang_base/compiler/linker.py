# coding=utf-8
"""
This file is dedicated to the linker for the Compiler, which 'link' link
together FileCompilationContext instances in a parent
ProgramCompilationContext

.

The linker will validate the existence of all items, and generate the required
outgoing code, in separate files. The headers for all items will be also
dynamically created for the C-native inclusion. The linker in this case acts
like a linker, while the outgoing code are C headers and files.
"""

__all__ = [
    "LinkerMetaData",
    "Linker"
]


class LinkerMetaData:
    """
    This is the Linker metadata instance, which will keep track of linker
    metadata inside a ProgramCompilationContext

, that are vital for the final
    generation of the C source code.

    This will keep track of dependencies, requirements, type-defs and origins
    of certain variables. This will though not apply any logical analysis,
    except validating that the required types are matching with the types
    that are needed in this specific context (asserted by the previous logical
    analysis, which are then kept as meta data in the ParseTokens)
    """
    ...


class Linker:
    """
    This is the linker for the Compiler, which will 'link' together
    FileCompilationContext instances in a parent ProgramCompilationContext
.
.

    The linker will validate the existence of all items, and generate the
    required outgoing code, in separate files. The headers for all items
    will be also dynamically created for the C-native inclusion. The linker
    in this case acts like a linker, while the outgoing code are C headers
    and files.

    This instance though will work itself inside a ProgramCompilationContext
    and update there the meta-data, while mainly just validating existence of
    items, and asserting what are required in the outgoing C code. This will
    update the LinkerMetaData instance and insert important data for generating
    the C source code (ProgramCompilationContext.linker_meta_data)
    """
    ...
