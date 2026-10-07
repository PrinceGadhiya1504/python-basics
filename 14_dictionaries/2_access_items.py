# Accessing Items
# We can access the items of a dictionary by referring to its key name, inside square brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# There is also a method called get() that will give same result
print(thisdict.get("model"))

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
x = thisdict.keys()
print(x) #before the change
thisdict["color"] = "white"
print(x) #after the change

# Get Values
# The values() method will return a list of all the values in the dictionary.
thisdict.values()

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
x = thisdict.values()
print(x) #before the change
thisdict["year"] = 2020
print(x) #after the change

# Add a new item to the original dictionary, and see that the values list gets updated as well
car = {
"brand": "Hundai",
"model": "Verna",
"year": 2024
}
x = car.values()
print(x) #before the change
car["color"] = "black"
print(x) #after the change

# Get Items
# The items() method will return a list of all the key:value pairs in the dictionary.
x = thisdict.items()
print(x) #before the change
thisdict["color"] = "red"
print(x) #after the change

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")