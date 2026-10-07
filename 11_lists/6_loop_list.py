# Loop Through a List
# We can loop through the list items by using a for loop
# Print all items in the list, one by one
thislist = ["Apple", "Ball", "Cat"]
for i in thislist:
    print(i)

# Loop Through the Index Numbers
# We can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using a While Loop
# We can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 
# and loop way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
thislist = ["Dog", "Elephant", "Fox"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists
# A short hand for loop that will print all items in a list
thislist = ["Bike", "Car", "Train"]
[print(x) for x in thislist]