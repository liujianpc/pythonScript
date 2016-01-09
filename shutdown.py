#!/usr/bin/python
#filename:shutdown.py
import os
import time

while 1:
    try:
        print 'input the shutdown time'
        h = int(raw_input('please input the shutdown_hour:'))
        if h <= 23 and h >=0:
            break
        else:
            continue
    except:
        continue

while 1:
    try:
        m = int(raw_input('please input the shutdown_minutes:'))
        if m >=0 and m <=59:
            break
        else:
            continue
    except:
        continue

while 1:
    try:
        s = int(raw_input('please input the shutdown_seconds:'))
        if s >=0 and s <= 59:
            break
        else:
            continue
    except:
        continue

now_time = list(time.localtime())
now_h = now_time[3]
now_m = now_time[4]
now_s = now_time[5]
command = 'cmd.exe /k shutdown -s -t 5 -c "it shutdowns now!"'

if now_h < h:
    time.sleep((h-now_h)*3600+(m-now_m)*60+s)
    os.system(command)
elif now_h == h:
    time.sleep((m-now_m)*60+s)
    os.system(command)
else:
    time.sleep((24+h-now_h)*3600+(m-now_m)*60+s)
    os.system(command)
    
                 
        
    









