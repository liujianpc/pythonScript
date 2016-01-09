#filename:jicheng.py
class School_member:
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

class Teacher(School_member):
    def __init__(self,name,sex,age,sno,salary):
        School_member.__init__(self,name,sex,age,sno)
        self.salary = salary
    def gongzi(self):
        print '我的薪水是%d' % self.salary
class Student(School_member):
    def __init__(self,name,sex,age,sno,banji):
        School_member.__init__(self,name,sex,age,sno)
        self.banji = banji
    def intro(self):    
        print '我在',self.banji,'班'
tech = Teacher('jim','男',40,'2010',8000)
tech.sayhi()
tech.gongzi()
stu = Student('liujian','男',20,'1990',4)
stu.sayhi()
stu.intro()
del tech
