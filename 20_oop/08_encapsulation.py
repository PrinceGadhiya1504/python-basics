# Encapsulation is about protecting data inside a class.
# It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
# This prevents accidental changes to your data and hides the internal details of how your class works.

# Private Properties
# In Python, we can make properties private by using a double underscore __ prefix
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Prince", 25)
print(p1.name)
# print(p1.__age) # This will cause an error
# Note: Private properties cannot be accessed directly from outside the class.

# Get Private Property Value
# To access a private property, we can create a getter method:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Prince", 25)
print(p1.get_age())

# Set Private Property Value
# To modify a private property, we can create a setter method.
# The setter method can also validate the value before setting it:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Prince", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

# Why Use Encapsulation?
# Encapsulation provides several benefits:
    # Data Protection: Prevents accidental modification of data
    # Validation: You can validate data before setting it
    # Flexibility: Internal implementation can change without affecting external code
    # Control: You have full control over how data is accessed and modified

# Example
# Use encapsulation to protect and validate data:
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0

    def set_grade(self, grade):
        if 0 <= self.__grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade

    def get_status(self):
        if self.__grade >= 60:
            return "Pass"
        else:
            return "Fail"

student = Student("Prince")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())

# Private Methods
# Private methods are methods that cannot be accessed from outside the class. 
# They are defined with a double underscore __ prefix
# Note: Just like private properties with double underscores, private methods cannot be called directly from outside the class. 
# The __validate method can only be used by other methods inside the class.

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num): # Accessing private method
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error

