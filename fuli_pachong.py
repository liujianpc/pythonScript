#! /usr/bin/env python
#coding=utf-8
import sys
from bs4 import BeautifulSoup
import urllib
import urllib2
import os
import re

reload(sys)
sys.setdefaultencoding('utf-8')
#打印信息
def display(str):
    print str.encode('gbk')
    
#获取页面内容
def get_page(url):
    display("Get(获取并分析页面):"+url)
    try:
        headers = {"User-Agent":"Mozzila/4.0(compatible;MSIE5.5;Windows NT)"}
        req = urllib2.Request(url,headers=headers)
        resp = urllib2.urlopen(req)
        content = resp.read()
        return content
    except urllib2.URLError,e:
        if hasattr(e,'code'):
            print e.code
        if hasattr(e,'reason'):
            print e.reason
            
            
def down_img(save_path,url):
    try:
        urllib.urlretrieve(url,save_path)
        display("下载了图片")
    except Exception,e:
        print "错误".encode('gbk'),e
        pass
    
def analysis_page(page_index,save_path):
    content = get_page("http://www.qiushibaike.com/f/girl/%d" % page_index)
    soup = BeautifulSoup(content,'html.parser')
    for img_div in soup.findAll('div',{'class':'article-block'}):
        img_tag = img_div.find('img')
        if img_tag is not None:
            p_tag = img_div.findAll('p')[1]
            if p_tag is not None:
                src = img_tag.attrs['src']
                img_name = p_tag.get_text().encode('gbk')
                #print img_name
                img_file = '%s%s' % (img_name.strip('\n'),img_tag.attrs['src'][-5:].encode('gbk'))
                #print img_tag.attrs['src'][-5:]
                #print img_file
                dir = save_path + str(img_file)
                #print dir
                if not os.path.exists(dir):
                    down_img(save_path+img_file,src)
                
def down_qb_img(start,end,save_path):
    for i in xrange(start,end):
        display("下载第"+str(i)+"页")
        analysis_page(i,save_path)
        

def main():
    save_path = 'D:\\img\\'
    start = 1
    end = 20
    down_qb_img(start,end,save_path)
    
if __name__ == '__main__':
    main()
    