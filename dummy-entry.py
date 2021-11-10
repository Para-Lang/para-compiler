# coding=utf-8
"""
Dummy entry for pyinstaller - uses importlib to specify relative import and
avoid global name shadowing the local ones
"""
import importlib

if __name__ == '__main__':
    # importing local modules
    parac = importlib.import_module("parac", __name__)
    parac_ext_cli = importlib.import_module("parac_ext_cli", __name__)

    getattr(parac_ext_cli, 'cli_run')()
