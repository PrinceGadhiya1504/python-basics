# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.
# Note: The self parameter is always the first parameter of the __init__() method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello " + self.name)

p1 = Person("Prince", 23)
p1.hello()

# Why Use self?
# Without self, Python would not know which object's properties you want to access
# The self parameter links the method to the specific object
class Person:
    def __init__(self, name):
        self.name = name
    def printname(self):
        print(self.name)

p1 = Person("Prince Gadhiya")
p2 = Person("Prince")
p1.printname()
p2.printname()

# self Does Not Have to Be Named "self"
# It does not have to be named self, we can call it whatever we like, but it has to be the first parameter of any method in the class
class Student:
    def __init__(std, name, class_no):
        std.name = name
        std.class_no = class_no
    def show(abc):
        print("Name: " + abc.name)
        print("Class: ", abc.class_no)
s1 = Student("Std 1", 5)
s2 = Student("Std 2", 6)
s1.show()
s2.show()
        
# Calling Methods with self
class Person:
    def __init__(self, name, age):
        self.name = name
    
    def printname(self):
        return "Hello " + self.name
    
    def welcom(self):
        message = self.printname()
        print(message + ", Welcome to the World of Python Object Oriented Programming")

p1 = Person("Prince", 23)
p1.welcom()
        