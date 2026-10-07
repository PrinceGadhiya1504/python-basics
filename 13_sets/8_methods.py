# 1. add()
# Adds an element to the set
set1 = {1, 2, 3}
set1.add(4)
print(set1)

# 2. clear()
# Removes all the elements from the set
set1.clear()
print(set1)

# 3. copy()
# Returns a copy of the set
set1 = {1, 2, 3}
set2 = set1.copy()
print(set2)
print(set1)

# 4. difference()
# Sortcut -
# Returns a new set with the difference between two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.difference(set2))

# 5. difference_update()
# Shortcut -= 
# Removes the difference between two sets from the original set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)

# 6. discard()
# Removes an element from the set if it is present
set1 = {1, 2, 3}
set1.discard(2)
print(set1)

# 7. intersection()
# Sortcut &
# Returns a new set with the intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))

# 8. intersection_update()
# Shortcut &= 
# Removes the intersection of two sets from the original set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)

# 9. isdisjoint()
# Returns True if there is NO intersection between two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.isdisjoint(set2))

# 10. issubset()
# Sortcut <= and <
# Returns True if all elements in one set are present in another
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))

# 11. issuperset()
# Shortcut >= and >
# Returns True if all elements in one set are present in another
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3}
print(set1.issuperset(set2))

# 12. pop()
# Removes and returns an arbitrary element from the set
set1 = {1, 2, 3}
print(set1.pop())
print(set1)

# 13. remove()
# Removes an element from the set if it is present
set1 = {1, 2, 3}
set1.remove(2)
print(set1)

# 14. symmetric_difference()
# Sortcut ^ 
# Returns a new set with the symmetric difference of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))

# 15. symmetric_difference_update()
# Shortcut ^=
# Removes the symmetric difference of two sets from the original set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)

# 16. union()
# Shortcut |
# Returns a new set with all elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

# 17. update()
# Shortcut |= 
# Adds all elements from one set to the original set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)