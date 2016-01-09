#! /usr/bin/env python
#coding=utf-8
import socket,sys
reload(sys)
sys.setdefaultencoding('utf-8')

host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)

print "主机:".encode('gbk'),host_name,"\tip:",ip