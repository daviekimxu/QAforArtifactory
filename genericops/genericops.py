def run(arturl. user, password):
	
	import os, sys
	import subprocess
	import requests
	import json
	from os.path import expanduser


	repo1="base"
	filename="generic.jar"
	url=arturl+"artifactory/base/generic.jar"

	os.call(["curl","-iuadmin:password", "-T", "generic.jar", url] )

	url = arturl + "artifactory/api/storage/"
	prop="?properties=QA=TEST&recursive=1"

	r=requests.put(url+repo1+prop, auth=(user, password))

	searchapi= "artifactory/api/search/prop?QA=TEST"
	r=requests.get(arturl+searchapi, auth=(user,password))
	print (r.content)