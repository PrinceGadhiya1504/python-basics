print('\n-----Space formatting-----')
name = "Prince"
# print() mein extra space kahan se aati hai?
# Python print() ka default separator sep=" " hota hai. Yaani multiple arguments ke beech Python apni taraf se ek space add karta hai.
# Extra space manage karne ke 3 methods
# Method 1 — F-string (recommended)
print(f"Name: {name}")
# Method 2 - sep=""
print("Name: ", name, sep="")
print("Name: ", name) # Without sep="", it will add extra space
# Method 3 — + operator
print("Name: " + name)

# For input we use input() function
# For output we use print() function

name = input("What is your name? ")
age = (input("What is your age? "))
print("Hello", name)
print("Your age is", age)

# The default return type of the input() function in Python is a string (str)
print(type(name))
print(type(age))

# We can change the user input from default string type to any other type (int, float, etc) by typecasting.
num1 = int(input("Enter a number: "))
print(num1, type(num1))

