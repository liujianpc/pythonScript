# coding=utf-8
#class_test.py
class Person:
    population = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.population = 0

    def __del__(self):
        self.population = 0
        print '释放了'
    def sayhi(self):
        print '我是',self.name,'今年',self.age
    def die(self):
        self.population -= 1
        print self.name,'挂了'
p = Person('lijinming',20)
p.sayhi()
p.die()

        
