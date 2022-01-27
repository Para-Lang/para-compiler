************
Installation
************

This section serves as the reference for how to install the Para compiler and
the Para CLI for usage in the console.

As Para is a natively a Python module, you have the option of using a built
version that provides a stable executable, or running the pypi module with
your own python instance. The latter is preferred if you desire more
customisation and easier updates, as a built executable won't be updated and
you have to install a completely new version.

.. important::

    To run a Para program, you will have to configure a C compiler yourself
    (for now), which will then actually execute the code that was generated.

    This will likely be automated in the future, though for now this is the
    most reasonable approach, as Para is still in early development.

    This is explained more in detail
    :ref:`here (C Compiler Setup) <C Compiler Setup>`.

Installer (Windows)
===================

For Windows Para provides a pre-built installer for each release, meaning you
can install it like any other application by running the installer.

For the installer go to the
`release page on github <https://github.com/Para-Lang/Para/releases>`_ and
download the version you want.

The installer will be named after the date of its creation in the following
format:

``para-installer-<year>-<month>-<day>.exe``

Running the Python Source Code (Unix+Windows)
=============================================

For all operating systems that can run Python ``>= 3.8`` you may run the source
code itself, as the compiler is written natively in Python and is distributed
as a python module that can be downloaded from pypi (The Python Package Index).

To install the Python module, go
`here (Python API Reference) <./pyapi_ref/index.html>`_.

.. note::

    Using the source Python API will provide a lot of flexibility, but also
    means that the C-compiler has to be installed, setup and checked yourself
    if you intend to run your compiled code as well.

Building it yourself (Unix+Windows)
===================================

For UNIX-systems there is no proper installer yet that can be used, and as such
you will have to build the Para Compiler and Para CLI yourself using a pre-made
script, which will build for your specific operating system.

The building process will also require Python ``>=3.8`` to be installed and you
will have to install the Python source code, like if you were intending to
:ref:`run the source code <Running the Python Source Code (Unix+Windows)>`
itself. Though the major difference in building the Para compiler is the
pre-configured structure and additional tools that are bundled
into a single executable by the build script. This also means you have a
separate instance from your Python interpreter, which will not break if you
update your Python version.

This provides a lot of safety and ease, though the building process might take
some time, which is why it is likely that in the future an installer,
``.AppImage`` or Snap Package will be made available for quick and simple
installation of Para.

Downloading
-----------

Before building go to the `release page on github <https://github.com/Para-Lang/Para/releases>`_
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

Inside the root folder of the source code, run the following command to execute
the pre-made script, which will automatically manage everything:

.. code:: bash

    python ./para-build.py

.. note::

    If you need additional info on the script, use:

    .. code:: bash

        python ./para-build.py --help

    This will display additional help on the command, such as how to specify
    an url and download it on runtime, or how to specifically install it
    globally.

The compilation may take a while since it will wrap the entire program
with the python instance into a standalone compiled binary, which can then
be used.

After the successful installation of Para, the root folder for Para
will be called ``para`` and will be located in the ``./dist/`` folder. This
folder can be deleted after the module was moved to its destination.

.. note::

    It does not matter where Para is located as long as the structure inside
    the root directory stays in tact. For that reason you can decide where it
    should be located when using it.

    It is recommended to use on unix-like systems the following directories:

    - ``/usr/bin``
    - ``/usr/local/bin``
    - ``/home/$USER/.local/bin``

    To make the script move to those destinations per default call the script
    using:

    .. code:: bash

        python ./para-build.py --install-global

    This will default to the following paths:

    - Unix (Linux, MacOS): ``/usr/local/bin/para/``
    - Windows: ``C:\\Program Files (x86)\\para\\``

    To specify a different path simply pass it as arg to ``--g-dest $PATH``,
    for example:

    .. code:: bash

        python ./para-build.py --install-global --g-dest /usr/bin/Para

Make para executable
---------------------

Per default para should be executable on all platforms. In the case though
it's not, then you may specify its execution permissions like here:

- On Linux

  .. code:: bash

    chmod a+x <your-dir>/bin/para

- On MacOS

  .. code:: bash

    chmod 755 <your-dir>/bin/para

.. note::

    On Windows this is obsolete, as the file-ending ``.exe`` defines per
    default that the file is executable and as such there should not be an
    issue when accessing it on Windows.

Make ``para`` available in the Command Line
--------------------------------------------

This step is entirely optional, though good if you want to have ``para`` in a
proper location, then you should do this.

Unix (Linux+MacOS)
^^^^^^^^^^^^^^^^^^

On UNIX, we can simply create an alias for the para executable.

To edit the ``~/.bashrc`` file (The ``~`` means your home folder of your user)
simply use a graphical editor, like Visual Studio Code (``code``) or in case
you use a text-based user interface, use preferably ``nano``.

Here, you can simply put the following at the end of the file to extend the
path by our Para ``/bin`` path:

.. code:: bash

    alias para="$DEST_PATH/bin/para"

.. note::

    Every time you change the location of the Para installation folder, the
    alias will break, so make sure to put it into a safe place and leave it
    there from that point on!

