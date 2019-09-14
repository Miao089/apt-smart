# Automated, robust apt-get mirror selection for Debian and Ubuntu.
#
# Author: martin68 and Peter Odding
# Last Change: June 22, 2018
# URL: https://apt-smart.readthedocs.io

"""Sphinx documentation configuration for the `apt-smart` package."""

import os
import sys

# Add the 'apt-smart' source distribution's root directory to the module path.
sys.path.insert(0, os.path.abspath(os.pardir))

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'humanfriendly.sphinx',
]

# Sort members by the source order instead of alphabetically.
autodoc_member_order = 'bysource'

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'apt-smart'
copyright = '2019 martin68, 2018 Peter Odding'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from apt_smart import __version__ as updater_version  # noqa

# The short X.Y version.
version = '.'.join(updater_version.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = updater_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = dict(
    python2=('https://docs.python.org/2', None),
    python3=('https://docs.python.org/3', None),
    executor=('https://executor.readthedocs.io/en/latest/', None),
    propertymanager=('https://property-manager.readthedocs.io/en/latest/', None),
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'

# Output file base name for HTML help builder.
htmlhelp_basename = 'aptmirrorupdaterdoc'
