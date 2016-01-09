#filename:file.py
poem = '''\
白日依山尽，黄河入海流。
欲穷千里目，更上一层楼。'''
f = file('D:\\dd.txt','w')
f.write(poem)
f.close()
f1 = file('d:\\dd.txt','r')
while 1:
    line = f1.readline()
    if len(line) == 0:
        break
    print line
