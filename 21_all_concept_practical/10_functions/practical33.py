# Task:
# 1. show_items(items) naam ka function banao.
# 2. Function ke andar enumerate() se list ke har item ka index aur value access karo.
# 3. Har item ko index: item format mein print karo.
# 4. Function ko ["Python", "Java", "C++"] ke saath call karo.
# Expected output:
# 0: Python
# 1: Java
# 2: C++

def show_items(items):
    for index, value in enumerate(items):
        print(f"{index}: {value}")

show_items(["Python", "Java", "C++"])