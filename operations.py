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

	arturl= config["Artifactory"]["artifactoryurl"]
	user= config["Artifactory"]["admin"]	
	password=config["Artifactory"]["password"]
	
else:
	exit()

samples{
	'maven' : 'maven'
	#
	#
	#
	#
}

for k, v in samples.items():
	with cd ('Samples'):
		shutil.copytree(k,'../' +v)

#makedictionary local directories 
#localdirs={
#		'MavenQA': mavenurl,
#		'NPMQA': npmurl
#	}

#for k, v in localdirs.items():
#
#	subprocess.call("mkdir " + k)
#	
#	with cd('./'+k):
#		subprocess.call("git clone " +v) #need a way to clone subdirectories

#subprocess.call(docker pull arturl/dockerhub:busybox)

#Run all simulation scripts in directory NEEDS FIX with libraries

reposcripts={
	'maven' :'Maven.py'
#	'npm' : 'npm.py'
#	'docker' : 'docker.py'		
}

with cd('./RepoScripts'):
	for k, v in reposcripts.items():
		subprocess.call('python ' + v )

#subprocess.call("run-parts ./RepoScripts")

#search
"""searchapi= "artifactory/api/search/prop?QA=TEST"
r=requests.get(artul+searchapi, auth=(user:password))
print (r.content) """

#Delete artifacts via AQL search of repositories
subprocess.call("groovy ./cleanup.groovy")


#clean local directory
subprocess.call("rm -Rf Maven NPM")
subprocess.call("docker -rm busybox")




