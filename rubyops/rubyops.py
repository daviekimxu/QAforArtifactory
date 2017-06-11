def run(arturl, user, password):

	import os, sys
	import subprocess
	import requests
	import json
	from os.path import expanduser
	
	url = arturl+"artifactory"
	repo1 = "ruby-local"

	start= os.getcwd()
	os.chdir("ruby")

	#search
	subprocess.call(["curl ",url+"api/gems/"+repo1+"/api/v1/search.json?query=sample"])

	#reindex
	requests.post(url+"/api/gems/"+repo1+"/reindex", auth=(user, password))
	#curl -X POST http://localhost:8081/artifactory/api/gems/<repository key>/reindex

	#update index
	requests.post(url+"/api/gems/"+repo1+"updateIndex", auth+(user, password))
	#curl -X POST http://localhost:8081/artifactory/api/gems/<repository key>/updateIndex