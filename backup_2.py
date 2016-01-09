#backup-versuion2
import os
import time
source_dir = [r'd:\a',r'd:\b']
backup_dir = r'd:\backup'
target_dir = backup_dir + os.sep + time.strftime('%Y-%m-%d')
target_name = target_dir + os.sep + time.strftime('%H-%M-%S') + '.zip'
tag = raw_input('请输入你自己的注释标签')
if tag:
    target_name = target_dir + os.sep + time.strftime('%H-%M-%S') + '-' + tag + '.zip'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print '已成功创建今日备份文件夹'
zip_command = 'zip -qr %s %s' %(target_name,' '.join(source_dir))
if os.system(zip_command) == 0:
    print '已经成功备份至：',target_dir
else:
    print '备份失败！'
