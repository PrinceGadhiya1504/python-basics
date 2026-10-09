# Class Properties
# Properties are variables that belong to a class. They store data for each object created from the class.

# Create a class with properties:
class Person:
    def __init__(self, name, age):
        self.name = name # Properties
        self.age = age 
        
p1 = Person("Prince", 23)

# Access object properties using dot notation
print("Name: ", p1.name)
print("Age: ", p1.age)

# Modify object properties:
p1.name = "Gadhiya"
p1.age = 24
print("Name: ", p1.name)
print("Age: ", p1.age)

# Delete properties from objects using the del keyword
del p1.age
print(p1.name) # This works
# print(p1.age) # This would cause an error

# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects
print("-----------Class Properties vs Object Properties----------")
class Person:
    species = "Human" # Class property

    def __init__(self, name):
        self.name = name # Object property

p1 = Person("Mayur")
p2 = Person("Harshil")
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# Modifying Class Properties
print("\n-----------Modifying Class Properties----------")
class Person:
    lastname = ""

    def __init__(self, name):
        self.name = name

p1 = Person("Mayur")
p2 = Person("Harshil")

Person.lastname = "Gadhiya"

print(p1.lastname)
print(p1.name)
print(p2.lastname)

# Add New Properties
# Note: Adding properties this way only adds them to that specific object, not to all objects of the class.
print("\n-----------Add New Properties----------")
p2.lastname = "Patel"
print(p2.lastname)
