def FirstDeco(func):
    print '第一个装饰器'

    return func

 
@FirstDeco
def test():
    print 'asdf'

test()
