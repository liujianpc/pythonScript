# -*- coding: cp936 -*-
#��Ӻ���
info = {}
import cPickle as p
def add():
	global info
	print '��������Ҫ��ӵ���ϵ����Ϣ��'
	name = raw_input('������')
	phone = raw_input('�绰���룺')
	addr = raw_input('סַ��')
	email = raw_input('�����ʼ���')
	
	try:
		F = file('dd.txt')
		info = dict(p.load(F))
	except EOFError:
		pass
	F.close()
	
	info.setdefault(name,[name,phone,addr,email])
	info =sorted(info.iteritems(),key=lambda d:d[0],reverse=False)#��������
	f = file('dd.txt','w')
	p.dump(info,f)
	f.close()
	print '��ϲ����ӳɹ���'
	

#�޸ĺ���
def modify():
	global info
	print '��������Ҫ�޸ĵ���ϵ��������'
	name = raw_input('��ϵ��������')
	
	try:
		F = file('dd.txt')
		info = dict(p.load(F))
	except EOFError:
		pass
	F.close()
	
	if name in info:
		print '''�������޸���:
			1���޸ĵ绰����		2���޸�סַ		3���޸ĵ����ʼ�'''
		selector = raw_input('�޸���Ϊ��')
		if selector == '1':
			info[name][1] = raw_input('�绰�����޸�Ϊ��')
		elif selector == '2':
			info[name][2] = raw_input('סַ�޸�Ϊ��')
		elif selector == '3':
			info[name][3] = raw_input('�����ʼ��޸�Ϊ��')
		else:
			print '����������������룡'
		f = file('dd.txt','w')
		p.dump(info,f)
		print '�޸ĳɹ���'
			
			
#ɾ������

def delete():
	
	global info
	print '��������Ҫɾ������ϵ��������'
	name = raw_input('��Ҫɾ������ϵ������Ϊ��')
	try:
		F = file('dd.txt')
		info = dict(p.load(F))
	except EOFError:
		pass
	
	if name in info:
		del info[name]
	info =sorted(info.iteritems(),key=lambda d:d[0],reverse=False)#ɾ������������һ�Σ���Ϊɾ���������
	f = file('dd.txt','w')
	p.dump(info,f)
	print '��ϲ��ɾ���ɹ���'
	
#���Һ���
def search():
	
	global info
	print '��������Ҫ���ҵ���ϵ��������'
	name = raw_input('������ϵ������Ϊ��')
	try:
		F = file('dd.txt')
		info = dict(p.load(F))
	except EOFError:
		pass
	F.close()
	
	if name in info:
		print info[name]
		print '��ϲ�����ҳɹ���'
	else:
		print '��Ǹ��ͨѶ¼�ڲ����ڴ��ˣ�'
		

#������
while 1:
	
	print '''��ӭ���������ͨѶ¼��
	1��A(a)�����ϵ��		2��M(m)�޸���ϵ����Ϣ
	3��D(d)ɾ����ϵ��		4��S(s)������ϵ����Ϣ
			5��E(e)�˳�ͨѶ¼'''
	chooser = raw_input('���������ѡ��')

	if chooser == '1' or chooser == 'A' or chooser == 'a':
		add()
	elif chooser == '2' or chooser == 'M' or chooser == 'm':
		modify()
	elif chooser == '3' or chooser == 'D' or chooser == 'd':
		delete()
	elif chooser == '4' or chooser == 'S' or chooser == 's':
		search()
	elif chooser == '5' or chooser == 'E' or chooser == 'e':
		print '�����˳�ͨѶ¼���򣬸�л���ʹ�ã��ټ���'
		break
		

		
		
		
					
			
		
		
		
