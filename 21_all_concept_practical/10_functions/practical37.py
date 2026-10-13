# Task:
# 1. safe_divide(a, b) naam ka function banao.
# 2. Function ke andar try-except use karo.
# 3. try block mein a / b ka result return karo.
# 4. Agar ZeroDivisionError aaye, to "Cannot divide by zero" return karo.
# 5. Function ko 10, 0 arguments ke saath call karke result print karo.
# Expected output:
# Cannot divide by zero

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 0))