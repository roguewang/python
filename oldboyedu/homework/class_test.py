#!/usr/bin/env python
# Author:rogue

class Person:
    country = "中国"
    language = "普通话"
    def __init__(self, name,age,sex):
        self.Name = name
        self.Age = age
        self.Sex = sex

    def say(self):
        print("name =",self.Name ,",age =",self.Age,",sex =",self.Sex)


class Car:
    pass


p1 = Person("hamuxia",18,"女")
p2 = Person("rogue",22,"男")
p1.country = "usa"
print(p1.country)


class Son(Person):
    pass

s = Son("王大锤","3","男")
s.say()
