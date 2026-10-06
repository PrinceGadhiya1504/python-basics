# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

"""
Numeric Types       : 	int, float, complex
Sequence Types      : 	String, list, tuple
Dictionary Type     : 	dict
Set Types           : 	set
Boolean Type        : 	bool
"""

# You can get the data type of any object by using the type() function:
x = 5
print(type(x))

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
# String:
x = "Hello World"
# Float:
x = 20.5
# Complex:
x = 1j
# List:
x = ["apple", "banana", "cherry"]
# Tuple:
x = ("apple", "banana", "cherry")
# Dict:
x = {"name" : "John", "age" : 36}
# Set:
x = {"apple", "banana", "cherry"}
# Boolean:
x = True



# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))
x = bool(5)



# Differance List, Tuple, Dictionary, Set

# Feature 			        List	                    Tuple	                    Set	                        Dictionary
# Syntax			        Square brackets []	        Parentheses ()	            Curly braces {}	            Curly braces with pairs {k: v}
# Ordered			        Yes	                        Yes	                        No	                        Yes (Python 3.7+)
# Mutable (Modifiable)      Yes	                        No	                        Yes (add/remove items)	    Yes (values can change)
# Duplicates Allowed        Yes	                        Yes	                        No	                        No for Keys, Yes for Values
# Access Method		        Index-based (e.g., x[0])	Index-based (e.g., x[0])	No indexing (looping only)	Key-based (e.g., x['key'])