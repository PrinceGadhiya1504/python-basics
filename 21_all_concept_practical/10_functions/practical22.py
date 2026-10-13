# Task:
# 1. check_numbers(numbers) naam ka function banao.
# 2. any() se check karo ki list mein kam se kam ek even number hai ya nahi.
# 3. all() se check karo ki list ke saare numbers even hain ya nahi.
# 4. Dono results ko alag-alag print karo.
# 5. Function ko [2, 4, 6, 7] ke saath call karo.
# Expected output:
# True
# False

def check_numbers(numbers):
    has_even_number = any(num % 2 == 0 for num in numbers)
    has_even_number = all(num % 2 == 0 for num in numbers)
    return has_even_number, has_even_number

result = check_numbers([2, 4, 6, 7])
print(result[0])
print(result[1])
