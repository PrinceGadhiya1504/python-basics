# A generator is a special type of function that produces values
# one at a time instead of creating and storing all values at once.

# Generators use the "yield" keyword instead of "return".

# The main benefit of generators is that they are memory efficient
# because they generate values only when they are needed.

# A normal function usually uses "return" to return a value.
def normal_function():
    return 1

# A generator function uses "yield" to produce values one by one.
def generator_function():
    yield 1
    yield 2
    yield 3

# "yield" is the most important keyword in generators.
# yield:
    # 1. Produces a value
    # 2. Pauses the function
    # 3. Saves the current state of the function
    # 4. Allows the function to continue from the same point later

def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()
print(next(gen))

# The execution happens like this:
#
# First next():
#     yield 1
#     ↓
#     returns 1
#     ↓
#     function pauses
#
# Second next():
#     continues from where it paused
#     ↓
#     yield 2
#     ↓
#     returns 2
#     ↓
#     function pauses
#
# Third next():
#     continues from where it paused
#     ↓
#     yield 3
#     ↓
#     returns 3
#
# After all values are generated, the generator is finished.



# return VS yield
# return:
    # Returns a value
    # Immediately ends the function

# yield:
    # Produces a value
    # Pauses the function
    # Allows the function to continue later

# next() WITH A GENERATOR
# The next() function is used to get the next value
# from a generator.
def generate_numbers():
    yield 10
    yield 20
    yield 30

gen = generate_numbers()

print(next(gen))
# 10

print(next(gen))
# 20

print(next(gen))
# 30

# If we call next() again after the generator is finished,
# Python raises StopIteration.
# print(next(gen))
# This will raise:
# StopIteration
# Usually, we do not need to handle StopIteration manually.
# A for loop handles it automatically.

# GENERATOR WITH for LOOP
def generate_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for number in generate_numbers():
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5


# The for loop automatically gets the next value from
# the generator until the generator is finished.

# GENERATOR WITH range()
# We can use a generator with range() to generate numbers
# in a specific range without creating a full list.
def generate_numbers():
    for number in range(1, 6):
        yield number

for number in generate_numbers():
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5


# WHY DO WE USE GENERATORS?
# The main reason to use generators is memory efficiency.
# Suppose we need a very large number of values.
# A list stores all values in memory.
# A generator produces values one by one when needed.

numbers = [1, 2, 3, 4, 5]
print(numbers)

# Example using a generator:

def generate_numbers():
    for number in range(1, 6):
        yield number

numbers = generate_numbers()
print(numbers)

# The generator does not create all values at once.
# It generates each value when it is requested.

# GENERATOR WITH A LIST
def generate_users(users):
    for user in users:
        yield user

users = ["Prince", "Rahul", "Amit", "Jay"]

for user in generate_users(users):
    print(user)

# Output:
# Prince
# Rahul
# Amit
# Jay

# The generator gives one user at a time.