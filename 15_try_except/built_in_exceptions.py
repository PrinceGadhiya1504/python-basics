# 1. ArithmeticError
# ArithmeticError is a base class for errors related to
# numeric calculations.
# Important child exceptions:
  # ZeroDivisionError
  # OverflowError
  # FloatingPointError
# We normally handle the more specific exception instead of
# using ArithmeticError directly.
try:
    print(10 / 0)
except ArithmeticError:
    print("Error in calculation")
# Output:
# Error in calculation

# 1.1 ZeroDivisionError
# ZeroDivisionError occurs when we try to divide a number by zero.
# It can happen with:
  # / division
  # // floor division
  # % modulo
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
# Output:
# Cannot divide by zero

# 2. AssertionError()
# AssertionError occurs when an assert statement's condition is False.
# assert is commonly used for checking assumptions while
# debugging/testing code.

# If condition is True:
#     nothing happens

# If condition is False:
#     AssertionError occurs.

x = "Hello"
try:
    assert x == "hello"
except AssertionError:
    print("Assertion condition failed")
# Output:
# Assertion condition failed

# 3. AttributeError()
# AttributeError occurs when we try to access an attribute or method that an object does not have.
try:
    print(x.toUpperCase())
except AttributeError:
    print("String does not have toUpperCase() method")
# Output:
# String does not have toUpperCase() method


# 4. EOFError
#  EOFError occurs when input() reaches an end-of-file condition without receiving input.
# On Linux/macOS, Ctrl+D can send EOF.
# On Windows, Ctrl+Z followed by Enter is commonly used.
try:
  x = int(input("Enter a number: "))
except EOFError:
  print("Error in input")
except:
  print("Something else went wrong")

# 6. FloatingPointError()
# FloatingPointError is part of ArithmeticError.
# In normal Python code, FloatingPointError is currently
# not normally raised by ordinary floating-point calculations.
try:
    print(10 / 0.0)
except ZeroDivisionError:
    print("Cannot divide by zero")
except FloatingPointError:
    print("Floating point error")
# Therefore, do NOT use this example to demonstrate
# FloatingPointError
# print(10 / 0.0)
# It is actually ZeroDivisionError.


# 6. GeneratorExit
# GeneratorExit occurs when a generator is closed.
#  It can happen when generator.close() is called.
def my_generator():
    try:
        yield 1
        yield 2
        yield 3

    except GeneratorExit:
        print("Generator was closed")

gen = my_generator()
print(next(gen))
gen.close()
# Output:
# 1
# Generator was closed

# 7. ImportError
# ImportError occurs when an imported module does not exist.
try:
    from math import something_that_does_not_exist
except ImportError:
    print("Could not import the requested item")
# Output:
# Could not import the requested item

# 8. IndentationError
# IndentationError occurs when indentation is not correct.
try:
    def my_function():
      print("This will cause an error")
except IndentationError:
    print("Indentation error occurred")
# Output:
# Indentation error occurred

# 9. IndexError
#  IndexError occurs when we try to access an index that does not exist in a sequence such as a list or tuple.
numbers = [10, 20, 30]
try:
    print(numbers[5])
except IndexError:
    print("Index does not exist")
# Output:
# Index does not exist

# 10. KeyError
# KeyError occurs when we try to access a dictionary key
# that does not exist.
user = {
    "name": "Prince",
    "age": 23
}
try:
    print(user["email"])
except KeyError:
    print("Key does not exist")
# Output:
# Key does not exist

# 11. KeyboardInterrupt
# KeyboardInterrupt occurs when the user presses the "Interrupt"
# signal, usually Ctrl+C (or Ctrl+Z on Windows).
try:
    name = input("Enter your name: ")
except KeyboardInterrupt:
    print("\nInput cancelled by user")
# Output:
# Enter your name: 
# Input cancelled by user

# 12. LookupError
#  LookupError is a base class for errors that happen when a lookup operation fails.
# Important child exceptions:
  # KeyError
  # IndexError
try:
    print(numbers[10])
except LookupError:
    print("Lookup failed")
# Output:
# Lookup failed

# 13. MemoryError
# MemoryError occurs when an operation cannot get enough memory to continue.
try:
    data = [0] * 10**15
except MemoryError:
    print("Not enough memory")

# 14. NameError
# NameError occurs when Python cannot find a variable/name.
try:
    print(username)
