# coding=utf-8
""" Main compile function that calls the CLI """
import parac_cli
from parac.logging import init_rich_console

if __name__ == '__main__':
    init_rich_console()
    parac_cli.cli_entry()
