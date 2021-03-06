import os, sys
import subprocess
import requests
import shutil
import time
import json
from operations import operations


#get PIP.  Might be better to prepackage requests 
class cd:  #basic context manager
	"""Context manager for changing the current working directory"""
	def __init__(self, newPath):
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		self.savedPath = os.getcwd()
		os.chdir(self.newPath)

	def __exit__(self, etype, value, traceback):
		os.chdir(self.savedPath)

"""if subprocess.call('pip')=="The program 'pip' is currently not installed. To run 'pip' please ask your administrator to install the package 'python-pip'":
	subprocess.call('apt-get update')
	subprocess.call('apt-get install python-pip', shell=True)
	subprocess.call('easy_install pip', shell=True)
else:
	subprocess.call('pip install requests', shell=True)
	subprocess.call('pip install configparser', shell=True)
"""

import requests
import configparser
config=configparser.ConfigParser()
config.sections()
#Set up reverse proxy for Docker.  Consult Arturo

#check if package managers/software are installed.  If not, install them.

#maven#################################################################################################################################################
if subprocess.call("mvn -version", shell=True) =="'mvn' not recognized as an internal or external command":
	subprocess.call("apt-get update")
	subprocess.call("apt-get install maven", shell=True)
	
else: #need root permissions
	shutil.move("./settings.xml", "/usr/share/maven/conf/settings.xml")
	shutil.copyfile("/usr/share/maven/conf/settings.xml", "./settings.xml")


#NPM###################################################################################################################################################
#"""if subprocess.call(npm install) == "npm:command not found":
#	subprocess.call("./nvminstall.sh")
	

# else
#	shutil.copyfile(".npmrc, ~/.npmrc") #needs home = os.path.expanduser, then copyfile and move
#"""

#repeat for gradle#####################################################################################################################################


"""repeat"""
#ivy####################################################################################################################################################

#ruby###################################################################################################################################################

#rpm####################################################################################################################################################

#generic################################################################################################################################################
#download file with requests.get




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
	"mvn-virtual-SNAPSHOT":"/mvn-virtual-SNAPSHOT.json",
	"mvn-virtual-RELEASE" : "/mvn-virtual-RELEASE.json"
	
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

#loop operations script
while True:
		operations.run(arturl, user, password)
		
