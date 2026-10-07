# Tuple
# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples can also be created without the parentheses
thistuple = "apple", "banana", "cherry"
print(thistuple)

# Note: If you create a tuple with only one item, you must add a comma after the item.
# A tuple with one item looks like this:
thistuple = ("apple",)
print(thistuple)
print(type(thistuple))

# Not like this:
thistuple = ("apple")
print(thistuple)
print(type(thistuple))

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# Allow Duplicates
# Since tuples are indexed, they can have items with the same value
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple length
# Get the number of items in a tuple:
print(len(thistuple))

# Create an Empty Tuple
thistuple = ()
print(type(thistuple))

# Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")

# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple'
# <class 'tuple'>
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)