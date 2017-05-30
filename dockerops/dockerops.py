def run(arturl, user, password):

	import os, sys
	import subprocess
	import requests
	import json
	from os.path import expanduser

	url = arturl + "artifactory"
	tagged = url+":QA"

	subprocess.call(["docker ", "login ",  url])
	subprocess.call(["docker ", "pull ",  "busybox"])
	subprocess.call(["docker ", "tag ", "busybox ", tagged])
	subprocess.call(["docker ", "push ", tagged])


	#search
	r=requests.get(url+"/v1/search?q=QA", auth=(user, password))
	print (r.content)

	#cleanup
	subprocess.call(["docker ", " rmi ", tagged ])
	subprocess.call(["docker ", "rmi ", "busybox"])