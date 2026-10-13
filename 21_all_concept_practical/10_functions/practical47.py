# Task
# 1. filter_positive(numbers) naam ka function banao.
# 2. List comprehension se sirf positive numbers select karo.
# 3. Nayi list return karo.
# 4. Function ko [-3, 5, 0, 8, -1, 2] ke saath call karo.
# 5. Returned list print karo.
# Expected output:
# [5, 8, 2]

def filter_positive(numbers):
    return [x for x in numbers if x > 0]

print(filter_positive([-3, 5, 0, 8, -1, 2]))