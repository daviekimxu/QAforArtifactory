import os, sys
import subprocess
import time
import configparser
import requests
import json
from os.path import expanduser


config=configparser.ConfigParser()
config.sections()

os.chdir("..")

arturl=""
user=""
password=""

config.read("properties.ini")
if "Artifactory" in config:
	arturl=config.get("Artifactory","artifactoryurl")
	user= config.get("Artifactory","user")
	password=config.get("Artifactory","password")

else:
	exit()

os.chdir("maven")
	
process = subprocess.Popen('mvn install',shell=True)

#assign properties to make our lives easier
url = arturl + "artifactory/api/storage/"
repo1="mvn-local-SNAPSHOT"
repo2="mvn-local-RELEASE"
prop="?properties=QA=TEST&recursive=1"

r=requests.put(url+repo1+prop, auth=(user, password))
r=requests.put(url+repo2+prop, auth=(user, password))


#index and recalculate metadata
reindexurl = arturl+"artifactory/api/maven?repos="
reindexforce="&force=1"
requests.post(reindexurl+repo1+reindexforce, auth=(user, password))
requests.post(reindexurl+repo2+reindexforce, auth=(user, password))

recalculateurl=arturl+"artifactory/api/maven/calculateMetadata/"
requests.post(recalculateurl+repo1)
requests.post(recalculateurl+repo2)

#search by properties - additional search per native package type
searchapi= "artifactory/api/search/prop?QA=TEST"
r=requests.get(arturl+searchapi, auth=(user,password))
print (r.content)

#delete .m2/repository
home = expanduser("~")
os.chdir(home+'/.m2')
subprocess.call("rm -rf repository" shell=True)

exit()