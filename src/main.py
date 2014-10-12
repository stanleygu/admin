import sys
import os
import bioservices
import templating as t


s = bioservices.BioModels()

model = s.getModelSBMLById('BIOMD0000000051')

params = {
    'name': 'BIOMD',
    'version': '1.0.0'
}

print model