''' When a derived class is inheriting from so many of base classes '''


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

    def __str__(self, guestId=None):
        if guestId:
            return super().__str__() + ", with staff number: " + self.staffnumber + ", as Guest with ID: " + guestId
        else:
            return super().__str__() + ", with staff number: " + self.staffnumber


class Client(Person):
    def __init__(self, first, last, age, clientId):
        super().__init__(first, last, age)
        self.clientId = clientId

    def __str__(self):
        return super().__str__() + ", with client ID: " + self.clientId

x = Person("Prabhakant", "Sinha", 23)
y = Employee("Andrius", "Zoltners", 28, "s868354")
z = Employee("Nitin", "Sharma", 24, "XXXXXXX").__str__("GID354673")
c = Client("Chris", "Sanders", 31, "CID647221")

print (x)
print (y)
print (z)
print (c)
