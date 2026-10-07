# 1. clear()
# Removes all the elements from the dictionary
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
print(thisdict.clear())

# 2. copy()
# Returns a copy of the dictionary
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
print(thisdict.copy())

# 3. fromkeys()
# Returns a dictionary with the specified keys and values
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# 4. get()
# Returns the value of the specified key
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
print(thisdict.get("brand"))

# 5. items()
# Returns a list containing a tuple for each key value pair
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
print(thisdict.items())

# 6. keys()
# Returns a list containing the dictionary's keys
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
print(thisdict.keys())

# 7. pop()
# Removes the element with the specified key
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
print(thisdict.pop("brand"))

# 8. popitem()
# Removes the last inserted key-value pair
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
print(thisdict.popitem())

# 9. setdefault()
# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
newdict = thisdict.setdefault("city", "Jamnagar")
print(newdict)
print(thisdict)

# 10. update()
# Updates the dictionary with the specified key-value pairs
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
thisdict.update({'color': 'White'})
print(thisdict)

# 11. values()
# Returns a list of all the values in the dictionary
thisdict = {
  "brand": "Hundai",
  "model": "Creta",
  "year": 2024,
  "color": "black",
  "isElectricCar": False
}
print(thisdict.values())