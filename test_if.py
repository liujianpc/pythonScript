# -*- coding: cp936 -*-

while True:
    grade = input("请输入成绩：")
    if grade >= 90:
        print("A")
    elif grade >=80 and grade < 90:
        print("B")
    elif grade >=70 and grade < 80:
        print("C")
    elif grade >=60 and grade < 70:
        print("D")
    elif grade >=0 and grade < 60:
        print("bad!")
    else:
        print("incorrect input!")
