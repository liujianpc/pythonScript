#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import urllib
import urllib2
import re
import cPickle as P
import os
reload(sys)
sys.setdefaultencoding('utf-8')

class QSBK:
    
    def __init__(self):
        self.url = "http://www.qiushibaike.com/hot/page/"
        self.headers =  {"User-Agent":"Mozzila/4.0(compatible;MSIE 5.5;Windows NT)"}
        self.pageIndex = 1
        
        #分析页面，并且把页面内所有段子都计数排入列表内存储
    def getPage(self):
        content_index = 0
        page_contents = []
        final_url = self.url + str(self.pageIndex)
        try:
            req = urllib2.Request(final_url,headers=self.headers)
            resp = urllib2.urlopen(req)
            content = resp.read().encode('cp936')
            patterns = re.compile('<div.*?class="author.*".*?>\n<a.*?>\n<(.*?)>\n</a>\n.*\n<h2>(.*)</h2>\n.*\n.*\n{3}<div.*>\n{2}(.*)\n.*\n{2}.*\n{4}.*')
           # print patterns
            items = re.findall(patterns,content)
            print items
            for item in items:
                content_index += 1
                page_contents.append([str(content_index),str(item[1]),str(item[2])])
        except urllib2.URLError,e:
            if hasattr(e,'code'):
                print e.code
            if hasattr(e,'reason'):
                print e.reason
                
        return page_contents
            
    
    #打印出故事
    def print_story(self):
        page_contents = self.getPage()
        print("按回车键，则每次显示一条段子。按q或者Q，则退出程序".encode('cp936')+'\n')
        while 1:
            input = raw_input()
            if input == 'Q' or input == 'q':
                break
            if len(page_contents) == 0:
                self.pageIndex += 1
                page_contents = self.getPage()
            story = page_contents[0]
            del page_contents[0]
            print '('+str(story[0])+').'+str(story[1])+os.linesep+str(story[2])+os.linesep*2
            
qb = QSBK()
qb.print_story()
    
            
        
            
        
