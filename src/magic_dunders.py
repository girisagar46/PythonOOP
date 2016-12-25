__author__ = "girisagar46@gmail.com"

"""
These are the special methods that we can use in our class. These are also called magic methods.
These methods allow us to emulate builtin behaviour within python. Using this we can also implement operator overload.
These methods are surrounded by double underscores or called as dunder.
"""

class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # repr returns the canonical string representation of the object.
    # used for debugging and logging
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # readable representation of object
    # __str__ is superior than __repr__ when print(object) is invoked
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("Sagar", "Giri", 50000)
emp_2 = Employee("Test", "User", 60000)

print emp_1 + emp_2 # calls __add__

print len(emp_1) # calles __len__

# this directly calles the special methods
print repr(emp_1)
print str(emp_1)

# can be called using this as well
print emp_1.__repr__()
print emp_1.__str__()