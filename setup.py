# coding=utf-8
""" Setup file for the entire project """
import os
from pathlib import Path

import setuptools

with open("./PYPI_README.md", "r", encoding='utf-8') as file:
    long_description = file.read()

with open("./requirements/common.txt", encoding='utf-8') as file:
    requirements = file.read()

setuptools.setup(
    name="paralang",
    version="0.1.dev7",
    author="Luna Klatzer",
    author_email="luna.klatzer@gmail.com",
    maintainer="Luna Klatzer",
    maintainer_email="luna.klatzer@gmail.com",
    description="Python-Compiler and API for the Para language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU GENERAL PUBLIC LICENSE v3.0",
    url="https://github.com/Para-Lang/Para/",
    project_urls={
        "Issue-Page": "https://github.com/Para-Lang/Para/issues/",
        "Changelog": "https://github.com/Para-Lang/Para/releases",
        "Docs": "https://para.readthedocs.org/"
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: C",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Compilers",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=requirements
)
