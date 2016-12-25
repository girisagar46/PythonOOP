__author__ = "girisagar46@gmail.com"

# A Employee Class. First letter must be capital


class Employee:

    def __init__(self, first, last, pay):
        # here self is the automatically invoked instance to the method
        self.first = first
        self.last = last
        self.pay = pay
        # email can be derived from the "first" and "last" name
        self.email = self.first+"."+self.last+"company.com"

    # a method that returns fullname. self is a must for any method
    def fullname(self):
        return "{} {}".format(self.first, self.last)

# instances
emp_1 = Employee("Sagar", "Giri", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.__dict__)
print(emp_2.email)

# While calling a function, don't forget the parenthesis
print(emp_1.fullname())
print(emp_2.fullname())

# calling method directly from class.
# To do so, we need to pass the instance we created.
# Remember the self we added in the method :)
print "Directly from class---> ",Employee.fullname(emp_1)
print "Directly from class---> ",Employee.fullname(emp_2)