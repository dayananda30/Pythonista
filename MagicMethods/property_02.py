"""
Python Property class class following syntax
property(fget=None, fset=None, fdel=None, doc=None)

The property() has the following syntax

"""

from pprint import pprint
class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    def getAge(self):
        return self.Age

    def setAge(self,age):
        if age < 0:
            raise ValueError("Age must be positive number")
        else:
            self.Age = age

    #property object age is a class attribute
    age = property(fget=getAge, fset=setAge)

print(Person.age)
daya = Person("Daya",33)
pprint(daya.__dict__)

daya.age = 34
pprint(daya.__dict__)