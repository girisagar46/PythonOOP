__author__ = "girisagar46@gmail.com"

"""
-While using inheritance, python has a MRO (Method Resolution Order).

-While creating a instance, if the method is not found in derived class, it looks for it in parent class. This chain is
known as MRO.


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


# Developer class inherits from Employee class
class Developer(object, Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # super(Developer, self).__init__(first, last, pay) # calling super in python2 convention
        # super().__init__(first, last, pay) # calling super in python3 convention
        Employee.__init__(self, first, last, pay) # calls Employee constructor same as above
        self.prog_lang = prog_lang


class Manager(Employee):

    # here employees = None because it is a list and list is mutable. We never pass mutable data types as args
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay) # call super init method
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print "--->",emp.fullname()

dev_1 = Developer("Sagar", "Giri", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "Java")


mgr_1 = Manager("Nick", "Fury", 90000, [dev_1])

mgr_1.add_employee(dev_2)
mgr_1.print_emps()
print "--------"
mgr_1.remove_employee(dev_1)
mgr_1.print_emps()


# isinstance() issubclass()
print isinstance(mgr_1, Manager)    # Output: True
print isinstance(mgr_1, Employee)   # Output: True because it inherits
print isinstance(mgr_1, Developer)  # Output: False because it doesnot inherits

print issubclass(Developer, Employee)
print issubclass(Manager, Employee)
print issubclass(Manager, Developer)