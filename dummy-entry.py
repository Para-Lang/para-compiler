# coding=utf-8
"""
Dummy entry for pyinstaller - uses importlib to specify relative import and
avoid global name shadowing the local ones
"""
import importlib

if __name__ == '__main__':
    # importing local modules
    para = importlib.import_module("paralang", __name__)
    para_ext_cli = importlib.import_module("para_ext_cli")

    getattr(para_ext_cli, 'cli_run')()
