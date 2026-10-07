# Change Item Value
# We can change the value of a specific item in a list
# by using its index number.

# Syntax:
# list[index] = new_value

# Example:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values,
# and refer to the range of index numbers where you want to insert the new values
# Syntax:
# list[start:end] = new_values
# The start index is included.
# The end index is NOT included.

# note: consider [1:3] in 3 as second index not third index # 1....3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the second value by replacing it with two new values
# The number of new items does not have to be the same as the number of old items.
# We can replace one item with two or more items.
# When this happens, the length of the list increases.
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
# [1:2] selects only index 1.
# index 1 -> banana
# We replace banana with two new values.
print(thislist)
# Output:
# ['apple', 'blackcurrant', 'watermelon', 'cherry']


# Change the second and third value by replacing it with one value
# We can also replace multiple items with fewer items.
# When this happens, the length of the list decreases.
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
# ['banana', 'cherry']
# These two items are replaced with:
# ['watermelon']
print(thislist)
# Output:
# ['apple', 'watermelon']


# Insert Items
# The insert() method is used to add a new item at a specific position in a list.
# insert() does NOT replace an existing item.
# It adds a new item and moves the existing items to the right.

# Syntax:
# list.insert(index, value)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


## Simple understandig
# 1. list[1] = "new"
#    → existing item change

# 2. list[1:3] = [...]
#    → range ke items change

# 3. [1:3]
#    → index 1 included
#    → index 3 excluded

# 4. list.insert(2, "new")
#    → index 2 par new item add

# 5. list.append("new")
#    → list ke end mein new item add