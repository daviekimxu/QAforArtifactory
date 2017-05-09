import requests
import json
import os

user='admin'
password='password'
arturl="http://104.199.127.225:12002/"

url=arturl+"artifactory/api/repositories/"

filepath=os.getcwd()+ '/jcenter.json'

#with open(filepath) as fh: #this works and returns the json contents
#	mydata=fh.read()
#print(mydata)

with open(filepath) as data_file:    
    mydata = json.dumps(json.load(data_file))

print (mydata)


headers = {
    'content-type': "application/json",
    }

response=requests.put(url+'jcenter', auth=(user, password), data=mydata, headers=headers)

print(response.text)


"""requests.put(url+'jcenter',
	auth=(user, password),
	data= mydata,
	headers={"Content-type":"application/json"},
	params={'pos':2})"""


#curl -iuadmin:password -XPUT --data @/Users/davidx/documents/scripting/ArtRepoJsons/jcenter.json "http://104.199.127.225:12002/artifactory/api/repositories/jcenter?pos=2" -H "content-type:application/json"