# Task:
# 1. process_numbers(numbers) function banao.
# 2. filter() aur lambda se sirf even numbers select karo.
# 3. map() aur lambda se selected numbers ke squares nikalo.
# 4. Final result ko list ke roop mein return karo.
# 5. Function ko [1, 2, 3, 4, 5, 6] ke saath call karke print karo.
# Expected output:
# [4, 16, 36]

def process_numbers(numbers):
    even_numbers = filter(lambda x : x % 2 == 0, numbers)
    squares = map(lambda x : x * x, even_numbers)
    return list(squares)

print(process_numbers([1, 2, 3, 4, 5, 6]))