__author__ = "girisagar46@gmail.com"

"""
Class variables are variables that are shared among all instance of a class.
instance variables can be unique for each instance.
"""

class Employee:

    # This is class variable
    # Class variable can be accessed from both Class and Instance of a class
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@company.com"
        # here it's unnecessary to use self.num_of_emps because,
        # for a company emp number is same. It is not necessarity a instance variable
        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * 1.04)
        """
        here 1.04 is applied for each instance uniquely, so,
        when we need to change pay for different employee,
        we have to change for every usage of 1.04
        The best way is to make 1.04 a class variable
        """

        # using class variable
        # using self.raise_amount gives ability to change it's value in single instance
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee("Sagar", "Giri", 50000)
emp_2 = Employee("Test", "User", 60000)

# print emp_1.pay
# emp_1.apply_raise()
# print emp_1.pay

# while doing emp_1.raise_amount these instance are accessing the variable value from the Class itself
print "Value of class variable in instances and classes--->", emp_1.raise_amount, Employee.raise_amount, emp_2.raise_amount
print "emp1 namespace--->",emp_1.__dict__ # no raise_amount here
print "Class namespace---> ",Employee.__dict__ # this has raise_amount

Employee.raise_amount = 1.05 # this changes the value of variable throughout class and it's instances
print "Change in class variable--->",Employee.raise_amount

emp_1.raise_amount = 1.06 # this only change for emp1 not the entire class
print Employee.raise_amount # output: 1.05
print emp_1.raise_amount # output: 1.06
print emp_1.__dict__    # {'pay': 50000, 'raise_amount': 1.06, 'last': 'Giri', 'email': 'Sagar.Giri@company.com', 'first': 'Sagar'}
print emp_2.raise_amount # output: 1.05

print Employee.num_of_emps # returns 2 because for each instance, number was increased
