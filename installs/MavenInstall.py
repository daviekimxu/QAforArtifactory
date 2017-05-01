import os

mvnstat = str(os.system(mvn -v))

if mvnstat = "'mvn' not recognized as an internal or external command’"
	os.system(sudo apt-get update)
	os.system(sudo apt-get install mvn)

else
	os.system(cp /resources/settings.xml| /usr/share/maven3/conf/settings.xml)