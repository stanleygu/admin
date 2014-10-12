'''
Functions for operating running shell commands
'''

from subprocess import Popen, PIPE
import os
from six import string_types


def shell(cmd='', dir=os.getcwd()):
    '''
    Execute shell commands in the directory
    '''
    if isinstance(cmd, string_types):
        cmd = cmd.split(' ')
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=dir)
    stdout, stderr = process.communicate()
    print '------------------------------'
    print 'STDOUT: %s' % stdout
    print 'STDERR: %s' % stderr
    
    return stdout, stderr
    