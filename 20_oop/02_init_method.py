# The __init__() Method
# All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
# Note: The __init__() method is called automatically every time the class is being used to create a new object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Prince", 23)
print(p1.name)
print(p1.age)

# Why Use __init__()?
# Without the __init__() method, we would need to set properties manually for each object
# Create a class without __init__():
class Person:
    pass

p1 = Person()
p1.name = "Prince"
p1.age = 23
print(p1.name)
print(p1.age)


# Default Values in __init__()
# We can also set default values for parameters in the __init__() method
class Person:
    def __init__(self, name, age = 18):
        self.name = name
        self.age = age

p1 = Person("Person 1")
p2 = Person("Person 2", 22)
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

# Multiple Parameters
# The __init__() method can have as many parameters as we need
class Employee:
    def __init__(self, name, age, department, city):
        self.name = name
        self.age = age
        self.department = department
        self.city = city

emp1 = Employee("Prince", 23, "IT", "Mumbai")
print(emp1.name)
print(emp1.age)
print(emp1.department)
print(emp1.city)
        