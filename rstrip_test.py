f = open('test.txt','r')
for line in f:
    #print line.rstrip() #ȥ���ұߵ��ַ���Ĭ��ɾ��ĩβ�Ŀո���print line��������ģ�print line�ǻ��Ӧ����һ�еĿ��е�
    print line.strip()#��rstrip()���ƣ����ܸ�ǿ����ͬʱȥ����ߺ��ұߵ��ַ�
    #print line.lstri()#ȥ����ߵ��ַ�

f.close()
