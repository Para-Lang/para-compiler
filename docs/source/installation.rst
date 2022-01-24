************
Installation
************

This section serves as the reference for how to install the Para compiler and
make it available for usage in your command line.

Installer for Windows
=====================

For Windows, the configured inno-setup installer should be used. The installer
will automatically do the installation based on your input and create the
correct entries to the system, so that you can utilise the compiler right after
installation.

For the installer go to the `release page on github <https://github.com/Para-Lang/Para/releases>`_
and download the version you want. The installer will be named after the date of
its creation in this format: ``para-installer-<year>-<month>-<day>.exe``.

Building it yourself (Unix+Windows)
===================================

For all other OS-systems, there are no installers yet for Para or entries
in package managers, meaning the compiler needs to be either built by yourself
using the `para-build.py` script or used with a python runtime using the
`distributed pypi module <../pyapi_ref/index.html> (Python API)`_.

.. note::

    Using the source Python API will provide a lot of flexibility, but also
    means that the C-compiler has to be installed, setup and checked yourself
    if you intend to run your compiled code as well.

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

    - POSIX (Unix, Linux, MacOS): ``/usr/local/bin/Para``
    - NT (Windows): ``C:\\Program Files (x86)\\Para\\``

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
    previous command will likely break, so make sure to put it into a safe
    place and leave it there from that point on!

Windows
^^^^^^^

Adding an item to the path is relatively easy on windows, and can be done over
the general settings user interface. For a walk-through with screenshots go
here: `Add to the path on Windows 10 <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>`_.

C-Compiler Setup
================

Note that at the moment, it will be very likely that the Para CLI build will
be shipped per default with `gcc` or `mingw-w64`, as such this will become
deprecated in the next few releases.
