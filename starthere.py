import os, sys
import subprocess
import requests
from shutil import copyfile #to move settings.xml
import time



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

if subprocess.call('pip')=="-bash: pip: command not found":
	subprocess.call('apt-get update')
	subprocess.call('apt-get install python-pip', shell=True)
	subprocess.call('easy_install pip', shell=True)
else:
	subprocess.call('pip install requests', shell=True)
	subprocess.call('pip install configparser', shell=True)

import requests
import configparser
config=configparser.ConfigParser()
config.sections()
#Set up reverse proxy for Docker.  Consult Arturo

#check if package managers/software are installed.  If not, install them.
#maven
if subprocess.call("mvn -version", shell=True) =="'mvn' not recognized as an internal or external command":
	subprocess.call("apt-get update")
	subprocess.call("apt-get install maven", shell=True)
	
else: #is this a good condition
	shutil.copyfile("settings.xml", "/usr/share/maven3/conf/settings.xml")

#repeat for NPM
"""if subprocess.call(npm install) == "npm:command not found":
	subprocess.call("./nvminstall.sh")
  	

 else
	shutil.copyfile(".npmrc, ~/.npmrc")
"""

"""#repeat for gradle"""


"""repeat"""


#create repositories via RESTAPI
#dictionary for repos.  Moved to setup, as these need to be created once
reponame={
	'mvn-local-RELEASE':'mvn-local-RELEASE',
	'mvn-local-SNAPSHOT':'mvn-local-SNAPSHOT', 
	"jcenter":"jcenter",
	
	#'docker' : 'docker-local'
	#'dockerhub' : 'dockerhub'

	}
with cd("./ArtRepoJsons"):
	put="artifactory/api/repositories/"
	url=arturl+put

	for k, v in reponame.items():
		
		filepath=v+'.json'
		with open(filepath) as fh:
			mydata=fh.read() 
		    requests.put(
		    	url+v, 
				auth=(user, password), 
				headers={"Content-type": "application/json"}, 
				params={'file':filepath}
				)


while True:
	if input():
		break
		#delete repos
		#for k, v in reponame.items():
		#	requests.delete(artul+'artifactory/'+v,
		#	auth=(user:password)
		#	)

	else:
		subprocess.call("./operations.py")
		time.sleep(10)

    