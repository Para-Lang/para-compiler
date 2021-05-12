""" Script for building the compiler as an executable """
import PyInstaller.__main__
import pkg_resources
import os

path: str = pkg_resources.resource_filename(__name__, 'compiler.py')
icon_path: str = f"{os.path.realpath(__name__)}\\..\\Para-C.ico"

PyInstaller.__main__.run([
    f'{path} ',
    '--log-level',
    'DEBUG',
    '--name',
    'parac',
    '--onefile',
    f'--icon={icon_path}'
])