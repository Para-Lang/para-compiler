
********************
Expression Statement
********************

Expression Statements are the most important statement in a Para-C program, as
they practically do all of the work and perform the tasks inside a program.
They are simple expressions which are following by a semi-colon (``;``).

Syntax
------

.. code:: c

    <expression-to-be-evaluated>;

Usage & Examples
----------------

1. Arithmetic Expression Statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: c

    entry status Main()
    {
        // three assignment expressions
        int x = 5;
        int y = 7;
        int z = 13;

        // assignment expression with assigned result of arithmetic expression
        int result = x * y * z;

        return (status) { .status_code = 0 };
    }


In this example there are three assignment expressions, which define
`variables <../declaration_and_types/index.html>`_, and another assignment
expression storing the result of the arithmetic expression (``x * y * z``) in
the variable ``result``.

2. Function Call Expression Statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: c

    long GetDouble(int value)
    {
        return value * 2;
    }

    entry status Main()
    {
        // assignment expression with assigned result of function call expression
        int result = GetDouble(2);

        print(f"Result of function call expression is {result}");

        return (status) { .status_code = 0 };
    }

Here we have a simple function definition, which is then invoked in the
``Main()`` function of the program. Here the function is called in the function
call expression, where afterwards the evaluated value of the expression is
stored in the variable ``result``.

The ``result`` is simply printed afterwards in another function call
expression with ``print()``, which though simply represents a function call
without any expression utilising the return of it afterwards.

Additional Notes
----------------
1. Arithmetic, Logical, Conditional and Relational Expressions are forbidden as
   expression statements, unless they store their value in an assignment
   expression. This is to prevent useless statements, where evaluation does not
   influence the program and the intentions are unclear.
