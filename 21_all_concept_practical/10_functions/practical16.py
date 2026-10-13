# Task:
# 1. print_numbers(numbers) naam ka function banao.
# 2. Function ke andar for loop se list ke har number ko alag-alag print karo.
# 3. Function ko [10, 20, 30, 40] list ke saath call karo.

# Expected output:
# 10
# 20
# 30
# 40

def print_numbers(numbers):
    for number in numbers:
        print(number)

print_numbers([10, 20, 30, 40])