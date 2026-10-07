# Loop Through a Tuple
# You can loop through the tuple items by using a for loop.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.
# Use range() and the len() function to create a suitable iterable.

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# While Loop
# You can use a while loop with the len() function and an index counter.

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1