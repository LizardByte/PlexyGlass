# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# standard imports
from datetime import datetime
import os
import shutil
import sys

try:
    import pathlib2 as pathlib
except ImportError:
    import pathlib


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

script_dir = os.path.dirname(os.path.abspath(__file__))  # the directory of this file
source_dir = os.path.dirname(script_dir)  # the source folder directory
root_dir = os.path.dirname(source_dir)  # the root folder directory

# destination for copies of services
service_destination_directory = os.path.join(source_dir, 'build', 'service_modules')
service_destination_path = pathlib.Path(service_destination_directory)
service_destination_path.mkdir(parents=True, exist_ok=True)


paths = [
    os.path.join(root_dir, 'Contents', 'Libraries', 'Shared'),  # location of plugin dependencies
    os.path.join(root_dir, 'Contents'),  # location of "Code" module, aka the Plugin
    service_destination_directory,  # location of copied service files
]

# Copy ServiceCode files to python modules
services_dir = os.path.join(root_dir, 'Contents', 'Services')

services = dict(
    URL=[
        'YouTube'
    ]
)

for service_type in services:
    for service in services[service_type]:
        service_file = os.path.join(services_dir, service_type, service, 'ServiceCode.pys')
        print(service_file)

        if os.path.isfile(service_file):
            shutil.copy(service_file, os.path.join(service_destination_directory, '%s.py' % service))

for directory in paths:
    sys.path.insert(0, directory)

# -- Project information -----------------------------------------------------
project = 'PlexyGlass'
project_copyright = '%s, %s' % (datetime.now().year, project)
epub_copyright = project_copyright
author = 'ReenigneArcher'

# The full version, including alpha/beta/rc tags
# https://docs.readthedocs.io/en/stable/reference/environment-variables.html#envvar-READTHEDOCS_VERSION
version = os.getenv('READTHEDOCS_VERSION', 'dirty')


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'm2r2',  # enable markdown files
    'numpydoc',  # this automatically loads `sphinx.ext.autosummary` as well
    'sphinx.ext.autodoc',  # autodocument modules
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',  # enable to-do sections
    'sphinx.ext.viewcode'  # add links to view source code
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['toc.rst']

# Extensions to include.
source_suffix = ['.rst', '.md']

# Change default contents file
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# images
html_favicon = os.path.join(root_dir, 'Contents', 'Resources', 'favicon.ico')
html_logo = os.path.join(root_dir, 'Contents', 'Resources', 'attribution.png')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
# html_css_files = [
#     'css/custom.css',
# ]
# html_js_files = [
#     'js/custom.js',
# ]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'analytics_id': 'G-SSW90X5YZX',  # Provided by Google in your dashboard
    'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': 'blob',
    'style_nav_header_background': '#151515',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# extension config options
autodoc_preserve_defaults = True  # Do not evaluate default arguments of functions
autosectionlabel_prefix_document = True  # Make sure the target is unique
todo_include_todos = True

# numpydoc config
numpydoc_validation_checks = {'all', 'SA01'}  # Report warnings for all checks *except* for SA01

# disable epub mimetype warnings
# https://github.com/readthedocs/readthedocs.org/blob/eadf6ac6dc6abc760a91e1cb147cc3c5f37d1ea8/docs/conf.py#L235-L236
suppress_warnings = ["epub.unknown_project_files"]
