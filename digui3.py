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
printNest(movies)#不设置默认参数
printNest(movies,True)#设置为缩进
printNest(movies,True,1)#设置缩进，并初始化level=1
