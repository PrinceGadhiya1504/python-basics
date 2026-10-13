# Task:
# 1. show_profile(**kwargs) naam ka function banao.
# 2. Function ke andar for loop se kwargs ki har key aur value access karo.
# 3. Har pair ko key: value format mein print karo.
# 4. Function ko name="Prince", age=22 aur city="Ahmedabad" ke saath call karo.
# Expected output:
# name: Prince
# age: 22
# city: Ahmedabad

def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_profile(name="Prince", age=22, city="Ahmedabad")