# 1. Lambda
# Lambda is a small anonymous function.
# Anonymous means the function does not need to have a normal function name.
# A lambda function is useful when we need a small function for a short/simple operation.

# 2. Lambda Syntax
# Basic syntax:
    # lambda arguments: expression

square = lambda x : x * x
print(square(5)) # 25

# 3. Lambda VS Normal Functoin
# Normal Function
def add(x, y):
    return x + y

# lambda Functoin
add = lambda x, y : x + y

# Both perform the same operation.
print(add(10, 20)) # 30

# 4. Lambda with no arguments
# A lambda function can have no arguments.
hello = lambda: "Hello Python"
print(hello())

# 5. lambda with one arguments
double = lambda x : x * 5
print(double(2)) 

# 6. lambda with multiple arguments 
total = lambda a, b, c : a + b + c
print(total(10, 20, 30))

# 7. lambda with default arguments
add_default = lambda a, b = 20 : a + b
print(add_default(20))
print(add_default(20, 30))


