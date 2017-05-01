import os
import time
import configparser

config=configparser.ConfigParser()
config.sessions()
#import requests
#import urllib2?

arturl=""
user=""
password=""

config.read(properties.ini)
if "Artifactory" in config:
	arturl=["Artifactory"],["artifactoryurl"]
	user=["Artifactory"],["user"]
	password=["Artifactory"],["password"]

else:
	exit()

os.chdir(..)
os.chdir(~/MavenQA)
	
os.system(mvn -install)
os.system(mvn -Durl=<url-of-the-repository-to-deploy>) #syntax needed
time.sleep()3

#assign properties to make our lives easier...how much of the path do we need?
os.system(curl -u user:password -XPUT arturl/mvn-local-SNAPSHOT/org/api/?properties=QA=TEST&recursive=1)

#index and recalculate metadata
os.system(curl -u user:password -XPOST arturl/api/maven?repos=mvn-local-SNAPSHOT, mvn-local-RELEASE&force=1)
os.system(curl -u user:password -XPOST arturl/api/maven/calculateMetadata/mvn-local-SNAPSHOT/org)
os.system(curl -u user:password -XPOST arturl/api/maven/calculateMetadata/mvn-local-RELEASE/org)

#exit()




