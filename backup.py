#!/usr/bin/python

# Filename: backup_ver1.py

import os

import time

# 1. ��Ҫ���ݵ��ļ���Ŀ¼��һ���б�ָ��

source = ['D:\\a', 'D:\\b']

# ע�����Ǳ������ַ����ڲ�ʹ��˫���Ž����пո��������������

# 2. ���ݱ������һ��������Ŀ¼��

target_dir = 'd://Backup' # ��ס�ı����Ｔ�ɸı�����Ҫʹ�õ���Ŀ¼

 

# 3. �ļ��ᱻ����Ϊһ��zip�ļ���

# 4. ���zip�ļ��Ե�ǰ�����ں�ʱ��������

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

 

# 5. ����ʹ��zip����ļ��鵵��һ��zip

zip_command = "zip -qr %s %s" % (target, ' '.join(source))

# ִ�б���

if os.system(zip_command) == 0:

    print('Successful backup to', target)

else:

    print('Backup FAILED')
