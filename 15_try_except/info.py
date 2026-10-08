# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# print(x) # This statement will raise an error, because x is not defined

# Try block raises an error, the except block will be executed.
try:
    print(x)
except:
    print("An error occurred")

# Many Exceptions
# We can define my exception block as we want, e.g. if we want to excute a special blobk of code for a special kind of error:

# Print one message if the try block raises a NameError and another for other errors
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Else
# We can use the else keyword to define a block of code to be executed if no errors were raised
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
# This can be used to close open files, database connections, etc.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")   

# Raise an exception
# As a Python developer we can choose to throw an exception if a condition occurs
# To throw (or raise) an exception, use the raise keyword.

# Raise an error and stop the program if x is lower than 0
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

# Raise a TypeError if the type of the variable is wrong:
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
    
