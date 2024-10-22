# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'pyeznosql'
copyright = '2024, z/OS VSAM RLS'
author = 'z/OS VSAM RLS'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []

# List of modules to be mocked during the build process
autodoc_mock_imports = ["c_ext"]
add_module_names = False
autodoc_class_signature = "separated"
autodoc_member_order = 'bysource'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Autodoc settings
# autodoc_default_options = {
#     "members": True,
#     "special-members": True,
# }


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
html_baseurl = 'https://ibm.github.io/eznosql/pydocs/'
html_static_path = ['_static']
