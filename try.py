import sys
try:
    s = raw_input('input something:')
except EOFError:
    print 'EOF error'
except:
    print 'it is anther error'
print 'done'
