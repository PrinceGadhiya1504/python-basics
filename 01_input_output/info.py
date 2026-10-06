# For the input will use input() function
# For the output will use print() function

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