__author__ = "girisagar46@gmail.com"


import datetime

"""
Regular methods: takes 'self' instance as first argument

Class method: takes class as a first argument. We use @classmethod decorator to turn regular to class method by using
'cls' instead of 'self'

Static method: don't take anything automatically (self or cls)
"""


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        """
        creates a instance of a Employee
        :param first: str
        :param last: str
        :param pay: int
        """
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@company.com"
        Employee.num_of_emps += 1

    def fullname(self):
        """
        return full name of an employee
        :return: str
        """
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        """
        apply raise to employee payment
        :return: None
        """
        self.pay = int(self.pay * self.raise_amount)

    # in classmethod, we work with the class instead of instance
    @classmethod # decorator
    def set_raise_amount(cls, amount): # cls is convention for class variable
        """
        set_raise_amount is used when we need to set raise amount for different employee according to rank
        :param amount: float
        :return: None
        """
        cls.raise_amount = amount

    # we can use classmethod to develop our own alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        """
        when our emp string comes in the format of "first-last-salary",
        we can use the classmethod to create new class
        :param emp_str: str
        :return: Employee instance
        """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # this creates new employee

    # we create static methods if the method is not dependent on any specific instance.
    # here is_workday() method is logically linked to Employee class
    @staticmethod
    def is_workday(day): # won't take cls or self as argument
        """
        check whether is a workday or not
        :param day: date
        :return: boolean
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Sagar", "Giri", 50000)
emp_2 = Employee("Test", "User", 60000)

# this changes the value of class variable
# because we are now working with the class instead of instance
# we can run class method from our instance like emp_1.set_raise_amount(1.06) but that doesn't make sense
Employee.set_raise_amount(1.06) # equivalent to: Employee.raise_amount = 1.06
print Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount # ouputs: 1.06


emp_str_1 = 'Tony-Stark-500000'
emp_str_2 = 'Bruce-Wane-600000'

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
print new_emp_1.__dict__ # {'pay': '500000', 'last': 'Stark', 'email': 'Tony.Stark@company.com', 'first': 'Tony'}
print Employee.num_of_emps # outputs: 4

my_date = datetime.date(2016, 7, 11)
print "Is workday-> ",Employee.is_workday(my_date) # calling is_workday staticmethod from Class itself