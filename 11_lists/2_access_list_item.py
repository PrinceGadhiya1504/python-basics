# Access Items
# List items are indexed and we can access them by referring to the index number
# The first item has index 0
# Print the second item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
# We can specify a range of indexes by specifying where the range starts and ends
# Note that the item included will be last
# Print the list from the second item to the third item
# Note: The search will start at index 2 (included) and end at index 5 (not included)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Range of Negative Indexes
# Note: The search will start at index -4 (included) and end at index -1 (not included)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# By leaving out the start value, the range will start at the first item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# By leaving out the end value, the range will go on to the end of the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
