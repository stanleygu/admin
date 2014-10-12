import libsbml

with open('{{path}}','r') as f:
    sbmlString = f.read()

sbml = libsbml.readSBMLFromString(sbmlString)

