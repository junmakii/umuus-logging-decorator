
project = 'umuus-logging-decorator'
copyright = ', Jun Makii'
author = 'Jun Makii'
version = '0.1'
release = '0.1'
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = None
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'umuus_logging_decoratordoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'A.tex', 'umuus-logging-decorator Documentation',
     'umuus-logging-decorator', 'manual'),
]
man_pages = [
    (master_doc, 'umuus_logging_decorator', 'umuus-logging-decorator Documentation', [author], 1)
]
texinfo_documents = [
    (master_doc, 'umuus-logging-decorator', 'umuus-logging-decorator Documentation',
     author, 'umuus_logging_decorator', 'One line description of project.',
     'Miscellaneous'),
]
epub_title = project
epub_exclude_files = ['search.html']