class shortException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    s = raw_input('请输入：')
    if len(s) < 3:
        raise shortException(len(s),3)
except EOFError:
    print 'it is a eof error'
except shortException,x:
    print '长度',x.length
    print '最小长度',x.atleast
else:
    print 'no error'
        
