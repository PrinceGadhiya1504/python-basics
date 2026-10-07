# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# Note: The remove() method will raise an error if the specified item does not exist.
# The discard() method will NOT raise an error if the specified item does not exist.
thisset.discard("banana")
print(thisset)

# You can also use the pop() method to remove an item, but this method will remove a random item, 
# so you cannot be sure what item that gets removed.
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
thisset = {"apple", "banana", "cherry"}
removed_item = thisset.pop()
print(removed_item)
print(thisset)

# The clear() method removes all items from the set.
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword also removes the set entirely.
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) # raise an error because the set is deleted
