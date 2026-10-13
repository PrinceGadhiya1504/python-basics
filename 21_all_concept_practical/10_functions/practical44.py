# Task
# 1. my_decorator(func) naam ka decorator banao.
# 2. Uske andar wrapper(*args, **kwargs) banao.
# 3. Wrapper pehle "Function started" print kare.
# 4. func(*args, **kwargs) se original function call karo aur result ko variable mein store karo.
# 5. "Function completed" print karo aur result return karo.
# 6. @my_decorator se add(a, b) function decorate karo, jo a + b return kare.
# 7. add(10, 20) call karke returned result print karo.
# Expected output:
# Function started
# Function completed
# 30

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function completed")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

print(add(10, 20))