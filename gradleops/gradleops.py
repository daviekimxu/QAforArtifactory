def run(arturl, user, password):

	import os, sys
	import subprocess
	import requests
	import json
	from os.path import expanduser

	
	start= os.getcwd()
	os.chdir("gradle")

	subprocess.call('./gradlew')

	url = arturl + "artifactory/api/storage/"
	repo1="gradle-dev"
	repo2="gradle-release"
	prop="?properties=QA=TEST&recursive=1"

	r=requests.put(url+repo1+prop, auth=(user, password))
	r=requests.put(url+repo2+prop, auth=(user, password))

	searchapi= "artifactory/api/search/prop?QA=TEST"
	r=requests.get(arturl+searchapi, auth=(user,password))
	print (r.content)

	home = os.path.expanduser("~")
	os.chdir(home+'/.m2')
	subprocess.call(["rm", "-rf", "caches"], shell=True)
	subprocess.call("mkdir caches")

	os.chdir(start)