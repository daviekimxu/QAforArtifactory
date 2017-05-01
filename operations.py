import os
import time
import configparser
from shutil import copyfile #to move settings.xml

config=configparser.ConfigParser()
config.sessions()

#open properties file, parse for Artifactory URL
#inheritance?

arturl=""
user=""
password=""
mavenurl=""

config.read("properties.ini") 
if "Artifactory" in config:

	arturl= config["Artifactory"]["artifactoryurl"]
	user= config["Artifactory"]["admin"]	
	password=config["Artifactory"]["password"]
	
else:
	exit()

#get github
if "GitHub" in config:

		mavenurl=["GitHub"],["mavenurl"]
else:
	exit()
class cd:  #basic context manager
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

#create repositories via RESTAPI
#I need a better way to execute http/REST calls
cd(~/ArtRepoJsons)
	os.system(curl -iu user:password -T /path/artifactory/mvn-local-SNAPSHOT.json arturl/mvn-local-SNAPSHOT -H (content-type:application/json))
	os.system(curl -iu user:password -T /path/to/mvn-local-RELEASE.json arturl/mvn-local-RELEASE -H (content-type:application/json))
	os.system(curl -iu user:password -T /path/to/jcenter.json arturl/jcenter -H (content-type:application/json))

#make directories, pull test image
os.system(mkdir MavenQA, NPMQA)
cd(~/MavenQA)
	
	os.system(git clone mavenurl) #urls as variables
	time.sleep(3)# to confirm git clone success-is there another check?

copyfile(properties.ini, ~/RepoScripts/properties.ini)

#repeat for NPM etc
#os.system(docker pull arturl/dockerhub:busybox)

#Run all simulation scripts in directory

os.system(run-parts ~/RepoScripts)

#search
print(os.system(curl -iu user:password -XGET arturl/api/search/prop?QA=TEST))

#Delete artifacts via properties

os.sytem(groovy ~/cleanup.groovy)

#Delete repos/artifacts/caches.  Again, need better way to execute HTTP
os.system(curl -iu user:password -XDELETE arturl/mvn-local-SNAPSHOT)
os.system(curl -iu user:password -XDELETE arturl/mvn-local-RELEASE)
os.system(curl -iu user:password -XDELETE arturl/jcenter)

#clean local files
os.system(rm -Rf MavenQA NPMQA)
os.system(docker -rm busybox)




