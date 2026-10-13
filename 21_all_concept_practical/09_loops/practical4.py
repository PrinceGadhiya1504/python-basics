# Task: List mein even numbers
    # 1. numbers = [12, 7, 4, 9, 16, 3, 20] list banao.
    # 2. for loop se har number par iterate karo.
    # 3. if condition se check karo ki number even hai ya nahi.
    # 4. Sirf even numbers print karo.
# Expected output:
    # 12
    # 4
    # 16
    # 20

numbers = [12, 7, 4, 9, 16, 3, 20]

for num in numbers:
    if num % 2 == 0:
        print(num)