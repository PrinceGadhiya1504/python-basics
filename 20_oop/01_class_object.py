# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# To create a class, use the keyword class:
class MyClass:
    x = 5
# class name: MyClass
# property/attributes: x (value 5)

# Create Object
# Now we can use the class named MyClass to create objects:
obj = MyClass()
print(obj.x)

# Delete Objects
# We can delete objects by using the del keyword
del obj
# print(obj.x) # give error because object is deleted

# Multiple Objects
# Note: Each object is independent and has its own copy of the class properties.
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()

print(obj1.x)
print(obj2.x)
print(obj3.x)

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, 
# put in the pass statement to avoid getting an error.
class Car:
    pass
