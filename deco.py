def FirstDeco(func):
    print '��һ��װ����'

    return func

 
@FirstDeco
def test():
    print 'asdf'

test()
