# Task:
# 1. my_decorator(func) banao.
# 2. wrapper() ke andar pehle "Starting" print karo.
# 3. Uske baad func() call karo.
# 4. Last mein "Finished" print karo.
# 5. @my_decorator se say_bye() function decorate karo, jo "Goodbye!" print kare.
# 6. say_bye() call karo.
# Expected output:
# Starting
# Goodbye!
# Finished

def my_decorator(func):
    def wrapper():
        print("Starting")
        func()
        print("Finished")
    return wrapper

@my_decorator
def say_bye():
    print("Goodbye!")

say_bye()