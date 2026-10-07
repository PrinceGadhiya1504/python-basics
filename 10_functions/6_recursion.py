# Recursion is when a function calls itself

# A simple recursive function that counts down from 5:
def countdown(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        countdown(n-1)

countdown(5)

# Base Case and Recursive Case
# Every recursive function must have two parts:
# A base case - A condition that stops the recursion
# A recursive case - The function calling itself with a modified argument
# Without a base case, the function would call itself forever, causing a stack overflow error.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# Recursion with Lists
# Calculate the sum of all elements in a list
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

# Find the maximum value in a list
def max_number(number):
    if len(number) == 1:
        return number[0]
    else:
        #  # with max method
        # return max(number[0], max_number(number[1:]))

        # without max method
        max_val = max_number(number[1:])
        return number[0] if number[0] > max_val else max_val

my_numbers = [1, 5, 2, 9, 3]
print(max_number(my_numbers))
    
