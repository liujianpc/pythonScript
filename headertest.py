#!/usr/bin/python
# -*- encoding:utf-8 -*-

import urllib
import urllib2

usrAgent = "Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)"
values = {'username':'xxx','password':'sssss'}
headers = {'User-Agent':usrAgent}
postData = urllib.urlencode(values)
url = 'http://www.server.com/login'

request = urllib2.Request(url,postData,headers)

response = urllib2.urlopen(request)

page = response.read()