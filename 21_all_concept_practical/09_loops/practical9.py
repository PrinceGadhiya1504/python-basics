# Task: Search number
    # 1. numbers = [2, 4, 6, 8] list banao.
    # 2. target = 5 banao.
    # 3. for loop se list mein target search karo.
    # 4. Agar target mil jaaye, to "Number found" print karke break karo.
    # 5. Agar loop bina break ke complete ho, to else mein "Number not found" print karo.
# Expected output:
    # Number not found

numbers = [2, 4, 6, 8]
target = 5

for num in numbers:
    if num == target:
        print("Number found")
        break
else:
    print("Number not found")