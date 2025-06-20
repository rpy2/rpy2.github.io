import collections
import jinja2
import os
import references
import shutil


LabelURL = collections.namedtuple('LabelURL', 'label url')
MENU = (
    LabelURL('Documentation', 'doc.html'),
    LabelURL('Docker', 'https://github.com/rpy2/rpy2-docker'),
    LabelURL('MyBinder', 'https://github.com/rpy2/rpy2-mybinder'),
    LabelURL('Extensions', 'extensions.html'),
)
SUBPROJECTS = (
    (LabelURL('R6', 'r6_doc.html'),
     'Map the R package for Object-Oriented Programming for R of the same name.'),
    (LabelURL('Matrix', 'matrix_doc.html'),
     'Map the R package Matrix.'),
    (LabelURL('Arrow', 'arrow_doc.html'),
     'Share Apache Arrow data structures between Python and R'),
)
DOC_PARAMS = ('doc.html', 'Documentation',
     LabelURL('rpy2', 'https://github.com/rpy2/rpy2'),
     (
         LabelURL('dev', 'doc/latest/html/index.html'),
         LabelURL('3.6.x', 'doc/v3.6.x/html/index.html'),
         LabelURL('3.5.x', 'doc/v3.5.x/html/index.html'),
         LabelURL('3.4.x', 'doc/v3.4.x/html/index.html'),
         LabelURL('3.3.x', 'doc/v3.3.x/html/index.html'),
         LabelURL('3.2.x', 'doc/v3.2.x/html/index.html'),
         LabelURL('3.1.x', 'doc/v3.1.x/html/index.html'),
         LabelURL('3.0.x', 'doc/v3.0.x/html/index.html'),
         LabelURL('2.9.x', 'doc/v2.9.x/html/index.html')
     )
    )

DOC_SUBPROJECT_PARAMS = (
    ('r6_doc.html', 'R6',
     LabelURL('rpy2-r6', 'https://github.com/rpy2/rpy2-r6'),
     (LabelURL('dev', 'https://rpy2.github.io/rpy2-r6/version/master/html/index.html'),)
    ),
    ('matrix_doc.html', 'R6',
     LabelURL('rpy2-r6', 'https://github.com/rpy2/rpy2-Matrix'),
     (LabelURL('dev', 'https://rpy2.github.io/rpy2-Matrix/version/master/html/index.html'),)
    ),
    ('arrow_doc.html', 'Arrow',
     LabelURL('rpy2-arrow', 'https://github.com/rpy2/rpy2-arrow'),
     (LabelURL('dev', 'https://rpy2.github.io/rpy2-arrow/version/main/html/index.html'),)
    ),
)

assert os.path.isdir('docs')
for d in ('css', 'images'):
    path = os.path.join('docs', d)
    if os.path.exists(path):
        shutil.rmtree(path)
    shutil.copytree(os.path.join('static', d),
                    os.path.join('docs', d))


env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

# render main page
print('Rendering index.html')
template = env.get_template('index.html')
head_scripts=("https://buttons.github.io/buttons.js", )
render = template.render(
    head_scripts=head_scripts,
    menu=MENU,
    references=references.REFERENCES
)
with open(os.path.join('docs', 'index.html'), 'w') as fh:
    fh.write(render)


# render documentation pages
print('Rendering doc.html')
template = env.get_template('doc.html')
output, active_label, project, lst_versions = DOC_PARAMS
render = template.render(page_title=project.label,
                         active_label=active_label,
                         project=project.label,
                         project_url=project.url,
                         doc_versions=lst_versions,
                         menu=MENU)
with open(os.path.join('docs', output), 'w') as fh:
    fh.write(render)

    print('Rendering doc_subproject.html')
template = env.get_template('doc_subproject.html')
for output, active_label, project, lst_versions in DOC_SUBPROJECT_PARAMS:
    render = template.render(page_title=project.label,
                             active_label=active_label,
                             project=project.label,
                             project_url=project.url,
                             doc_versions=lst_versions,
                             menu=MENU)
    with open(os.path.join('docs', output), 'w') as fh:
        fh.write(render)

# render extensions
template = env.get_template('extensions.html')
render = template.render(menu=MENU, projects=SUBPROJECTS)
with open(os.path.join('docs', 'extensions.html'), 'w') as fh:
    fh.write(render)

# render use-cases
print('Rendering use-cases.html')
template = env.get_template('use-cases.html')
render = template.render(menu=MENU,
                         references=references.REFERENCES)
with open(os.path.join('docs', 'use-cases.html'), 'w') as fh:
    fh.write(render)
