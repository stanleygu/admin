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
    
    params = {
        'name': id,
        'version': VERSION,
        'description': '%s from BioModels' % id,
        'url': 'http://www.ebi.ac.uk/biomodels-main/%s' %s id,
        
    }