except NameError:
    print("Variable does not exist")
# Output:
# Variable does not exist

# 15. UnboundLocalError
# UnboundLocalError is a child of NameError.
# It occurs when a local variable is referenced before it has been assigned a value inside a function.
def test():
    try:
        print(x)
        x = 10
    except UnboundLocalError:
        print("Local variable used before assignment")
test()

# 16. NotImplementedError
# NotImplementedError is commonly used in a base class when a method is expected to be implemented by a child class.
class Animal:
    def make_sound(self):
        raise NotImplementedError("Child class must implement this method")
class Dog (Animal):
    def make_sound(self):
        return "Woof!"
dog = Dog()
print(dog.make_sound())
# Output:
# Woof

# If we directly use Animal:
try:
    animal = Animal()
    animal.make_sound()
except NotImplementedError as error:
    print(error)
# Output:
# Child class must implement this method

# 17. OSError
# OSError occurs when an operating-system related operation fails.
# Common examples:
    # file not found
    # permission problem
    # invalid file path
    # OS-level I/O problem
try:
    file = open("file_that_does_not_exist.txt", "r")
except OSError:
    print("Operating system or file error")

# Output:
# Operating system or file error

# 18. OverflowError()
# This error is raised when the result of a calculation is too large to be stored in memory.
# IMPORTANT: It does NOT simply mean "result is too large to store in memory."
# It means the numeric result cannot be represented by the relevant numeric representation. 
import math
try:
    print(math.exp(1000))
except OverflowError:
    print("Calculation result is too large")
# Output:
# Calculation result is too large

# 19. ReferenceError
# ReferenceError occurs when a weak reference object refers to an object that 
# has been garbage collected (deleted).
# Weak references allow you to refer to an object without increasing its reference count.
import weakref
class User:
    pass
user = User()
proxy = weakref.proxy(user)
del user
try:
    print(proxy)
except ReferenceError:
    print("Referenced object no longer exists")
# Output:
# Referenced object no longer exists

# 20. RuntimeError
# RuntimeError is raised when an error occurs during runtime but does not fit a more specific built-in exception.
try:
    raise RuntimeError("Something went wrong during runtime")
except RuntimeError as error:
    print(error)
# Output:
# Something went wrong during runtime

# 21. StopIteration
# StopIteration indicates that an iterator has no more values.
numbers = iter([10, 20])
print(next(numbers))
print(next(numbers))
try:
    print(next(numbers))
except StopIteration:
    print("No more values")
# Output:
# 10
# 20
# No more values

# 22. SyntaxError
# yntaxError occurs when Python code does not follow Pthon's syntax rules.
# Example of incorrect code:
# if True
#     print("Hello")
# The colon ":" is missing.

# IMPORTANT:
# SyntaxError occurs while Python is parsing the code,
# so it normally cannot be caught using try/except
# in that same invalid source file.

# 23. TabError
# It occurs when tabs and spaces are used inconsistently for indentation.
try:
        print("This will cause an error")
except TabError:
    print("Tab error occurred")
# Output:
# Tab error occurred

# 24. SystemError
# SystemError indicates an internal error detected by the Python interpreter.
# It is uncommon in normal Python application code.
# It may occur because of a problem at a low-level interpreter/API level.
# Example:
# You normally should NOT intentionally create SystemError.
# If it occurs unexpectedly, check the Python version,
# third-party libraries, and interpreter environment.
#

# 25. SystemExit
# It is raised when the sys.exit() function is called
# Normally sys.exit() is used to stop a program.
import sys
try :
    sys.exit()
except SystemExit:
    print("Program is exiting")
# Output:
# Program is exiting

# 26. TypeError
# Raised when two different types are combined
try:
    result = "10" + 5
except TypeError:
    print("Can not combine string and int")
# Output:
# Can not combine string and int

# 27. ValueError
# Raise when type of value is correct, but the value itself is inappropriate
try:
    int("Hello")
except ValueError:
    print("Invalid value")
# Output:
# Invalid value

# Easy difference:
# TypeError  -> wrong type
# ValueError -> correct type, wrong value

# 28. UnicodeError
# UnicodeError is a base class for Unicode-related errors.
# Important child exceptions:
    # UnicodeEncodeError
    # UnicodeDecodeError
    # UnicodeTranslateError

