# Task: Sum of numbers
    # 1. number = 1 banao.
    # 2. total = 0 banao.
    # 3. while loop se 1 se 5 tak numbers process karo.
    # 4. Har iteration mein current number ko total mein add karo.
    # 5. number ko 1 se increase karo.
    # 6. Loop complete hone ke baad total print karo.
# Expected output:
    # Sum: 15

number = 1
total = 0

while number <= 5:
    total += number
    number += 1

print("Sum:", total)