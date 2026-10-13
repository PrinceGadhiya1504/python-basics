# Task: Odd numbers skip karo
    # 1. numbers = [1, 2, 3, 4, 5, 6] list banao.
    # 2. for loop se har number par iterate karo.
    # 3. Agar number odd ho, to continue use karke us iteration ko skip karo.
    # 4. Sirf even numbers print karo.
# Expected output:
    # 2
    # 4
    # 6

numbers = [1, 2, 3, 4, 5, 6]

for num in numbers:
    if num % 2 != 0:
        continue
    print(num)