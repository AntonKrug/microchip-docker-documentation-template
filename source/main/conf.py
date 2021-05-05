import os
import sys
from datetime import date
import sphinx_rtd_theme


project = u'Example document'
release = u'v1.0'
copyright = date.today().strftime("%Y") + u' Microchip'
author = u'Microchip'


sys.path.insert(0, os.path.abspath('.'))

needs_sphinx = '3.3'

extensions = [
    'sphinx.ext.todo', 'sphinx_tabs.tabs', 'sphinx.ext.graphviz', 
    'myst_parser', 'sphinxcontrib.wavedrom', 'sphinx_copybutton', 'sphinx_rtd_theme' ]

numfig = True
wavedrom_html_jsinline = False

autosectionlabel_prefix_document = True

sphinx_tabs_valid_builders = ['linkcheck']
templates_path = []
source_suffix = ['.md']
source_encoding = 'utf-8-sig'
master_doc = 'index'

language = None
exclude_patterns = ['Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['myRtdOverrides.css']
html_logo = '_static/mhcp-100.png'

templates_path = ['_templates']

html_show_sphinx = False
html_show_sourcelink = False