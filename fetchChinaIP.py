#! /usr/bin/env python
#coding=utf-8
import sys
import urllib,urllib2,MySQLdb,simplejson,time,httplib

reload(sys)
sys.setdefaultencoding("utf-8")

#整型转ip
def int_to_ip(s):
    ip_1 = s >> 16 & 0xff
    ip_2 = s >> 8 & 0xff
    ip_3 = s & 0xff
    return "%d.%d.%d.%d" %(ip_1,ip_2,ip_3,0)

#三段式ip转整型
def ipv3_to_int(s):
    int_list = [int(i) for i in s.split(".")]
    return (int_list[0] << 16) | (int_list[1] << 8) | int_list[3]

#连接mysql并且新建数据库
def create_database():
    #charset设置编码为utf-8
    con = MySQLdb.connect(host="localhost",user="root",passwd="abc7612776",port=3306,charset='utf8')
    cur = con.cursor()
    #如果不存在数据库chinaip，则新建该数据库
    cur.execute("create database if not exists chinaip")
    con.select_db("chinaip")
    #以下内容为新建数据库的表，mysql中text类型不能作为主键和索引项
    try:
        cur.execute('''create table ipdata(
                        ip_int integer(32) primary key,
                        ip text,
                        country text,
                        country_id text,
                        area text,
                        area_id text,
                        region text,
                        region_id text,
                        city text,
                        city_id text,
                        isp text,
                        isp_id text
                        )''')
                        
    except Exception:
        pass
    finally:
        con.commit()
        cur.close()
    #向数据库中插入信息
def db_insert(ip_int,ip_info):
    con = MySQLdb.connect(host="localhost",user="root",passwd="abc7612776",port=3306,charset='utf8')
    con.select_db("chinaip")
    cur = con.cursor()
    cur.execute('insert ignore into ipdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(ip_int,ip_info['data']['ip'],ip_info['data']['country'],ip_info['data']['country_id'],ip_info['data']['area'],ip_info['data']['area_id'],ip_info['data']['region'],ip_info['data']['region_id'],ip_info['data']['city'],ip_info['data']['city_id'],ip_info['data']['isp'],ip_info['data']['isp_id']))
    con.commit()
    cur.close()
    
    #基于淘宝的api获取ip地址的信息
def get_ip_info(ip_addr):
    #设置headers
    headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    base_url = "http://ip.taobao.com/service/getIpInfo.php"
    param = {"ip":ip_addr}
    url = base_url + "?" + urllib.urlencode(param)
    print url
    fail = 0
    try:
        req = urllib2.Request(url,headers=headers)
        response = simplejson.load(urllib2.urlopen(req,timeout=2))
    except (urllib2.URLError,IOError,httplib.BadStatusLine,RuntimeError):
        #httplib.BadStatusLine为防止网络问而程序中断退出
        fail += 1
        #如果失败次数少于10次，递归重新调用
        if fail < 200:
            response = get_ip_info(ip_addr)
        else:
            #如果失败次数大于10次，则挂起300s后继续递归调用
            time.sleep(10)
            response = get_ip_info(ip_addr)
    return response
        
        
       
    
def main():
    create_database()
    try:
        file_handle = open("ChinaIPAddress.txt","r")
        number_list = [i.strip() for i in file_handle.readlines()]
        
        for ip_int in number_list:
            ip_int = int(ip_int)
            ipv4 = int_to_ip(ip_int)
            ip_info = get_ip_info(ipv4)
            if ip_info["code"] != 0:
                pass
            else:
                db_insert(ip_int,ip_info)
    except IOError:
        print "error!"
    finally:
        file_handle.close()
        
if __name__ == '__main__':
    main()