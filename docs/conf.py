extensions = ['sphinx.ext.graphviz']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Administrative Initiative Canvas'
copyright = u'2016, Chris Gough'
author = u'Chris Gough'
# TODO: set version/release by git/introspection
version = u'0.0'
release = u'0.0'

language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'AdministrativeInitiativeCanvasdoc'

# -- Options for LaTeX output ---------------------------------------------
latex_elements = {
     'papersize': 'A4',
     # The font size ('10pt', '11pt' or '12pt').
     # 'pointsize': '10pt',
}

# TODO: use variables for consistency
latex_documents = [
    (
        master_doc, 'AdministrativeInitiativeCanvas.tex',
        u'Administrative Initiative Canvas Documentation',
        u'Chris Gough', 'manual'),
]

# -- Options for manual page output ---------------------------------------
man_pages = [
    (master_doc, 'administrativeinitiativecanvas', u'Administrative Initiative Canvas Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------
texinfo_documents = [
    (master_doc, 'AdministrativeInitiativeCanvas', u'Administrative Initiative Canvas Documentation',
     author, 'AdministrativeInitiativeCanvas', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
