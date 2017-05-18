"""from operations import operations

operations.run("http://104.199.127.225:12002//", "admin", "password")"""

import subprocess
import os

print(os.getcwd())

subprocess.Popen('/usr/bin/env groovy cleanup.groovy')