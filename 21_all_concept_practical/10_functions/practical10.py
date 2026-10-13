# Task:
    # 1. show_details(**kwargs) naam ka function banao.
    # 2. Function ke andar kwargs ko print karo.
    # 3. Function ko name="Prince" aur age=22 arguments ke saath call karo.
# Expected output:
    # {'name': 'Prince', 'age': 22}

def show_details(**kwargs):
    print(kwargs)

show_details(name = "Prince", age = 22)