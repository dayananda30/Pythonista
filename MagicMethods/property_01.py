"""
https://www.pythontutorial.net/python-oop/python-properties/

"""

class Person:
    def __init__(self, name, age):
        self.Name = name
        self.setage(age)

    def setage(self,age):
        if age < 0:
            raise ValueError("Age must be greater than 0")
        else:
            self.Age = age

    def getage(self):
        return self.Age

p1 = Person("Daya",33)
p2 = Person("Deepu",30)
print("P1 , Name is : {} and Age is : {}".format(p1.Name, p1.Age))
print("P2 , Name is : {} and Age is : {}".format(p2.Name, p2.Age))

p2.setage(31)

print("P2 , Name is : {} and Age is : {}".format(p2.Name, p2.Age))

"""
Thw problem with this approach is backward compactibility

This code works just fine. But it has a backward compatibility issue.
Suppose you released the Person class for a while and other developers 
have been already using it. And now you add the getter and setter, 
all the code that uses the Person won’t work anymore.

To define a getter and setter method while achieving backward compatibility,
 you can use the property() class.
"""