Windows
^^^^^^^

Adding an item to the path is relatively easy on windows, and can be done over
the general settings user interface. For a walk-through with screenshots go
here: `Add to the path on Windows 10 <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>`_.

C Compiler Setup
================

Currently the compiler setup is not done globally, but locally for each single
project. This may change in the future, as Para continues to be developed.

Linux
-----

Installation
""""""""""""

On Linux, you may simple use the native default GCC compiler.
Though, in many cases, GCC might be already pre-installed,
so to check if you have a compatible version, do the following:

.. code:: bash

    gcc --version

If GCC is not found, search online how you can install GCC with your
package manger.

Validate Installation
"""""""""""""""""""""

Afterwards, get the location of the executable, as you will need this to
properly configure a Para project:

.. code:: bash

    type gcc

The output may look like this:

.. code:: bash

    gcc is /usr/bin/gcc

Copy the path ``/usr/bin/gcc`` or whatever path you will get, and put it into
your configuration file.

Windows
-------

On Windows, as there is no native GCC you will have to use MinGW-w64
(Minimalist GNU for Windows) or LLVM clang (recommended as it appears more
stable).

At the moment, there is also no support for the Visual Studio C Compiler, and
likely there will never be support for it.

Chocolatey
^^^^^^^^^^

For an installation of MinGW-w64 or clang it is recommended to use the tool
called chocolatey, which is an easy package manager and installer that will
handle the installation of the compiler for you.

For a guide on how to install chocolatey go
`here (Choco Setup) <https://docs.chocolatey.org/en-us/choco/setup>`_.

Install LLVM Clang
^^^^^^^^^^^^^^^^^^

Installation
""""""""""""

To install clang run the following:

.. code:: bash

    choco install llvm

Validate Installation
"""""""""""""""""""""

After the successful installation, go and see whether the proper clang
version has been installed using:

.. code:: bash

    clang --version

Afterwards locate the path of the clang executable, as you will need this to
properly configure a Para project:

.. code:: bash

    where.exe clang

Install MinGW-w64
^^^^^^^^^^^^^^^^^

Installation
""""""""""""

To install mingw run the following:

.. code:: bash

    choco install mingw

Validate Installation
"""""""""""""""""""""

After the successful installation, go and see whether the proper GCC
version has been installed using:

.. code:: bash

    gcc --version

If there is proper output showing a
:ref:`supported version of GCC <Supported GCC Versions>`, then you may proceed.

Afterwards locate the path of the MinGW executable, as you will need this to
properly configure a Para project:

.. code:: bash

    where.exe gcc

MacOS
-----

On MacOS, you may use either GCC or clang, though clang is recommended, due its
stability on MacOS.

Homebrew
^^^^^^^^

For the installation of clang, you will have to install
`homebrew <https://brew.sh/>`_ to properly install and setup the compiler.
(There are alternative methods, but `homebrew <https://brew.sh/>`_ is the
simplest way to install the compilers on MacOS)

To install homebrew copy the following snippet and run it:

.. code:: bash

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install LLVM Clang
^^^^^^^^^^^^^^^^^^

Installation
""""""""""""

To install clang, run the following command:

.. code:: bash

    brew install llvm

Validate Installation
"""""""""""""""""""""

Afterwards, get the location of the executable, as you will need this to
properly configure a Para project:

.. code:: bash

    type clang

The output may look like this:

.. code:: bash

    clang is /usr/bin/clang

Copy the path ``/usr/bin/clang`` or whatever path you will get, and put it into
your configuration file.

Supported Clang Versions
========================

+---------------------------------+-------------+
| Version                         | Support     |
+=================================+=============+
| 5.x                             | ❌          |
+---------------------------------+-------------+
| 6.x                             | ❌          |
+---------------------------------+-------------+
| 7.x                             | ✔️          |
+---------------------------------+-------------+
| 8.x                             | ✔️          |
+---------------------------------+-------------+
| 9.x                             | ✔️          |
+---------------------------------+-------------+
| 10.x                            | ✔️          |
+---------------------------------+-------------+
| 11.x                            | ✔️          |
+---------------------------------+-------------+
| 12.x                            | ✔️          |
+---------------------------------+-------------+
| 13.x                            | ✔️          |
+---------------------------------+-------------+

*❌ = not supported*
*❓ = support unknown and issues can occur / not fully tested yet*
*✔️ = fully supported and validated*

Supported GCC Versions
======================

*This also counts for MinGW gcc versions*

+---------------------------------+-------------+
| Version                         | Support     |
+=================================+=============+
| 6.x                             | ❌          |
+---------------------------------+-------------+
| 7.x                             | ❌          |
+---------------------------------+-------------+
| 8.x                             | ❓          |
+---------------------------------+-------------+
| 9.x                             | ✔️          |
+---------------------------------+-------------+
| 10.x                            | ✔️          |
+---------------------------------+-------------+
| 11.x                            | ✔️          |
+---------------------------------+-------------+

*❌ = not supported*
*❓ = support unknown and issues can occur / not fully tested yet*
*✔️ = fully supported and validated*
