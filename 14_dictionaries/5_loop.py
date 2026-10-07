# Loop Through a Dictionary
# We can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, 
# but there are methods to return the values as well.

thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}

# Print all key names in the dictionary, one by one
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])

# Another way to print all values in the dictionary, one by one
for x in thisdict.values():
  print(x)

# Print all keys names in the dictionary, one by one
for x in thisdict.keys():
  print(x)

# Print all key names and values in the dictionary, one by one using .items() method
for x, y in thisdict.items():
  print(x, y)