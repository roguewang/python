#!/usr/bin/env python
# Author:rogue

class Person:

    def say(self):
        print("hello world")

    @staticmethod
    def sayhello():
        print("hello")

p = Person()
p.say()
Person.sayhello()