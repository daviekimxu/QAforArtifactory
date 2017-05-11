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
	user=config.get("Artifactory","user")
	password=config.get("Artifactory","password")

else:
	exit()



os.chdir("./maven")

print(os.getcwd())	

home = expanduser("~")
os.chdir(home)
print(os.getcwd())
#process = subprocess.Popen('mvn install',shell=True)
