#! /usr/bin/env python
#coding=utf-8
import urllib
import urllib2
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BDTB:
    def __init__(self):
        self.url = "http://tieba.baidu.com/p/2884111109?see_lz=1&pn="
        self.pageIndex = 1
        self.headers = {"User-Agent":"Mozzila/4.0(compatible;MSIE 5.5;Windows NT)"}
        
        
    def getPage(self):
        while self.pageIndex <= 4:
            try:
                url = self.url + str(self.pageIndex)
                #print url
                req = urllib2.Request(url,headers = self.headers)
                resp = urllib2.urlopen(req)
                content = resp.read().encode('utf-8')
                #print content
                patterns = re.compile("(1*\d\d*\、)(\w*\s?\w*)")
                #print 'hello'
                #print patterns
                items = re.findall(patterns,content)
                #print items
                for item in items:
                    print (str(item[0])+str(item[1])).encode('cp936')
            except urllib2.URLError,e:
                if hasattr(e,'code'):
                    print e.code
                if hasattr(e,'reason'):
                    print e.reason
            finally:
                self.pageIndex += 1
        return True


bdtb = BDTB()
bdtb.getPage()
            