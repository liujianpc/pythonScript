#!/usr/bin/python
#coding:cp936
#连接测试
import httplib
def check_web_connect(host,port,path):#定义一个函数，用于连接一个网站，并获取相应目录
    h = httplib.HTTPConnection(host,port)#创建一个连接
    h.request('GET',path)#请求路径
    response = h.getresponse()#获取服务器响应
    print 'HTTP Response:'
    print ' status =',response.status#服务器响应的status
    print ' reason =',response.reason#服务器响应的reason
    print 'HTTP Headers:'

    for hdr in response.getheaders():
        print '     %s: %s' % hdr#打印headers内容
check_web_connect('www.python.org',80,'/')
#check_web_connect('www.baidu.com',80,'/')

