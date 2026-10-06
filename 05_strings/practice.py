# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# Quotes Inside Quotes
# use quotes inside a string, as long as they don't match the quotes surrounding the string
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings
# assign a multiline string to a variable by using three quotes
str1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(str1)

# Strings are Arrays
# Strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
str2 = "Hello"
print(str2[1])

#Looping Through a String
for x in str2:
  print(x)

# String Length
# Use the len() function to return the length of a string
print(len(str2))

#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is not present.")

  
