class shortException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    s = raw_input('�����룺')
    if len(s) < 3:
        raise shortException(len(s),3)
except EOFError:
    print 'it is a eof error'
except shortException,x:
    print '����',x.length
    print '��С����',x.atleast
else:
    print 'no error'
        
