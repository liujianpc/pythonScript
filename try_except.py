x = '12345'

def getIndexChar(obj,index):
    try:
        print obj[index]
    except:
        print 'wrong!'
    else:
        print "no error"
        
getIndexChar(x,1)
