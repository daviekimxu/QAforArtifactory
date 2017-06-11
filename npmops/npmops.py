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
	os.chdir("npmops")

	subprocess.call(npm install)
	subprocess.call(npm publish)
	
	url = arturl + "artifactory/api/storage/"
	repo1="mvn-local-SNAPSHOT"
	repo2="mvn-local-RELEASE"
	prop="?properties=QA=TEST&recursive=1"

	r=requests.put(url+repo1+prop, auth=(user, password))
	r=requests.put(url+repo2+prop, auth=(user, password))

	#npm reindex
	indexturl=arturl+"artifactory/api/npm"
	#POST /api/npm/{repoKey}/reindex
	reindex=requests.post(indexturl+repo1+"/reindex", auth=(user,password)) 
	reindex=requests.post(indexturl+repo2+"/reindex", auth=(user,password)) 

	#npmsearch [QA] [arturl+"artifactory/"+ repo1]. This is broken, use default search
	#subprocess.call(["npm search ", "QA ", arturl+"artifactory/"+repo1])
	#subprocess.call(["npm search ", "QA ", arturl+"artifactory/"+repo1])

	with cd("/usr/local/lib/node_modules"):
		subprocess.call(["rm ", "-r ", "*"])

	
