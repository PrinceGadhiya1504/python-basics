# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "Pineapple"
x = tuple(y)
print(x)

# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
# Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, 
# add your item(s), and convert it back into a tuple.

tuple1 = ("apple", "banana", "cherry")
y = list(tuple1)
y.append("orange")
tuple1 = tuple(y)
print(tuple1)

# Add tuple to a tuple: You can add one tuple to another tuple by using the + operator.
tuple1 = ("apple", "banana", "cherry")
tuple2 = ("orange",)
tuple1 += tuple2
print(tuple1)

# Remove Items
# Note: You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
# Or you can delete the tuple completely
# The del keyword can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists