# coding=utf-8
""" Script for building the compiler as an executable """
import PyInstaller.__main__
import pkg_resources
import shutil
import os

required = [
    'parac.ico',
    'parac.png',
    'LICENSE',
    'USAGE-README.md'
]

path: str = pkg_resources.resource_filename(__name__, 'compiler.py')
icon_path: str = f"{os.path.realpath(__name__)}\\..\\parac.ico"

PyInstaller.__main__.run([
    path,
    '--log-level',
    'DEBUG',
    '--name',
    'parac',
    f'--icon={icon_path}'
])

os.mkdir(".\\dist\\parac\\bin\\")
for entry in os.scandir(".\\dist\\parac\\"):
    entry: os.DirEntry
    shutil.move(entry.path, ".\\dist\\parac\\bin\\")

for entry in required:
    shutil.copy(".\\%s" % entry, ".\\dist\\parac\\")

shutil.copy(".\\README.md", ".\\dist\\parac\\GITHUB-README.md")
