from _create import create
from _remove import remove
from _shell import shell
import os

VERSION = 20140916 # Version of BioModels used
DIR_REPOS = os.path.abspath(
                os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             '../repos'
                )
            )

ids = ['BIOMD0000000051']

for id in ids:
    remove(DIR_REPOS)
    create(id, DIR_REPOS, VERSION)
    shell(cmd='git status', dir=os.path.join(DIR_REPOS, id))