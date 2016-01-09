#!/usr/bin/python
#-*- coding:cp936 -*-
import os
from sys import argv
script, FileName = argv
print '我们将处理文件:%s' % FileName
fileSource = open(FileName,'a')
print '输入你的内容'
line_1 = raw_input('第一行：')
line_2 = raw_input('第二行：')
line_3 = raw_input('第三行：')
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
