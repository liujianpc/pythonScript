#!/usr/bin/python
# -*- encoding:utf-8 -*-
import urllib
import urllib2
values = {"username":"695966004@qq.com","password":"ljpc213430256707"}
postData = urllib.urlencode(values)
url = "https://passport.csdn.net/"
request = urllib2.Request(url,postData)
response = urllib2.urlopen(request)
print response.read()