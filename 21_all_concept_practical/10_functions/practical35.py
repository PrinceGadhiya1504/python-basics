# Task:
# 1. remove_duplicates(numbers) naam ka function banao.
# 2. Function list se duplicate numbers remove karke ek list return kare.
# 3. Function ko [1, 2, 2, 3, 4, 4, 5] ke saath call karo.
# 4. Returned list print karo.
# Expected output: Is practical mein set() use karna hai, isliye list ka order guaranteed nahi hai.
# [1, 2, 3, 4, 5]

def remove_duplicates(numbers):
    return list(set(numbers))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))