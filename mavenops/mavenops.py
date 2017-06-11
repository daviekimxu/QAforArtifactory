def run(arturl, user, password):

	import os, sys
	import subprocess
	import requests
	import json
	from os.path import expanduser

	class cd:  #basic context manager
	"""Context manager for changing the current working directory"""
	def __init__(self, newPath):
		self.newPath = os.path.expanduser(newPath)

	def __enter__(self):
		self.savedPath = os.getcwd()
		os.chdir(self.newPath)

	def __exit__(self, etype, value, traceback):
		os.chdir(self.savedPath)
	
	start= os.getcwd()
	os.chdir("maven")
	
	process = subprocess.call('mvn install',shell=True)
	process = subprocess.call('mvn deploy',shell=True)


	url = arturl + "artifactory/api/storage/"
	repo1="mvn-local-SNAPSHOT"
	repo2="mvn-local-RELEASE"
	prop="?properties=QA=TEST&recursive=1"

	r=requests.put(url+repo1+prop, auth=(user, password))
	r=requests.put(url+repo2+prop, auth=(user, password))
	
	reindexurl = arturl+"artifactory/api/maven?repos="
	reindexforce="&force=1"
	requests.post(reindexurl+repo1+reindexforce, auth=(user, password))
	requests.post(reindexurl+repo2+reindexforce, auth=(user, password))

	recalculateurl=arturl+"artifactory/api/maven/calculateMetadata/"
	requests.post(recalculateurl+repo1, auth=(user, password))
	requests.post(recalculateurl+repo2, auth=(user, password))


	searchapi= "artifactory/api/search/prop?QA=TEST"
	r=requests.get(arturl+searchapi, auth=(user,password))
	print (r.content)


	home = os.path.expanduser("~")
	m2dir = os.chdir(home+'/.m2')
	subprocess.call(["rm -rf repository"], shell=True)
	#cd .m2/repository
	 #cd rm -r *
	with cd (m2dir):
		subprocess.call(["rm ","-r ", "*"])




