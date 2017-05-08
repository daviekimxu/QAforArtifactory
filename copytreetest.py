import shutil
from contextlib import contextmanager
import os

class cd:  #basic context manager
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


samples ={
	'maven' : 'maven'
	#
	#
	#
	#
}

for k, v in samples.items():
	with cd('Samples'):
		shutil.copytree('maven','../maven')