# This is the code for inheritance in Python.

class Person:
    ''' Base Class '''
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return self.firstname + " " + self.lastname

class Employee(Person):
    ''' Derived Class '''
    def __init__(self, first, last, staffnum):
        # Person.__init__(self,first,last)
        # super().__init__(first,last)
        super(Employee, self).__init__(first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber

x = Person("Steve", "Jobs")
y = Employee("Tim", "Cook", "s123456")

print (x.Name())
print (y.GetEmployee())
