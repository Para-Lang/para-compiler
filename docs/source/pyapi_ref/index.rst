***********************************
Welcome to the Python API Reference
***********************************

.. toctree::
    :hidden:

    Exceptions <exceptions>
    ABC Classes <abc>
    Para-C Compiler <compiler/index>
    Pre-Processor <preprocessor/index>

This serves as a throughout reference for the Python module `parac` and API,
which can be used for customised usage of the Para-C Compiler, Pre-Processor
and utilities.

Through the structure of Para-C, the compiler module can be used independently
from the binaries and CLI, and modified as wanted to also allow for specific
customisation or runtime usage.

This also means it enables for example; Running the Pre-Processor alone, using
syntax-checks on specific files or running project-structure tools inside a
Python script made by you.

.. Note::

    The Python API requires an active Python installation (``>=3.8``), since
    using the API means running the Compiler source code itself. If you want
    compiled standalone binaries go to the page `Installation <../installation>`_

Installation
############

For the distribution of the package, python`s pip and pypi.org are used to
store the built wheel and source files of the module.

To install simply do the following:

.. tab:: Regular

    .. code::

        python3 -m pip install -U parac


.. tab:: With specific version

    .. code::

        python3 -m pip install -U parac==version


.. Hint::

    If the command ``pip`` is not found, try to either install it using your
    package-manager (for linux) or run the script ``get-pip.py`` (for Windows: `here <https://www.geeksforgeeks.org/how-to-install-pip-on-windows/>`_, for MacOS `here <https://www.geeksforgeeks.org/how-to-install-pip-in-macos/>`_).
    
Requirements
############

+---------------------------------+-------------+
| Requirement                     | Version     |
+=================================+=============+
| Python                          | >=3.8       |
+---------------------------------+-------------+
| colorama                        | >=0.4.4     |
+---------------------------------+-------------+
| click                           | >=8.0.0     |
+---------------------------------+-------------+
| setuptools                      | >=51.1.2    |
+---------------------------------+-------------+
| rich                            | >=10.0.0    |
+---------------------------------+-------------+
| antlr4-python3-runtime          | >=4.9       |
+---------------------------------+-------------+
| cached-property                 | >=1.5.1     |
+---------------------------------+-------------+

.. Note::

    Module Requirements (except Python) will be automatically installed with
    `pip install`

Overview
########

- `Exceptions <./exceptions.html>`_ - Exceptions in the Para-C Compiler and Python API
- `Pre-Processor <./preprocessor.html>`_ - Pre-Processor for handling directives
- `Para-C Compiler <./compiler.html>`_ - Core Para-C Compiler for handling Para-C code and generating the C counterpart
- `ABC Classes <./abc.html>`_ - ABC Classes, which are implemented in the Compiler and Pre-Processor
