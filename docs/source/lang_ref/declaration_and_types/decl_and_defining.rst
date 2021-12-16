********************************
Declaring and Defining Variables
********************************

Overview
========

Like in C, the Para-C language bases on the declaration and definition system
for managing it's variables. That means that the scope of a variable can be
declared, which can then be either defined declared or in a scope that has
access to it.

.. note::

    For proper info on scopes go to section :ref:`Scopes <Scopes>`

This is an important difference to know while programming to also be able to
properly differentiate and utilise the two, as they build the fundamental basis
for all programming.

Scopes
======

First of all, to understand how to properly use variables in general, the logic
of scopes is rather important. Para-C sticks here as with most things to C, aka.
to not re-invent the wheel and overcomplicate processes that are already simple
enough.

Scopes can be easily split into the following types:

- "Project/Global Scope" - The scope that inclusion is handled, which may be
  accessed by all files that are connected together. This is though in reality
  accessing the scope of another file and importing it into the local file one
  using the pre-processor
- Local File Scope (Local Global Scope) - Local File scope, which defines the
  local variables, which may be accessed by all function scopes and compound
  scopes in this file
- `Function Scope / Function Definition Scope <../functions/index.html>`_
- `Compound Statement ({ }) <../statements/compound_statement.html>`_

Declaring Variables
===================


Defining Variables
==================

