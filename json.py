#-*- coding:cp936 -*-
import json
s = '''{"id1": 1, "name1": "����", "description1": "mmmmmm", "id2": 2, "name2": "����", "description2": "NNNNNNN", "id3": 3, "name3": "����", "description3": "TTTTT"}'''
print eval(s)

#json.load(s,encoding='cp936')
