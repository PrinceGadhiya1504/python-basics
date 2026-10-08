# Iterator
# An iterator is an object that gives us values one by one.
# Instead of getting all values at once, an iterator remembers
# its current position and gives us the next value when we ask for it.

# We use:
    # iter()  -> to create/get an iterator
    # next()  -> to get the next value

# Example:
numbers = [10, 20, 30]
iterator = iter(numbers)

print(next(iterator)) # 10
print(next(iterator)) # 20
print(next(iterator)) # 30
# print(next(iterator)) # StopIteration

# Iterable
# Before understanding Iterator, we need to understand Iterable.
# An Iterable is an object whose values can be accessed one by one.
# In simple words:
# Iterable = Something that we can loop over.
# Examples of Iterable:
    # list
    # tuple
    # string
    # set
    # dictionary
    # range

numbers = [10, 20, 30]
for num in numbers:
    print(num)
# Output:
# 10
# 20
# 30
#
# The list is an Iterable because we can loop over it.

# String is also an Iterable
string = "Hello"
for char in string:
    print(char)
# Output:
# H
# e
# l
# l
# o

# Creating an Iterator using iter()
# We can use the iter() function to get an Iterator from an Iterable.

numbers = [10, 20, 30]
iterator = iter(numbers)
print(iterator)
# Now:
    # numbers  -> Iterable
    # iterator -> Iterator

# Using next()
# The next() function returns the next value from an Iterator.
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator)) # 10
print(next(iterator)) # 20
print(next(iterator)) # 30
# Every time we call next(), the iterator moves forward.

# Iterator remembers its current position
# An Iterator remembers where it currently is.
print("---Print only 2 numbers---")
numbers = [10, 20, 30, 40]
iterator = iter(numbers)
print(next(iterator))   # 10
print(next(iterator))   # 20
print('---use For loop---')
for num in iterator:
    print(num)
# Output:
# 30
# 40
# The iterator does not start from the beginning every time.

# StopIteration
# What happens when the Iterator has no more values?
# Python raises a StopIteration exception.
numbers = [10, 20, 30]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# There are no more values now.
# print(next(iterator))
# The last line would raise:
# StopIteration
# StopIteration means:
# "There are no more values in this iterator."

# Handling StopIteration
# We can handle StopIteration using try/except.
numbers = [10, 20, 30]
iterator = iter(numbers)
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("No more values")
# Output:
# 10
# 20
# 30
# No more values

# How for loop uses Iterator
# When we use a for loop, Python internally uses the Iterator concept.
numbers = [10, 20, 30]
for number in numbers:
    print(number)
# Conceptually, Python does something similar to:
# iterator = iter(numbers)
# next(iterator)
# next(iterator)
# next(iterator)
# When there are no more values:
# StopIteration
# The for loop handles StopIteration automatically.


# Iterable vs Iterator
# Iterable:
    # An Iterable is an object that we can iterate over.
    # Examples:
    # list
        # tuple
        # string
        # set
        # dictionary
        # range
# Iterator:
    # An Iterator is an object that gives us the next value one by one.
    # We can get an Iterator from an Iterable using iter().

numbers = [10, 20, 30] # Iterable
iterator = iter(numbers) # Iterator
print(iterator) # <list_iterator object at 0x...>

# Checking Iterable and Iterator
numbers = [10, 20, 30]
iterator = iter(numbers)
print(hasattr(numbers, "__iter__")) # True (Iterable has __iter__)
print(hasattr(numbers, "__next__")) # False (Iterable does not have __next__)
print(hasattr(iterator, "__iter__")) # True (Iterator also has __iter__)
print(hasattr(iterator, "__next__")) # True (Iterator has __next__)

# Iterator Protocol
# __iter__() # Returns the iterator object.
# __next__() # Returns the next value. Raises StopIteration when no more values.

# Custom Iterator
# Custom Iterator# We can create our own Iterator using a class.
print("---Custom Iterator---")
class Mynumbers:
    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

num = Mynumbers()
iterator = iter(num)
# With for loop
print("---With for loop---")
for number in Mynumbers():
    print(number)
# The for loop automatically handles StopIteration.

# Manualy using next()
print("---Manualy using next()---")
print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5
print(next(iterator)) # StopIteration

