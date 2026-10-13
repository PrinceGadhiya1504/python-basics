# Task:
# 1. calculate(a, b) naam ka outer function banao.
# 2. calculate() ke andar add(x, y) naam ka inner function banao.
# 3. Inner function dono numbers ka sum return kare.
# 4. Outer function ke andar add(a, b) call karke result return karo.
# 5. calculate(10, 20) call karke result print karo.
# Expected output:
# 30

def calculate(a, b):
    def add(x, y):
        return x + y
    return add(a, b)

print(calculate(10, 20))