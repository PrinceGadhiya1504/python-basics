# Loops are used to execute a block of code repeatedly until a condition is met or all items in a sequence are processed
# two type of loops
    #1. for
    #2. while

#1. For loop
# A for loop is used to iterate over a sequence 
# like a list, tuple, dictionary, set, or string 
# It is typically chosen when you know 
# in advance how many times you need to repeat a task
# The loop continues until it has processed every item in the sequence.

# syntax : 
# for variable in sequence:
#     # code block to be executed

# Example 1: Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Iterate over a string
for char in "python":
    print(char)

#Range function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, 
# starting from 0 by default, 
# increments by 1 (by default), and 
# ends at a specified number.

# example 1
for i in range(6): # print 0 to 5
  print(i)


# Example 2
for i in range(2, 6): # print 2 to 5
    print(i)

# Example 3
for i in range(1, 10, 2): # print 1 to 9 odd number => If we add number 5 then increment with 5
    print(i)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Nested loop
# A nested loop is a loop inside a loop
for i in range(3):
    for j in range(2):
        print(i, j)

#2. While loop
# A while loop is used to execute a block of code 
# repeatedly as long as a certain condition is true.
# It is typically chosen when you do not know in advance 
# how many times you need to repeat a task.
# The loop continues as long as the condition remains True.

# syntax : 
# while condition:
#     # code block to be executed

#Example 1: Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

#Example 2: 
count = 0
while count < 3:
    print("Inside loop")
    count += 1


#The break Statement
# With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#The else Statement
# With the else statement we can run a block of code once when the condition no longer is true
# Note: The else block will NOT be executed if the loop is stopped by a break statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
    

