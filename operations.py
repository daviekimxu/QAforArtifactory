import os, sys
import time
import subprocess
import configparser
import shutil
import requests
import json

config=configparser.ConfigParser()
config.sections()

#open properties file, parse for Artifactory URL
#inheritance?

arturl=""
user=""
password=""
mavenurl=""
npmurl=""

class cd:  #basic context manager
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

config.read("properties.ini") 
if "Artifactory" in config:

	arturl= config.get("Artifactory","artifactoryurl")
	user= config.get("Artifactory", "user")	
	password=config.get("Artifactory","password")
	
else:
	exit()

samples={
	'maven' : 'maven'
	#
	#
	#
	#
}

for k, v in samples.items():
	with cd ('Samples'):
		shutil.copytree(k,'../' +v)


reposcripts={
	'maven' :'Maven.py'
#	'npm' : 'npm.py'
#	'docker' : 'docker.py'		
}

with cd('./RepoScripts'):
	for k, v in reposcripts.items():
		subprocess.call('python ' + v +'.py' )

#Delete artifacts via AQL search of repositories
subprocess.call("groovy ./cleanup.groovy")


#clean local directory
subprocess.call("rm -Rf maven NPM")
subprocess.call("docker -rm busybox")

exit()


