#!/usr/bin/env python
# Author:rogue

class Person:
    def __init__(self,name,age,sex,country):
        self.Name = name
        self.Age = age
        self.Sex = sex
        self.Country = country

    def fun(self,m=0):
        msg = """Hi, this is one test function.
        Test Name = %s
        Test Age = %s
        Test Sex = %s
        Test Country = %s
        """%(self.Name,self.Age,self.Sex,self.Country)
        if m != 0:
            print(msg)
        else:
            pass

p = Person("andy",18,"M","USA")
p.fun(1)