# Task:
    # 1. calculate(a, b) naam ka function banao.
    # 2. Function se a + b aur a - b dono values return karo.
    # 3. Function call karke dono returned values ko sum_result aur sub_result mein store karo.
    # 4. Dono variables ko alag-alag print karo.
# Expected output:
    # 30
    # 10

def calculate(a, b):
    return a + b, a - b

sum_result, sub_result = calculate(20, 10)
print(sum_result)
print(sub_result)