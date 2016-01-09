#!/usr/bin/python

# Filename: backup_ver1.py

import os

import time

# 1. 需要备份的文件和目录由一个列表指定

source = ['D:\\a', 'D:\\b']

# 注意我们必须在字符串内部使用双引号将带有空格的名字括起来。

# 2. 备份必须存在一个主备份目录中

target_dir = 'd://Backup' # 记住改变这里即可改变你想要使用的主目录

 

# 3. 文件会被备份为一个zip文件。

# 4. 这个zip文件以当前的日期和时间命名。

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

 

# 5. 我们使用zip命令将文件归档成一个zip

zip_command = "zip -qr %s %s" % (target, ' '.join(source))

# 执行备份

if os.system(zip_command) == 0:

    print('Successful backup to', target)

else:

    print('Backup FAILED')
