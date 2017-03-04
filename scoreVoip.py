import subprocess
import sys

teamExten = sys.argv[1] + "99"
sipcmdString = "l1;c" + teamExten + ";d1234;h"

gateway = "10.0.2.99"
username = sys.argv[2]
password = sys.argv[3]

output = subprocess.Popen(["sipcmd", "-P" "sip", "-u",username, "-c", password, "-w", gateway, "-x", sipcmdString], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#output = subprocess.Popen(["./sipcmd"])

out = output.communicate()

#print("************* OUTPUT *****************")
for line in out:
	if line.find("Problem running command sequence") != -1:
		#print "Error"
		print("fail")
		quit()

print("pass")
