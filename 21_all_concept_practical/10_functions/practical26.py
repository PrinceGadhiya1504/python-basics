# Task:
# 1. find_min_max(numbers) naam ka function banao.
# 2. Function list ka minimum aur maximum number find kare.
# 3. Dono values ko return karo.
# 4. Function ko [12, 5, 27, 3, 19] ke saath call karo.
# 5. Returned values ko minimum aur maximum variables mein store karke alag-alag print karo.
# Expected output:
# 3
# 27

def find_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = find_min_max([12, 5, 27, 3, 19])

print(minimum)
print(maximum)