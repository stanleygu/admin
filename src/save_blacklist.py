'''
Create blacklisted models that were not created
'''

from _constants import FILE_BLACKLIST
import pickle

blacklist = [
    'MODEL1311110001'    
]

pickle.dump(blacklist, open(FILE_BLACKLIST, 'w'))