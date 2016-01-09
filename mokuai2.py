#! /usr/bin/env python
#coding=utf-8
def print_nested(nested_list,bool,level = 0):
	for content in nested_list:
		if isinstance(content,list):
			print_nested(content,bool,level + 1)
		else:
			if bool == True:
				for i in range(level):
					print("\t");
				print content
			else:
				print content
				
movies = ['forrest gump',['hello','tom hanks'],'java','spierberg',['do',['oscar','get',['liudehua','china']]]]
print_nested(movies,True)