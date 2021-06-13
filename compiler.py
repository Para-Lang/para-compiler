# coding=utf-8
""" Main compile function that calls the CLI """
from paraccompiler import __main__, init_rich_console

if __name__ == '__main__':
    init_rich_console()
    __main__.cli()
