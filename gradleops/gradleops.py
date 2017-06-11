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
	m2dir = os.chdir(home+'/.m2')
	subprocess.call(["rm -rf repository"], shell=True)
	#cd .m2/repository
	 #cd rm -r *
	with cd (m2dir):
		subprocess.call(["rm ","-r ", "*"])