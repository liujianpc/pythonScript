#!/usr/bin/env python
#coding=utf-8
import sys
import os
from bs4 import BeautifulSoup
import urllib
import urllib2
import time
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

reload(sys)
sys.setdefaultencoding('utf-8')
#type = sys.getdefaultencoding()
#print type

class taobaoMM():
    def __init__(self,startPage = 1,endPage = 2):
        self.startPage = startPage
        self.endPage = endPage
        self.baseUrl = "https://mm.taobao.com/json/request_top_list.htm?type=0&page="
        self.headers = {"User-Agent":"Mozzila/4.0(compatible;MSIE5.5;Windows NT)"}
    
    def firstPage(self):
        
        for index in xrange(self.startPage,self.endPage + 1):
            url = self.baseUrl + str(index)
            try:
                req = urllib2.Request(url,headers=self.headers)
                resp = urllib2.urlopen(req)
                content = resp.read()
                soup = BeautifulSoup(content,'html.parser')
                for div in soup.findAll('div',{'class':'pic-word'}):
                    a_tag_1 = div.findAll('a')[0]
                    link = a_tag_1.attrs['href']
                    link = 'https:'+str(link)
                    print link
                    a_tag_2 = div.findAll('a')[1]
                    name = a_tag_2.get_text()
                    #print name
                    #link = a_tag[0].attrs('href')
                    #name = a_tag[1].get_text().encode('gbk')
                    ##
                    save_path = 'd:/img/'+str(name).decode("gb2312").encode("utf-8")
                    if not os.path.exists(save_path):
                        os.makedirs(save_path)
                    print save_path
                    #print link
                    self.secondPage(link,save_path)
                
            except urllib2.URLError,e:
                if hasattr(e,'code'):
                    print e.code
                if hasattr(e,'reason'):
                    print e.reason
            
            
            
                
                
                
    def secondPage(self,link,path):
        #print '11111'
        index = 0
        #print self.headers
        req = urllib2.Request(link,headers = self.headers)
        #print '222'
        resp = urllib2.urlopen(req)
        content = resp.read()
        #print 'hello'
        #print content
        soup = BeautifulSoup(content,'html.parser')
        #print soup
        for img_tag in soup.findAll('img',{'style':'float: none;margin: 10.0px;'}):
            links = img_tag.attrs['src']
            #print 'hello'
            #print links
            global index
            index = index + 1
            print index
            file_path = path +'/'+ str(index) + links[-5:-1]
            urllib.urlretrieve(links,file_path)
            time.sleep(5)
            
           # print 'hello'
            


            

                
def main():
    startPage = int(raw_input('please input startPage:'))
    endPage = int(raw_input('please input endPage:'))
    tb = taobaoMM(startPage,endPage)
    tb.firstPage()

if __name__ == '__main__':
    main()
                    
            
        
        
        
            
