import requests
import json
import os

user='user'
password='password'

arturl="http://104.199.127.225:12002/"

reponame={
	'mvn-local-RELEASE':'mvn-local-RELEASE',
	'mvn-local-SNAPSHOT':'mvn-local-SNAPSHOT', 
	"jcenter":"jcenter",
	}

url=arturl+"artifactory/api/repositories/"

for k, v in reponame.items():
		
	filepath=v+'.json'
	with open(filepath) as fh:
		mydata=fh.read() 
		requests.put(url+v,
			auth=(user, password),
			data=mydata,
			headers={"Content-type":"application/json"},
			params={'file':filepath})


curl -iuadmin:password -XPUT --data @/Users/davidx/documents/scripting/ArtRepoJsons/jcenter.json "http://104.199.127.225:12002/artifactory/api/repositories/jcenter?pos=2" -H "content-type:application/json"