#!/usr/bin/python
#-*- coding:cp936 -*-
import os
from sys import argv
script, FileName = argv
print '���ǽ������ļ�:%s' % FileName
fileSource = open(FileName,'a')
print '�����������'
line_1 = raw_input('��һ�У�')
line_2 = raw_input('�ڶ��У�')
line_3 = raw_input('�����У�')
fileSource.write(line_1)
fileSource.write('\n')
fileSource.write(line_2)
fileSource.write('\n')
fileSource.write(line_3)
fileSource.write('\n')

fileSource.close()
fileSource_2 = open(FileName,'r')
for content in fileSource_2:
    #print fileSource_2.readline()
    print content
