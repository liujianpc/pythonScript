#backup-versuion2
import os
import time
source_dir = [r'd:\a',r'd:\b']
backup_dir = r'd:\backup'
target_dir = backup_dir + os.sep + time.strftime('%Y-%m-%d')
target_name = target_dir + os.sep + time.strftime('%H-%M-%S') + '.zip'
tag = raw_input('���������Լ���ע�ͱ�ǩ')
if tag:
    target_name = target_dir + os.sep + time.strftime('%H-%M-%S') + '-' + tag + '.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print '�ѳɹ��������ձ����ļ���'
zip_command = 'zip -qr %s %s' %(target_name,' '.join(source_dir))
if os.system(zip_command) == 0:
    print '�Ѿ��ɹ���������',target_dir
else:
    print '����ʧ�ܣ�'
