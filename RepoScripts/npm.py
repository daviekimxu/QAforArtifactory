import os
import subprocess
import time
import configparser
import requests
import json

config=configparser.ConfigParser()
config.sessions()

os.chdir("..")

arturl=""
user=""
password=""

config.read("properties.ini")
if "Artifactory" in config:
	arturl=["Artifactory"],["artifactoryurl"]
	user=["Artifactory"],["user"]
	password=["Artifactory"],["password"]

else:
	exit()

os.chdir("./NPMQA")
	
subprocess.call("npm -install")
subprocess.call("npm -publish") #syntax needed

#assign properties to make our lives easier
url = arturl + "artifactory/api/storage/"
repo1="npm-local"
prop="?properties=QA=TEST&recursive=1"

r=requests.put(url+repo1+prop, auth=(user, password))

#index and recalculate metadata
reindexurl = arturl+"/api/npm/" + repo1 + "/reindex"
requests.post(reindexurl, auth=(user, password))








