# Python frozenset
# frozenset is an immutable version of a set.
#  "Immutable" means: Once a frozenset is created, we cannot change its elements.

# We cannot:
# - add a new element
# - remove an element
# - update existing elements

# Like a normal set:
# - frozenset stores unique values
# - frozenset is unordered
# - frozenset does not support indexing

# The main difference is:
# set       -> mutable
# frozenset -> immutable


# Set vs Frozenset
# Normal set:
my_set = {1, 2, 3}
# We can change it:
my_set.add(4)
print(my_set)
# Frozenset:
my_frozenset = frozenset({1, 2, 3})
# We CANNOT change it:
# my_frozenset.add(4)      # ERROR
# my_frozenset.remove(1)   # ERROR


# Creating a frozenset
# We use the frozenset() constructor to create a frozenset.
fruits = frozenset({"apple", "banana", "cherry"})
print(fruits)
print(type(fruits))

# We can also create a frozenset from a list.
numbers = frozenset([1, 2, 3, 4, 5])
print(numbers)

# We can create a frozenset from a tuple.
colors = frozenset(("red", "green", "blue"))
print(colors)

# Why do we use frozenset?
# If we have a collection of unique values that should not be
# changed accidentally, we can use a frozenset.
permissions = frozenset({"read", "write", "delete"})
print(permissions)
# We cannot add or remove permissions from this frozenset.

# Frozenset Methods
# Being immutable means you cannot add or remove elements. 
# However, frozensets support all non-mutating operations of sets.

# 1. copy() => Returns a shallow copy
fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)

# 2. difference()
# Sortcut -
# difference() returns the elements that are present in the first frozenset but NOT present in the second.
set1 = frozenset({1, 2, 3}) 
set2 = frozenset({3, 4, 5})
# print(set1 - set2)
print(set1.difference(set2))

# 3. intersection()
# Sortcut &
# Returns the values that are common between both frozensets.
set1 = frozenset({1, 2, 3})
set2 = frozenset({3, 4, 5})
# print(set1 & set2)
print(set1.intersection(set2))

# 4. isdisjoint()
# Returns True if there is NO intersection between two frozensets
set1 = frozenset({1, 2, 3})
set2 = frozenset({3, 4, 5})
print(set1.isdisjoint(set2))

# 5. issubset()
# Sortcut 	<= / <
# Returns True if all elements in one frozenset are present in another
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

# 6. issuperset()
# Sortcut 	>= / >
# Returns True if all elements of another frozenset are present in the current frozenset.
a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)

# 7. symmetric_difference()
# Sortcut ^
# Returns elements that are present in either frozenset, but NOT in both.
# In simple words: Remove the common values and keep the remaining values.
set1 = frozenset({1, 2, 3})
set2 = frozenset({3, 4, 5})
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 8. union()
# Sortcut |
# Returns a new frozenset with all items from both sets
# Duplicate values are automatically removed.
set1 = frozenset({1, 2, 3})
set2 = frozenset({3, 4, 5})
print(set1 | set2)
print(set1.union(set2))

# Important: These methods create a NEW frozenset
# Frozenset cannot be changed.
# So methods like:
    # union()
    # intersection()
    # difference()
    # symmetric_difference()
# do not modify the original frozenset.
# They return a new result.
# Original frozensets are still unchanged.