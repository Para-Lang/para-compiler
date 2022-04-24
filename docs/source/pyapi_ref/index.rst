***********************************
Welcome to the Python API Reference
***********************************

.. toctree::
    :hidden:

    Exceptions <exceptions>
    ABC Classes <abc>
    Para Compiler <compiler/index>
    Extensions <extensions/index>

This serves as a throughout reference for the Python module `para` and API,
which can be used for customised usage of the Para Compiler/

Through the structure of Para, the compiler module can be used independently
from the binaries and CLI, and modified as wanted to also allow for specific
customisation or runtime usage.

Compiler Installation - ``paralang-base``
=========================================

For the distribution of the package, python`s  pip and pypi.org are used to
store the built wheel and source files of the module.

To install simply do the following:

.. tab:: Regular

    .. code::

        python3 -m pip install -U paralang-base


.. tab:: With specific version

    .. code::

        python3 -m pip install -U paralang-base==version


.. Hint::

    If the command ``pip`` is not found, try to either install it using your
    package-manager (for linux) or run the script ``get-pip.py``
    (for Windows:
    `here <https://www.geeksforgeeks.org/how-to-install-pip-on-windows/>`_,
    for MacOS
    `here <https://www.geeksforgeeks.org/how-to-install-pip-in-macos/>`_
    ).


Compiler Requirements
---------------------

+---------------------------------+-------------+
| Requirement                     | Version     |
+=================================+=============+
| Python                          | >=3.8       |
+---------------------------------+-------------+
| setuptools                      | >=51.1.2    |
+---------------------------------+-------------+
| antlr4-python3-runtime          | >=4.9       |
+---------------------------------+-------------+
| cached-property                 | >=1.5.1     |
+---------------------------------+-------------+

.. note::

    Module Requirements (except Python) will be automatically installed with:

    .. code::

        pip install para

CLI Installation - ``paralang-cli``
===================================

Additionally to the module ``paralang-base``, the optional module
``paralang-cli`` may be installed, which implements the CLI for the para
module.

To install simply do the following:

.. tab:: Regular

    .. code::

        python3 -m pip install -U paralang_cli


.. tab:: With specific version

    .. code::

        python3 -m pip install -U paralang_cli==version

With the installation the CLI will automatically register the ``para``
identifier in the console and add the installation path to the global ``$PATH``.

This means you can after having installed the CLI, you can directly access it
using:

.. code::

    para --help

CLI Requirements
----------------

+---------------------------------+-------------+
| Requirement                     | Version     |
+=================================+=============+
| colorama                        | >=0.4.4     |
+---------------------------------+-------------+
| click                           | >=8.0.0     |
+---------------------------------+-------------+
| rich                            | >=10.0.0    |
+---------------------------------+-------------+

.. note::

    These requirements extend the base requirements from the
    :ref:`previous ones. <Compiler Requirements>`

Overview
========

- `Exceptions <./exceptions.html>`_ - Exceptions in the Para Compiler and Python API.
- `Para Compiler <./compiler.html>`_ - Core Para Compiler for handling Para code and generating the C counterpart.
- `ABC Classes <./abc.html>`_ - ABC Classes, which are implemented in the Compiler.
- `Para Extensions <./extensions/index.html>`_ - Para CLI Extensions and Tools.
