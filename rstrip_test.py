f = open('test.txt','r')
for line in f:
    #print line.rstrip() #去除右边的字符，默认删除末尾的空格，与print line是有区别的，print line是会答应出多一行的空行的
    print line.strip()#与rstrip()类似，功能更强大，是同时去除左边和右边的字符
    #print line.lstri()#去除左边的字符

f.close()
