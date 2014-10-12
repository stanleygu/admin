def getSetupTemplate(params):
    from jinja2 import Template
    
    def readFile(path):
        with open(path,'r') as f:
            output = f.read()
        return output
    
    setupTemplate = readFile('templates/setup.py.tpl')
    template = Template(setupTemplate)
    return template.render(params)
