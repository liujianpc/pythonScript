#! /usr/bin/env python
# -*- coding: utf-8 -*-

import md5
import base64
import urllib2
import urllib
import json
import random
import os
import sys
import string

#string.replace(u'\xa0', u' ')

reload(sys)
sys.setdefaultencoding('utf-8')

#设置cookie
cookie_opener = urllib2.build_opener()
cookie_opener.addheaders.append(('Cookie', 'appver=2.0.2'))
cookie_opener.addheaders.append(('Referer', 'http://music.163.com'))
urllib2.install_opener(cookie_opener)

#加密
#def encrypted_id(id):
#    byte1 = bytearray('3go8&$8*3*3h0k(2)2')
#    byte2 = bytearray(id)
#    byte1_len = len(byte1)
#    for i in xrange(len(byte2)):
#        byte2[i] = byte2[i]^byte1[i%byte1_len]
#    m = md5.new()
#    m.update(byte2)
#    result = m.digest().encode('base64')[:-1]
#    result = result.replace('/', '_')
#    result = result.replace('+', '-')
#    return result
#
#根据歌手名搜索歌手，获取歌手的信息
def search_artist_by_name(name):
    search_url = 'http://music.163.com/api/search/get'
    params = {
            's': name,
            'type': 100,#100是搜索歌手
            'offset': 0,
            'sub': 'false',
            'limit': 10
    }
    params = urllib.urlencode(params)
    resp = urllib2.urlopen(search_url, params)
    artists = json.loads(resp.read())
    if artists['code'] == 200 and artists['result']['artistCount'] > 0:
        return artists['result']['artists'][0]
    else:
        return None

#根据歌手名搜索专辑，获取歌手的专辑的信息
def search_album_by_name(name):
    search_url = 'http://music.163.com/api/search/get'
    params = {
            's': name,
            'type': 10,#10是搜索专辑
            'offset': 0,
            'sub': 'false',
            'limit': 20
    }
    params = urllib.urlencode(params)
    resp = urllib2.urlopen(search_url, params)
    resp_js = json.loads(resp.read())
    if resp_js['code'] == 200 and resp_js['result']['albumCount'] > 0:
        result = resp_js['result']
        album_id = 0
        if result['albumCount'] > 1:
            for i in xrange(len(result['albums'])):
                album = result['albums'][i]
                #列出歌手名、专辑名
                print '[%2d]artist:%s\talbum:%s' % (i+1, album['artist']['name'], album['name'])
            #个人选择专辑
            select_i = int(raw_input('Select One:'))
            if select_i < 1 or select_i > len(result['albums']):
                print '错误选择'.encode('gbk')
                return None
            else:
                album_id = select_i - 1
                return result['albums'][album_id]#返回专辑信息
    else:
        return None


#根据歌曲名搜索歌曲,获取歌曲的信息
def search_song_by_name(name):
    search_url = 'http://music.163.com/api/search/get'
    params = {
            's': name,
            'type': 1,#搜索单曲
            'offset': 0,
            'sub': 'false',
            'limit': 30
    }
    params = urllib.urlencode(params)
    resp = urllib2.urlopen(search_url, params)
    resp_js = json.loads(resp.read())
    if resp_js['code'] == 200 and resp_js['result']['songCount'] > 0:
        result = resp_js['result']
        song_id = result['songs'][0]['id']
        if result['songCount'] > 1:
            for i in xrange(len(result['songs'])):
                song = result['songs'][i]
                #打印歌曲名、歌手名、专辑名
                #index_str = '['+str(i+1)+']'+'song:'+song['name']+"\t"+'artist:'+song['artists'][0]['name']+"\t"+'album:'+ song['album']['name']
                try:
                    print "[%2d]--%s---%s---%s" % (i+1,song['name'].encode('gbk'),song['artists'][0]['name'].encode('gbk'),song['album']['name'].encode('gbk'))
                except UnicodeEncodeError,e:
                    print "[%2d]--%s---%s---%s" % (i+1,song['name'],song['artists'][0]['name'],song['album']['name'])
                #print index_str
                #print '[%2d]song:%s\tartist:%s\talbum:%s' % (i+1,song['name'], song['artists'][0]['name'], song['album']['name'])
            #选择一首歌曲
            select_i = int(raw_input("选择一首（输号码）:".encode('gbk')))
            if select_i < 1 or select_i > len(result['songs']):
                print '错误选择'.encode('gbk')
                return None
            else:
                song_id = result['songs'][select_i-1]['id']
                #由歌曲的id查询歌曲的信息(mp3链接)
                detail_url = 'http://music.163.com/api/song/detail?ids=[%d]' % song_id
                resp = urllib2.urlopen(detail_url)
                song_js = json.loads(resp.read())
                return song_js['songs'][0]#返回歌曲的信息，包括MP3链接
    else:
        return None

