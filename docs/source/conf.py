# coding=utf-8
"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

# -- Testing path ------------------------------------------------------------

import parac
import parac_ext_cli

assert parac.__version__
assert parac_ext_cli.__version__

# -- Project information -----------------------------------------------------

project = 'Para-C'
copyright = '2021, Luna Klatzer'
author = 'Luna Klatzer'

# The full version, including alpha/beta/rc tags
release = 'v0.1.dev6'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
    "sphinx_autodoc_typehints",
    "sphinxext.opengraph",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_title = f'Para-C {release}'
html_theme = 'pydata_sphinx_theme'
html_logo = '../../img/parac.ico'
html_favicon = '../../img/parac.ico'
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/Para-C/Para-C",
            "icon": "fab fa-github-square",
        }
    ],
    "icon_links_label": "Quick Links",
    "external_links": [
        {
            "name": "License ",
            "url": "https://github.com/Para-C/Para-C/blob/main/LICENSE"
        },
        {
            "name": "Report an issue ",
            "url": "https://github.com/Para-C/Para-C/issues/new/"
        },
        {
            "name": "Discussion Page ",
            "url": "https://github.com/Para-C/Para-C/discussions/"
        },
        {
            "name": "PyPi Page ",
            "url": "https://pypi.org/project/parac/"
        }
    ]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


def skip(app, what, name, obj, skip, options):
    """ Ensures that the __init__ method gets documented. """
    if name == "__init__":
        return False
    return skip


def setup(app):
    """ Setup function for autodoc """
    # Adding the skip function
    app.connect("autodoc-skip-member", skip)


# Suppressing the warning 'duplicate label'
suppress_warnings = ['autosectionlabel.*']

# See: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autodoc_member_order
autodoc_member_order = 'groupwise'

# Sets the Type Checking flag to import even more types
set_type_checking_flag = True
