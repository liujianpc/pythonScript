#!/usr/bin/python
#coding:cp936
#���Ӳ���
import httplib
def check_web_connect(host,port,path):#����һ����������������һ����վ������ȡ��ӦĿ¼
    h = httplib.HTTPConnection(host,port)#����һ������
    h.request('GET',path)#����·��
    response = h.getresponse()#��ȡ��������Ӧ
    print 'HTTP Response:'
    print ' status =',response.status#��������Ӧ��status
    print ' reason =',response.reason#��������Ӧ��reason
    print 'HTTP Headers:'

    for hdr in response.getheaders():
        print '     %s: %s' % hdr#��ӡheaders����
check_web_connect('www.python.org',80,'/')
#check_web_connect('www.baidu.com',80,'/')

