# 1. square_numbers(numbers) naam ka function banao.
# 2. map() aur lambda ka use karke list ke har number ka square nikalo.
# 3. Result ko ek list ke roop mein return karo.
# 4. Function ko [1, 2, 3, 4, 5] ke saath call karke result print karo.
# Expected output:
# [1, 4, 9, 16, 25]

def square_numbers(numbers):
    # return list(map(lambda num : num ** 2, numbers))
    return list(map(lambda num : num * num, numbers))

print(square_numbers([1, 2, 3, 4, 5]))