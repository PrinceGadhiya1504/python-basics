# Task:
# 1. check_division(a, b) naam ka function banao.
# 2. try block mein a / b ka result print karo.
# 3. except ZeroDivisionError mein "Cannot divide by zero" print karo.
# 4. finally block mein "Division attempt completed" print karo.
# 5. Function ko 10, 0 arguments ke saath call karo.
# Expected output:
# Cannot divide by zero
# Division attempt completed

def check_division(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Division attempt completed")

check_division(10, 0)