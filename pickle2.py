import cPickle as p
li = ['a','b','c']
f = open('t.txt','w')
p.dump(li,f)
f.close()
f1 = open('t.txt')
s = p.load(f1)
print s
f1.close()
