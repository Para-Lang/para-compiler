*******************
Function Specifiers
*******************

Function Specifiers are specifiers that indicate certain functionality of a
function. They can be applied to every generic function with the exception
of lambda functions

Entry-Point Specifier
=====================

The entry-point specifier is a unique single-usage specifier used to signalise
to the compiler that a specific function should be the entry for the program.

.. note::

    The return type of the function **must** be `status` as it is specifically
    the function which exit the program, and as such requires a return code
    aka. exit-status to report if the program was successful or not.

    If `exit()` is called, the `status` value will be simply passed as the
    argument.

Syntax
------

.. code:: c

    entry status <identifier>(<arg-signature>) { }


Usage & Examples
----------------

1. Example with a simple function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: c

    entry status Main()
    {
        return (status) { .status_code = 0 };
    }

Footnotes
-----------

1. At least one `entry` specifier is needed inside the entry-file for the Para
   project to properly run. If none is provided the compiler will raise an error.

No-Return Specifier
=====================

The `noreturn` is a specifier used to signalise that a function will not return.
This can mean either the function will run forever or will call the function `exit()`
during it's operation, stopping the program before return.

Syntax
------

.. code:: c

    noreturn <identifier>(<arg-signature>) { }

1. Example with a simple function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: c

    noreturn void x()
    {
        // Working hard ...

        exit((status) { .status_code = 0 });
    }