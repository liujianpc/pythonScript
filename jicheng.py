#filename:jicheng.py
class School_member:
    __salary = 0
    name = ''
    sex = ''
    age= 0
    def __init__(self,name,sex,age,sno):
        self.sno = sno
        self.name =name
        self.sex = sex
        self.age = age
        print 'my name is',self.name,self.sno,self.sex,self.age
    def __dele__(self):
        print'free'
    def sayhi(self):
        print 'hello,i am',self.name
tech = School_member('jim','ÄÐ',40,'2010')
tech.sayhi()
stu = School_member('liujian','ÄÐ',20,'1990')
stu.sayhi()
del tech
