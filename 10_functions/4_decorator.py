# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

# Define the decorator first, then apply it with @decorator_name above the function.

# Example
# A basic decorator that uppercases the return value of the decorated function.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())
# By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
# The function changecase is the decorator.
# The function myfunction is the function that gets decorated.


# Multiple Decorator Calls
# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())

# Arguments in the Decorated Function
# Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam
print(myfunction("Prince"))

# Multiple arguments in the Decorated Function

def changecase(func):
  def myinner(x, y):
    return func(x, y).upper()
  return myinner

@changecase
def myfunction(nam1, nam2):
  return "Hello " + nam1 + " " + nam2
print(myfunction("Prince", "Patel"))

# *args and **kwargs
def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("Prince"))

# Decorator With Arguments
# Decorators can accept their own arguments by adding another wrapper level
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Prince"

print(myfunction())

# Multiple Decorators
# You can use multiple decorators on one function.
# This is done by placing the decorator calls on top of each other.
# Decorators are called in the reverse order, starting with the one closest to the function.
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Prince"

print(myfunction())

# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
# Normally, a function's name can be returned with the __name__ attribute
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# Try returning the name from a decorated function and you will not get the same result
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)