# Python has a set of built-in methods that you can use on strings.

# 1. Upper Case
# The upper() method returns the string in upper case
a = "Hello, World!"
print(a.upper())

# 2. Lower Case
# The lower() method returns the string in lower case
a = "Hello, World!"
print(a.lower())

# 3. Remove whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end
a = " Hello, World!   "
print(a.strip())

# 4. Replace String
# The replace() method replaces a specified phrase with another specified phrase.
a = "Hello, World!"
print(a.replace("World", "Python"))

# 5. Split String
# The split() method splits the string into a list.
a = "Hello, World!"
print(a.split(","))
