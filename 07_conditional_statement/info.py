# Conditional statements are used to control the flow of execution in a program based on specific conditions. 
# They allow programs to execute different blocks of code depending on whether a condition evaluates to True or False.

#1. IF statement
# An "if statement" is written by using the if keyword.
# Python supports the usual logical conditions from mathematics
# The if statement evaluates a condition (an expression that results in True or False).
# If the condition is true, the code block inside the if statement is executed.
# If the condition is false, the code block is skipped.
a = 15
b = 5

if a > b:
    print("a is greater than b")


# 2. IF-ELSE statement
# The if-else statement is an extension of the if statement.
# It provides an alternative block of code to be executed when the condition is false.
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")

# 3. Nested if statement
# An if statement can also contain other if statements inside it.
x = 41

if x > 10:
    print("Above ten")
    if x > 20:
        print("and also above twenty!")
    else:
        print("but not above twenty.")
else:
    print("Below ten")

# 4. IF-ELIF-ELSE statement
# The if-elif-else statement is an extension of the if-else statement.
# It provides an alternative block of code to be executed when the condition is false.
# The elif statement is written by using the elif keyword.
a = 200
b = 33
c = 500

if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("a and b are equal")


# 5. Short Hand If
# If only one statement to execute, you can put it on the same line as the if statement.
a = 10
if a > 5: print("a is greater than 5")

# 6. Short Hand If ... Else
# If you have one statement for if and one for else,
# you can put them on the same line using a conditional expression
a = 2
b = 330
print("a") if a > b else print("b")


# 7. Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# 8. LOGIC OPERATORS
# and - True if both conditions are true
# or - True if at least one condition is true
# not - Reverses the result (True becomes False, False becomes True)

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are true")

if (a > b or a > c):
    print("At least one of the conditions is true")

if not (a > b):
    print("a is not greater than b")


age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")


# 9. TERNARY OPERATOR
# This is a shorthand for the if-else statement
a = 2
b = 1
print("A") if a > b else print("B")

# 10. pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
age = 20

if age < 18:
  pass # Add underage logic later
else:
  print("Access granted")