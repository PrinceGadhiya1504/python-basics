# A variable is only available from inside the region it is created. This is called scope

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
  x = 100
  print(x)

myfunc()

# Function Inside Function
# The local variable can be accessed from a function within the function
def myfunc():
  x = 200
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
x = 300
def myfunc():
  print(x)

myfunc()
print(x)

#Naming Variables
# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in the global scope 
# (outside the function) and one available in the local scope (inside the function)
x = 400
def myfunc():
  x = 500
  print(x)

myfunc()
print(x)

#Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global
def myfunc():
  global x
  x = 600

myfunc()

print(x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = 700

def myfunc():
  global x
  x = 800

myfunc()
print(x)

# Nonlocal Keyword
# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
#change the value of parent scope from the child scope

def myfunc1():
  x = "Prince"
  def myfunc2():
    nonlocal x
    x = "Hello World"
  myfunc2()
  return x

print(myfunc1())

#The LEGB Rule
# Python follows the LEGB rule when looking up variable names, and searches for them in this order:
# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

# check first in current function if not found then check enclose if not found then check global if not found then check built-in
# Local -> Enclose -> Global -> Built-in

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)