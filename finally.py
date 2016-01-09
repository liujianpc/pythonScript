#exception
import time
f = file('d:\\dd.txt','r')
try:
    while 1:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line
finally:
    f.close()
    print 'close successfully'
