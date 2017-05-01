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

os.system(docker login -u user -p password arturl)
os.system(docker tag busybox http://104.199.127.225:12002/QAbusybox). #need cleaner solution for this
os.system(docker push http://104.199.127.225:12002/QAbusybox)

time.sleep(3)

exit()

