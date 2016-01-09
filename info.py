# -*- coding: cp936 -*-
#添加函数
info = {}
import cPickle as p
def add():
	global info
	print '请输入需要添加的联系人信息！'
	name = raw_input('姓名：')
	phone = raw_input('电话号码：')
	addr = raw_input('住址：')
	email = raw_input('电子邮件：')
	
	try:
		F = file('dd.txt')
		info = dict(p.load(F))
	except EOFError:
		pass
	F.close()
	
	info.setdefault(name,[name,phone,addr,email])
	info =sorted(info.iteritems(),key=lambda d:d[0],reverse=False)#按键排序
	f = file('dd.txt','w')
	p.dump(info,f)
	f.close()
	print '恭喜，添加成功！'
	

#修改函数
def modify():
	global info
	print '请输入需要修改的联系人姓名！'
	name = raw_input('联系人姓名：')
	
	try:
		F = file('dd.txt')
		info = dict(p.load(F))
	except EOFError:
		pass
	F.close()
	
	if name in info:
		print '''请输入修改项:
			1、修改电话号码		2、修改住址		3、修改电子邮件'''
		selector = raw_input('修改项为：')
		if selector == '1':
			info[name][1] = raw_input('电话号码修改为：')
		elif selector == '2':
			info[name][2] = raw_input('住址修改为：')
		elif selector == '3':
			info[name][3] = raw_input('电子邮件修改为：')
		else:
			print '输出错误，请重新输入！'
		f = file('dd.txt','w')
		p.dump(info,f)
		print '修改成功！'
			
			
#删除函数

def delete():
	
	global info
	print '请输入需要删除的联系人姓名！'
	name = raw_input('需要删除的联系人姓名为：')
	try:
		F = file('dd.txt')
		info = dict(p.load(F))
	except EOFError:
		pass
	
	if name in info:
		del info[name]
	info =sorted(info.iteritems(),key=lambda d:d[0],reverse=False)#删除后仍需排序一次，因为删除后会乱序
	f = file('dd.txt','w')
	p.dump(info,f)
	print '恭喜，删除成功！'
	
#查找函数
def search():
	
	global info
	print '请输入需要查找的联系人姓名！'
	name = raw_input('查找联系人姓名为：')
	try:
		F = file('dd.txt')
		info = dict(p.load(F))
	except EOFError:
		pass
	F.close()
	
	if name in info:
		print info[name]
		print '恭喜，查找成功！'
	else:
		print '抱歉！通讯录内不存在此人！'
		

#主程序
while 1:
	
	print '''欢迎来到《煎锅通讯录》
	1、A(a)添加联系人		2、M(m)修改联系人信息
	3、D(d)删除联系人		4、S(s)查找联系人信息
			5、E(e)退出通讯录'''
	chooser = raw_input('请输入你的选择：')

	if chooser == '1' or chooser == 'A' or chooser == 'a':
		add()
	elif chooser == '2' or chooser == 'M' or chooser == 'm':
		modify()
	elif chooser == '3' or chooser == 'D' or chooser == 'd':
		delete()
	elif chooser == '4' or chooser == 'S' or chooser == 's':
		search()
	elif chooser == '5' or chooser == 'E' or chooser == 'e':
		print '你已退出通讯录程序，感谢你的使用！再见！'
		break
		

		
		
		
					
			
		
		
		
