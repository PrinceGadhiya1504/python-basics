# Task:
# 1. outer() naam ka function banao.
# 2. outer() ke andar inner() naam ka function define karo.
# 3. inner() ke andar "Hello from inner function" print karo.
# 4. outer() ke andar inner ko call kiye bina return karo.
# 5. outer() ko call karke returned function ko result variable mein store karo.
# 6. result() call karo.

# Expected output:
# Hello from inner function

def outer():
    def inner():
        print("Hello from inner function")
    return inner

result = outer()
result()