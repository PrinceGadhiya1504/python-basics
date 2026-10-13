# Task:
# 1. count_positive(*args) naam ka function banao.
# 2. Function mein count karo ki kitne arguments positive hain, yani 0 se bade hain.
# 3. Total count return karo.
# 4. Function ko -2, 5, 0, 8, -1, 3 arguments ke saath call karke result print karo.
# Expected output:
# 3


def count_positive(*args):
    count = 0
    for num in args:
        if num > 0:
            count += 1

    return count

print(count_positive(-2, 5, 0, 8, -1, 3))