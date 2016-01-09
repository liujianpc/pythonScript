#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import urllib
import urllib2
import re
import cPickle as P
reload(sys)
sys.setdefaultencoding('utf-8')

myFile = file("qiubai.txt","wb+")
#myFile = file("qiubai.txt","a")
page = 1
count = 0
temp = ''
url = "http://www.qiushibaike.com/hot/page/"+str(page)
headers = {"User-Agent":"Mozzila/4.0(compatible;MSIE 5.5;Windows NT)"}
try:
	req = urllib2.Request(url,headers=headers)
	resp = urllib2.urlopen(req)
	content = resp.read().encode('cp936')
	patterns = re.compile('<div.*?class="author.*".*?>\n<a.*?>\n<(.*?)>\n</a>\n.*\n<h2>(.*)</h2>\n.*\n.*\n{3}<div.*>\n{2}(.*)\n.*\n{2}.*\n{4}.*')
	items = re.findall(patterns,content)
	#print 'hello'
	for item in items:
		count = count + 1
		temp += '('+str(count)+')'+str(item[1])+'\n'+str(item[2])+'\n'+'\n'
		
		#print temp
	print temp
		
	P.dump(temp,myFile)
except urllib2.URLError,e:
	if hasattr(e,'code'):
		print e.code
	if hasattr(e,'reason'):
		print e.reason
		
finally:
	myFile.close()
	myFile = open('qiubai.txt','rb')
	#for i in myFile.readlines():
	#	print i
	content = P.load(myFile)
	print content
	myFile.close()
	
