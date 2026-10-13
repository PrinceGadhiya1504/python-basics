# Task:
# 1. add(a, b, c) function banao, jo teen numbers ka sum return kare.
# 2. Ek tuple banao: numbers = (10, 20, 30).
# 3. Function ko tuple unpacking ke saath call karo: add(*numbers).
# 4. Returned result print karo.
# Expected output:
# 60

def add(a, b, c):
    return a + b + c

numbers = (10, 20, 30)

print(add(*numbers))