import collections
import jinja2
import os
import shutil


LabelURL = collections.namedtuple('LabelURL', 'label url')
PROJECTS = (
    LabelURL('Documentation', 'rpy2_doc.html'),
    LabelURL('Docker', 'https://github.com/rpy2/rpy2-docker'),
    LabelURL('MyBinder', 'https://github.com/rpy2/rpy2-mybinder'),
    LabelURL('R6', 'https://github.com/rpy2/rpy2-R6'),
    LabelURL('Matrix', 'https://github.com/rpy2/rpy2-Matrix')
)
DOC_PARAMS = (
    ('rpy2_doc.html', 'rpy2',
     (
         LabelURL('dev', 'doc/latest/html/index.html'),
         LabelURL('3.3.x', 'doc/v3.3.x/html/index.html'),
         LabelURL('3.2.x', 'doc/v3.2.x/html/index.html'),
         LabelURL('3.1.x', 'doc/v3.1.x/html/index.html'),
         LabelURL('3.0.x', 'doc/v3.0.x/html/index.html'),
         LabelURL('2.9.x', 'doc/v2.9.x/html/index.html')
     )
    ),
    ('r6_doc.html', 'rpy2-R6', (LabelURL('dev', '#'),)
    )
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
template = env.get_template('index.html')
render = template.render(projects=PROJECTS)
with open(os.path.join('docs', 'index.html'), 'w') as fh:
    fh.write(render)


# render documentation pages
template = env.get_template('doc.html')
for output, page_title, lst_versions in DOC_PARAMS:
    render = template.render(page_title=page_title,
                             project=page_title,
                             doc_versions=lst_versions,
                             projects=PROJECTS)
    with open(os.path.join('docs', output), 'w') as fh:
        fh.write(render)
