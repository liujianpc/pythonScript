#! /usr/bin/env python
#coding=utf-8

import urllib2
import cookielib


import re
import json
import urllib
import base64
import rsa
import binascii

class WeiboLogin:
    def __init__(self, user, pwd, enableProxy = False):
        "初始化WeiboLogin，enableProxy表示是否使用代理服务器，默认关闭"
        print "Initializing WeiboLogin..."
        self.userName = user
        self.passWord = pwd
        self.enableProxy = enableProxy

        self.serverUrl = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.11)&_=1379834957683"
        self.loginUrl = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.11)"
        self.postHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}
    def Login(self):
        "登陆程序"  
        self.EnableCookie(self.enableProxy)#cookie或代理服务器配置

        serverTime, nonce, pubkey, rsakv = self.GetServerTime()#登陆的第一步
        postData = self.PostEncode(self.userName, self.passWord, serverTime, nonce, pubkey, rsakv)#加密用户和密码
        print "Post data length:\n", len(postData)
        req = urllib2.Request(self.loginUrl, postData, self.postHeader)
        print "Posting request..."
        result = urllib2.urlopen(req)#登陆的第二步——解析新浪微博的登录过程中3
        text = result.read()
        try:
            loginUrl = self.sRedirectData(text)#解析重定位结果
            urllib2.urlopen(loginUrl)
        except:
            print 'Login error!'
            return False

        print 'Login sucess!'
        return True

    def sRedirectData(text):
        p = re.compile('location\.replace\([\'"](.*?)[\'"]\)')
        loginUrl = p.search(text).group(1)
        print 'loginUrl:',loginUrl
        return loginUrl

    def PostEncode(self,userName, passWord, serverTime, nonce, pubkey, rsakv):
        "Used to generate POST data"

        encodedUserName = self.GetUserName(userName)#用户名使用base64加密
        encodedPassWord = self.get_pwd(passWord, serverTime, nonce, pubkey)#目前密码采用rsa加密
        postPara = {
            'entry': 'weibo',
            'gateway': '1',
            'from': '',
            'savestate': '7',
            'userticket': '1',
            'ssosimplelogin': '1',
            'vsnf': '1',
            'vsnval': '',
            'su': encodedUserName,
            'service': 'miniblog',
            'servertime': serverTime,
            'nonce': nonce,
            'pwencode': 'rsa2',
            'sp': encodedPassWord,
            'encoding': 'UTF-8',
            'prelt': '115',
            'rsakv': rsakv,     
            'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
            'returntype': 'META'
        }
        postData = urllib.urlencode(postPara)#网络编码
        return postData


    def EnableCookie(self, enableProxy):
        "Enable cookie & proxy (if needed)."

        cookiejar = cookielib.LWPCookieJar()#建立cookie
        cookie_support = urllib2.HTTPCookieProcessor(cookiejar)
        if enableProxy:
            proxy_support = urllib2.ProxyHandler({'http':'http://xxxxx.pac'})#使用代理
            opener = urllib2.build_opener(proxy_support, cookie_support, urllib2.HTTPHandler)
            print "Proxy enabled"
        else:
            opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)#构建cookie对应的opener
    def GetServerTime(self):
        "Get server time and nonce, which are used to encode the password"

        print "Getting server time and nonce..."
        serverData = urllib2.urlopen(self.serverUrl).read()#得到网页内容
        print serverData
        try:
            serverTime, nonce, pubkey, rsakv = self.sServerData(serverData)#解析得到serverTime，nonce等
            return serverTime, nonce, pubkey, rsakv
        except:
            print 'Get server time & nonce error!'
            return None

    def sServerData(serverData):
        "Search the server time & nonce from server data"

        p = re.compile('\((.*)\)')
        jsonData = p.search(serverData).group(1)
        data = json.loads(jsonData)
        serverTime = str(data['servertime'])
        nonce = data['nonce']
        pubkey = data['pubkey']#
        rsakv = data['rsakv']#
        print "Server time is:", serverTime
        print "Nonce is:", nonce
        return serverTime, nonce, pubkey, rsakv

    def GetUserName(userName):
        "Used to encode user name"

        userNameTemp = urllib.quote(userName)
        userNameEncoded = base64.encodestring(userNameTemp)[:-1]
        return userNameEncoded

    def get_pwd(password, servertime, nonce, pubkey):
        rsaPublickey = int(pubkey, 16)
        key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
        message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
        passwd = rsa.encrypt(message, key) #加密
        passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
        return passwd



if __name__ == '__main__':
    weiboLogin = WeiboLogin('695966004@qq.com','ljpc213430256707')
    if weiboLogin.Login() == True:
        print '登录成功'
        
