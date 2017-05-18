

def run(arturl, user, password):
	from mavenops import mavenops
	import os, sys
	import time
	import subprocess
	import shutil
	import requests
	import json
	
	
	class cd:  #basic context manager
		def __init__(self, newPath):
			self.newPath = os.path.expanduser(newPath)

		def __enter__(self):
			self.savedPath = os.getcwd()
			os.chdir(self.newPath)

		def __exit__(self, etype, value, traceback):
			os.chdir(self.savedPath)


	
	
	samples={
    	'maven' : 'maven'
    	}

	for k, v in samples.items():
		shutil.rmtree(v)
		with cd ('Samples'):
			
			shutil.copytree(k,'../' +v) 

	mavenops.run(arturl,user, password)


	
		
	#Delete artifacts via AQL search of repositories
	#subprocess.call("/usr/bin/env","cleanup.groovy")


	#clean local directory
	subprocess.call("rm -Rf maven NPM")
	