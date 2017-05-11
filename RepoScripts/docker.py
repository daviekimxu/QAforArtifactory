import os
import configparser
import time

config=configparser.ConfigParser()
config.sessions()

arturl=""
user=""
password=""

config.read("properties.ini")

if "Artifactory" in config:
	arturl=["Artifactory"],[""]
	user=["Artifactory"],["user"]

subprocess.call("docker login -u user -p password arturl")
subprocess.call("docker tag busybox http://104.199.127.225:12002/artifactory:QAbusybox"). #need cleaner solution for this
subprocess.call("docker push http://104.199.127.225:12002/artifactory:QAbusybox")

subprocess.call("docker search http://104.199.127.225:12002/artifactory:QAbusybox") 

exit()

