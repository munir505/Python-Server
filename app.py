#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import os
import socket
import json

home_path = os.getenv("HOME")
PID_val = str(os.getpid())
print(PID_val)
add_pid = open(home_path + "/PID", "w")
add_pid.write(PID_val)
add_pid.close()

# create info.json
os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/public")
info = {
	"host_name": socket.gethostname(),
	"version": 1
}
with open('info.json', 'w') as outfile:
    json.dump(info, outfile)

# configure and run the server
PORT = 9000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print socket.gethostname()
httpd.serve_forever()


