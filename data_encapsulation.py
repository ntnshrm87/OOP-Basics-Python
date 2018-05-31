''' Data Encapsulation '''
# It refers to the restriction of access to methods and variables defined.
# This prevent direct modification.
# This can be done using single underscore or double underscore.


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

class CEO(Employee):
    def __init__(self, first, last, age, staffnum, uId):
        super().__init__(first, last, age, staffnum)
        self.__uId = uId

    def __str__(self):
        return super().__str__() + ", and uId: " + self.__uId

    def change_uId(self, new_uid):
        self.__uId = new_uid


x = Person("Prabhakant", "Sinha", 23)
y = Employee("Andrius", "Zoltners", 28, "s868354")
z = Employee("Nitin", "Sharma", 24, "XXXXXXX").__str__("GID354673")
c = Client("Chris", "Sanders", 31, "CID647221")
d = CEO("Chris", "Wright", "30", "s621601", "uid007ceo")

print (x)
print (y)
print (z)
print (c)
print (d)

# trying to change uId directly
d.__uid = "uid006ceo"
print(d.__str__())

# trying to change uId using a function
d.change_uId("uid786ceo")
print(d.__str__())
