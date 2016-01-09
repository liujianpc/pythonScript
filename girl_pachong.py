#! /usr/bin/env python
#coding=utf-8
# encoding=utf-8

import sys
import urllib
from bs4 import BeautifulSoup
import os
reload(sys)
sys.setdefaultencoding('utf-8')
debug = True # 设置是否打印log
def log(message):
    if debug:
        print message.encode('gbk')


def download_image(url, save_path):
    '''根据图片url下载图片到save_path '''
    try:
        urllib.urlretrieve(url, save_path)
        log('Downloaded a image: ' + save_path)
    except Exception, e:
        #print 'An error catched when download a image:', e
        #print url
        url = "http://qiubaichengren.com/"+url
        #print url
        urllib.urlretrieve(url, save_path)
        log('Downloaded a image: ' + save_path)
        

def load_page_html(url):

    ''' 得到页面的HTML文本 '''
    log('Get a html page : '+ url)
    return urllib.urlopen(url).read()


def down_page_images(page, save_dir):
    '''下载第page页的图片'''
    html_context = load_page_html('http://qiubaichengren.com/%d.html' % page)
    soup = BeautifulSoup(html_context,'html.parser')
    for ui_module_div in soup.findAll('div', {'class': 'ui-module'}):
        img_tag = ui_module_div.find('img')
        if img_tag is not None and img_tag.has_attr('alt') and img_tag.has_attr('src'):
            alt = img_tag.attrs['alt'] # 图片的介绍
            src = img_tag.attrs['src'] # 图片的地址
            filename = '%s%s' % (alt, src[-4:]) # 取后四位（有的图片后缀是'.jpg'而有的是'.gif'）
            dst = save_dir + filename
            if not os.path.exists(dst):
                download_image(src, save_dir + filename)


def download_qbcr(frm=1, page_count=3, save_dir='./'):
    for x in xrange(frm, frm + page_count):
        log('Page : ' + `x`)
        down_page_images(x, save_dir)

def main(frm,page_count):
    base_path = 'D:\\'
    download_qbcr(frm, page_count, save_dir=base_path)

if __name__ == '__main__':
    print "****福利爬虫****".encode('gbk')
    frm = int(raw_input("开始页为：".encode('gbk')))
    page_count =int(raw_input("增量页为：".encode('gbk')))
    main(frm,page_count)
