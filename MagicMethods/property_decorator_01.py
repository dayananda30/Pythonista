"""
Assume Below is the code base, all the dev are using this from a while.

"""


class Employee:
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name
        self.email = self.firstName + self.lastName + "@gmail.com"

    def getFullName(self):
        return "{}{}".format(self.firstName, self.lastName)


emp1 = Employee("Daya", "nanda")
print(emp1.email)
print(emp1.getFullName())

# Problem lies here, If we change firstname , it will not reflect in email address.
emp1.firstName = "Dayananda"
emp1.lastName = "DR"
print(emp1.email)
print(emp1.getFullName())

"""
Why email attribute is not getting updated with the change in first and lastname?
email address is at constructor level and it is getting called only once.

To avoid this, we should add a new method by the name email and set the email address.

Again there is a problem...
Since this code is already being used by many developers, we should not change email attribute to method.

How can we achieve above requirement? 
Yes, we can achieve via property decorator.
"""
