from _create import create
from _remove import remove
from _shell import shell
import os
import bioservices

VERSION = 20140916 # Version of BioModels used
DIR_REPOS = os.path.abspath(
                os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             '../repos'
                )
            )

s = bioservices.BioModels()

ids = s.getAllModelsId() 
# ids = ['BIOMD0000000051']
# all = s.getAllModelsId()
# curated = s.getAllCuratedModelsId()
# noncurated = s.getAllNonCuratedModelsId()

for id in ids:
    remove(DIR_REPOS)
    create(id, DIR_REPOS, VERSION)
    shell(cmd='hub create biomodels/%s' % id, dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git init', dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git add .', dir=os.path.join(DIR_REPOS, id))
    shell(cmd=['git', 'commit', '-m', 'Initial Commit'], dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git remote add origin git@github.com:biomodels/%s.git' % id, dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git push -u -f origin master', dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git tag %s' % VERSION, dir=os.path.join(DIR_REPOS, id))
    shell(cmd='git push --tags', dir=os.path.join(DIR_REPOS, id))
    
    