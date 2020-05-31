#!/usr/bin/python
import sys
from subprocess import Popen, PIPE
host = sys.argv[1]
	
process = Popen(['ping', '-i', '0.01', str(host), '-W', '0', '-D', '-n'], stdout=PIPE)	
prev = 0
prev_time = 0
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:1
        break
    if output and not output.startswith('PING'):
 #	a = output.strip()
	a = output
	print a
	a = a.split() 
	next_ = int(a[5][9:])
        next_time = float(a[0][1:-1])
        if next_ - prev > 1:
            print next_time - prev_time
 	    process.kill()      
	    exit(2)
        prev = next_
        prev_time = next_time
print "check"