# 29. UnicodeEncodeError
# UnicodeEncodeError occurs when a string cannot be encoded into bytes using the selected encoding.
text = "😀"
try:
    text.encode("ascii")
except UnicodeEncodeError:
    print("Text cannot be encoded using ASCII")
# Output:
# Text cannot be encoded using ASCII

# 30. UnicodeDecodeError
# UnicodeDecodeError occurs when bytes cannot be decoded using the selected encoding.
b = b'\xff'
try:
    b.decode("utf-8")
except UnicodeDecodeError:
    print("Bytes cannot be decoded using UTF-8")
# Output:
# Bytes cannot be decoded using UTF-8

# 31. UnicodeTranslateError
# UnicodeTranslateError occurs when characters cannot be translated during encoding/decoding.
text = "😀"
try:
    text.encode("ascii", errors="strict")
except UnicodeTranslateError:
    print("Character cannot be translated")
# Output:
# Character cannot be translated


# QUICK SUMMARY

# ArithmeticError
# -> Base class for arithmetic-related errors.
#
# AssertionError
# -> assert condition is False.
#
# AttributeError
# -> Object does not have requested attribute/method.
#
# EOFError
# -> input() reaches EOF without receiving data.
#
# FloatingPointError
# -> Currently not normally used by Python.
#
# GeneratorExit
# -> Generator/coroutine is closed.
#
# ImportError
# -> Problem importing a module/name.
#
# IndentationError
# -> Incorrect indentation.
#
# IndexError
# -> Sequence index does not exist.
#
# KeyError
# -> Dictionary key does not exist.
#
# KeyboardInterrupt
# -> User interrupts program, normally Ctrl+C.
#
# LookupError
# -> Base class for lookup errors such as IndexError
#    and KeyError.
#
# MemoryError
# -> Operation cannot get enough memory.
#
# NameError
# -> Name/variable cannot be found.
#
# UnboundLocalError
# -> Local variable used before it gets a value.
#
# NotImplementedError
# -> Base-class method requires implementation in child class.
#
# OSError
# -> Operating-system related operation fails.
#
# OverflowError
# -> Arithmetic result is too large to be represented.
#
# ReferenceError
# -> Weak reference refers to an object that no longer exists.
#
# RuntimeError
# -> Runtime error that does not fit another specific category.
#
# StopIteration
# -> Iterator has no more values.
#
# SyntaxError
# -> Python syntax is invalid.
#
# TabError
# -> Inconsistent tabs/spaces in indentation.
#
# SystemError
# -> Internal interpreter-level error.
#
# SystemExit
# -> sys.exit() is called.
#
# TypeError
# -> Operation/function receives an inappropriate type.
#
# UnicodeError
# -> Base class for Unicode-related errors.
#
# UnicodeEncodeError
# -> Unicode string cannot be encoded.
#
# UnicodeDecodeError
# -> Bytes cannot be decoded.
#
# UnicodeTranslateError
# -> Unicode translation fails.
#
# ValueError
# -> Correct type but inappropriate value.
#
# ZeroDivisionError
# -> Division/modulo by zero.




# MOST IMPORTANT EXCEPTIONS TO REMEMBER
# For normal Python development, focus especially on:
# 1. TypeError
# 2. ValueError
# 3. IndexError
# 4. KeyError
# 5. NameError
# 6. AttributeError
# 7. ZeroDivisionError
# 8. FileNotFoundError
# 9. ImportError / ModuleNotFoundError
# 10. OSError

# BaseException
# │
# ├── GeneratorExit
# ├── KeyboardInterrupt
# ├── SystemExit
# │
# └── Exception
#     │
#     ├── ArithmeticError
#     │   ├── FloatingPointError
#     │   ├── OverflowError
#     │   └── ZeroDivisionError
#     │
#     ├── LookupError
#     │   ├── IndexError
#     │   └── KeyError
#     │
#     ├── NameError
#     │   └── UnboundLocalError
#     │
#     ├── OSError
#     │
#     ├── RuntimeError
#     │   └── NotImplementedError
#     │
#     ├── SyntaxError
#     │   └── IndentationError
#     │       └── TabError
#     │
#     ├── UnicodeError
#     │   ├── UnicodeEncodeError
#     │   ├── UnicodeDecodeError
#     │   └── UnicodeTranslateError
#     │
#     ├── TypeError
#     └── ValueError