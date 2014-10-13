'''
Constants used by scripts and other modules
'''

import os

VERSION = 20140916 # Version of BioModels used
DIR_REPOS = os.path.abspath(
                os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             '../repos'
                )
            )
            
FILE_REPO_LIST = os.path.abspath(
                    os.path.join(
                        os.path.dirname(os.path.realpath(__file__)),
                        '../repos.pickle'
                    )
                )

FILE_BLACKLIST = os.path.abspath(
                    os.path.join(
                        os.path.dirname(os.path.realpath(__file__)),
                        '../blacklist.pickle'
                    )
                )