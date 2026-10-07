# Set
# Sets are used to store multiple items in a single variable.
# Sets are used to store multiple items in a single variable.
# Do not allow duplicate values
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Duplicates Not Allowed
# Duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates
# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:
# True and 1 is considered the same value
# False and 0 is considered the same value
thisset = {"apple", "banana", "cherry", True, 1, 2, False, 0}
print(thisset)

# Get the Length of a Set
# To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data Types
# Set items can be of any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types
set1 = {"abc", 34, True, 40, "male"}

# type()
# From Python's perspective, sets are defined as objects with the data type 'set':
# <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)