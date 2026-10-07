# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Create a dictionary that contain three dictionaries
myfamily = {
  "child1" : {
    "name" : "Abc",
    "year" : 2004
  },
  "child2" : {
    "name" : "Def",
    "year" : 2007
  },
  "child3" : {
    "name" : "Ghi",
    "year" : 2011
  }
}
print(myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {
  "name" : "Abc",
  "year" : 2004
}
child2 = {
  "name" : "Def",
  "year" : 2007
}
child3 = {
  "name" : "Ghi",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary
print(myfamily["child2"]["name"])

# Loop Through Nested Dictionaries
# We can loop through a dictionary by using the items() method like this
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

