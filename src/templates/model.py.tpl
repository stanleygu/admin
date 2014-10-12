import libsbml
import os

path = os.path.dirname(os.path.realpath(__file__))
sbmlFilePath = os.path.join(path, '{{path}}')

with open(sbmlFilePath,'r') as f:
    sbmlString = f.read()

sbml = libsbml.readSBMLFromString(sbmlString)

