*************
Styling Guide
*************

Styling Guidelines on how to format Para-C files, write code and how to
appropriately name things.

This is intended as a reference, and does not necessarily have to be followed,
but it nonetheless recommend to be respected to ensure a consistent styling
across projects.

Naming Conventions
==================

The naming conventions refer to the naming scheme that should be used, when
`declaring and defining variables <../declaration_and_types/index.html>`_ and
naming special items (``typedef`` and files). This should ensure a consistent
naming and styling, and the ability to differentiate between the items more
easily.

+--------------------------------------------+---------------------------------------+-----------------+
| Type                                       | Public                                | Internal*       |
+============================================+=======================================+=================+
|                                            |                                       |                 |
| Header-file                                | Any                                   |                 |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Source-file                                | Any                                   |                 |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Structures (Classes, Structs)              | PascalCase                            | _PascalCase     |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Exceptions                                 | PascalCase (with Error at the end)    |                 |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Functions/Methods                          | PascalCase                            | _ snake_case    |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Property field (struct or simple class)    | snake_case                            |                 |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Variables                                  | snake_case                            | _snake_case     |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Instances                                  | snake_case                            | _snake_case     |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Constants                                  | PascalCase with a leading k           | _SNAKE_CASE     |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Built-In Types                             | alllowercase                          | (Forbidden)     |
+--------------------------------------------+---------------------------------------+-----------------+
|                                            |                                       |                 |
| Typedef Types                              | PascalCase with a trailing _T         | (Forbidden)     |
+--------------------------------------------+---------------------------------------+-----------------+