import configparser
config=configparser.ConfigParser()
config.sections()

arturl=""
user=""
password=""
mavenurl=""
npmurl=""

config.read("properties.ini")
if "Artifactory" in config:
	arturl=config.get("Artifactory","artifactoryurl")
	user=["Artifactory"],["user"]
	#password=["Artifactory"],["password"]

else:
	exit()

print(arturl + "artifactory/api/repositories/")