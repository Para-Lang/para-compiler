# coding=utf-8
"""
Main file that calls the CLI - This file is used as the entry for pyinstaller
"""
try:
    import parac_ext_cli
except ImportError as e:
    raise ImportError(
        "Failed to locate child module 'parac_ext_cli'. "
        "This module has to be installed to utilise the CLI version of Para-C"
    ) from e

try:
    from parac.logging import init_rich_console
except ImportError as e:
    raise ImportError("Failed to locate parent module 'parac'") from e

if __name__ == '__main__':
    init_rich_console()
    parac_ext_cli.cli_entry()
