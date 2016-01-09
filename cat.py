import sys
def read(filename):
    f = file(filename)
    while 1:
        line = f.readline()
        if len(line) == 0:
            break
        print line
    f.close()

if len(sys.argv) < 2:
    print 'no input'
    sys.exit()
    
if sys.argv[1].startswith('--'):
    if sys.argv[1][2:] == 'help':
        print '''\
    help
    help
    help

'''

    elif sys.argv[1][2:] == 'version':
        print 'the version is 3.0'

    else:
        print 'no arguments'
        sys.exit()


else:
    for filename in sys.argv[1:]:
        read(filename)
        
        
