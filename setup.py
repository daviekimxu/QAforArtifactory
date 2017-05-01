import os
import time
import configparser
from shutil import copyfile #to move settings.xml

config=configparser.ConfigParser()
config.sessions()


class cd:  #basic context manager
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

#Set up reverse proxy for Docker.  Consult Arturo

#check if package managers/software are installed.  If not, install them.
#maven
if os.system(mvn -version) =="'mvn' not recognized as an internal or external command" = True:
	os.system(apt-get update)
	os.system(apt-get install maven)
	
else: #is this a good condition
	copyfile(settings.xml, /usr/share/maven3/conf/settings.xml ~/.m2/settings.xml)

#repeat for NPM
#npm. needs response form curl requests that need to be added to .npmrc file

"""if os.system(npm install) == "npm:command not found" = True:
	os.system(sudo apt-get update)
  	os.system(sudo apt-get install nodejs)
  	os.system(sudo apt-get install npm)

 else
#get the updated npmrc file into the npm diretory 
"""

"""#repeat for gradle"""

"""repeat for yum"""

#need a good condition to loop operations until key input
while True:
	if input():
		break

	else:
	os.system (./operations.py)
	time.sleep(10)

