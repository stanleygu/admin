import sys
import os
import bioservices
import templating as t

VERSION = 20140916 # Version of BioModels used
DIR_REPOS = '../repos'

def mkdirp(path):
    if not os.path.exists(path):
        os.makedirs(path)

mkdirp(DIR_REPOS)

s = bioservices.BioModels()

ids = ['BIOMD0000000051']

for id in ids:
    sbml = s.getModelSBMLById(id)
    mkdirp(os.path.join(DIR_REPOS, id, 'src'))
    
    setup_params = {
        'name': id,
        'version': VERSION,
        'description': '%s from BioModels' % id,
        'url': 'http://www.ebi.ac.uk/biomodels-main/%s' % id
    }
    
    model_params = {
        'path': '%s.xml' % id
    }
    
    init_params = {}
    
    with open(os.path.join(DIR_REPOS, id, 'setup.py'), 'w') as f:
        f.write(t.setuppy_template(setup_params))
        
    with open(os.path.join(DIR_REPOS, id, 'src/model.py'), 'w') as f:
        f.write(t.modelpy_template(model_params))
    with open(os.path.join(DIR_REPOS, id, 'src', id + '.xml'), 'w') as f:
        f.write(sbml.encode('utf-8'))
    with open(os.path.join(DIR_REPOS, id, '__init__.py'), 'w') as f:
        f.write(t.initpy_template(init_params))        
