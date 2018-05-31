# Method overriding is an object oriented programming feature that
# allows a subclass to provide a different implementation of a
# method that is already defined by its superclassor by one of its
# superclasses. The implementation in the subclass overrides the
# implementation of the superclass by providing a method with the
# same name, same parameters, or signature and same return type as
# the method of the parent class.
# Here the overriden methods are __str__ and __init__

class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + str(self.age)

class Employee(Person):
    def __init__(self,first,last,age,staffnum):
        super().__init__(first, last, age)
        self.staffnumber = staffnum

    def __str__(self):
        return super().__str__() + ", " +self.staffnumber

x = Person("Abhishek", "Yadav", 24)
y = Employee("Akshay", "Raut", 28, "s621601")

print(x)
print(y)
