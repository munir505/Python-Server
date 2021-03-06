#!/usr/bin/python
import shutil
import os
import signal
import subprocess

home_path = os.getenv("HOME")
PID_val = 0
pid_val = 0

try:
	read_file = open(home_path + "/PID", "r")
	PID_val = read_file.read().strip()
	pid_int = int(PID_val)
	print(PID_val)
except IOError as error:
	print("1")

try:
	os.kill(pid_int, signal.SIGTERM)
except:
	print("3")

try:
	shutil.rmtree(home_path + "/install")
except:
	print("4")


os.mkdir(home_path + "/install")

shutil.copy2("/var/lib/jenkins/workspace/Python-Script/app.py", home_path + "/install")
shutil.copytree("/var/lib/jenkins/workspace/Python-Script/public", home_path + "/install/public")

os.system("chmod +x " + home_path + "/install/app.py")
#os.system(home_path + "/install/app.py &")
proc = subprocess.Popen(home_path + "/install/app.py")
print(proc.pid)
os.system("disown")
