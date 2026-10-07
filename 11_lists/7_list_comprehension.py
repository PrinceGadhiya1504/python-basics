# List comprehension offers a shorter syntax when we want to create a new list based on the values of an existing list.
# Syntax: [expression for item in iterable]
thislist = ["apple", "banana", "cherry"]
newlist = [x for x in thislist]
print(newlist)

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#With list comprehension you can do all that with only one line of code
#The Syntax
#newlist = [expression for item in iterable if condition == True]
#The return value is a new list, leaving the old list unchanged.
newlist = [x for x in fruits if 'a' in x]
print(newlist)

# The condition is like a filter that only accepts the items that evaluate to True.
# Only accept items that are not "apple"
newlist = [x for x in fruits if x != 'apple']
print(newlist)

# The condition is optional and can be omitted
newlist = [x for x in fruits]
print(newlist)

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable
newlist = [x for x in range(10)]
print(newlist)

# Accept only numbers lower than 5
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Using an expression
# Set the values in the new list to upper case
newlist = [x.upper() for x in fruits]
print(newlist)

# We can set the outcome to whatever you like
# Set all values in the new list to 'hello'
newlist = ['hello' for x in fruits]
print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
# Return "orange" instead of "banana"
# "Return the item if it is not banana, if it is banana return orange".
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)