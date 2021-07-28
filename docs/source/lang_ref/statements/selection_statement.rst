
*******************
Selection Statement
*******************

The selection statement is the standard way of executing a block of code depending
on the evaluation of a expression which can either return ``1``/``true`` or
``0``/``false``. These are in Para-C, like in C, implemented with ``if`` statements
and ``switch`` statements.

If Statement
============

The if-statement is the most common way of utilising a selection statement.

It performs, based on an initial ``if`` statement and possible following
``else if`` or ``else`` statements, evaluations of each expression one after
one until an expression evaluates to ``1``/``true`` (This can also be one single
initial ``if`` statement) or the else-block is reached (optional).

.. Important::

    Expressions that do not evaluate to boolean values (``0``/``1``) will be
    counted as ``true``, since their value is non-zero.

Syntax
------

.. code:: c

    if ( <expression> )
        <statement-or-block>
    else if ( <expression> ) // optional, can be repeated
        <statement-or-block>
    else // optional, can be repeated
        <statement-or-block>


Usage & Examples
----------------

1. Simple Example of a comparison of two values:

.. code:: c

    entry status main()
    {
        int x = 4;
        int y = 3;

        if (x == y)
        {
            print("x equals y");
        }
        else
        {
            print(f"x does NOT equal y. Actual value: x={x}, y={y}");
        }
    }


In this case the expression that is evaluated is ``x == y`` which will return
a bool value. The following block or `compound statement <./compound_statement.html>`_
is executed only if the previous expression evaluated to ``true``.

In this case the evaluation will *"fail"* and the program will proceed to execute
the else block, since no other option exists, which could be attempted to be
evaluated.

2. Simple Example of the previous example without { }

.. code:: c

    entry status main()
    {
        int x = 4;
        int y = 3;

        // selection statements without compound statement and just a single statement
        if (x == y)
            print("x equals y");  // statement
        else
            print(f"x does NOT equal y. Actual value: x={x}, y={y}");  // statement
    }

In this case the program will do the exact same as in the first program but
in this case without a `compound statement <./compound_statement.html>`_ and just
a regular statement (call of a function).

3. Simple Example of an ``if`` statement with multiple options and nested ``if`` statement

.. code:: c

    entry status main()
    {
        int x = 4;

        if (x < 3)
        {
            // selection statements without compound statement and just a single statement
            if (x < 0)
                print("x is smaller than 3 and negative");
            else if (x == 0)
                print("x is smaller than 3 and not positive nor negative");
            else
                print("x is smaller than 3 and positive");
        }
        else if (x < 5)
        {
            print("x is smaller than 5");
        }
    }

In this case the evaluation of the first block can either lead to another
if-statement or the continuation to an ``else if`` statement. Though no ``else``
block exists, meaning when reaching the second statement, if variable ``x`` is not
smaller than ``5``, the selection statement will end without any block execution
and the program simply end.

Switch Statement
================

Syntax
------

Usage & Examples
----------------

Additional Notes
----------------
