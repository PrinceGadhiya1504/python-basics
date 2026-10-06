# 01
# 1.1 Basic Assignment: Variables are assigned values using the = operator.
x = 5
y = 3.14
z = "Hello"

# 1.2 Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.
x = 10
print(x, type(x))
x = "Now a string"
print(x, type(x))
x = 5.5
print(x, type(x))

# 1.3 Assigning Same Value: Same value can be assigned to multiple variables in a single line.
a = b = c = 10
print("Same value", a, b, c)

# 1.4 Assigning Different Values: Different values can be assigned to multiple variables in a single line.
x, y, z = 10, 20, 30
print("Different values", x, y, z)

# 1.5 Can also use the + operator to output multiple values
# Note: the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



# 02
# Global Variables

# 2.1 Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.

x = "2.1 awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# 2.2 If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.

x = "2.2 awesome"

def myfunc():
  x = "fantastic"  # local variable
  print("Python is " + x)

myfunc()

#03
# The global Keyword

# 3.1 Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def myfunc():
  global x
  x = "3.1 fantastic"

myfunc()

print("Python is " + x)

# 3.2 Also, use the global keyword if you want to change a global variable inside a function.
# Without the global keyword, the variable x would remain local, and can only be used inside the function.

x = "3.2 awesome"

def myfunc():
  global x
  x = "3.2 fantastic"

myfunc()

print("Python is " + x)