'''
# 01
name = input("Enter your name: ")
age = input("Enter your age: ")
mobile_no = input("Enter your mobile number: ")

print("Hello", name, "you are", age, "years old", "and your mobile number is", mobile_no)

# input 
#     Enter your name: Prince Patel
#     Enter your age: 23
#     Enter your mobile number: 9316143877
# output
#     Hello Prince Patel you are 23 years old and your mobile number is 9316143877

'''
# 02
# We can also take multiple inputs at once from the user in a single line,
# splitting the values entered by the user into separate variables for each value using the split() method

x, y = input("Enter two numbers: ").split()
print(x, y)

# input
#     Enter two numbers: 10 20
# output
#     10 20

# If we try to enter only single value then got the erro => ValueError: not enough values to unpack (expected 2, got 1)
