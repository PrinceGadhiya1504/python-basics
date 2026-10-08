# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# To create a module just save the code you want in a file with the file extension .py

# Created a new file for module with mymodule.py name

# Use a Module
# Now we can use the module we just created, by using the import statement
# Note: When using a function from a module, use the syntax: module_name.function_name.
import mymodule
mymodule.myName("Prince Gadhiya")

# Variables in Module
# Module can also support array, dictionaries, object etc.
# Import the module named mymodule, and access the person1 dictionary
import mymodule
a = mymodule.person1["age"]
print(a)

# Naming a Module
# We can name the module file whatever we like, but it must have the file extension .py

# Re-naming a Module
# We can create an alias when we import a module, by using the as keyword
import mymodule as mx
mx.myName("Prince Gadhiya")

# Built-in Modules
# There are several built-in modules in Python, which we can import whenever we like
import platform
x = platform.system()
print(x)

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function
# List all the defined names belonging to the platform module
import platform
x = dir(platform)
print(x)

# Import From Module
# We can choose to import only parts from a module, by using the from keyword
# Import only the person1 dictionary from the module
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]
from mymodule import person1
print (person1["age"])