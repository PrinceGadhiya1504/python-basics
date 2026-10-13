# Task:
# 1. get_even_numbers(numbers) naam ka function banao.
# 2. Function list mein se sirf even numbers select kare.
# 3. Even numbers ki new list return karo.
# 4. Function ko [1, 2, 3, 4, 5, 6] ke saath call karke result print karo.

# Expected output:
# [2, 4, 6]

def get_even_numbers(numbers):
    # return [number for number in numbers if number % 2 == 0]
    return list(filter(lambda number : number % 2 == 0, numbers))

print(get_even_numbers([1, 2, 3, 4, 5, 6]))