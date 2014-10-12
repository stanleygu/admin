'''
Functions for templating of repo content files
'''

from jinja2 import Template

def read_file(path):
    with open(path,'r') as f:
        output = f.read()
    return output
    
def setuppy_template(params):
    s = read_file('templates/setup.py.tpl')
    template = Template(s)
    return template.render(params)
    
def modelpy_template(params):
    s = read_file('templates/model.py.tpl')
    template = Template(s)
    return template.render(params)

def initpy_template(params):
    s = read_file('templates/__init__.py.tpl')
    template = Template(s)
    return template.render(params)