
************
Installation
************

This section serves as the reference for how to install the Para-C compiler and
CLI compiled standalone binaries.

.. Caution::
    The installation of the Para-C Compiler binaries will only include the
    compiled binaries and NOT the source code or module of the compiler.
    For info how to install that please go to `Python API Reference <../api_ref/index.html>`_

Installer for Windows
=====================

For Windows, the configured inno-setup installer should be used. The installer
will automatically do the installation based on your input and create the
correct entries to the system, so that you can utilise the compiler right after
installation.

For the installer go to the `release page on github <https://github.com/Para-C/Para-C/releases>`_
and download the version you want. The installer will be named after the date of
its creation in this format: ``parac-installer-<year>-<month>-<day>.exe``.

Building it yourself (Unix+Win)
===============================

For all other OS-systems, there are no installers yet for Para-C or entries
in package managers, meaning the compiler needs to be either built yourself
using python or used with a python runtime using the `distributed pypi module <../api_ref/index.html>`_.

Downloading
-----------

Before building go to the `release page on github <https://github.com/Para-C/Para-C/releases>`_
and download either the ``.zip`` (win) or ``.tar.gz`` (unix) file depending on
your OS.

* For ``.tar.gz`` extract afterwards using:

  .. code:: bash

     tar -xf <insert-name>.tar.gz

* For ``.zip`` click on the file on windows and select extract.

Building the Binaries
---------------------

To build the binaries a pre-made script is used, which will generate a dist and
build folder containing the data of the build. The build folder can be in this
case ignored, except logs and data of pyinstaller is wanted.

Run inside the root folder of the extracted module:

.. code:: bash

    python ./src/build-exe.py

The compilation can take a while since it will wrap the entire program
with the python instance into a standalone compiled binary, which can then
be used.

After the successful installation of Para-C, the root folder for Para-C
will be called ``parac`` and will be located in the ``./dist/`` folder. This
folder can be deleted after the module was moved to its destination.

.. Note::

    It does not matter where Para-C is located as long as the structure inside
    the root directory stays in tact. For that reason you can decide where it
    should be located when using it.

    It is recommended though to use `/opt`, `/usr`, `/usr/local` or similar on unix-like systems.

Make parac executable on Linux
------------------------------

.. code:: bash

    chmod a+x <your-dir>/bin/parac

Make parac executable on MacOS
------------------------------

.. code:: bash

    chmod 755 <your-dir>/bin/parac

Add Para-C as alias
-------------------

Linux
^^^^^

1. Open your ``~/.bash_aliases`` file using ``nano ~/.bash_aliases``
2. Add ``alias parac="<your-dir>/bin/parac"`` to the last line of the file, where your-dir is the directory you moved parac into.
3. Save the ``.bash_aliases`` file.
4. Activate for the terminal session using ``source ~/.bash_aliases``.
5. Permanently add the alias by adding this line to the end of your ``~/.bashrc`` file:

.. code:: bash

    if [ -f ~/.bash_aliases ]; then
        . ~/.bash_aliases
    fi

MacOS
^^^^^

The previous instructions for linux also work on MacOS due to it being unix as well.

`Additional Info on MacOS Dock Aliases the official website. <https://support.apple.com/en-al/guide/mac-help/mchlp1046/mac>`_

Windows
^^^^^^^

For Windows an alias in not required, since the item can easily be added to
the PATH, which will then automatically search for the item inside the specified
directory.

.. seealso::

    For more info on that go `here <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>`_.

C-Compiler Setup
================

