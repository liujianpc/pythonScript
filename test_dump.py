import cPickle as p
list_dump = [1,2,3,4,5]

filename = 'test.liujian'
f = open(filename,'w')
p.dump(list_dump,f)
f.close()
