# -*- coding: cp936 -*-
def printNest(nestList,indent = False,level = 0):
    for content in nestList:
        if isinstance(content,list):
            printNest(content,indent,level = level + 1)
        else:
            if indent:
                print '\t'*level,content
            else:
                print content

movies = ['forrest',['dashanghai',['beijingren','caonima'],'hello'],'good']
printNest(movies)#������Ĭ�ϲ���
printNest(movies,True)#����Ϊ����
printNest(movies,True,1)#��������������ʼ��level=1
