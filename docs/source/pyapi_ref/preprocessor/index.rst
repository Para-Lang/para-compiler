********************
Para Pre-Processor
********************

.. toctree::
    :hidden:

    Pre-Processor ABCs <abc>
    Compilation Context <ctx>
    Parse Tokens <parse_tokens>
    Parse Stream <parse_stream>
    Error Handler <error_handler>
    Listener <listener>
    Parser <parser>

Para Pre-Processor, which handles the Para directives and alters the code
before it is then sent to the main `Compiler <../compiler/index.html>`_

Reference Overview
==================

- `Pre-Processor ABCs <./abc.html>`_ - ABCs for the Pre-Processor.
- `Compilation Context <./ctx.html>`_ - Compilation Context used to store the information about Para files, programs and its contents. (Pre-Processor specific).
- `Parse Tokens <./parse_tokens.html>`_ - Parse Tokens used to represent and store logical content of a Para file.
- `Parse Stream <./parse_stream.html>`_ - Parse Stream used to represent and store a Para file's content.
- `Error Handler <./error_handler.html>`_ - Error Handler which is used with the Antlr4 Listener to recognise Syntax Errors and other problems inside the user-files.
- `Listener <./listener.html>`_ - Listener, which goes through the Antlr4 generated tree and generates the Token Streams.
- `Antlr4 Parser <./parser.html>`_ - Antlr4 Parser, which lexers and parses the files (auto-generated by the grammar file).
