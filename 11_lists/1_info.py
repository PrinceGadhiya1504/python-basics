# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets

# Create a List
thisList = ["Apple", "Banana", "Pineapple"]
print(thisList)

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.
# Note: There are some list methods(append(), insert(), pop()) that will change the order, but in general: the order of the items will not change.
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
# Lists allow duplicate values. Lists can have the same item values multiple times.

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types
# List items can be of any data type:
# String, int and boolean data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]

# type()
# From Python's perspective, lists are defined as objects with the data type 'list'
# <class 'list'>

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
# We can also use the list() constructor to make a list.
mylist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(mylist)

