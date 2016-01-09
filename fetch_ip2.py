#! /usr/bin/env python
#coding=utf-8
import re
 
#将ipv3格式转为整型，比如255.255.255.0 这种类型转为整型 
def ipv3_to_int(s):
  l = [int(i) for i in s.split('.')]
  return (l[0] << 16) | (l[1] << 8) | l[2]#利用移位进行转换
 
  #将整形转化成ipv3格式
def int_to_ipv3(s):
  ip1 = s >> 16 & 0xFF
  ip2 = s >> 8 & 0xFF
  ip3 = s & 0xFF
  return "%d.%d.%d" % (ip1, ip2, ip3)
 #读取ChinaIP.csv中的内容，将其每条对应IP域转化成整型，并写入ChinaIpAddress_2.txt文件。
try:
    i = open('ChinaIP.csv', 'r')
    list = i.readlines()
    for iplist in list:
      pattern = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3})\.\d{1,3}')#此处利用了正则表达式的捕获
      ips = re.findall(pattern,iplist)
      x = ips[0]
      y = ips[1]
      for ip in range (ipv3_to_int(x),ipv3_to_int(y)):
        ipadress=str(ip)
        #ip_address = int_to_ipv3(ip)
        o = open('ChinaIPAddress_2.txt','a')
        #print "hello"
        o.writelines(ipadress)
        o.writelines('\n')
except IndexError:
    print "done!"
finally:
    o.close()
    i.close()
