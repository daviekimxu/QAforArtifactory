import requests
import json
import sys
import os
import configparser
config=configparser.ConfigParser()
config.sections()

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

config.read("properties.ini")
if "Artifactory" in config:
	arturl=config.get("Artifactory","artifactoryurl")
	user= config.get("Artifactory","user")
	password=config.get("Artifactory","password")

else:
	exit()

#create repositories via RESTAPI
#dictionary for repos.  Moved to setup, as these need to be created once
reponame={
	'mvn-local-RELEASE':'/mvn-local-RELEASE.json',
	'mvn-local-SNAPSHOT':'/mvn-local-SNAPSHOT.json', 
	"jcenter":"/jcenter.json",
	
	#'docker' : 'docker-local.json'
	#'dockerhub' : 'dockerhub.json'

	}
with cd ("./ArtRepoJsons"):
	url=arturl+"artifactory/api/repositories/"

	for k, v in reponame.items():
		
		filepath=os.getcwd()+v
		
		print(filepath)
		with open(filepath) as data_file:
			mydata= json.dumps(json.load(data_file))
			print(mydata)

			
			response=requests.put(url+k, auth=(user, password), headers={"Content-type":"application/json"}, data=mydata)