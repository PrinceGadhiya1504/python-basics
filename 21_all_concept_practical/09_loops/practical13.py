# Task: Sirf odd numbers print karo
    # 1. number = 0 banao.
    # 2. while number < 10: loop chalao.
    # 3. Har iteration mein number ko 1 se increase karo.
    # 4. Agar number even ho, to continue use karke us iteration mein printing skip karo.
    # 5. Sirf odd numbers print karo.
# Expected output:
    # 1
    # 3
    # 5
    # 7
    # 9

number = 0

while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)