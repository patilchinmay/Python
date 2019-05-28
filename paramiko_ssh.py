#!/usr/bin/python

import sys, paramiko
import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

# if len(sys.argv) < 4:
#     print "args missing"
#     sys.exit(1)

hostname = "x.x.x.x"
password = "#####"
command = "which python"

username = "XXX"
port = 22

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    client.connect(hostname=hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)
    print stdout.read(),

finally:
    client.close()