#! /usr/bin/env python
#coding=cp936
def printNest(nestList,indent = False,level = 0,fh = sys.stdout):
    for content in nestList:
        if isinstance(content,list):
            printNest(content,indent,level = level + 1,fh)
        else:
            if indent:
                print '\t'*level,content
            else:
                print(content,file = fn)



