# Task:
    # 1. Function ke bahar count = 0 variable banao.
    # 2. increase_count() function banao.
    # 3. Function ke andar global count use karo.
    # 4. count ki value 1 se increase karo.
    # 5. Function ko do baar call karo aur har call ke baad count print karo.
# Expected output:
    # 1
    # 2

count = 0

def increase_count():
    global count
    count = count + 1
    print(count)

increase_count()
increase_count()