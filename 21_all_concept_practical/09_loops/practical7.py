# Task: Number search
    # 1. numbers = [4, 7, 12, 15, 20] list banao.
    # 2. for loop se list ke numbers par iterate karo.
    # 3. Jab num == 12 ho, to "Number found" print karo.
    # 4. Uske baad break se loop stop kar do.
    # 5. 12 milne se pehle jo numbers process hote hain, unhe bhi print karo.
# Expected output:
    # Checking: 4
    # Checking: 7
    # Checking: 12
    # Number found

numbers = [4, 7, 12, 15, 20]

for num in numbers:
    print(f"Checking: {num}")
    if num == 12:
        print("Number found")
        break