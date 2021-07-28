
***********************************
Welcome to the Python API Reference
***********************************

This serves as a throughout reference for the Python module `parac` and API,
which can be used for customised usage of the Para-C Compiler, Pre-Processor
and utilities.

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
    package-manager (on linux) or run the script ``get-pip.py``. Go
    `here for info about that <https://stackoverflow.com/questions/9780717/>`_


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

