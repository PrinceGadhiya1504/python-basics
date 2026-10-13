# Task: Find the first number divisible by 7
    # 1. numbers = [10, 15, 21, 28, 35] list banao.
    # 2. for loop se numbers check karo.
    # 3. Har number ke liye print karo: Checking: <number>
    # 4. Jaise hi koi number 7 se completely divisible ho, "Found: <number>" print karo.
    # 5. Uske baad break se loop stop kar do.
# Expected output:
    # Checking: 10
    # Checking: 15
    # Checking: 21
    # Found: 21

numbers = [10, 15, 21, 28, 35]

for i in numbers:
    print(f"Checking: {i}")
    if i % 7 == 0:
        print(f"Found: {i}")
        break