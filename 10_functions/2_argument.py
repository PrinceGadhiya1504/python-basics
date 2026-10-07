# Information can be passed into functions as arguments
# Arguments are specified after the function name, inside the parentheses. we can add as many arguments as we want, just separate them with a comma.

# Example:

def name(username):
  print(f"Hello {username}!")

name("Prince")
name("Harshil")
name("Mayur")

# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called

def my_function(name): # name is a parameter
  print("Hello", name)
my_function("Prince") # "Prince" is an argument

# Number of Arguments
# If your function expects 2 arguments, you must call it with exactly 2 arguments.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Prince", "Gadhiya")

# Default Parameter Values
# You can assign default values to parameters. If the function is called without an argument, it uses the default value
def my_function(country = "India"):
  print("I am from ", country)
my_function("America")
my_function()

# Keyword Arguments
# Arguments are sent to function with the keyword word - this way the order of the arguments does not matter.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function(lname = "Gadhiya", fname = "Prince")

# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Tommy")

# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.
# However, positional arguments must come before keyword arguments

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Prince", lname = "Gadhiya") # Correct: positional (fname) before keyword (lname)
# my_function(lname = "Gadhiya", "Prince") # Error: positional argument after keyword argument

# Passing Different Data Types
# We can send any data type as an argument to a function (string, number, list, dictionary, etc.).
# The data type will be preserved inside the function
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"] #Sending a list as an argument
my_function(my_fruits)

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Prince", "age": 23} #Sending a dictionary as an argument
my_function(my_person)

# Return Values
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# Returning Different Data Types
# Functions can return any data type, including lists, tuples, dictionaries, and more
def my_function():
  return ["apple", "banana", "cherry"] #returns a list

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function():
  return (10, 20)  #returns a tuple

x, y = my_function()
print("x:", x)
print("y:", y)

def my_function():
  return {"name": "Prince", "age": 23}  #returns a dictionary

person = my_function()
print("Name:", person["name"])
print("Age:", person["age"])

# *args and **kwargs
# By default, a function must be called with the correct number of arguments.
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.

# # Arbitrary Arguments - *args
# The *args syntax allows a function to accept a variable number of positional arguments
# These arguments are passed as a tuple inside the function

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Prince", "Gadhiya", "Jamnagar")

# Using *args with Regular Arguments
# We can combine regular parameters with *args.
# Regular parameters must come before *args
def my_function(fname, *args):
  for name in args:
    print(fname, name)

my_function("Prince", "Gadhiya", "Jamnagar")

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly
def my_function(**kwargs):
  print("Type:", type(kwargs))
  print("Name:", kwargs["name"])
  print("Age:", kwargs["age"])
  print("All data:", kwargs)

my_function(name = "Prince", age = 23, city = "Jamnagar")

# Using **kwargs with Regular Arguments
# We can combine regular parameters with **kwargs.
# Regular parameters must come before **kwargs
def my_function(fname, **kwargs):
  print("First Name:", fname)
  print("All data:", kwargs)

my_function("Prince", name = "Gadhiya", age = 23, city = "Jamnagar")

# Combining *args and **kwargs
# We can use both *args and **kwargs in the same function.
# The order must be:
# regular parameters
# *args
# **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Prince", "Patel", age = 23, city = "Jamnagar")