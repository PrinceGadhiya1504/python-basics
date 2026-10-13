# Task:
# 1. print_even_numbers(numbers) naam ka function banao.
# 2. Function ke andar for loop se list ke numbers check karo.
# 3. Sirf even numbers print karo.
# 4. Function ko [1, 2, 3, 4, 5, 6, 7, 8] list ke saath call karo.

# Expected output:
# 2
# 4
# 6
# 8

def even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

even_numbers([1, 2, 3, 4, 5, 6, 7, 8])
