# Task: Multiplication pattern
    # 1. Nested for loops use karo.
    # 2. Outer loop i ko 1 se 3 tak chalaye.
    # 3. Inner loop j ko 1 se 2 tak chalaye.
    # 4. Har iteration mein i aur j ki values print karo, format i=1, j=1 jaisa ho.
# Expected output:
    # i=1, j=1
    # i=1, j=2
    # i=2, j=1
    # i=2, j=2
    # i=3, j=1
    # i=3, j=2

for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")