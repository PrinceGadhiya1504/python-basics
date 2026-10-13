# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple

# Packing a tuple
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
# Tuple unpacking means taking the values from a tuple and assigning them to separate variables.
# Unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Note: The number of variables must match the number of values in the tuple, 
# if not, you must use an asterisk to collect the remaining values as a list.

# Using Asterisk *
# If you expect a variable to hold more than one value, assign an * to the variable name.
# The variable with * receives the remaining values as a LIST.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# Add a star to the variable in the beginning or the middle of the tuple, 
# and the values will be assigned to the variable as a list:
# Note: The first variable will receive only one value, regardless of the number of values in the tuple
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)