# Task:
# 1. my_decorator(func) naam ka decorator function banao.
# 2. Iske andar wrapper() naam ka function define karo.
# 3. wrapper() mein pehle "Before function" print karo.
# 4. Phir func() call karo.
# 5. Uske baad "After function" print karo.
# 6. wrapper return karo.
# 7. @my_decorator se say_hello() function decorate karo, jo "Hello!" print kare.
# 8. say_hello() call karo.
# Expected output:
# Before function
# Hello!
# After function

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator # Work like this say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

say_hello()

# Yahan func ek parameter hai. Is parameter mein hum kisi doosre function ko pass kar sakte hain.
