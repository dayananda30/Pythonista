"""
__call__ will get called when you call the object.
object() is shorthand for object.__call__()

"""

class Person:
    def __init__(self):
        print("Person object created!!!")

    def __call__(self, *args, **kwargs):
        print("I am in call function")

p1 = Person()
p1() # equaivalent to p1.__call__()
p1.__call__()