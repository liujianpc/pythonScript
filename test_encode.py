#! /usr/bin/env python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
myFile = open('Encode.txt','a')
myFile.write('去你大爷的编码')
myFile.close()

print sys.getdefaultencoding()