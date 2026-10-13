# Task
    # Nested for loops ki help se ye pattern print karo:

# Rules:
    # 1. Outer loop 5 rows ke liye chale.
    # 2. Inner loop har row mein utne * print karne mein help kare jitna row number hai.
    # 3. print() ke end parameter ka use kar sakte ho, taaki stars ek hi line mein print hon.

# Expected output:
    # *
    # **
    # ***
    # ****
    # *****

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()