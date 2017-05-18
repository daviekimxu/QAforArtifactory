import os, sys
import time
import subprocess
import shutil
import requests
import json
import mavenops


class cd:  #basic context manager
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


arturl=""
user=""
password=""
mavenurl=""
npmurl=""

def run(a, b, c, d, e,):



samples={
	'maven' : 'maven'
	#
	#
	#
	#
}

for k, v in samples.items():
	with cd ('Samples'):
		shutil.copytree(k,'../' +v) #


reposcripts={
	'maven' :'Maven.py'
#	'npm' : 'npm.py'
#	'docker' : 'docker.py'		
}

with cd('./RepoScripts'):
	for k, v in reposcripts.items():
		subprocess.Popen('python ' + v, shell= True)

#Delete artifacts via AQL search of repositories
subprocess.call("groovy cleanup.groovy")


#clean local directory
subprocess.call("rm -Rf maven NPM")
subprocess.call("docker -rm busybox")



