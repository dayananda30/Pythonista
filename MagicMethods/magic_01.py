"""
__repr__(self)
is one of the magic methods where you define how your object look like.

__repr__() function returns the object representation in string format

If you try to print p1 with __repr__ then you would memory address of that object.
<__main__.Person object at 0x0000025F5F4A7640>
"""

class Person:
    def __init__(self, name=None, age=None, address=None):
        self.Name = name
        self.Age = age
        self.Address = address

    def __repr__(self):
        return "Person({},{}, {})".format(self.Name, self.Age, self.Address)


p1 = Person("Daya", 33, "Dommalur")
print(p1) # similar to print(repr(p1))
print(repr(p1))
