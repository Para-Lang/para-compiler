
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

The switch-statement is a compare-statement, which compares a passed value
with the so-called ``cases``, which define a value that can be compared against.
Those cases must be either a constant value, a single int-based value or an
expression that evaluates to one of the two.

.. Important::

    Int-based variables are variables that are actually represented as integers.
    This does not include floating point integers at the moment, due to the
    restrictions of the base of the Para-C switch: the C switch. This uses a
    so-called lookup table, where integers are strictly enforced, meaning that
    other values will need to be compared using an :ref:`if statement<If Statement>`

Those ``cases`` are not like in if-statements limited to their own branch, but
``cases`` can fall-through (enter blocks of other cases) if no `break` statement
is used. This means that the ``cases`` actually define `entry-points` for the code
that was written inside these cases. It will execute all code downwards from
the point it reached a compare that returned ``true``. This can be stopped
though using a `break` statement, which will abort any further execution.

If no case is met, the ``default`` branch is called if it exists.

.. Warning::

    If the ``default`` keyword is hit, every case after it will **not** be compared
    against anymore, since ```default``` always returns ``true``. Fall-through
    will still work though, but the `case` will practically be useless with
    the exception of the code written inside the block.

Syntax
------

At least one ``case`` or ``default`` block is required.

.. code:: c

    switch ( <expression> )
    {
        case <constant-or-variable>:
            <block>
        default:
            <block>
    }


Usage & Examples
----------------
