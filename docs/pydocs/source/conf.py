# Configuration file for the Sphinx documentation builder.
import os
import sys

# Point at the Python package directory so autodoc can import pyeznosql
sys.path.insert(0, os.path.abspath('../..'))

# Mock the C extension which cannot be compiled outside z/OS
autodoc_mock_imports = ['c_ext']

project = 'pyeznosql'
copyright = '2024, z/OS VSAM RLS'
author = 'z/OS VSAM RLS'
release = '1.1.3'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = []

autodoc_member_order = 'bysource'
