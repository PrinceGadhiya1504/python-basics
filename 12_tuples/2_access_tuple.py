# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets
# Print the second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Note: The first item has index [0], second item has index [1], and so on.

# Negative Indexing
# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
# Example
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
# Note: The search will start at index 2 (included) and end at index 5 (not included).
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# By leaving out the start value, the range will start at the first item
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# By leaving out the end value, the range will go on to the end of the tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")