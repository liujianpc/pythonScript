#filename:file.py
poem = '''\
������ɽ�����ƺ��뺣����
����ǧ��Ŀ������һ��¥��'''
f = file('D:\\dd.txt','w')
f.write(poem)
f.close()
f1 = file('d:\\dd.txt','r')
while 1:
    line = f1.readline()
    if len(line) == 0:
        break
    print line
