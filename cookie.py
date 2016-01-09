import urllib
import urllib2
import cookielib

fileName = 'cookie.txt'
cookie = cookielib.MozillaCookieJar(fileName)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postData = urllib.urlencode({"username":"2013060104021","password":"xxxxxx"})
loginUrl = "https://uis.uestc.edu.cn/amserver/UI/Login?goto=http%3A%2F%2Fportal.uestc.edu.cn%2Flogin.portal"
result = opener.open(loginUrl,postData)
cookie.save(ignore_discard=True,ignore_expires=True)
otherUrl = "http://portal.uestc.edu.cn/index.portal?.pn=p1043"
result = opener.open(otherUrl)
print result.read()
<div.*?class="author.*".*?>\n<a.*?>\n<(.*?)>\n(.*)\n.*\n.*\n{3}<div class="content">\n{2}(.*)\n.*\n{2}.*\n{4}<div class="stats">\n<span.*?class="stats-vote"><i class="number">(.*?)</i>