
******************
Compound Statement
******************

Compound statements are the technical term for a ``{ }`` aka. code block, where
statements can be written inside of brackets. Meaning simply:

*A compound statement is a list of statements enclosed by braces ({ }).*

Compound statements are commonly used for `functions <../index.html>`_,
`iteration statements <./iteration_statement.html>`_ and
`selection statements <./selection_statement.html>`_

Syntax
------

.. code:: c

    {
        // child statements
    }

Usage & Examples
----------------

1. Function Example
^^^^^^^^^^^^^^^^^^^

.. code:: c

    entry status Main()
    // This is a compound statement
    {
        print("Hello world!"); // call statement inside compound statement
        return (status) { .status_code = 0 }; // return statement inside compound statement
    }

*Output:*

.. code:: bash

    Hello world!


Simple function usage, where the function **requires** a compound statement to
properly work.

2. Nested Block Example
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: c

    entry status Main()
    // This is a compound statement
    {
        // A simple example where a compound statement is nested
        {
            print("Hello world!"); // call statement inside compound statement
        }
        return (status) { .status_code = 0 }; // return statement inside compound statement
    }

*Output:*

.. code:: bash

    Hello world!

Simple example where a compound statement is in another compound statement.
Here the compound statement is partly useless, as the content of the nested
block is executed either way without any change in execution.

2. Nested Block Example with `while` loop
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: c

    entry status Main()
    // This is a compound statement
    {
        int i = 0;

        // A simple while loop where a compound statement is required
        while (i < 10)
        {
            print("Hello world!"); // call statement inside compound statement
        }
        return (status) { .status_code = 0 }; // return statement inside compound statement
    }

*Output:*

.. code:: bash

    Hello world!
    Hello world!
    Hello world!
    Hello world!
    Hello world!
    Hello world!
    Hello world!
    Hello world!
    Hello world!
    Hello world!

Simple Example of the usage inside a `while loop <./iteration_statement.html>`_

Additional Notes
----------------

1. Compound statements can be only used in combination of a function definition
   or as a child of another compound statement (See :ref:`Nested Block Example<2. Nested Block Example>`)
