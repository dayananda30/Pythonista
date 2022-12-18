class Employee:
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name

    @property
    def email(self):
        return "{}{}@gmail.com".format(self.firstName, self.lastName)

    @property
    def fullname(self):
        return "{}{}".format(self.firstName, self.lastName)

    @fullname.setter
    def fullname(self, name):
        self.firstName = name.split()[0]
        self.lastName = name.split()[1]


emp1 = Employee("Daya", "nanda")
print(emp1.email)
print(emp1.fullname)

emp1.firstName = "Dayananda"
emp1.lastName = "DR"
print(emp1.email)
print(emp1.fullname)

""""
you can't set full name because it is connected firstname and lastname
we can accomplish this by setter 
"""

emp1.fullname = "Deepu Daya"
print(emp1.email)
print(emp1.fullname)
