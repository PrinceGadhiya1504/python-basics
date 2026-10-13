# Task:
# 1. factorial(n) naam ka function banao.
# 2. Agar n == 0 ho, to 1 return karo.
# 3. Otherwise, n * factorial(n - 1) return karo.
# 4. Function ko 5 ke saath call karke result print karo.

# Expected output:
# 120

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))