#根据歌手获取歌手的专辑
#def get_artist_albums(artist):
#    albums = []
#    offset = 0
#    while True:
#        url = 'http://music.163.com/api/artist/albums/%d?offset=%d&limit=50' % (artist['id'], offset)
#        resp = urllib2.urlopen(url)
#        tmp_albums = json.loads(resp.read())
#        albums.extend(tmp_albums['hotAlbums'])
#        if tmp_albums['more'] == True:
#            offset += 50
#        else:
#            break
#    return albums

#根据专辑获取专辑的歌曲
#def get_album_songs(album):
#    url = 'http://music.163.com/api/album/%d/' % album['id']
#    resp = urllib2.urlopen(url)
#    songs = json.loads(resp.read())
#    return songs['album']['songs']

#将id对应歌曲下载到硬盘
def save_song_to_disk(song, folder):
    name = song['name']
    fpath = os.path.join(folder, name+'.mp3')
    if os.path.exists(fpath):
        return None

    
    url = song['mp3Url']
    #print '%s\t%s' % (url, name)
    #return
    print '正在下载---'.encode('gbk'),song['name'].encode('gbk')
    resp = urllib2.urlopen(url)
    data = resp.read()
    f = open(fpath, 'wb')
    f.write(data)
    f.close()

#根据歌名下载歌曲
def download_song_by_search(name, folder='.'):
    song = search_song_by_name(name)
    if not song:
        print '没找到---'.encode('gbk'),name
        return None

    if not os.path.exists(folder):
        os.makedirs(folder)
    save_song_to_disk(song, folder)
    
#获取歌单
def search_playlist_by_name(name):
    search_url = 'http://music.163.com/api/search/get'
    params = {
            's': name,
            'type': 1000,#1000是搜索歌单
            'offset': 0,
            'sub': 'false',
            'limit': 30
    }
    params = urllib.urlencode(params)
    resp = urllib2.urlopen(search_url, params)
    resp_js = json.loads(resp.read())
    if resp_js['code'] == 200 and resp_js['result']['playlistCount'] > 0:
        result = resp_js['result']
        playlist_id = 0
        if result['playlistCount'] > 1:
            for i in xrange(len(result['playlists'])):
                playlist = result['playlists'][i]
                #列出歌手名、专辑名
                try:
                    print '[%2d]playlist:%s' %(i+1,playlist['name'].encode('gbk'))
                except UnicodeEncodeError,e:
                    print '[%2d]playlist:%s' %(i+1,playlist['name'])
            #个人选择专辑
            select_i = raw_input("选择一个歌单（输号码）:".encode('gbk'))
            select_i = int(select_i)
            if select_i < 1 or select_i > len(result['playlists']):
                print '错误选择'.encode('gbk')
                return None
            else:
                playlist_id = select_i - 1
                return result['playlists'][playlist_id]#返回歌单信息
    else:
        return None
#获取歌单中的歌曲的信息
def get_playlist_songs(playlist):
    url = 'http://music.163.com/api/playlist/detail?id=%d' % playlist['id']
    resp = urllib2.urlopen(url)
    songs = json.loads(resp.read())
    return songs['result']['tracks']#返回歌曲信息

#根据歌单下载
def download_playlist_by_search(name,folder='.'):
    playlist = search_playlist_by_name(name)
    if not playlist:
        print "没找到---".encode('gbk'),name
        return None
    name = playlist['name']
    folder = os.path.join(folder,name)
    
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    songs = get_playlist_songs(playlist)
    for song in songs:
        save_song_to_disk(song,folder)
    


#根据专辑名下载专辑
#def download_album_by_search(name, folder='.'):
#    album = search_album_by_name(name)
#    if not album:
#        print 'Not found ' + name
#        return
#    
#    name = album['name']
#    folder = os.path.join(folder, name)
#
#    if not os.path.exists(folder):
#        os.makedirs(folder)
#
#    songs = get_album_songs(album)
#    for song in songs:
#        save_song_to_disk(song, folder)

#if __name__ == '__main__':
#    if len(sys.argv) < 3:
#        sys.exit(0)
#    download_playlist_by_search(sys.argv[1], sys.argv[2])
if __name__ == '__main__':
    while True:
        print '''**************************************************************************
        ##本程序可以根据歌曲名下载单曲，也可以下载歌单（网易的专辑没API）##
                   输入1，则进入下载单曲功能。
                   输入2，则进入下载歌单功能。
                   输入3，则退出程序。'''.encode('gbk')
        
        sel = raw_input('请输入你的选择：'.encode('gbk'))
        sel = int(sel)
        if sel == 1:
            print '单曲下载功能（输入歌曲名即可下载）'.encode('gbk')
            name = raw_input("输入需要下载的歌曲名：".encode('gbk'))
            download_song_by_search(name,folder="d://song")
        elif sel == 2:
            print '歌单下载功能（可下载歌单内所有歌曲）'.encode('gbk')
            name = raw_input('输入需要下载的歌单名：'.encode('gbk'))
            #name = name.encode('gbk')
            download_playlist_by_search(name,folder='d://song')
        elif sel == 3:
            break
            print '已退出程序'.encode('gbk')
        else:
            print "输入错误，请重试".encode('gbk')