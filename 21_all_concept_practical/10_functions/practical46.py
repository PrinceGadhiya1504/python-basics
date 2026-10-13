# Task
# 1. divide_numbers(a, b) function banao.
# 2. Agar b == 0 ho, to "Cannot divide by zero" return karo.
# 3. Otherwise, try-except use karke division ka result return karo.
# 4. Agar TypeError aaye, to "Invalid input" return karo.
# 5. Function ko in teen cases ke saath test karo:
#    - divide_numbers(10, 2)
#    - divide_numbers(10, 0)
#    - divide_numbers(10, "a")
# Expected output:
# 5.0
# Cannot divide by zero
# Invalid input

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        try:
            result = a / b
            return result
        except TypeError:
            return "Invalid input"

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, "a"))