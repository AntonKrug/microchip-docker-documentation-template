import os
import sys
from datetime import date
import sphinx_ops_theme


project = u'Documetation title'
copyright = date.today().strftime("%Y") + u' Microchip'
author = u'Microchip'


sys.path.insert(0, os.path.abspath('.'))

needs_sphinx = '3.3'

extensions = [
    'sphinx.ext.todo', 'sphinx_tabs.tabs', 'sphinx.ext.graphviz', 
    'myst_parser', 'sphinxcontrib.wavedrom', 'sphinx_copybutton' ]

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

html_theme = "sphinx_ops_theme"
html_theme_path = [sphinx_ops_theme.get_html_theme_path()]
html_static_path = ['_static']
html_css_files = ['myRtdOverrides.css']
html_logo = '_static/mhcp-100.png'

html_show_sphinx = False
html_show_sourcelink = False