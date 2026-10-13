# Task:
# 1. outer() naam ka function banao.
# 2. outer() ke andar message = "Hello" variable banao.
# 3. Uske andar inner() function banao, jo message print kare.
# 4. outer() se inner function return karo.
# 5. Returned function ko greet variable mein store karo.
# 6. greet() call karo.
# Expected output:
# Hello

def outer():
    message = "Hello"
    def inner():
        print(message)
    return inner

greet = outer()
greet()