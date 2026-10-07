# 1. append() => Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# 2. clear() => Removes all the elements from the list
fruits.clear()
print(fruits)

# 3. copy() => Returns a copy of the list
fruits = ['apple', 'banana', 'cherry']
mylist = fruits.copy()
print(mylist)

# 4. count() => Returns the number of times an element appears in the list
fruits = ['apple', 'banana', 'cherry', 'apple', 'banana', 'apple']
print(fruits.count("apple"))

# 5. extend() => Adds all the elements from one list to another
fruits = ['apple', 'banana', 'cherry']
mylist = ['orange', 'mango', 'kiwi']
fruits.extend(mylist)
print(fruits)

# 6. index() => Returns the index of the first occurrence of an element
fruits = ['apple', 'banana', 'cherry', 'banana']
print(fruits.index("banana"))

# 7. insert() => Inserts an element at a specific index
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# 8. pop() => Removes and returns the element at a specific index (default is the last element)
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# 9. remove() => Removes the first occurrence of a specific value
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove("banana")
print(fruits)

# 10. reverse() => Reverses the order of the elements
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# 11. sort() => Sorts the list in ascending order
fruits = ['apple', 'banana', 'cherry']
fruits.sort()
print(fruits)

# 12. sort() => Sorts the list in descending order
fruits = ['apple', 'banana', 'cherry']
fruits.sort(reverse=True)
print(fruits)

# 13. sorted() => Returns a new sorted list (original list is unchanged)
fruits = ['apple', 'banana', 'cherry']
mylist = sorted(fruits)
print(mylist)

# 14. sum() => Returns the sum of all elements in the list
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

# 15. max() => Returns the largest element in the list
numbers = [1, 2, 3, 4, 5]
print(max(numbers))

# 16. min() => Returns the smallest element in the list
numbers = [1, 2, 3, 4, 5]
print(min(numbers))

# 17. len() => Returns the number of elements in the list
fruits = ['apple', 'banana', 'cherry']
print(len(fruits))

# 18. list() => Creates a new list from an iterable
mylist = list("apple")
print(mylist)
