import os
import

#check if maven is installed
mvnstat = str(os.system(mvn -v))

if mvnstat = "'mvn' not recognized as an internal or external command’"
	os.system(sudo apt-get update)
	os.system(sudo apt-get install mvn)

else
	os.system(cp /resources/settings.xml| /usr/share/maven3/conf/settings.xml)

#check for NPM

#open properties file, parse for Artifactory URL
properties = open ("properties.txt","r") 
arturl=
user=
password=
mvngiturl=



#create repositories via RESTAPI
os.system(curl -iu user:password -T /path/to/ArtRepoJsons.json arturl/mvn-local-SNAPSHOT -H (content-type:application/json))
os.system(curl -iu user:password -T /path/to/ArtRepoJsons.json arturl/mvn-local-RELEASE -H (content-type:application/json))
os.system(curl -iu user:password -T /path/to/ArtRepoJsons.json arturl/jcenter -H (content-type:application/json))

#need a good condition
while 

else
	os.system (./ path/to/operations.sh)

	os.system(curl -iu user:password -XDELETE arturl/mvn-local-SNAPSHOT)
	os.system(curl -iu user:password -XDELETE arturl/mvn-local-RELEASE)
	os.system(curl -iu user:password -XDELETE arturl/jcenter)
