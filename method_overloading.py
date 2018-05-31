''' Method Overloading in Python '''

# Method Overloading is the ability to define the same method
# with the same name but with a different number of arguments
# and types. Its the ability of one function to perform
# different tasks, depending on the number of parameters or the
# types of the parameters
# Case 1: def sucessor(number):
#             return number + 1
# This is a very simple case for integer an float values
# Case 2:

class Person:
        def __init__(self, first, last, age):
            self.firstname = first
            self.lastname = last
            self.age = age

        def __str__(self):
            return self.firstname + " " + self.lastname + " " + str(self.age)

class Employee(Person):
        def __init__(self, first, last, age, staffnum):
            super().__init__(first, last, age)
            self.staffnumber = staffnum

        def __str__(self, guestId = None):
            if guestId:
                return super().__str__() + ", with staff number: " + self.staffnumber + ", as Guest with ID: " + guestId
            else:
                return super().__str__() + ", with staff number: " + self.staffnumber

x = Person("Abhishek", "Yadav", 24)
y = Employee("Akshay", "Raut", 28, "s621601")
z = Employee("Deepak", "Pant", 29, "sXXXXXX").__str__("GID234123")

print(x)
print(y)
print(z)
