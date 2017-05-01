This is a series of scripts to simulate regular pull, deploy, search, index, and delete operations on artifactory. 
This script is designed to be expanded via addition of package-manager specific operation scripts in the RepoScripts Directory

requirements:
docker
artifactory
Java
python
Groovy

Artifactory URL username, password, and github project urls can be set in properties.ini

To run this script, execute setup.py
-setup.py will confirm package manager installs, and will install them if not found.  
-setup.py will them loop and perform operations.py until manual keystroke is detected
-operations.py will set up local directories and artifactory repositories, run all scripts in RepoScript directory, and perform cleanup

Reposcript contains scripts for each technology.  Each script will:
-use artifactory as remote repository proxy
-deploy/publish builds, modules and artifacts to artifactory
-tag the uploads with a property
-Reindex

