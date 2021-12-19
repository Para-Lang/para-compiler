************
Installation
************

This section serves as the reference for how to install the Para-C compiler and
CLI compiled standalone binaries.

.. Caution::
    The installation of the Para-C Compiler binaries will only include the
    compiled binaries and NOT the source code or module of the compiler. This
    means this section of the docs will focus on the CLI of Para-C!

    For info how to install the Python API please go to the
    `Python API Reference <./pyapi_ref/index.html>`_

Installer for Windows
=====================

For Windows, the configured inno-setup installer should be used. The installer
will automatically do the installation based on your input and create the
correct entries to the system, so that you can utilise the compiler right after
installation.

For the installer go to the `release page on github <https://github.com/Para-C/Para-C/releases>`_
and download the version you want. The installer will be named after the date of
its creation in this format: ``parac-installer-<year>-<month>-<day>.exe``.

Building it yourself (Unix+Windows)
===================================

For all other OS-systems, there are no installers yet for Para-C or entries
in package managers, meaning the compiler needs to be either built by yourself
using the `parac-build.py` script or used with a python runtime using the
`distributed pypi module <../pyapi_ref/index.html> (Python API)`_.

.. note::

    Using the source Python API will provide a lot of flexibility, but also
    means that the C-compiler has to be installed, setup and checked yourself
    if you intend to run your compiled code as well.

Downloading
-----------

Before building go to the `release page on github <https://github.com/Para-C/Para-C/releases>`_
and download either the ``.zip`` (win) or ``.tar.gz`` (unix) file depending on
your OS.

* For ``.tar.gz`` (Commonly Unix):

  .. code:: bash

     tar -xf <insert-name>.tar.gz

* For ``.zip`` (Commonly Windows):

  1. Right Click on the item in ``File Explorer``
  2. Select ``Extract All`` in the opened menubar
  3. Select the destination path, where the contents are going to be un-zipped
     to.


Building the Binaries
---------------------

To build the binaries a pre-made script is used, which will generate a dist and
build folder containing the data of the build. The build folder can be in this
case ignored, except logs and data of pyinstaller is wanted.

Inside the root folder of the source code, run the following command:

.. code:: bash

    python ./parac-build.py

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

    It is recommended to use `/usr/bin`, `/usr/local/bin`,
    `/home/$USER/.local/bin` on unix-like systems.

Make parac executable on Linux
------------------------------

.. code:: bash

    chmod a+x <your-dir>/bin/parac

Make parac executable on MacOS
------------------------------

.. code:: bash

    chmod 755 <your-dir>/bin/parac

Add Para-C to your OS path
--------------------------

The compiled binaries folder should contain a ``/bin`` folder. That folder is
the wanted item to be added to the path, as it contains the executable ``parac``.

Unix (Linux+MacOS)
^^^^^^^^^^^^^^^^^^

On UNIX and similar, modifying the ``$PATH`` requires editing the ``.bashrc``
file, which is run every time a standard bash terminal is opened.

Here, you can simply put the following at the end of the file to extend the
path by our Para-C ``/bin`` path:

.. code:: bash

    export PATH="$PATH:ENTER_THE_PARAC_BIN_PATH_HERE"

To edit the ``~/.bashrc`` file (The ``~`` means your home folder of your user)
simply use a graphical editor, like Visual Studio Code (``code``) or in case
you use a text-based user interface, use preferably ``nano`` (Though if you are
already using a TUI, then I am sure you knew all of this already).

.. note::

    Every time you change the location of the Para-C installation folder, the
    previous command will likely break, so make sure to put it into a safe
    place and leave it there from that point on!

Windows
^^^^^^^

Adding an item to the path is relatively easy on windows, and can be done over
the general settings user interface. For a walk-through with screenshots go
here: `Add to the path on Windows 10 <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>`_.

C-Compiler Setup
================

Note that at the moment, it will be very likely that the Para-C CLI build will
be shipped per default with `gcc` or `mingw-w64`, as such this will become
deprecated in the next few releases.
