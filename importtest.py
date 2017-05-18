
import subprocess

#operations.run("http://104.199.127.225:12002//", "admin", "password")

samples={
    	'maven' : 'maven'
    	}

for k, v in samples.items(): 
	subprocess.call(['rm', '-rf', v])