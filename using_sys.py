#!/usr/bin/python
#fileName:using_system.py
import sys

print 'the comand line arguments are :'
for i in sys.argv:
    print i
    print '\n\n the pythonPATH is',sys.path,'\n'
print __name__
