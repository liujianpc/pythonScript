#! /usr/bin/env python
#coding=utf-8
import re

#此函数将ip的前三段变为一个整形数字
def ipv3_to_int(s):
    int_list = [int(i) for i in s.split('.')]
    return (int_list[0] << 16) | (int_list[1] << 8) | int_list[2]

#此函数将整形数字转为ip前三段模式

def int_to_ipv3(s):
    ipv_1 = s >> 16 & 0xff
    ipv_2 = s >> 8 & 0xff
    ipv_3 = s & 0xff
    return "%d.%d.%d"%(ipv_1,ipv_2,ipv_3)

fileName = open("chinaIP.csv",'rb')

list = fileName.readlines()

for ip_list in list:
    pattern = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3})\.\d{1,3}')
    ips = re.findall(pattern,ip_list)
    start = ips[0]
    end = ips[1]
   # print "hello"
    
    for ip in xrange(ipv3_to_int(start),ipv3_to_int(end)):
        ip_addr = int_to_ipv3(ip)
        ip_addr = str(ip_addr)+"\.1-254"
        fileName_2 = open("chinaIp.txt",'a')
        fileName_2.writelines(ip_addr)
        fileName_2.writelines("\n")
    fileName_2.close()
fileName.close()
        
        