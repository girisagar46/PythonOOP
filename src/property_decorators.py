__author__ = "girisagar46@gmail.com"
"""
property decorators helps to implement getter and setter method.
property decorator allow us to define a method we can access it like a attribute
"""


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property # using this we can access the method as a attribute
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print "Delete name"
        self.first = None
        self.last = None

emp1 = Employee("Sagar", "Giri")

emp1.fullname = "Tony Stark"

print emp1.first
print emp1.email

# print emp1.fullname() # when @property decorator is not implemented

# when @property decorator is implemented
print emp1.fullname

del emp1.fullname
print emp1.__dict__